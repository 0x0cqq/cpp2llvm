parser grammar cpp20Parser;

options {
    tokenVocab = cpp20Lexer;
}

translationUnit : statement*;

constExpression : Literals;

expression :
    expression ASSIGN expression
    | expression MULT expression 
    | expression DIV expression 
    | expression MOD expression 
    | expression ADD expression 
    | expression SUB expression 
    | expression BITOR expression
    | expression BITAND expression
    | expression XOR expression
    | expression OR expression
    | expression AND expression
    | expression LSHIFT expression
    | expression RSHIFT expression
    | expression LT expression
    | expression GT expression
    | expression LEQ expression
    | expression GEQ expression
    | expression EQ expression
    | expression NOT_EQ expression
    | functionCall | Literals | Identifier;


statement : 
    ifStatement
    | switchStatement
    | whileStatement
    | doWhileStatement
    | forStatement
    | returnStatement
    | breakStatement
    | continueStatement
    | block
    | declaration
    | expression? SEMI;
block : 
    LBRACE (statement)* RBRACE;




functionCall : Identifier LPAREN (expression (COMMA expression)*)? RPAREN;

ifStatement : IF LPAREN expression RPAREN statement (ELSE statement)?;

caseStatement : CASE constExpression COLON statement;

switchStatement : SWITCH LPAREN expression RPAREN LBRACE (caseStatement)* RBRACE;

whileStatement : WHILE LPAREN expression RPAREN statement;

doWhileStatement : DO statement WHILE LPAREN expression RPAREN SEMI;

forStatement : FOR LPAREN expression? SEMI expression? SEMI expression? RPAREN statement;

returnStatement : RETURN expression? SEMI;

breakStatement : BREAK SEMI;

continueStatement : CONTINUE SEMI;


declaration : 
    variableDeclaration
    | functionDeclaration
    ;

variableDeclaration : 
    typeSpecifier Identifier SEMI;

functionDeclaration : 
    typeSpecifier Identifier LPAREN (functionParameter (COMMA functionParameter)*)? RPAREN block;

functionParameter :
    typeSpecifier Identifier;

typeSpecifier : 
    integerTypeSpecifier
    | realTypeSpecifier
    | booleanTypeSpecifier
    | charTypeSpecifier
    | voidTypeSpecifier
    ;

integerTypeSpecifier : 
    INT
    | LONG
    | SHORT
    | LONG  LONG;

realTypeSpecifier:
    FLOAT
    | DOUBLE
    | LONG DOUBLE
    ;

booleanTypeSpecifier:
    BOOL
    ;

charTypeSpecifier:
    CHAR
    ;

voidTypeSpecifier:
    VOID
    ;

