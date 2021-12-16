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

integerLiteral: DecimalLiteral IntegerSuffix?;

characterLiteral: CharTypeSpecificaton? SQUOTE CChar SQUOTE;

stringLiteral: CharTypeSpecificaton? DQUOTE SChar* DQUOTE;


// translation

translationUnit : declaration*;

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
    | Identifier (LSQUARE DecimalLiteral RSQUARE) ;

expression :
    functionCall 
    | literals 
    | Identifier
    | LPAREN expression RPAREN
    | NOT expression
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
    | Identifier LSQUARE DecimalLiteral RSQUARE
    | leftExpression ASSIGN expression;
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

forStatement : FOR LPAREN expression? SEMI expression? SEMI expression? RPAREN statement;

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
    typeSpecifier Identifier LSQUARE DecimalLiteral RSQUARE (ASSIGN LBRACE expression (COMMA expression)* RBRACE)?;

variableDeclaration: Identifier  #varDeclWithoutInit
    | Identifier ASSIGN expression #varDeclWithInit
    ;

variableDeclarator : 
    typeSpecifier variableDeclaration (COMMA variableDeclaration)* SEMI;

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

