parser grammar cpp20parser;

options {
	tokenVocab = cpp20lexer;
}


translationUnit : ;

expression : ;

statement : ;

declaration : 
;

identifier: NONDIGIT (DIGIT | NONDIGIT)*;


 
builtinTypeSpecifier :

// declarations

// not include variables, as only `extern int x;` is a declaration

/*  
+ function definition
+ template declaration
+ explicit template instantiation/specialization
+ namespace definition
+ linkage specification
+ attribution declartion
+ empty declaration (;)
+ function declaration without a decl-specifier-seq:
*/
attr : '[[' .* ']]';

declaration : ;



simpleDeclaration : ;

functionDeclaration :;

temp





initDeclarators : 
    declarator initializer
    | declarator requiresClause;

// https://en.cppreference.com/w/cpp/language/initialization
initializer : ;

// https://en.cppreference.com/w/cpp/language/constraints#Requires_clauses
requiresClause : ;

// https://en.cppreference.com/w/cpp/language/declarations#:~:text=A-,declarator,-is%20one%20of
declarator : ;

definition :  type identifier ASSIGN expression SEP ;

declSpecifier : ;

// https://en.cppreference.com/w/cpp/language/identifiers
identifier: NONDIGIT (DIGIT | NONDIGIT)*;

unqualifiedId : identifier;

qualifiedId : identifier;



cv : CONST | VOLATILE;


