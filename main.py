from antlr4 import *

from src.cpp20Lexer import cpp20Lexer
from src.cpp20Parser import cpp20Parser
from src.cpp20ParserListener import cpp20ParserListener as cpp20Listener
from src.cpp20ParserVisitor import cpp20ParserVisitor as cpp20Visitor



class myCpp20Visitor(cpp20Visitor):
    def visitFunctionDeclaration(self, ctx: cpp20Parser.FunctionDeclarationContext):
        print(f"visitFunctionDeclaration: {ctx.Identifier().getText()}",)
        return super().visitFunctionDeclaration(ctx)
    pass

if __name__ == "__main__":
    input_stream = FileStream("test.cpp")
    # lexer
    lexer = cpp20Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    # parser
    parser = cpp20Parser(stream)
    tree = parser.translationUnit()
    print(tree.toStringTree(recog=parser))
    visitor = myCpp20Visitor()
    visitor.visit(tree)
    pass
