from antlr4 import *
from llvmlite.ir.values import ReturnValue

from src.cpp20Lexer import cpp20Lexer
from src.cpp20Parser import cpp20Parser
from src.cpp20ParserListener import cpp20ParserListener as cpp20Listener
from src.cpp20ParserVisitor import cpp20ParserVisitor as cpp20Visitor
from tables import *
from llvmlite import ir

double = ir.DoubleType()
int1 = ir.IntType(1)
int8 = ir.IntType(8)
int16 = ir.IntType(16)
int32 = ir.IntType(32)
int64 = ir.IntType(64)
void = ir.VoidType()

class myCpp20Visitor(cpp20Visitor):
    def __init__(self):
        super(cpp20Visitor,self).__init__()
        
        # llvm生成模块
        self.Module=ir.Module()

        # 待生成的llvm语句块
        # 每生成一块语句时，将当前语句块加到末尾，以self.Builder[-1]调用
        self.Builders=[]
        
        #符号表
        self.symbolTable = NameTable()
        
    def visitFunctionDeclaration(self, ctx: cpp20Parser.FunctionDeclarationContext):
        print(f"visitFunctionDeclaration: {ctx.Identifier().getText()}",) #test for debug
        '''
        对应语法：typeSpecifier Identifier '(' (functionParameter (COMMA functionParameter)*)? ')' block
        '''
        #函数名
        FunctionName = ctx.getChild(1).getText()
        #TODO:获取参数列表，填充到ParameterList里
        ReturnType = self.visit(ctx.getChild(0))
        ParameterList = [] 
        #生成llvm函数
        LLVMFuncType = ir.FunctionType(ReturnType,ParameterList)
        LLVMFunc = ir.Function(self.Module, LLVMFuncType, name= FunctionName)
        #储存函数为block
        Block = LLVMFunc.append_basic_block(name = FunctionName)
        Builder= ir.IRBuilder(Block)
        self.Builders.append(Builder)
        #访问函数块，返回值到ValueToReturn
        ChildCount = ctx.getChildCount()
        ValueToReturn=self.visit(ctx.getChild(ChildCount-1))
        return {
            'type': ReturnType,
            'signed':True,
            'value':ValueToReturn
        }
    pass

    def visitTypeSpecifier(self, ctx: cpp20Parser.TypeSpecifierContext):
        '''
        对应语法：typeSpecifier : integerTypeSpecifier | realTypeSpecifier | booleanTypeSpecifier | charTypeSpecifier | voidTypeSpecifier;
        '''
        #TODO: 定义visitRealTypeSpecifier即后面类型的函数
        Type = self.visit(ctx.getChild(0))
        return Type
    
    def visitIntegerTypeSpecifier(self, ctx: cpp20Parser.IntegerTypeSpecifierContext):
        if(ctx.getText()== 'int' or ctx.getText() == 'long'):
            return int32
        elif(ctx.getText()=='short'):
            return int16
        elif(ctx.getText()=='long long'):
            return int64

    def isExprJudge(self,realText):
        #没有处理 NOT_EQ中"not_equ"的情况
        if (realText == ">"):
            return True
        elif(realText == "<"):
            return True
        elif(realText == ">="):
            return True
        elif(realText == "<="):
            return True
        elif(realText == "=="):
            return True
        elif(realText == "!="):
            return True
        else:
            return False
    pass
    
    def isExprCal(self,realText):
        if (realText == "+"):
            return True
        elif(realText == "-"):
            return True
        elif(realText == "*"):
            return True
        elif(realText == "/"):
            return True
        elif(realText == "%"):
            return True
        else:
            return False
    pass   

    def isInt(self,llvmNum):
        if llvmNum['type']==int32 or llvmNum['type']== int64 or llvmNum['type'] == int16 or llvmNum['type'] == int8 or llvmNum['type'] == int1:
            return True
        return False

    def intConvert(self,src,target):
        Builder = self.Builders[-1]        
        if(src['type'].width == 1):
            ValueToReturn= Builder.zext(src['value'],target['type'])
            return{
                'type':target['type'],
                'signed':src['signed'],
                'value':ValueToReturn
            }
        else:
            if(src['signed']):
                ValueToReturn = Builder.sext(src['value'],target['type'])
            else:
                ValueToReturn = Builder.zext(src['value'],target['type'])
            return {
                'type':target['type'],
                'signed':src['signed'],
                'value':ValueToReturn
            }
        
            
    def intToDouble(self,llvmNum):
        Builder = self.Builders[-1]
        if(llvmNum['signed']):
            ValueToReturn = Builder.sitofp(llvmNum['value'],double)
        else:
            ValueToReturn = Builder.uitofp(llvmNum['value'],double)
        return{
            'type':double,
            'value':ValueToReturn
        }

    def toBool(self,llvmNum):
        Builder = self.Builders[-1]
        if llvmNum['type'] == double:
            ValueToReturn = Builder.fcmp_ordered('==', llvmNum['value'], ir.Constant(int1,0))
        else:
            ValueToReturn = Builder.icmp_signed('==', llvmNum['value'], ir.Constant(int1,0))
        return{
            'type':int1,
            'signed':True,
            'value':ValueToReturn
        }
    
    def exprTypeConvert(self,left,right):
        #left和right的符号类型不一致时，类型转换为一致，向大的类型转换
        #left,right可能的类型：int1,int8,int16,int32,int64,double...（暂时支持这几种）
        if(left['type']==right['type']):
            return left,right
        elif self.isInt(left) and self.isInt(right):
            if left['type'].width < right['type'].width:
                left = self.intConvert(left,right)
            else:
                right = self.intConvert(right,left)
        elif self.isInt(left) and right['type']==double:
            left = self.intToDouble(left)
        elif left['type']==double and self.isInt(right):
            right = self.intToDouble(right)
        return left,right
    

    def visitExpression(self, ctx: cpp20Parser.ExpressionContext):
        ChildCount=ctx.getChildCount()
        Builder = self.Builders[-1]
        if(ChildCount == 1):
          grandChildren = ctx.getChild(0).getChildCount()
          if(grandChildren):
              '''
              对应语法：expression: Literals|functionCall;
              '''
              result = self.visit(ctx.getChild(0))
              return result
          else:
              '''
              对应语法：expression: Identifier
              '''
              symbol = self.symbolTable.getProperty(ctx.getText())
              return{
                'type':symbol.get_type(),
                'signed':symbol.get_signed(),
                'value':symbol.get_value()
              }

        elif(ChildCount == 2):
          '''
          对应语法：expression: NOT expression
          '''  
          Builder = self.Builders[-1]
          result = self.visit(ctx.getChild(1))
          if result['type'] == double:
            ValueToReturn = Builder.fcmp_ordered('!=', result['value'], ir.Constant(int1,0))
          else:
            ValueToReturn = Builder.icmp_signed('!=', result['value'], ir.Constant(int1,0))
          return {
              'type':int1,
              'signed':True,
              'value':ValueToReturn
          }
          
        elif(ChildCount>3):
          '''
          对应语法：expression: expression '[' expression ']'
          '''
          #TODO：读数组？这个不太明白
          print("array index")

        elif(ChildCount == 3 and ctx.getChild(0).getText()=='('):
          '''
          对应语法：expression: '(' expression ')'
          '''
          result = self.visit(ctx.getChild(1))
          return result

        else:
          Operation = ctx.getChild(1).getText()
          left = self.visit(ctx.getChild(0))
          right = self.visit(ctx.getChild(2))
          if(self.isExprJudge(Operation)):
            '''
            对应语法： expression: expression '==' | '!=' | '<' | '<=' | '>' | '>=' expr
            '''
            left,right = self.exprTypeConvert(left,right)
            if(left['type']==double):
                valueToReturn = Builder.fcmp_ordered(Operation,left['value'],right['value'])
            elif(left['type']==int32 or left['type'] == int64 or left['type'] == int8 or left['type']==int1):
                if(left['signed']):
                    valueToReturn = Builder.icmp_signed(Operation,left['value'],right['value'])
                else:
                    valueToReturn = Builder.icmp_unsigned(Operation,left['value'],right['value'])                
            return{
                'type':int1,
                'signed':True,
                'value':valueToReturn
            }

          elif(Operation == '+' or Operation == '-' or Operation == '*' or Operation == '/' or Operation == '%' or Operation == '<<' or Operation == '>>'):
            '''
            对应语法：expression: expression '+'|'-'|'*'|'/'|'%' expression
            '''
            left,right = self.exprTypeConvert(left,right)
            if(Operation == '+'):
                valueToReturn = Builder.add(left['value'],right['value'])
            elif(Operation == '-'):
                valueToReturn = Builder.sub(left['value'],right['value'])
            elif(Operation == '*'):
                valueToReturn = Builder.mul(left['value'],right['value'])
            elif(Operation == '/'):
                valueToReturn = Builder.sdiv(left['value'],right['value'])
            elif(Operation == '%'):
                valueToReturn = Builder.srem(left['value'],right['value'])
            elif(Operation == '<<'):
                valueToReturn = Builder.shl(left['value'],right['value'])
            elif(Operation == '>>'):
                valueToReturn = Builder.lshr(left['value'],right['value'])
            return{
                'type':right['type'],
                'signed':True,
                'value':valueToReturn
            }

          elif(Operation == '='):
            '''
            对应语法： expression: leftExpression '=' expression
            '''


          elif(Operation == '|' or Operation == 'bitor' or Operation == '&' or Operation == 'bitand' or Operation == '^' or Operation == 'xor'):
            '''
            对应语法： expression: expression BITOR|BITAND|XOR expression
            '''
            left,right = self.exprTypeConvert(left,right)
            Signed = False
            if left['signed'] or right['signed']:
                Signed = True
            if(Operation == '|' or Operation == 'bitor'):
                ValueToReturn = Builder.or_(left['value'],right['value'])
            elif(Operation == '&' or Operation == 'bitand' ):
                ValueToReturn = Builder.and_(left['value'],right['value'])
            elif(Operation == '^' or Operation == 'xor'):
                ValueToReturn = Builder.xor(left['value'],right['value'])
            return{
                'type':left['type'],
                'signed':Signed,
                'value':ValueToReturn
            }
          
          elif(Operation == '&&' or Operation == 'and' or Operation == '||' or Operation == 'or'):
            '''
            对应语法：expression AND|OR expression
            '''
            left = self.toBool(left)
            right = self.toBool(right)
            if(Operation == '&&' or Operation == 'and'):
                ValueToReturn = Builder.and_(left['value'],right['value'])
            elif(Operation == '||' or Operation == 'or'):
                ValueToReturn = Builder.or_(left['value'],right['value'])
            return{
                'type':int1,
                'signed':True,
                'value':ValueToReturn
            }
    pass     
     
    def visitLiterals(self, ctx: cpp20Parser.LiteralsContext):
        result = self.visit(ctx.getChild(0))
        return result
    
    def visitIntegerLiteral(self, ctx: cpp20Parser.IntegerLiteralContext):
        Signed = True
        if(ctx.getText()[-2:] == 'll' or ctx.getText()[-2:] == 'LL'):
            ReturnType = int64
            if ctx.getText()[-3] == 'u' or ctx.getText()[-3] == 'U':
                Signed = False
                textOutOfSuffix = ctx.getText()[:-3]
            else:
                textOutOfSuffix = ctx.getText()[:-2]
        elif(ctx.getText()[-1]=='l' or ctx.getText()[-2:-1] == 'L'):
            ReturnType = int32
            if ctx.getText()[-2] == 'u' or ctx.getText()[-2] == 'U':
                Signed = False
                textOutOfSuffix = ctx.getText()[:-2]
            else:
                textOutOfSuffix = ctx.getText()[:-1]
        else:
            ReturnType = int32
            if ctx.getText()[-1] == 'u' or ctx.getText()[-1] == 'U':
                Signed = False
                textOutOfSuffix = ctx.getText()[:-1]
            else:
                textOutOfSuffix = ctx.getText()
        return {
            'type':ReturnType,
            'signed':Signed,
            'value':ir.Constant(ReturnType,int(textOutOfSuffix))
        }
    
    def visitFloatingLiteral(self, ctx: cpp20Parser.FloatingLiteralContext):
        return{
            'type':double,
            'value':ir.Constant(double,float(ctx.getText()))
        }
    
    def visitLeftExpression(self, ctx: cpp20Parser.LeftExpressionContext):
        if(ctx.getText()[-1]==']'):
            '''
            对应语法：leftExpression:Identifier (LSQUARE expression RSQUARE)
            '''
            #TODO:需要先写好数组的索引方式才能调用
        else:
            '''
            对应语法：leftExpression:Identifier
            '''

if __name__ == "__main__":
    input_stream = FileStream("test2.cpp")
    # lexer
    lexer = cpp20Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    # parser
    parser = cpp20Parser(stream)
    tree = parser.translationUnit()
    print(tree.toStringTree(recog=parser))
    visitor = myCpp20Visitor()
    visitor.visit(tree)
    print(visitor.Module)
    pass
