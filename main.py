from antlr4 import *

from src.cpp20Lexer import cpp20Lexer
from src.cpp20Parser import cpp20Parser
from src.cpp20ParserListener import cpp20ParserListener as cpp20Listener
from src.cpp20ParserVisitor import cpp20ParserVisitor as cpp20Visitor
from tables import *
from llvmlite import ir

double = ir.DoubleType()
int1 = ir.IntType(1)
int8 = ir.IntType(8)
int32 = ir.IntType(32)
int64 = ir.IntType(64)
int16 = ir.IntType(16)
void = ir.VoidType()

class myCpp20Visitor(cpp20Visitor):
    def __init__(self):
        super(cpp20Visitor,self).__init__()
        
        # llvm生成模块
        self.Module=ir.Module()

        # 待生成的llvm语句块
        # 每生成一块语句时，将当前语句块加到末尾，以self.Builder[-1]调用
        self.Builders=[]
 
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

    def exprTypeConvert(self,left,right):
        #TODO:left和right的符号类型不一致时，类型转换为一致
        if(left['type']==right['type']):
            return left,right

        return left,right

    def visitExpression(self, ctx: cpp20Parser.ExpressionContext):
        ChildCount=ctx.getChildCount()
        Builder = self.Builders[-1]
        #print(ChildCount)
        if(ChildCount==0):
          '''
          对应语法：expression: Identifier
          '''
          #TODO:在符号表中检索当前作用域是否有该字符
          #返回该字符对应的（虚寄存器）？

        if(ChildCount==1):
          '''
          对应语法：expression: Literals;
          '''
          result = self.visit(ctx.getChild(0))
          return result

        elif(ChildCount>3):
          '''
          对应语法：expression: expression '[' expression ']'
          '''
          print("array index")
        
        else:
          #Builder = self.Builders[-1]
          Operation = ctx.getChild(1).getText()
          left = self.visit(ctx.getChild(0))
          right = self.visit(ctx.getChild(2))
          left,right = self.exprTypeConvert(left,right)
          if(self.isExprJudge(Operation)):
            '''
            对应语法： expression: expression '==' | '!=' | '<' | '<=' | '>' | '>=' expr
            '''
            if(left['type']==double):
                valueToReturn = Builder.fcmp_ordered(Operation,left['value'],right['value'])
            elif(left['type']==int32 or left['type'] == int64 or left['type'] == int8 or left['type']==int1):
                #TODO:无符号数的情况的处理
                valueToReturn = Builder.icmp_signed(Operation,left['value'],right['value'])
            return{
                'type':int1,
                'value':valueToReturn
            }

          elif(Operation == '+'):
            '''
            对应语法：expression: expression '+' expression
            '''
            valueToReturn = Builder.add(left['value'],right['value'])
            return{
                'type':right['type'],
                'value':valueToReturn
            }

          elif(Operation == '-'):
            '''
            对应语法：expression: expression '-' expression
            '''
            valueToReturn = Builder.sub(left['value'],right['value'])
            return{
                'type':right['type'],
                'value':valueToReturn
            }

          elif(Operation == '*'):
            '''
            对应语法：expression: expression '*' expression
            '''
            valueToReturn = Builder.mul(left['value'],right['value'])
            return{
                'type':right['type'],
                'value':valueToReturn
            }

          elif(Operation == '/'):
            '''
            对应语法：expression: expression '/' expression
            '''
            valueToReturn = Builder.sdiv(left['value'],right['value'])
            return{
                'type':right['type'],
                'value':valueToReturn
            }

          elif(Operation == '%'):
            '''
            对应语法：expression: expression '%' expression
            '''
            valueToReturn = Builder.srem(left['value'],right['value'])
            return{
                'type':right['type'],
                'value':valueToReturn
            }

          elif(Operation == '='):
            '''
            对应语法： expression: leftExpression '=' expression
            '''
    pass     
     
    def visitLiterals(self, ctx: cpp20Parser.LiteralsContext):
        result = self.visit(ctx.getChild(0))
        return result
    
    def visitIntegerLiteral(self, ctx: cpp20Parser.IntegerLiteralContext):
        #TODO:根据后缀判断是int32还是int64
        #去掉后缀，用int()等函数进行类型转换
        return {
            'type':int32,
            'value':ir.Constant(int32,int(ctx.getText()))
        }
    
    def visitFloatingLiteral(self, ctx: cpp20Parser.FloatingLiteralContext):
        return{
            'double':double,
            'value':ir.Constant(double,float(ctx.getText()))
        }

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
