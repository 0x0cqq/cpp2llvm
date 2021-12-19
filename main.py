from antlr4 import *
from llvmlite.ir.values import GlobalVariable, ReturnValue
import sys
import ast

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

        # 符号表
        self.symbolTable = NameTable()
        
        # 用于存储switch表达式的结果，来与case匹配
        self.Switchexpression = []
        # 用于存储switch表达式中label的值
        self.Switchcaselabel = []

        # break,continue语句跳转到的block
        self.blockToBreak=[]
        self.blockToContinue=[]

    def getTypeFromText(name : str) :
        if(name == "int"):
            return int32
        elif(name == "int16"):
            return int16

        
    def visitConstExpression(self, ctx: cpp20Parser.ConstExpressionContext):
        return self.visit(ctx.literals())

    def visitVarDeclWithConstInit(self, ctx: cpp20Parser.VarDeclWithConstInitContext):
        '''
            语法： Identifier ASSIGN constExpression #varDeclWithConstInit
        '''
        if(self.symbolTable.current_scope_level == 0):
            newvar = GlobalVariable(self.Module,self.type,ctx.Identifier().getText())
            newvar.initializer = self.visit(ctx.constExpression())['value']
            self.symbolTable.addGlobal(ctx.Identifier().getText(),
                NameProperty(
                    type  = self.type,
                    value = newvar)) # 只需要记录虚拟寄存器即可   
        else:
            self.symbolTable.addLocal(ctx.Identifier().getText(),
                NameProperty(
                    type= self.type,
                    value=self.visit(ctx.constExpression())['value'])) # 只需要记录虚拟寄存器即可  
        return 
    
    def visitVarDeclWithInit(self, ctx: cpp20Parser.VarDeclWithInitContext):
        '''
        对应语法：Identifier ASSIGN expression
        '''
        # print("varDeclWithInit")
        if(self.symbolTable.current_scope_level == 0):
            #全局变量
            raise BaseException("global var must be initialized with a const expression")
        else:
            #局部变量
            self.symbolTable.addLocal(ctx.Identifier().getText(),
                NameProperty(
                    type= self.type,
                    value=self.visit(ctx.expression())['value'])) # 只需要记录虚拟寄存器即可        
        

        return

    def visitVarDeclWithoutInit(self, ctx: cpp20Parser.VarDeclWithoutInitContext):
        '''
        对应语法：Identifier
        '''
        # print(f"varDeclWithOutInit: {ctx.Identifier().getText()}")
        if(self.symbolTable.current_scope_level == 0):
            newvar = GlobalVariable(self.Module,self.type,ctx.Identifier().getText())
            self.symbolTable.addGlobal(ctx.Identifier().getText(),
                NameProperty(
                    type=self.type,
                    value=newvar))
        else:
            self.symbolTable.addLocal(ctx.Identifier().getText(),
                NameProperty(
                    type=self.type,
                    value=None)) # 这里可能还是得给一个初始的值，但是也未必
        return

    def visitVariableDeclarator(self, ctx: cpp20Parser.VariableDeclaratorContext):
        '''
        对应语法 ：typeSpecifier variableDeclaration (COMMA variableDeclaration)* SEMI;
        '''
        # print("Variable Declaration")
        # print(f"{len(ctx.variableDeclaration())} variables: ",end='')

        # for declaration in ctx.variableDeclaration():
        #     print(declaration.getChildCount())
        
        self.type = self.visit(ctx.typeSpecifier())
        
        # print("type:", self.type)

        for declaration in ctx.variableDeclaration():
            self.visit(declaration)

        del self.type
        return
    
    def visitNormalArrDecl(self, ctx: cpp20Parser.NormalArrDeclContext):
        '''
        对应语法：typeSpecifier Identifier LSQUARE DecimalLiteral RSQUARE (ASSIGN LBRACE expression (COMMA expression)* RBRACE)? SEMI;
        '''
        #数组长度
        ArrayLength = int(ctx.getChild(3).getText())
        #数据类型
        ArrayType = self.visit(ctx.getChild(0))
        LLVMArrayType = ir.ArrayType(ArrayType,ArrayLength)
        #数据标识符
        ArrayName = ctx.getChild(1).getText()
        #变量的声明
        if(self.symbolTable.current_scope_level == 0):
            NewVar=ir.GlobalVariable(self.Module,LLVMArrayType,name = ArrayName)
        else:
            Builder=self.Builders[-1]
            NewVar=Builder.alloca(LLVMArrayType,name = ArrayName)

        symbolProperty = NameProperty(LLVMArrayType,NewVar)
        self.symbolTable.addLocal(ArrayName,symbolProperty)
        ChildCount=ctx.getChildCount()
        if ChildCount > 6:
            #赋初值给数组中的元素
            ChildToVisit = 8
            elementIndex = 0
            Builder = self.Builders[-1]
            while(elementIndex<ArrayLength and ChildToVisit<ChildCount):
                address = Builder.gep(NewVar,[ir.Constant(int32,0),ir.Constant(int32,elementIndex)])
                valueToStore = self.visit(ctx.getChild(ChildToVisit))['value']
                Builder.store(valueToStore,address)
                ChildToVisit += 2
                elementIndex += 1
        return 
    

    def visitStringDecl(self, ctx: cpp20Parser.StringDeclContext):
        '''
        对应语法：typeSpecifier Identifier LSQUARE DecimalLiteral RSQUARE (ASSIGN stringLiteral) SEMI 
        '''
        #数组长度
        ArrayLength = int(ctx.getChild(3).getText())
        #数据类型
        ArrayType = self.visit(ctx.getChild(0))
        LLVMArrayType = ir.ArrayType(ArrayType,ArrayLength)
        #数据标识符
        ArrayName = ctx.getChild(1).getText()
        #变量的声明
        if(self.symbolTable.current_scope_level == 0):
            NewVar=ir.GlobalVariable(self.Module,LLVMArrayType,name = ArrayName)
        else:
            Builder=self.Builders[-1]
            NewVar=Builder.alloca(LLVMArrayType,name = ArrayName)

        symbolProperty = NameProperty(LLVMArrayType,NewVar)
        self.symbolTable.addLocal(ArrayName,symbolProperty)
        ChildCount=ctx.getChildCount()
        if ChildCount>6:
            stringLiteral = self.visit(ctx.stringLiteral())
            ScharNum = len(stringLiteral)
            elementIndex = 0
            while(elementIndex < ScharNum-1):
                charToStore = ir.Constant(ArrayType,ord(stringLiteral[elementIndex]))

                address = Builder.gep(NewVar,[ir.Constant(int32,0),ir.Constant(int32,elementIndex)])
                Builder.store(charToStore,address)
                elementIndex += 1
        return

    def visitReturnStatement(self, ctx: cpp20Parser.ReturnStatementContext):
        '''
            对应语法： RETURN expression? SEMI;
        '''
        if(ctx.expression() is None):
            self.Builders[-1].ret_void()
        else:
            self.Builders[-1].ret(self.visit(ctx.expression())['value'])

    def visitFunctionParameter(self, ctx: cpp20Parser.FunctionParameterContext):
        '''
            对应语法：typeSpecifier Identifier | DOTS;
        '''
        if(ctx.DOTS() is None):
            return {
                "name": ctx.Identifier().getText(),
                "type": self.visit(ctx.typeSpecifier())
            }
        else:
            return {
                "name": "varargs",
                "type": "varargs"
            }

    def visitFunctionCall(self, ctx: cpp20Parser.FunctionCallContext):
        '''
        对应语法：functionCall : Identifier LPAREN (expression (COMMA expression)*)? RPAREN;
        '''
        Builder = self.Builders[-1]
        functionName = ctx.Identifier().getText()
        property = self.symbolTable.getProperty(functionName)
        if(property.get_type().__class__.__name__ == ir.FunctionType.__name__):
            # 参数列表
            paramList = []
            for expression in ctx.expression():
                paramList.append(self.visit(expression)['value'])
            # 检查合法性
            # print("paramList & argsList: ", paramList,property.get_type().args)
            if(property.get_type().var_arg):
                # 只和vararg之前的比较
                vaild_paramList = paramList[:len(property.get_type().args)]
            else:
                vaild_paramList = paramList

            if(len(vaild_paramList) != len(property.get_type().args)):
                raise BaseException("wrong args number")
            for real_param, param in zip(vaild_paramList,property.get_type().args):
                if(param != real_param.type):
                    raise BaseException("wrong args type")
            # 函数调用
            ret_value = Builder.call(property.get_value(), paramList, name='', cconv=None, tail=False, fastmath=())
            ret_type = property.get_type().return_type
            return {
                "type" : ret_type,
                'value': ret_value
            }
        else:
            raise BaseException("not a function name")

    def visitFunctionDecl(self, ctx: cpp20Parser.FunctionDeclContext):
        '''
            typeSpecifier Identifier LPAREN (functionParameter (COMMA functionParameter)*)? RPAREN SEMI #functionDef
        '''
        # print("visit function declaration")
        #函数名
        FunctionName = ctx.Identifier().getText()
        ReturnType = self.visit(ctx.typeSpecifier())
        ParameterList = []
        for param in ctx.functionParameter():
            ParameterList.append(self.visit(param))
        ParameterList = tuple(ParameterList)
        # print(ParameterList)
        ParameterTypeTuple = tuple(param['type'] for param in ParameterList)
        is_var_arg = "varargs" in ParameterTypeTuple
        if(is_var_arg):
            if(ParameterTypeTuple.count("varargs") > 1):
                raise BaseException("too many varargs")
            if(ParameterTypeTuple[-1] != "varargs"):
                raise BaseException("varargs must be the last parameter")
            ParameterTypeTuple = ParameterTypeTuple[:-1]
        # 声明而非定义
        LLVMFuncType = ir.FunctionType(ReturnType,ParameterTypeTuple,var_arg=is_var_arg)
        LLVMFunc = ir.Function(self.Module, LLVMFuncType, name=FunctionName)
        self.symbolTable.addGlobal(FunctionName,NameProperty(type = LLVMFuncType,value = LLVMFunc))


    
    def visitFunctionDef(self, ctx: cpp20Parser.FunctionDefContext):
        #print(f"visitfunctionDefinition: {ctx.Identifier().getText()}",) #test for debug
        '''
        对应语法：typeSpecifier Identifier '(' (functionParameter (COMMA functionParameter)*)? ')' block
        '''
        #函数名
        FunctionName = ctx.getChild(1).getText()
        #获取参数列表，填充到ParameterList里
        ReturnType = self.visit(ctx.getChild(0))
        ParameterList = []
        for param in ctx.functionParameter():
            ParameterList.append(self.visit(param))
        ParameterList = tuple(ParameterList)
        # print(ParameterList)
        ParameterTypeTuple = tuple(param['type'] for param in ParameterList)
        if("varargs" in ParameterTypeTuple):
            raise BaseException("varargs not allowed in function definition")
        # if(ParameterList == []):
        #     ParameterList.append(None)
        # print("print par", ParameterTypeTuple)
        #生成llvm函数
        LLVMFuncType = ir.FunctionType(ReturnType,ParameterTypeTuple)
        LLVMFunc = ir.Function(self.Module, LLVMFuncType, name=FunctionName)
        # 将函数原型存入符号表
        self.symbolTable.addGlobal(FunctionName,NameProperty(type = LLVMFuncType,value = LLVMFunc))
        #储存函数为block
        Block = LLVMFunc.append_basic_block(name="__"+FunctionName)
        Builder= ir.IRBuilder(Block)
        self.Builders.append(Builder)
        #进入作用域
        self.symbolTable.enterScope()
        #将函数形参存入符号表
        for param, argsValue in zip(ParameterList,LLVMFunc.args):
            self.symbolTable.addLocal(param['name'], NameProperty(param['type'], argsValue))
        #访问函数块，返回值到ValueToReturn
        ValueToReturn=self.visit(ctx.block())
        #可能还要强制加上一个ret void，不然不知道会不会有bug。。。
        # if(self.Builders[-1].)
        # self.Builders[-1].ret_void()
        #退出作用域
        self.symbolTable.exitScope()

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
    
    def visitVoidTypeSpecifier(self, ctx: cpp20Parser.VoidTypeSpecifierContext):
        return void

    def visitRealTypeSpecifier(self, ctx: cpp20Parser.RealTypeSpecifierContext):
        return double
    
    def visitBooleanTypeSpecifier(self, ctx: cpp20Parser.BooleanTypeSpecifierContext):
        return int1

    def visitCharTypeSpecifier(self, ctx: cpp20Parser.CharTypeSpecifierContext):
        return int8
    

    def visitIntegerTypeSpecifier(self, ctx: cpp20Parser.IntegerTypeSpecifierContext):
        if(ctx.getText()== 'int' or ctx.getText() == 'long'):
            return int32
        elif(ctx.getText()=='short'):
            return int16
        elif(ctx.getText()=='longlong'):
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
        if(target['type'].width >= src['type'].width): # 往大扩展   
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
        else: # 往小了转换，其实是 undefined 行为
            ValueToReturn = Builder.trunc(src['value'],target['type'])
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

    
    def doubleToInt(self,llvmNum,target):
        Builder = self.Builders[-1]
        if(llvmNum['signed']):
            ValueToReturn = Builder.fptosi(llvmNum['value'],target['type'])
        else:
            ValueToReturn = Builder.fptoui(llvmNum['value'],target['type'])
        return {
            'type':target['type'],
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

    def assignTypeConvert(self,left,right):
        # 赋值语句中用的类型转换
        # 强制把右侧的类型转换为左侧的类型
        if(left['type'] != right['type']):
            if(self.isInt(left) and self.isInt(right)):
                right = self.intConvert(right,left)
            elif(self.isInt(left) and self.isInt(right)==False):
                right = self.doubleToInt(right,left)
            elif(self.isInt(left)==False and self.isInt(right)):
                right = self.intToDouble(right)
            else:
                pass
        return left,right
    
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
        # print(f"visitExpression:{ctx.getText()}, {ctx.getChildCount()}")
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
                if(symbol.level == 0):
                    ret_value = Builder.load(symbol.get_value())
                else:
                    ret_value = symbol.get_value()
                return {
                    'name':ctx.getText(),
                    'type':ret_value.type,
                    'signed':symbol.get_signed(),
                    'value':ret_value
                }

        elif(ChildCount == 2):
            '''
            对应语法：expression: NOT expression | SUB expression
            对应语法：leftexpression MINUS_MINUS | leftexpression PLUS_PLUS
            '''  
            if(ctx.getChild(0).getText() == '-' or ctx.getChild(0).getText() == '!'):
                Builder = self.Builders[-1]
                result = self.visit(ctx.getChild(1))
                if(ctx.getChild(0).getText() == '!'):
                    if result['type'] == double:
                        ValueToReturn = Builder.fcmp_ordered('!=', result['value'], ir.Constant(int1,0))
                    else:
                        ValueToReturn = Builder.icmp_signed('!=', result['value'], ir.Constant(int1,0))
                    return {
                        'type':int1,
                        'signed':True,
                        'value':ValueToReturn
                    }
                elif(ctx.getChild(0).getText() == '-'):
                    if result['type'] == double:
                        ValueToReturn = Builder.fneg(result['value'])
                    else:
                        ValueToReturn = Builder.neg(result['value'])
                    return {
                        'type':result['type'],
                        'signed':True,
                        'value':ValueToReturn
                    }
            else:
                # 减减或者加加
                Builder = self.Builders[-1]
                lhs = self.visit(ctx.getChild(0))
                # 先 load
                if('address' in lhs):
                    lhs['value'] = Builder.load(lhs['address'])
                # 再 + 1 / -1
                if(ctx.getChild(1).getText() == '++'):
                    ValueToReturn = Builder.add(lhs['value'],ir.Constant(lhs['type'],1))
                else:
                    ValueToReturn = Builder.sub(lhs['value'],ir.Constant(lhs['type'],1))
                # 存储
                if('address' in lhs): # 数组，反正是地址
                    Builder.store(ValueToReturn, lhs['address'])
                    return {
                        'type':lhs['type'],
                        'signed':True,
                        'address':lhs['address'],
                        'value': ValueToReturn
                    }    
                else: # 变量
                    self.symbolTable.setProperty(ctx.getChild(0).getText(), value = ValueToReturn)
                    return {
                        'type':lhs['type'],
                        'signed':True,
                        'value': ValueToReturn
                    }
        elif(ChildCount > 3):
            '''
            对应语法：expression: Identifier '[' expression ']'
            '''
            index = self.symbolTable.getProperty(ctx.getChild(0).getText())
            subscribe = self.visit(ctx.getChild(2))['value']
            if(isinstance(index.get_type(),ir.types.ArrayType)):
                Builder = self.Builders[-1]
                Address = Builder.gep(index.get_value(),[ir.Constant(int32,0),subscribe],inbounds=True)
                ValueToReturn = Builder.load(Address)
                print("call arrayItem",ValueToReturn)
                return{
                    'type':index.get_type().element,
                    'signed':True,
                    'value':ValueToReturn,
                    'address':Address
                }
            else:
                raise BaseException("the array isn't defined")

        elif(ChildCount == 3 and ctx.getChild(0).getText()=='('):
            '''
            对应语法：expression: '(' expression ')'
            '''
            result = self.visit(ctx.getChild(1))
            return result

        else:
            Operation = ctx.getChild(1).getText()
            # print(f"Operation:{Operation},child0:{ctx.getChild(0).getText()},child2:{ctx.getChild(2).getText()}")

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
                # result = self.visit(ctx.expression())
                ChildCount=ctx.getChild(0).getChildCount()
                print(left," is an varible")
                if('address' in left): # 全局变量或者数组
                    # 强制转换就先不管了
                    Builder.store(right['value'],left['address'])
                    return {
                        'type':right['type'],   
                        'value': Builder.load(left['address'])
                    }
                else: # 局部变量
                    left,right = self.assignTypeConvert(left,right) # 强制类型转换
                    self.symbolTable.setProperty(ctx.getChild(0).getText(), value = right['value'])
                    return {
                        'type':right['type'],
                        'value':right['value'],
                        'signed': True
                    }

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

    def visitBlock(self, ctx: cpp20Parser.BlockContext):
        self.symbolTable.enterScope()
        super().visitBlock(ctx)
        self.symbolTable.exitScope()
        return

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
    
    def visitStringLiteral(self, ctx: cpp20Parser.StringLiteralContext):
        # 笑死，根本写不出来
        return ast.literal_eval(ctx.getText())
        

    
    def visitLeftExpression(self, ctx: cpp20Parser.LeftExpressionContext):
        if(ctx.getText()[-1]==']'):
            '''
            对应语法：leftExpression:Identifier (LSQUARE expression RSQUARE)
            '''
            index = self.symbolTable.getProperty(ctx.getChild(0).getText())
            subscribe = self.visit(ctx.getChild(2))['value']
            if(isinstance(index.get_type(),ir.types.ArrayType)):
                Builder = self.Builders[-1]
                Address = Builder.gep(index.get_value(),[ir.Constant(int32,0),ir.Constant(int32,subscribe)],inbounds=True)
                ValueToReturn = Builder.load(Address)
                print("call arrayItem",ValueToReturn)
                return{
                    'type':index.get_type().element,
                    'signed':True,
                    'value':ValueToReturn,
                    'address':Address
                }
            else:
                raise BaseException("the array isn't defined")
            
        else:
            '''
            对应语法：leftExpression:Identifier
            '''
            symbol = self.symbolTable.getProperty(ctx.getText())
            if(symbol.level == 0):
                return {
                        'type':symbol.get_type(),
                        'signed':symbol.get_signed(),
                        'address':symbol.get_value(),
                    }
            else:
                return {
                        'type':symbol.get_type(),
                        'signed': True,
                        'value':symbol.get_value(),
                    }
    
    
    def visitWhileStatement(self, ctx: cpp20Parser.WhileStatementContext):
        '''
        对应语法：WHILE LPAREN expression RPAREN statement
        '''
        print(f"visitWhileStatement:{ctx.getText()}, {ctx.getChildCount()}")
        Builder = self.Builders[-1]
        #新建三个块，代表判断条件，while循环内部块，while循环外
        expressionBlock = Builder.append_basic_block()
        whileStatementBlock = Builder.append_basic_block()
        endWhileBlock = Builder.append_basic_block()

        self.blockToBreak.append(endWhileBlock)
        self.blockToContinue.append(expressionBlock)

        #expressionBlock
        Builder.branch(expressionBlock)
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(expressionBlock))
        result = self.visit(ctx.getChild(2))
        condition = self.toBool(result)
        self.Builders[-1].cbranch(condition['value'],whileStatementBlock,endWhileBlock)
        
        #whileStatementBlock
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(whileStatementBlock))
        print("this blocktobreak",self.blockToBreak[-1])
        self.visit(ctx.getChild(4))
        if(not self.Builders[-1].block.is_terminated):
            self.Builders[-1].branch(expressionBlock)

        #endWhileBlock
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(endWhileBlock))

        self.blockToContinue.pop()
        self.blockToBreak.pop()

        return

    def visitDoWhileStatement(self, ctx: cpp20Parser.DoWhileStatementContext):
        '''
        对应语法：DO statement WHILE LPAREN expression RPAREN SEMI;
        '''
        Builder = self.Builders[-1]
        #新建语法块，doStatementBlock,expressionblock,endWhileBlock
        doStatementBlock = Builder.append_basic_block()
        expressionBlock = Builder.append_basic_block()
        endWhileBlock = Builder.append_basic_block()
        self.blockToBreak.append(endWhileBlock)
        self.blockToContinue.append(expressionBlock)

        #doStatementBlock
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(doStatementBlock))
        self.visit(ctx.getChild(1))
        if(not self.Builders[-1].block.is_terminated):
            self.Builders[-1].branch(expressionBlock)

        #expressionBlock
        self.Builders[-1].branch(expressionBlock)
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(expressionBlock))
        result = self.visit(ctx.getChild(4))
        condition = self.toBool(result)
        self.Builders[-1].cbranch(condition['value'],doStatementBlock,endWhileBlock)

        #endWhileBlock
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(endWhileBlock))
        self.blockToContinue.pop()
        self.blockToBreak.pop()
        return

    def visitForStatement(self, ctx: cpp20Parser.ForStatementContext):
        '''
        对应语法：FOR LPAREN forExprSet? SEMI expression? SEMI forExprSet? RPAREN statement;
        '''
        Builder = self.Builders[-1]
        #判断三个expression是否存在
        ChildCount = ctx.getChildCount()
        flag1 = True
        flag2 = True
        flag3 = True

        if(ctx.getChild(2).getText()==';'):
            flag1 = False
        for i in range(ChildCount-1):
            text1 = ctx.getChild(i).getText()
            text2 = ctx.getChild(i+1).getText()
            if(text1 == ';' and text2 != ';'):
                expressionIndex = i + 1
                break
            if(text1 == text2):
                flag2 = False
        if(ctx.getChild(ChildCount-3).getText()==';'):
            flag3 = False
        
        #运行第一个forExprSet的语句
        if(flag1):
            self.visit(ctx.getChild(2))

        #新建语法块，JudgeBlock,loopBlock,forExpr3Block,endLoopBlock
        JudgeBlock = Builder.append_basic_block()
        loopBlock = Builder.append_basic_block()
        forExpr3Block = Builder.append_basic_block()
        endLoopBlock = Builder.append_basic_block()
        self.blockToBreak.append(endLoopBlock)
        self.blockToContinue.append(forExpr3Block)
        
        #JudgeBlock
        if(flag2):
            self.Builders[-1].branch(JudgeBlock)
            self.Builders.pop()
            self.Builders.append(ir.IRBuilder(JudgeBlock))
            result = self.visit(ctx.getChild(expressionIndex))
            condition = self.toBool(result)
            self.Builders[-1].cbranch(condition['value'],loopBlock,endLoopBlock)

        #loopBlock
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(loopBlock))
        self.visit(ctx.getChild(ChildCount-1))
        if(not self.Builders[-1].block.is_terminated):
            self.Builders[-1].branch(forExpr3Block)

        #forExpr3Block
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(forExpr3Block))
        if(flag3):
            self.visit(ctx.getChild(ChildCount-3))
        if(flag2):
            self.Builders[-1].branch(JudgeBlock)
        else:
            self.Builders[-1].branch(loopBlock)    


        #endLoopBlock
        self.Builders.pop() 
        self.Builders.append(ir.IRBuilder(endLoopBlock))
        self.blockToBreak.pop()
        self.blockToContinue.pop()
            
        return
        
    def visitIfStatement(self, ctx:cpp20Parser.IfStatementContext):
        '''
        ifStatement : IF LPAREN expression RPAREN statement (ELSE statement)?;
        '''
        print(f"visitIfStatement:{ctx.getText()}, {ctx.getChildCount()}")
        self.symbolTable.enterScope()
        Builder = self.Builders[-1]
        trueblock = Builder.append_basic_block()

        #if else的情况
        if len(ctx.statement())==2:
            falseblock = Builder.append_basic_block()
            endblock = Builder.append_basic_block()
            
            #条件跳转
            result = self.visit(ctx.getChild(2))
            condition = self.toBool(result)
            Builder.cbranch(condition['value'], trueblock, falseblock)
            
            #if块
            trueblockbuilder = ir.IRBuilder(trueblock)
            self.Builders.pop()
            self.Builders.append(trueblockbuilder)
            self.visit(ctx.getChild(4))
            if(not self.Builders[-1].block.is_terminated):
                self.Builders[-1].branch(endblock)
            
            #else块
            falseblockbuilder = ir.IRBuilder(falseblock)
            self.Builders.pop()
            self.Builders.append(falseblockbuilder)
            self.visit(ctx.getChild(6))
            #self.Builders[-1].branch(endblock)
            if(not self.Builders[-1].block.is_terminated):
                self.Builders[-1].branch(endblock)
            
            #endif标识符
            self.Builders.pop()
            self.Builders.append(ir.IRBuilder(endblock))
            
        #只有if没有else的情况
        else:
            endblock = Builder.append_basic_block()
            
            #条件跳转
            result = self.visit(ctx.getChild(2))
            condition = self.toBool(result)
            Builder.cbranch(condition['value'], trueblock, endblock)
            
            #if块
            trueblockbuilder = ir.IRBuilder(trueblock)
            self.Builders.pop()
            self.Builders.append(trueblockbuilder)
            self.visit(ctx.getChild(4))
            if(not self.Builders[-1].block.is_terminated):
                self.Builders[-1].branch(endblock)
            
            #endif标识符
            self.Builders.pop()
            self.Builders.append(ir.IRBuilder(endblock))

        self.symbolTable.exitScope()
        return
    
    def visitSwitchStatement(self, ctx:cpp20Parser.SwitchStatementContext):
        '''
        switchStatement : SWITCH LPAREN expression RPAREN LBRACE (caseStatement)* RBRACE;
        '''
        print(f"visitSwitchStatement:{ctx.getText()}, {ctx.getChildCount()}")
        self.symbolTable.enterScope()
        casenum = ctx.getChildCount()-6
        Builder = self.Builders[-1]
        
        result = self.visit(ctx.getChild(2))
        self.Switchexpression.append(result)
        
        temarray = []
        for i in range(casenum*2+2):
            temarray.append(Builder.append_basic_block())
        self.Switchcaselabel.append(temarray)
        self.blockToBreak.append(temarray[-1])
        print("len(break)",len(self.blockToBreak))
        EndSwitch = temarray[-1]
        
        Builder.branch(temarray[0])
        
        for i in range(casenum):
            self.visit(ctx.getChild(i+5))
        
        assert len(self.Switchcaselabel[-1]) == 2
        ir.IRBuilder(self.Switchcaselabel[-1][0]).branch(self.Switchcaselabel[-1][1])
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(self.Switchcaselabel[-1][1]))
        
        self.Switchexpression.pop()
        self.Switchcaselabel.pop()
        self.blockToBreak.pop()
        
        self.symbolTable.exitScope()
        return
        
    def visitCaseStatement(self, ctx:cpp20Parser.CaseStatementContext):
        '''
        caseStatement : CASE constExpression COLON statement;
        '''
        print(f"visitCaseStatement:{ctx.getText()}, {ctx.getChildCount()}")
        print("len(break)",len(self.blockToBreak))
        self.symbolTable.enterScope()
        judgeblock = self.Switchcaselabel[-1][0]
        statementblock = self.Switchcaselabel[-1][1]
        targetjudgeblock = self.Switchcaselabel[-1][2]
        targetstatementblock = self.Switchcaselabel[-1][3]
        
        judgebuilder = ir.IRBuilder(judgeblock)
        
        left = self.Switchexpression[-1]
        right = self.visit(ctx.getChild(1))
            
        left,right = self.exprTypeConvert(left,right)
        Operation = '=='
        if(left['type']==double):
            valueToReturn = judgebuilder.fcmp_ordered(Operation,left['value'],right['value'])
        elif(left['type']==int32 or left['type'] == int64 or left['type'] == int8 or left['type']==int1):
            if(left['signed']):
                valueToReturn = judgebuilder.icmp_signed(Operation,left['value'],right['value'])
            else:
                valueToReturn = judgebuilder.icmp_unsigned(Operation,left['value'],right['value'])                
        
        judgebuilder.cbranch(valueToReturn, statementblock, targetjudgeblock)
        
        self.Builders.pop()
        self.Builders.append(ir.IRBuilder(statementblock))
        print("len(break)",len(self.blockToBreak))
        self.visit(ctx.getChild(3))
        if(not self.Builders[-1].block.is_terminated):
            self.Builders[-1].branch(targetstatementblock)
        
        self.symbolTable.exitScope()
        
        self.Switchcaselabel[-1].pop(0)
        self.Switchcaselabel[-1].pop(0)
        return
        
        
        

    def visitBreakStatement(self, ctx: cpp20Parser.BreakStatementContext):
        print(f"visitBreakStatement:{ctx.getText()}, {ctx.getChildCount()}")
        print("len(break)",len(self.blockToBreak))
        if self.blockToBreak:
            Builder = self.Builders[-1]
            Builder.branch(self.blockToBreak[-1])
        else:
            raise BaseException("cannot break")        
        return

    def visitContinueStatement(self, ctx: cpp20Parser.ContinueStatementContext):
        if self.blockToContinue:
            Builder = self.Builders[-1]
            Builder.branch(self.blockToContinue[-1])
        else:
            raise BaseException("cannot continue")
        return

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        filename = "test2.cpp"
        outputfilename = None
    else:
        filename = sys.argv[1]
        outputfilename = sys.argv[2] 
    # print(filename)      
    
    input_stream = FileStream(filename)
    # lexer
    lexer = cpp20Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    # parser
    parser = cpp20Parser(stream)
    tree = parser.translationUnit()
    print(tree.toStringTree(recog=parser))
    visitor = myCpp20Visitor()
    visitor.visit(tree)
    if(outputfilename):
        with open(outputfilename, 'w') as f:
            f.write(str(visitor.Module))
    else:
        print(visitor.Module)
    pass
