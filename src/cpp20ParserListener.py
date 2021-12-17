# Generated from grammar/cpp20Parser.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cpp20Parser import cpp20Parser
else:
    from cpp20Parser import cpp20Parser

# This class defines a complete listener for a parse tree produced by cpp20Parser.
class cpp20ParserListener(ParseTreeListener):

    # Enter a parse tree produced by cpp20Parser#literals.
    def enterLiterals(self, ctx:cpp20Parser.LiteralsContext):
        pass

    # Exit a parse tree produced by cpp20Parser#literals.
    def exitLiterals(self, ctx:cpp20Parser.LiteralsContext):
        pass


    # Enter a parse tree produced by cpp20Parser#floatingLiteral.
    def enterFloatingLiteral(self, ctx:cpp20Parser.FloatingLiteralContext):
        pass

    # Exit a parse tree produced by cpp20Parser#floatingLiteral.
    def exitFloatingLiteral(self, ctx:cpp20Parser.FloatingLiteralContext):
        pass


    # Enter a parse tree produced by cpp20Parser#integerLiteral.
    def enterIntegerLiteral(self, ctx:cpp20Parser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by cpp20Parser#integerLiteral.
    def exitIntegerLiteral(self, ctx:cpp20Parser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by cpp20Parser#characterLiteral.
    def enterCharacterLiteral(self, ctx:cpp20Parser.CharacterLiteralContext):
        pass

    # Exit a parse tree produced by cpp20Parser#characterLiteral.
    def exitCharacterLiteral(self, ctx:cpp20Parser.CharacterLiteralContext):
        pass


    # Enter a parse tree produced by cpp20Parser#stringLiteral.
    def enterStringLiteral(self, ctx:cpp20Parser.StringLiteralContext):
        pass

    # Exit a parse tree produced by cpp20Parser#stringLiteral.
    def exitStringLiteral(self, ctx:cpp20Parser.StringLiteralContext):
        pass


    # Enter a parse tree produced by cpp20Parser#translationUnit.
    def enterTranslationUnit(self, ctx:cpp20Parser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by cpp20Parser#translationUnit.
    def exitTranslationUnit(self, ctx:cpp20Parser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by cpp20Parser#baseSpecifierList.
    def enterBaseSpecifierList(self, ctx:cpp20Parser.BaseSpecifierListContext):
        pass

    # Exit a parse tree produced by cpp20Parser#baseSpecifierList.
    def exitBaseSpecifierList(self, ctx:cpp20Parser.BaseSpecifierListContext):
        pass


    # Enter a parse tree produced by cpp20Parser#accessSpecifier.
    def enterAccessSpecifier(self, ctx:cpp20Parser.AccessSpecifierContext):
        pass

    # Exit a parse tree produced by cpp20Parser#accessSpecifier.
    def exitAccessSpecifier(self, ctx:cpp20Parser.AccessSpecifierContext):
        pass


    # Enter a parse tree produced by cpp20Parser#accessLabel.
    def enterAccessLabel(self, ctx:cpp20Parser.AccessLabelContext):
        pass

    # Exit a parse tree produced by cpp20Parser#accessLabel.
    def exitAccessLabel(self, ctx:cpp20Parser.AccessLabelContext):
        pass


    # Enter a parse tree produced by cpp20Parser#memberDeclaration.
    def enterMemberDeclaration(self, ctx:cpp20Parser.MemberDeclarationContext):
        pass

    # Exit a parse tree produced by cpp20Parser#memberDeclaration.
    def exitMemberDeclaration(self, ctx:cpp20Parser.MemberDeclarationContext):
        pass


    # Enter a parse tree produced by cpp20Parser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:cpp20Parser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by cpp20Parser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:cpp20Parser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by cpp20Parser#destructorDeclaration.
    def enterDestructorDeclaration(self, ctx:cpp20Parser.DestructorDeclarationContext):
        pass

    # Exit a parse tree produced by cpp20Parser#destructorDeclaration.
    def exitDestructorDeclaration(self, ctx:cpp20Parser.DestructorDeclarationContext):
        pass


    # Enter a parse tree produced by cpp20Parser#memberSpecification.
    def enterMemberSpecification(self, ctx:cpp20Parser.MemberSpecificationContext):
        pass

    # Exit a parse tree produced by cpp20Parser#memberSpecification.
    def exitMemberSpecification(self, ctx:cpp20Parser.MemberSpecificationContext):
        pass


    # Enter a parse tree produced by cpp20Parser#classDefinition.
    def enterClassDefinition(self, ctx:cpp20Parser.ClassDefinitionContext):
        pass

    # Exit a parse tree produced by cpp20Parser#classDefinition.
    def exitClassDefinition(self, ctx:cpp20Parser.ClassDefinitionContext):
        pass


    # Enter a parse tree produced by cpp20Parser#constExpression.
    def enterConstExpression(self, ctx:cpp20Parser.ConstExpressionContext):
        pass

    # Exit a parse tree produced by cpp20Parser#constExpression.
    def exitConstExpression(self, ctx:cpp20Parser.ConstExpressionContext):
        pass


    # Enter a parse tree produced by cpp20Parser#leftExpression.
    def enterLeftExpression(self, ctx:cpp20Parser.LeftExpressionContext):
        pass

    # Exit a parse tree produced by cpp20Parser#leftExpression.
    def exitLeftExpression(self, ctx:cpp20Parser.LeftExpressionContext):
        pass


    # Enter a parse tree produced by cpp20Parser#expression.
    def enterExpression(self, ctx:cpp20Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by cpp20Parser#expression.
    def exitExpression(self, ctx:cpp20Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by cpp20Parser#statement.
    def enterStatement(self, ctx:cpp20Parser.StatementContext):
        pass

    # Exit a parse tree produced by cpp20Parser#statement.
    def exitStatement(self, ctx:cpp20Parser.StatementContext):
        pass


    # Enter a parse tree produced by cpp20Parser#block.
    def enterBlock(self, ctx:cpp20Parser.BlockContext):
        pass

    # Exit a parse tree produced by cpp20Parser#block.
    def exitBlock(self, ctx:cpp20Parser.BlockContext):
        pass


    # Enter a parse tree produced by cpp20Parser#functionCall.
    def enterFunctionCall(self, ctx:cpp20Parser.FunctionCallContext):
        pass

    # Exit a parse tree produced by cpp20Parser#functionCall.
    def exitFunctionCall(self, ctx:cpp20Parser.FunctionCallContext):
        pass


    # Enter a parse tree produced by cpp20Parser#ifStatement.
    def enterIfStatement(self, ctx:cpp20Parser.IfStatementContext):
        pass

    # Exit a parse tree produced by cpp20Parser#ifStatement.
    def exitIfStatement(self, ctx:cpp20Parser.IfStatementContext):
        pass


    # Enter a parse tree produced by cpp20Parser#caseStatement.
    def enterCaseStatement(self, ctx:cpp20Parser.CaseStatementContext):
        pass

    # Exit a parse tree produced by cpp20Parser#caseStatement.
    def exitCaseStatement(self, ctx:cpp20Parser.CaseStatementContext):
        pass


    # Enter a parse tree produced by cpp20Parser#switchStatement.
    def enterSwitchStatement(self, ctx:cpp20Parser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by cpp20Parser#switchStatement.
    def exitSwitchStatement(self, ctx:cpp20Parser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by cpp20Parser#whileStatement.
    def enterWhileStatement(self, ctx:cpp20Parser.WhileStatementContext):
        pass

    # Exit a parse tree produced by cpp20Parser#whileStatement.
    def exitWhileStatement(self, ctx:cpp20Parser.WhileStatementContext):
        pass


    # Enter a parse tree produced by cpp20Parser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:cpp20Parser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by cpp20Parser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:cpp20Parser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by cpp20Parser#forStatement.
    def enterForStatement(self, ctx:cpp20Parser.ForStatementContext):
        pass

    # Exit a parse tree produced by cpp20Parser#forStatement.
    def exitForStatement(self, ctx:cpp20Parser.ForStatementContext):
        pass


    # Enter a parse tree produced by cpp20Parser#forExprSet.
    def enterForExprSet(self, ctx:cpp20Parser.ForExprSetContext):
        pass

    # Exit a parse tree produced by cpp20Parser#forExprSet.
    def exitForExprSet(self, ctx:cpp20Parser.ForExprSetContext):
        pass


    # Enter a parse tree produced by cpp20Parser#returnStatement.
    def enterReturnStatement(self, ctx:cpp20Parser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by cpp20Parser#returnStatement.
    def exitReturnStatement(self, ctx:cpp20Parser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by cpp20Parser#breakStatement.
    def enterBreakStatement(self, ctx:cpp20Parser.BreakStatementContext):
        pass

    # Exit a parse tree produced by cpp20Parser#breakStatement.
    def exitBreakStatement(self, ctx:cpp20Parser.BreakStatementContext):
        pass


    # Enter a parse tree produced by cpp20Parser#continueStatement.
    def enterContinueStatement(self, ctx:cpp20Parser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by cpp20Parser#continueStatement.
    def exitContinueStatement(self, ctx:cpp20Parser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by cpp20Parser#declaration.
    def enterDeclaration(self, ctx:cpp20Parser.DeclarationContext):
        pass

    # Exit a parse tree produced by cpp20Parser#declaration.
    def exitDeclaration(self, ctx:cpp20Parser.DeclarationContext):
        pass


    # Enter a parse tree produced by cpp20Parser#arrayDeclarator.
    def enterArrayDeclarator(self, ctx:cpp20Parser.ArrayDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp20Parser#arrayDeclarator.
    def exitArrayDeclarator(self, ctx:cpp20Parser.ArrayDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp20Parser#varDeclWithoutInit.
    def enterVarDeclWithoutInit(self, ctx:cpp20Parser.VarDeclWithoutInitContext):
        pass

    # Exit a parse tree produced by cpp20Parser#varDeclWithoutInit.
    def exitVarDeclWithoutInit(self, ctx:cpp20Parser.VarDeclWithoutInitContext):
        pass


    # Enter a parse tree produced by cpp20Parser#varDeclWithInit.
    def enterVarDeclWithInit(self, ctx:cpp20Parser.VarDeclWithInitContext):
        pass

    # Exit a parse tree produced by cpp20Parser#varDeclWithInit.
    def exitVarDeclWithInit(self, ctx:cpp20Parser.VarDeclWithInitContext):
        pass


    # Enter a parse tree produced by cpp20Parser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:cpp20Parser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp20Parser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:cpp20Parser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp20Parser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:cpp20Parser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by cpp20Parser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:cpp20Parser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by cpp20Parser#functionParameter.
    def enterFunctionParameter(self, ctx:cpp20Parser.FunctionParameterContext):
        pass

    # Exit a parse tree produced by cpp20Parser#functionParameter.
    def exitFunctionParameter(self, ctx:cpp20Parser.FunctionParameterContext):
        pass


    # Enter a parse tree produced by cpp20Parser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:cpp20Parser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp20Parser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:cpp20Parser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp20Parser#integerTypeSpecifier.
    def enterIntegerTypeSpecifier(self, ctx:cpp20Parser.IntegerTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp20Parser#integerTypeSpecifier.
    def exitIntegerTypeSpecifier(self, ctx:cpp20Parser.IntegerTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp20Parser#realTypeSpecifier.
    def enterRealTypeSpecifier(self, ctx:cpp20Parser.RealTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp20Parser#realTypeSpecifier.
    def exitRealTypeSpecifier(self, ctx:cpp20Parser.RealTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp20Parser#booleanTypeSpecifier.
    def enterBooleanTypeSpecifier(self, ctx:cpp20Parser.BooleanTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp20Parser#booleanTypeSpecifier.
    def exitBooleanTypeSpecifier(self, ctx:cpp20Parser.BooleanTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp20Parser#charTypeSpecifier.
    def enterCharTypeSpecifier(self, ctx:cpp20Parser.CharTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp20Parser#charTypeSpecifier.
    def exitCharTypeSpecifier(self, ctx:cpp20Parser.CharTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp20Parser#voidTypeSpecifier.
    def enterVoidTypeSpecifier(self, ctx:cpp20Parser.VoidTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp20Parser#voidTypeSpecifier.
    def exitVoidTypeSpecifier(self, ctx:cpp20Parser.VoidTypeSpecifierContext):
        pass



del cpp20Parser