parser grammar cpp20Parser;

options {
    tokenVocab = cpp20Lexer;
}



// Integer literals

literals:
	floatingLiteral
	| integerLiteral
	| characterLiteral
	| stringLiteral;


floatingLiteral: FloatingLiteral;

integerLiteral: DecimalLiteral;

characterLiteral: CharTypeSpecificaton? SQUOTE CChar SQUOTE;

stringLiteral: StringLiteral;

// translation

translationUnit : declaration* EOF;

baseSpecifierList: (accessSpecifier? Identifier) (COMMA accessSpecifier? Identifier)*;

accessSpecifier : PUBLIC | PROTECTED | PRIVATE;

accessLabel : accessSpecifier COLON;

memberDeclaration : functionDeclaration | variableDeclarator;

constructorDeclaration :  Identifier LPAREN (functionParameter (COMMA functionParameter)*)? RPAREN  (COLON functionCall)? block;

destructorDeclaration :  COMPL Identifier LPAREN RPAREN block;

memberSpecification : (accessLabel | memberDeclaration | constructorDeclaration | destructorDeclaration)*;

classDefinition: (CLASS | STRUCT) Identifier (COLON baseSpecifierList)? LBRACE memberSpecification RBRACE SEMI;

constExpression : literals;


leftExpression :
    Identifier
    | Identifier (LSQUARE expression RSQUARE) 
    ;


expression :
    functionCall 
    | literals 
    | Identifier
    | LPAREN expression RPAREN
    | NOT expression
    | SUB expression
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
    | Identifier LSQUARE expression RSQUARE
    | leftExpression ASSIGN expression
    | leftExpression PLUS_PLUS
    | leftExpression MINUS_MINUS;
// statement 


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
    | variableDeclarator
    | arrayDeclarator
    | expression? SEMI;

block : 
    LBRACE (statement)* RBRACE;

functionCall : Identifier LPAREN (expression (COMMA expression)*)? RPAREN;

ifStatement : IF LPAREN expression RPAREN statement (ELSE statement)?;

caseStatement : CASE constExpression COLON statement;

switchStatement : SWITCH LPAREN expression RPAREN LBRACE (caseStatement)* RBRACE;

whileStatement : WHILE LPAREN expression RPAREN statement;

doWhileStatement : DO statement WHILE LPAREN expression RPAREN SEMI;

forStatement : FOR LPAREN forExprSet? SEMI expression? SEMI forExprSet? RPAREN statement;

forExprSet: expression (COMMA expression)*;

returnStatement : RETURN expression? SEMI;

breakStatement : BREAK SEMI;

continueStatement : CONTINUE SEMI;


// Declaration



declaration : 
    arrayDeclarator
    | variableDeclarator
    | functionDeclaration
    | classDefinition;

arrayDeclarator : 
    typeSpecifier Identifier LSQUARE DecimalLiteral RSQUARE (ASSIGN LBRACE expression (COMMA expression)* RBRACE)? SEMI #normalArrDecl
    | charTypeSpecifier Identifier LSQUARE DecimalLiteral RSQUARE (ASSIGN stringLiteral)? SEMI #stringDecl
    ;

// with global variable in line 2
variableDeclaration: Identifier  #varDeclWithoutInit
    | Identifier ASSIGN constExpression #varDeclWithConstInit
    | Identifier ASSIGN expression #varDeclWithInit
    ;

variableDeclarator : 
    typeSpecifier variableDeclaration (COMMA variableDeclaration)* SEMI;

functionDeclaration : 
    typeSpecifier Identifier LPAREN (functionParameter (COMMA functionParameter)*)? RPAREN SEMI #functionDecl
    | typeSpecifier Identifier LPAREN (functionParameter (COMMA functionParameter)*)? RPAREN block #functionDef
    ; 

functionParameter :
    typeSpecifier Identifier
    | DOTS;

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
    | LONG LONG;

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

