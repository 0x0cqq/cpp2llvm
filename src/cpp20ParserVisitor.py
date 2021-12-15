# Generated from grammar/cpp20Parser.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cpp20Parser import cpp20Parser
else:
    from cpp20Parser import cpp20Parser

# This class defines a complete generic visitor for a parse tree produced by cpp20Parser.

class cpp20ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cpp20Parser#literals.
    def visitLiterals(self, ctx:cpp20Parser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#floatingLiteral.
    def visitFloatingLiteral(self, ctx:cpp20Parser.FloatingLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#integerLiteral.
    def visitIntegerLiteral(self, ctx:cpp20Parser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#characterLiteral.
    def visitCharacterLiteral(self, ctx:cpp20Parser.CharacterLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#stringLiteral.
    def visitStringLiteral(self, ctx:cpp20Parser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#translationUnit.
    def visitTranslationUnit(self, ctx:cpp20Parser.TranslationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#baseSpecifierList.
    def visitBaseSpecifierList(self, ctx:cpp20Parser.BaseSpecifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#accessSpecifier.
    def visitAccessSpecifier(self, ctx:cpp20Parser.AccessSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#accessLabel.
    def visitAccessLabel(self, ctx:cpp20Parser.AccessLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#memberDeclaration.
    def visitMemberDeclaration(self, ctx:cpp20Parser.MemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#constructorDeclaration.
    def visitConstructorDeclaration(self, ctx:cpp20Parser.ConstructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#destructorDeclaration.
    def visitDestructorDeclaration(self, ctx:cpp20Parser.DestructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#memberSpecification.
    def visitMemberSpecification(self, ctx:cpp20Parser.MemberSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#classDefinition.
    def visitClassDefinition(self, ctx:cpp20Parser.ClassDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#constExpression.
    def visitConstExpression(self, ctx:cpp20Parser.ConstExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#leftExpression.
    def visitLeftExpression(self, ctx:cpp20Parser.LeftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#expression.
    def visitExpression(self, ctx:cpp20Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#statement.
    def visitStatement(self, ctx:cpp20Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#block.
    def visitBlock(self, ctx:cpp20Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#functionCall.
    def visitFunctionCall(self, ctx:cpp20Parser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#ifStatement.
    def visitIfStatement(self, ctx:cpp20Parser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#caseStatement.
    def visitCaseStatement(self, ctx:cpp20Parser.CaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#switchStatement.
    def visitSwitchStatement(self, ctx:cpp20Parser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#whileStatement.
    def visitWhileStatement(self, ctx:cpp20Parser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:cpp20Parser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#forStatement.
    def visitForStatement(self, ctx:cpp20Parser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#returnStatement.
    def visitReturnStatement(self, ctx:cpp20Parser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#breakStatement.
    def visitBreakStatement(self, ctx:cpp20Parser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#continueStatement.
    def visitContinueStatement(self, ctx:cpp20Parser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#declaration.
    def visitDeclaration(self, ctx:cpp20Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#arrayDeclarator.
    def visitArrayDeclarator(self, ctx:cpp20Parser.ArrayDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:cpp20Parser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:cpp20Parser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#functionParameter.
    def visitFunctionParameter(self, ctx:cpp20Parser.FunctionParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:cpp20Parser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#integerTypeSpecifier.
    def visitIntegerTypeSpecifier(self, ctx:cpp20Parser.IntegerTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#realTypeSpecifier.
    def visitRealTypeSpecifier(self, ctx:cpp20Parser.RealTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#booleanTypeSpecifier.
    def visitBooleanTypeSpecifier(self, ctx:cpp20Parser.BooleanTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#charTypeSpecifier.
    def visitCharTypeSpecifier(self, ctx:cpp20Parser.CharTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp20Parser#voidTypeSpecifier.
    def visitVoidTypeSpecifier(self, ctx:cpp20Parser.VoidTypeSpecifierContext):
        return self.visitChildren(ctx)



del cpp20Parser