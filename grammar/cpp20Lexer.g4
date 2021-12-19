lexer grammar cpp20Lexer;


LT: '<';

GT: '>';

DQUOTE: '"';

SQUOTE: '\'';

LBRACE: '{';

RBRACE: '}';

LSQUARE: '[';

RSQUARE: ']';

LPAREN: '(';

RPAREN: ')';

SHARP: '#';

COMMA: ',';

SEMI: ';';

DOT: '.';

COLON: ':';

// operators

ASSIGN: '=';

ADD: '+';

ADD_ASSIGN: '+=';

SUB: '-';

SUB_ASSIGN: '-=';

MULT: '*';

MULT_ASSIGN: '*=';

DIV: '/';

DIV_ASSIGN: '/=';

MOD: '%';

MOD_ASSIGN: '%=';

LSHIFT: '<<';

LSHIFT_ASSIGN: '<<=';

RSHIFT: '>>';

RSHIFT_ASSIGN: '>>=';

EQ: '==';

DOTS: '...';

DOT_STAR: '.*';

LEQ: '<=';

GEQ: '>=';

ARROW: '->';

ARROW_STAR: '->*';

PLUS_PLUS: '++';

MINUS_MINUS: '--';

// keywords

AND: '&&' | 'and';

AND_EQ: '&=' | 'and_eq';

ASM: 'asm';

AUTO: 'auto';

BITAND: '&' | 'bitand';

BITOR: '|' | 'bitor';

BOOL: 'bool';

BREAK: 'break';

CASE: 'case';

CATCH: 'catch';

CHAR: 'char';

CHAR8_T: 'char8_t';

CHAR16_T: 'char16_t';

CHAR32_T: 'char32_t';

CLASS: 'class';

COMPL: '~' | 'compl';

CONCEPT: 'concept';

CONST: 'const';

CONSTEVAL: 'consteval';

CONSTEXPR: 'constexpr';

CONSTINIT: 'constinit';

CONST_CAST: 'const_cast';

CONTINUE: 'continue';

DEFAULT: 'default';

DELETE: 'delete';

DO: 'do';

DOUBLE: 'double';

DYNAMIC_CAST: 'dynamic_cast';

ELSE: 'else';

ENUM: 'enum';

EXPLICIT: 'explicit';

EXPORT: 'export';

EXTERN: 'extern';

FALSE_: 'false';

FLOAT: 'float';

FOR: 'for';

FRIEND: 'friend';

GOTO: 'goto';

IF: 'if';

INLINE: 'inline';

INT: 'int';

LONG: 'long';

MUTABLE: 'mutable';

NAMESPACE: 'namespace';

NEW: 'new';

NOT: '!' | 'not';

NOT_EQ: '!=' | 'not_eq';

NULLPTR: 'nullptr';

OPERATOR: 'operator';

OR: '||' | 'or';

OR_EQ: '|=' | 'or_eq';

PRIVATE: 'private';

PROTECTED: 'protected';

PUBLIC: 'public';

REGISTER: 'register';

REINTERPRET_CAST: 'reinterpret_cast';

REQUIRES: 'requires';

RETURN: 'return';

SHORT: 'short';

SIGNED: 'signed';

SIZEOF: 'sizeof';

STATIC: 'static';

STATIC_ASSERT: 'static_assert';

STATIC_CAST: 'static_cast';

STRUCT: 'struct';

SWITCH: 'switch';

TEMPLATE: 'template';

THIS: 'this';

THREAD_LOCAL: 'thread_local';

THROW: 'throw';

TRUE_: 'true';

TRY: 'try';

TYPEDEF: 'typedef';

TYPEID: 'typeid';

TYPENAME: 'typename';

UNION: 'union';

UNSIGNED: 'unsigned';

USING: 'using';

VIRTUAL: 'virtual';

VOID: 'void';

VOLATILE: 'volatile';

WCHAR_T: 'wchar_t';

WHILE: 'while';

XOR: '^' | 'xor';

XOR_EQ: '^=' | 'xor_eq';

// 

// identifier



fragment DIGIT: '0' ..'9';

fragment OCTALDIGIT: '0' ..'7';

fragment HEXDIGIT: '0' ..'9' | 'A' ..'F' | 'a' ..'f';

fragment NONDIGIT: '_' | 'a' ..'z' | 'A' ..'Z';

fragment HEXQUAD: HEXDIGIT HEXDIGIT HEXDIGIT HEXDIGIT;

WHITESPACE: (' ' | '\t' | '\f') -> skip;

NEWLINE: ('\r' | '\n') -> skip;

LINE_COMMENT:
	'//' (~('\n' | '\r'))* ('\r'? '\n') -> channel(HIDDEN);

COMMENT: '/*' .*? '*/' -> channel(HIDDEN);

Identifier: NONDIGIT (DIGIT | NONDIGIT)*;

IntegerSuffix: UnsignedSuffix? (LongLongSuffix | LongSuffix );


// General Literals
fragment UnsignedSuffix: 'u' | 'U';

fragment LongSuffix: 'l' | 'L';

fragment LongLongSuffix: 'll' | 'LL';

DecimalLiteral: '0' | (('1' ..'9') ('0' ..'9')*) IntegerSuffix?;

FloatingLiteral:
	 (DigitSequence DecimalExponent )
	| (DigitSequence DOT DecimalExponent)
    | (DigitSequence DOT DigitSequence DecimalExponent?);

// Floating literals

DigitSequence: ('0' ..'9')+;


DecimalExponent: ('e' | 'E') (ADD | SUB)? DigitSequence;

// TBD: Optional single quotes (') can be inserted between the digits as a separator, they are
// ignored when compiling.

// Character literals

SChar: ~["\\\r\n] | Escapesequence | Universalcharactername;

CChar: ~ ['\\\r\n] | Escapesequence | Universalcharactername;

CharTypeSpecificaton: ('u8' | 'u' | 'U' | 'L');



Escapesequence:
	Simpleescapesequence
	| Octalescapesequence
	| Hexadecimalescapesequence;

Simpleescapesequence:
	'\\\''
	| '\\"'
	| '\\?'
	| '\\\\'
	| '\\a'
	| '\\b'
	| '\\f'
	| '\\n'
	| '\\r'
	| ('\\' ('\r' '\n'? | '\n'))
	| '\\t'
	| '\\v';

Octalescapesequence:
	'\\' OCTALDIGIT
	| '\\' OCTALDIGIT OCTALDIGIT
	| '\\' OCTALDIGIT OCTALDIGIT OCTALDIGIT;

Hexadecimalescapesequence: '\\x' HEXDIGIT+;

// UTF code 
Universalcharactername: '\\u' HEXQUAD | '\\U' HEXQUAD HEXQUAD;

// Strings Literals


// RawString is not supported User defined literals are not supported

