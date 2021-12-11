# Generated from grammar/cpp20Parser.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u009c")
        buf.write("\u0122\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\7\2\66\n\2\f\2\16\29\13\2\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\5\4A\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4|\n\4\f\4\16")
        buf.write("\4\177\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5\u008c\n\5\3\5\5\5\u008f\n\5\3\6\3\6\7\6\u0093\n")
        buf.write("\6\f\6\16\6\u0096\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\7\7")
        buf.write("\u009f\n\7\f\7\16\7\u00a2\13\7\5\7\u00a4\n\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00af\n\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u00bc\n\n\f\n\16\n")
        buf.write("\u00bf\13\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\5\r\u00d4\n\r")
        buf.write("\3\r\3\r\5\r\u00d8\n\r\3\r\3\r\5\r\u00dc\n\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\5\16\u00e3\n\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\21\3\21\5\21\u00ef\n\21\3\22\3\22\3")
        buf.write("\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00fb\n\23")
        buf.write("\f\23\16\23\u00fe\13\23\5\23\u0100\n\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u010d\n")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\5\26\u0114\n\26\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u011a\n\27\3\30\3\30\3\31\3\31\3\32\3")
        buf.write("\32\3\32\2\3\6\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\2\2\2\u013e\2\67\3\2\2\2\4:\3\2\2\2")
        buf.write("\6@\3\2\2\2\b\u008e\3\2\2\2\n\u0090\3\2\2\2\f\u0099\3")
        buf.write("\2\2\2\16\u00a7\3\2\2\2\20\u00b0\3\2\2\2\22\u00b5\3\2")
        buf.write("\2\2\24\u00c2\3\2\2\2\26\u00c8\3\2\2\2\30\u00d0\3\2\2")
        buf.write("\2\32\u00e0\3\2\2\2\34\u00e6\3\2\2\2\36\u00e9\3\2\2\2")
        buf.write(" \u00ee\3\2\2\2\"\u00f0\3\2\2\2$\u00f4\3\2\2\2&\u0104")
        buf.write("\3\2\2\2(\u010c\3\2\2\2*\u0113\3\2\2\2,\u0119\3\2\2\2")
        buf.write(".\u011b\3\2\2\2\60\u011d\3\2\2\2\62\u011f\3\2\2\2\64\66")
        buf.write("\5\b\5\2\65\64\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678\3")
        buf.write("\2\2\28\3\3\2\2\29\67\3\2\2\2:;\7\u0084\2\2;\5\3\2\2\2")
        buf.write("<=\b\4\1\2=A\5\f\7\2>A\7\u0084\2\2?A\7\u0083\2\2@<\3\2")
        buf.write("\2\2@>\3\2\2\2@?\3\2\2\2A}\3\2\2\2BC\f\30\2\2CD\7\22\2")
        buf.write("\2D|\5\6\4\31EF\f\27\2\2FG\7\27\2\2G|\5\6\4\30HI\f\26")
        buf.write("\2\2IJ\7\31\2\2J|\5\6\4\27KL\f\25\2\2LM\7\33\2\2M|\5\6")
        buf.write("\4\26NO\f\24\2\2OP\7\23\2\2P|\5\6\4\25QR\f\23\2\2RS\7")
        buf.write("\25\2\2S|\5\6\4\24TU\f\22\2\2UV\7/\2\2V|\5\6\4\23WX\f")
        buf.write("\21\2\2XY\7.\2\2Y|\5\6\4\22Z[\f\20\2\2[\\\7}\2\2\\|\5")
        buf.write("\6\4\21]^\f\17\2\2^_\7[\2\2_|\5\6\4\20`a\f\16\2\2ab\7")
        buf.write("*\2\2b|\5\6\4\17cd\f\r\2\2de\7\35\2\2e|\5\6\4\16fg\f\f")
        buf.write("\2\2gh\7\37\2\2h|\5\6\4\rij\f\13\2\2jk\7\3\2\2k|\5\6\4")
        buf.write("\flm\f\n\2\2mn\7\4\2\2n|\5\6\4\13op\f\t\2\2pq\7$\2\2q")
        buf.write("|\5\6\4\nrs\f\b\2\2st\7%\2\2t|\5\6\4\tuv\f\7\2\2vw\7!")
        buf.write("\2\2w|\5\6\4\bxy\f\6\2\2yz\7X\2\2z|\5\6\4\7{B\3\2\2\2")
        buf.write("{E\3\2\2\2{H\3\2\2\2{K\3\2\2\2{N\3\2\2\2{Q\3\2\2\2{T\3")
        buf.write("\2\2\2{W\3\2\2\2{Z\3\2\2\2{]\3\2\2\2{`\3\2\2\2{c\3\2\2")
        buf.write("\2{f\3\2\2\2{i\3\2\2\2{l\3\2\2\2{o\3\2\2\2{r\3\2\2\2{")
        buf.write("u\3\2\2\2{x\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~")
        buf.write("\7\3\2\2\2\177}\3\2\2\2\u0080\u008f\5\16\b\2\u0081\u008f")
        buf.write("\5\22\n\2\u0082\u008f\5\24\13\2\u0083\u008f\5\26\f\2\u0084")
        buf.write("\u008f\5\30\r\2\u0085\u008f\5\32\16\2\u0086\u008f\5\34")
        buf.write("\17\2\u0087\u008f\5\36\20\2\u0088\u008f\5\n\6\2\u0089")
        buf.write("\u008f\5 \21\2\u008a\u008c\5\6\4\2\u008b\u008a\3\2\2\2")
        buf.write("\u008b\u008c\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008f\7")
        buf.write("\17\2\2\u008e\u0080\3\2\2\2\u008e\u0081\3\2\2\2\u008e")
        buf.write("\u0082\3\2\2\2\u008e\u0083\3\2\2\2\u008e\u0084\3\2\2\2")
        buf.write("\u008e\u0085\3\2\2\2\u008e\u0086\3\2\2\2\u008e\u0087\3")
        buf.write("\2\2\2\u008e\u0088\3\2\2\2\u008e\u0089\3\2\2\2\u008e\u008b")
        buf.write("\3\2\2\2\u008f\t\3\2\2\2\u0090\u0094\7\7\2\2\u0091\u0093")
        buf.write("\5\b\5\2\u0092\u0091\3\2\2\2\u0093\u0096\3\2\2\2\u0094")
        buf.write("\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0097\3\2\2\2")
        buf.write("\u0096\u0094\3\2\2\2\u0097\u0098\7\b\2\2\u0098\13\3\2")
        buf.write("\2\2\u0099\u009a\7\u0083\2\2\u009a\u00a3\7\13\2\2\u009b")
        buf.write("\u00a0\5\6\4\2\u009c\u009d\7\16\2\2\u009d\u009f\5\6\4")
        buf.write("\2\u009e\u009c\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a3\u009b\3\2\2\2\u00a3\u00a4\3\2\2\2")
        buf.write("\u00a4\u00a5\3\2\2\2\u00a5\u00a6\7\f\2\2\u00a6\r\3\2\2")
        buf.write("\2\u00a7\u00a8\7P\2\2\u00a8\u00a9\7\13\2\2\u00a9\u00aa")
        buf.write("\5\6\4\2\u00aa\u00ab\7\f\2\2\u00ab\u00ae\5\b\5\2\u00ac")
        buf.write("\u00ad\7F\2\2\u00ad\u00af\5\b\5\2\u00ae\u00ac\3\2\2\2")
        buf.write("\u00ae\u00af\3\2\2\2\u00af\17\3\2\2\2\u00b0\u00b1\7\62")
        buf.write("\2\2\u00b1\u00b2\5\4\3\2\u00b2\u00b3\7\21\2\2\u00b3\u00b4")
        buf.write("\5\b\5\2\u00b4\21\3\2\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7")
        buf.write("\7\13\2\2\u00b7\u00b8\5\6\4\2\u00b8\u00b9\7\f\2\2\u00b9")
        buf.write("\u00bd\7\7\2\2\u00ba\u00bc\5\20\t\2\u00bb\u00ba\3\2\2")
        buf.write("\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be")
        buf.write("\3\2\2\2\u00be\u00c0\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0")
        buf.write("\u00c1\7\b\2\2\u00c1\23\3\2\2\2\u00c2\u00c3\7|\2\2\u00c3")
        buf.write("\u00c4\7\13\2\2\u00c4\u00c5\5\6\4\2\u00c5\u00c6\7\f\2")
        buf.write("\2\u00c6\u00c7\5\b\5\2\u00c7\25\3\2\2\2\u00c8\u00c9\7")
        buf.write("C\2\2\u00c9\u00ca\5\b\5\2\u00ca\u00cb\7|\2\2\u00cb\u00cc")
        buf.write("\7\13\2\2\u00cc\u00cd\5\6\4\2\u00cd\u00ce\7\f\2\2\u00ce")
        buf.write("\u00cf\7\17\2\2\u00cf\27\3\2\2\2\u00d0\u00d1\7M\2\2\u00d1")
        buf.write("\u00d3\7\13\2\2\u00d2\u00d4\5\6\4\2\u00d3\u00d2\3\2\2")
        buf.write("\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d7")
        buf.write("\7\17\2\2\u00d6\u00d8\5\6\4\2\u00d7\u00d6\3\2\2\2\u00d7")
        buf.write("\u00d8\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00db\7\17\2")
        buf.write("\2\u00da\u00dc\5\6\4\2\u00db\u00da\3\2\2\2\u00db\u00dc")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\7\f\2\2\u00de")
        buf.write("\u00df\5\b\5\2\u00df\31\3\2\2\2\u00e0\u00e2\7c\2\2\u00e1")
        buf.write("\u00e3\5\6\4\2\u00e2\u00e1\3\2\2\2\u00e2\u00e3\3\2\2\2")
        buf.write("\u00e3\u00e4\3\2\2\2\u00e4\u00e5\7\17\2\2\u00e5\33\3\2")
        buf.write("\2\2\u00e6\u00e7\7\61\2\2\u00e7\u00e8\7\17\2\2\u00e8\35")
        buf.write("\3\2\2\2\u00e9\u00ea\7@\2\2\u00ea\u00eb\7\17\2\2\u00eb")
        buf.write("\37\3\2\2\2\u00ec\u00ef\5\"\22\2\u00ed\u00ef\5$\23\2\u00ee")
        buf.write("\u00ec\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef!\3\2\2\2\u00f0")
        buf.write("\u00f1\5(\25\2\u00f1\u00f2\7\u0083\2\2\u00f2\u00f3\7\17")
        buf.write("\2\2\u00f3#\3\2\2\2\u00f4\u00f5\5(\25\2\u00f5\u00f6\7")
        buf.write("\u0083\2\2\u00f6\u00ff\7\13\2\2\u00f7\u00fc\5&\24\2\u00f8")
        buf.write("\u00f9\7\16\2\2\u00f9\u00fb\5&\24\2\u00fa\u00f8\3\2\2")
        buf.write("\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd")
        buf.write("\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff")
        buf.write("\u00f7\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\3\2\2\2")
        buf.write("\u0101\u0102\7\f\2\2\u0102\u0103\5\n\6\2\u0103%\3\2\2")
        buf.write("\2\u0104\u0105\5(\25\2\u0105\u0106\7\u0083\2\2\u0106\'")
        buf.write("\3\2\2\2\u0107\u010d\5*\26\2\u0108\u010d\5,\27\2\u0109")
        buf.write("\u010d\5.\30\2\u010a\u010d\5\60\31\2\u010b\u010d\5\62")
        buf.write("\32\2\u010c\u0107\3\2\2\2\u010c\u0108\3\2\2\2\u010c\u0109")
        buf.write("\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010b\3\2\2\2\u010d")
        buf.write(")\3\2\2\2\u010e\u0114\7R\2\2\u010f\u0114\7S\2\2\u0110")
        buf.write("\u0114\7d\2\2\u0111\u0112\7S\2\2\u0112\u0114\7S\2\2\u0113")
        buf.write("\u010e\3\2\2\2\u0113\u010f\3\2\2\2\u0113\u0110\3\2\2\2")
        buf.write("\u0113\u0111\3\2\2\2\u0114+\3\2\2\2\u0115\u011a\7L\2\2")
        buf.write("\u0116\u011a\7D\2\2\u0117\u0118\7S\2\2\u0118\u011a\7D")
        buf.write("\2\2\u0119\u0115\3\2\2\2\u0119\u0116\3\2\2\2\u0119\u0117")
        buf.write("\3\2\2\2\u011a-\3\2\2\2\u011b\u011c\7\60\2\2\u011c/\3")
        buf.write("\2\2\2\u011d\u011e\7\64\2\2\u011e\61\3\2\2\2\u011f\u0120")
        buf.write("\7y\2\2\u0120\63\3\2\2\2\27\67@{}\u008b\u008e\u0094\u00a0")
        buf.write("\u00a3\u00ae\u00bd\u00d3\u00d7\u00db\u00e2\u00ee\u00fc")
        buf.write("\u00ff\u010c\u0113\u0119")
        return buf.getvalue()


class cpp20Parser ( Parser ):

    grammarFileName = "cpp20Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'", "'\"'", "'''", "'{'", "'}'", 
                     "'['", "']'", "'('", "')'", "'#'", "','", "';'", "'.'", 
                     "':'", "'='", "'+'", "'+='", "'-'", "'-='", "'*'", 
                     "'*='", "'/'", "'/='", "'%'", "'%='", "'<<'", "'<<='", 
                     "'>>'", "'>>='", "'=='", "'...'", "'.*'", "'<='", "'>='", 
                     "'->'", "'->*'", "'++'", "'--'", "<INVALID>", "<INVALID>", 
                     "'asm'", "'auto'", "<INVALID>", "<INVALID>", "'bool'", 
                     "'break'", "'case'", "'catch'", "'char'", "'char8_t'", 
                     "'char16_t'", "'char32_t'", "'class'", "<INVALID>", 
                     "'concept'", "'const'", "'consteval'", "'constexpr'", 
                     "'constinit'", "'const_cast'", "'continue'", "'default'", 
                     "'delete'", "'do'", "'double'", "'dynamic_cast'", "'else'", 
                     "'enum'", "'explicit'", "'export'", "'extern'", "'false'", 
                     "'float'", "'for'", "'friend'", "'goto'", "'if'", "'inline'", 
                     "'int'", "'long'", "'mutable'", "'namespace'", "'new'", 
                     "<INVALID>", "<INVALID>", "'nullptr'", "'operator'", 
                     "<INVALID>", "<INVALID>", "'private'", "'protected'", 
                     "'public'", "'register'", "'reinterpret_cast'", "'requires'", 
                     "'return'", "'short'", "'signed'", "'sizeof'", "'static'", 
                     "'static_assert'", "'static_cast'", "'struct'", "'switch'", 
                     "'template'", "'this'", "'thread_local'", "'throw'", 
                     "'true'", "'try'", "'typedef'", "'typeid'", "'typename'", 
                     "'union'", "'unsigned'", "'using'", "'virtual'", "'void'", 
                     "'volatile'", "'wchar_t'", "'while'" ]

    symbolicNames = [ "<INVALID>", "LT", "GT", "DQUOTE", "SQUOTE", "LBRACE", 
                      "RBRACE", "LSQUARE", "RSQUARE", "LPAREN", "RPAREN", 
                      "SHARP", "COMMA", "SEMI", "DOT", "COLON", "ASSIGN", 
                      "ADD", "ADD_ASSIGN", "SUB", "SUB_ASSIGN", "MULT", 
                      "MULT_ASSIGN", "DIV", "DIV_ASSIGN", "MOD", "MOD_ASSIGN", 
                      "LSHIFT", "LSHIFT_ASSIGN", "RSHIFT", "RSHIFT_ASSIGN", 
                      "EQ", "DOTS", "DOT_STAR", "LEQ", "GEQ", "ARROW", "ARROW_STAR", 
                      "PLUS_PLUS", "MINUS_MINUS", "AND", "AND_EQ", "ASM", 
                      "AUTO", "BITAND", "BITOR", "BOOL", "BREAK", "CASE", 
                      "CATCH", "CHAR", "CHAR8_T", "CHAR16_T", "CHAR32_T", 
                      "CLASS", "COMPL", "CONCEPT", "CONST", "CONSTEVAL", 
                      "CONSTEXPR", "CONSTINIT", "CONST_CAST", "CONTINUE", 
                      "DEFAULT", "DELETE", "DO", "DOUBLE", "DYNAMIC_CAST", 
                      "ELSE", "ENUM", "EXPLICIT", "EXPORT", "EXTERN", "FALSE_", 
                      "FLOAT", "FOR", "FRIEND", "GOTO", "IF", "INLINE", 
                      "INT", "LONG", "MUTABLE", "NAMESPACE", "NEW", "NOT", 
                      "NOT_EQ", "NULLPTR", "OPERATOR", "OR", "OR_EQ", "PRIVATE", 
                      "PROTECTED", "PUBLIC", "REGISTER", "REINTERPRET_CAST", 
                      "REQUIRES", "RETURN", "SHORT", "SIGNED", "SIZEOF", 
                      "STATIC", "STATIC_ASSERT", "STATIC_CAST", "STRUCT", 
                      "SWITCH", "TEMPLATE", "THIS", "THREAD_LOCAL", "THROW", 
                      "TRUE_", "TRY", "TYPEDEF", "TYPEID", "TYPENAME", "UNION", 
                      "UNSIGNED", "USING", "VIRTUAL", "VOID", "VOLATILE", 
                      "WCHAR_T", "WHILE", "XOR", "XOR_EQ", "WHITESPACE", 
                      "NEWLINE", "LINE_COMMENT", "COMMENT", "Identifier", 
                      "Literals", "IntegerLiteral", "DecimalLiteral", "OctalLiteral", 
                      "HexadecimalLiteral", "BinaryLiteral", "IntegerSuffix", 
                      "UnsignedSuffix", "LongSuffix", "LongLongSuffix", 
                      "DigitSequence", "HexDigitSequence", "FloatingLiteral", 
                      "DecimalExponent", "HexExponent", "FloatSuffix", "CharacterLiteral", 
                      "CChar", "Escapesequence", "Simpleescapesequence", 
                      "Octalescapesequence", "Hexadecimalescapesequence", 
                      "Universalcharactername", "StringLiteral", "SChar" ]

    RULE_translationUnit = 0
    RULE_constExpression = 1
    RULE_expression = 2
    RULE_statement = 3
    RULE_block = 4
    RULE_functionCall = 5
    RULE_ifStatement = 6
    RULE_caseStatement = 7
    RULE_switchStatement = 8
    RULE_whileStatement = 9
    RULE_doWhileStatement = 10
    RULE_forStatement = 11
    RULE_returnStatement = 12
    RULE_breakStatement = 13
    RULE_continueStatement = 14
    RULE_declaration = 15
    RULE_variableDeclaration = 16
    RULE_functionDeclaration = 17
    RULE_functionParameter = 18
    RULE_typeSpecifier = 19
    RULE_integerTypeSpecifier = 20
    RULE_realTypeSpecifier = 21
    RULE_booleanTypeSpecifier = 22
    RULE_charTypeSpecifier = 23
    RULE_voidTypeSpecifier = 24

    ruleNames =  [ "translationUnit", "constExpression", "expression", "statement", 
                   "block", "functionCall", "ifStatement", "caseStatement", 
                   "switchStatement", "whileStatement", "doWhileStatement", 
                   "forStatement", "returnStatement", "breakStatement", 
                   "continueStatement", "declaration", "variableDeclaration", 
                   "functionDeclaration", "functionParameter", "typeSpecifier", 
                   "integerTypeSpecifier", "realTypeSpecifier", "booleanTypeSpecifier", 
                   "charTypeSpecifier", "voidTypeSpecifier" ]

    EOF = Token.EOF
    LT=1
    GT=2
    DQUOTE=3
    SQUOTE=4
    LBRACE=5
    RBRACE=6
    LSQUARE=7
    RSQUARE=8
    LPAREN=9
    RPAREN=10
    SHARP=11
    COMMA=12
    SEMI=13
    DOT=14
    COLON=15
    ASSIGN=16
    ADD=17
    ADD_ASSIGN=18
    SUB=19
    SUB_ASSIGN=20
    MULT=21
    MULT_ASSIGN=22
    DIV=23
    DIV_ASSIGN=24
    MOD=25
    MOD_ASSIGN=26
    LSHIFT=27
    LSHIFT_ASSIGN=28
    RSHIFT=29
    RSHIFT_ASSIGN=30
    EQ=31
    DOTS=32
    DOT_STAR=33
    LEQ=34
    GEQ=35
    ARROW=36
    ARROW_STAR=37
    PLUS_PLUS=38
    MINUS_MINUS=39
    AND=40
    AND_EQ=41
    ASM=42
    AUTO=43
    BITAND=44
    BITOR=45
    BOOL=46
    BREAK=47
    CASE=48
    CATCH=49
    CHAR=50
    CHAR8_T=51
    CHAR16_T=52
    CHAR32_T=53
    CLASS=54
    COMPL=55
    CONCEPT=56
    CONST=57
    CONSTEVAL=58
    CONSTEXPR=59
    CONSTINIT=60
    CONST_CAST=61
    CONTINUE=62
    DEFAULT=63
    DELETE=64
    DO=65
    DOUBLE=66
    DYNAMIC_CAST=67
    ELSE=68
    ENUM=69
    EXPLICIT=70
    EXPORT=71
    EXTERN=72
    FALSE_=73
    FLOAT=74
    FOR=75
    FRIEND=76
    GOTO=77
    IF=78
    INLINE=79
    INT=80
    LONG=81
    MUTABLE=82
    NAMESPACE=83
    NEW=84
    NOT=85
    NOT_EQ=86
    NULLPTR=87
    OPERATOR=88
    OR=89
    OR_EQ=90
    PRIVATE=91
    PROTECTED=92
    PUBLIC=93
    REGISTER=94
    REINTERPRET_CAST=95
    REQUIRES=96
    RETURN=97
    SHORT=98
    SIGNED=99
    SIZEOF=100
    STATIC=101
    STATIC_ASSERT=102
    STATIC_CAST=103
    STRUCT=104
    SWITCH=105
    TEMPLATE=106
    THIS=107
    THREAD_LOCAL=108
    THROW=109
    TRUE_=110
    TRY=111
    TYPEDEF=112
    TYPEID=113
    TYPENAME=114
    UNION=115
    UNSIGNED=116
    USING=117
    VIRTUAL=118
    VOID=119
    VOLATILE=120
    WCHAR_T=121
    WHILE=122
    XOR=123
    XOR_EQ=124
    WHITESPACE=125
    NEWLINE=126
    LINE_COMMENT=127
    COMMENT=128
    Identifier=129
    Literals=130
    IntegerLiteral=131
    DecimalLiteral=132
    OctalLiteral=133
    HexadecimalLiteral=134
    BinaryLiteral=135
    IntegerSuffix=136
    UnsignedSuffix=137
    LongSuffix=138
    LongLongSuffix=139
    DigitSequence=140
    HexDigitSequence=141
    FloatingLiteral=142
    DecimalExponent=143
    HexExponent=144
    FloatSuffix=145
    CharacterLiteral=146
    CChar=147
    Escapesequence=148
    Simpleescapesequence=149
    Octalescapesequence=150
    Hexadecimalescapesequence=151
    Universalcharactername=152
    StringLiteral=153
    SChar=154

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TranslationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.StatementContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.StatementContext,i)


        def getRuleIndex(self):
            return cpp20Parser.RULE_translationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTranslationUnit" ):
                listener.enterTranslationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTranslationUnit" ):
                listener.exitTranslationUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTranslationUnit" ):
                return visitor.visitTranslationUnit(self)
            else:
                return visitor.visitChildren(self)




    def translationUnit(self):

        localctx = cpp20Parser.TranslationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_translationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & ((1 << (cpp20Parser.LBRACE - 5)) | (1 << (cpp20Parser.SEMI - 5)) | (1 << (cpp20Parser.BOOL - 5)) | (1 << (cpp20Parser.BREAK - 5)) | (1 << (cpp20Parser.CHAR - 5)) | (1 << (cpp20Parser.CONTINUE - 5)) | (1 << (cpp20Parser.DO - 5)) | (1 << (cpp20Parser.DOUBLE - 5)))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (cpp20Parser.FLOAT - 74)) | (1 << (cpp20Parser.FOR - 74)) | (1 << (cpp20Parser.IF - 74)) | (1 << (cpp20Parser.INT - 74)) | (1 << (cpp20Parser.LONG - 74)) | (1 << (cpp20Parser.RETURN - 74)) | (1 << (cpp20Parser.SHORT - 74)) | (1 << (cpp20Parser.SWITCH - 74)) | (1 << (cpp20Parser.VOID - 74)) | (1 << (cpp20Parser.WHILE - 74)) | (1 << (cpp20Parser.Identifier - 74)) | (1 << (cpp20Parser.Literals - 74)))) != 0):
                self.state = 50
                self.statement()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Literals(self):
            return self.getToken(cpp20Parser.Literals, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_constExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstExpression" ):
                listener.enterConstExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstExpression" ):
                listener.exitConstExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstExpression" ):
                return visitor.visitConstExpression(self)
            else:
                return visitor.visitChildren(self)




    def constExpression(self):

        localctx = cpp20Parser.ConstExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_constExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(cpp20Parser.Literals)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(cpp20Parser.FunctionCallContext,0)


        def Literals(self):
            return self.getToken(cpp20Parser.Literals, 0)

        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.ExpressionContext,i)


        def ASSIGN(self):
            return self.getToken(cpp20Parser.ASSIGN, 0)

        def MULT(self):
            return self.getToken(cpp20Parser.MULT, 0)

        def DIV(self):
            return self.getToken(cpp20Parser.DIV, 0)

        def MOD(self):
            return self.getToken(cpp20Parser.MOD, 0)

        def ADD(self):
            return self.getToken(cpp20Parser.ADD, 0)

        def SUB(self):
            return self.getToken(cpp20Parser.SUB, 0)

        def BITOR(self):
            return self.getToken(cpp20Parser.BITOR, 0)

        def BITAND(self):
            return self.getToken(cpp20Parser.BITAND, 0)

        def XOR(self):
            return self.getToken(cpp20Parser.XOR, 0)

        def OR(self):
            return self.getToken(cpp20Parser.OR, 0)

        def AND(self):
            return self.getToken(cpp20Parser.AND, 0)

        def LSHIFT(self):
            return self.getToken(cpp20Parser.LSHIFT, 0)

        def RSHIFT(self):
            return self.getToken(cpp20Parser.RSHIFT, 0)

        def LT(self):
            return self.getToken(cpp20Parser.LT, 0)

        def GT(self):
            return self.getToken(cpp20Parser.GT, 0)

        def LEQ(self):
            return self.getToken(cpp20Parser.LEQ, 0)

        def GEQ(self):
            return self.getToken(cpp20Parser.GEQ, 0)

        def EQ(self):
            return self.getToken(cpp20Parser.EQ, 0)

        def NOT_EQ(self):
            return self.getToken(cpp20Parser.NOT_EQ, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = cpp20Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 59
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 60
                self.match(cpp20Parser.Literals)
                pass

            elif la_ == 3:
                self.state = 61
                self.match(cpp20Parser.Identifier)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 121
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 64
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 65
                        self.match(cpp20Parser.ASSIGN)
                        self.state = 66
                        self.expression(23)
                        pass

                    elif la_ == 2:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 67
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 68
                        self.match(cpp20Parser.MULT)
                        self.state = 69
                        self.expression(22)
                        pass

                    elif la_ == 3:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 70
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 71
                        self.match(cpp20Parser.DIV)
                        self.state = 72
                        self.expression(21)
                        pass

                    elif la_ == 4:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 73
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 74
                        self.match(cpp20Parser.MOD)
                        self.state = 75
                        self.expression(20)
                        pass

                    elif la_ == 5:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 76
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 77
                        self.match(cpp20Parser.ADD)
                        self.state = 78
                        self.expression(19)
                        pass

                    elif la_ == 6:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 79
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 80
                        self.match(cpp20Parser.SUB)
                        self.state = 81
                        self.expression(18)
                        pass

                    elif la_ == 7:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 82
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 83
                        self.match(cpp20Parser.BITOR)
                        self.state = 84
                        self.expression(17)
                        pass

                    elif la_ == 8:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 85
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 86
                        self.match(cpp20Parser.BITAND)
                        self.state = 87
                        self.expression(16)
                        pass

                    elif la_ == 9:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 88
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 89
                        self.match(cpp20Parser.XOR)
                        self.state = 90
                        self.expression(15)
                        pass

                    elif la_ == 10:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 91
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 92
                        self.match(cpp20Parser.OR)
                        self.state = 93
                        self.expression(14)
                        pass

                    elif la_ == 11:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 94
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 95
                        self.match(cpp20Parser.AND)
                        self.state = 96
                        self.expression(13)
                        pass

                    elif la_ == 12:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 97
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 98
                        self.match(cpp20Parser.LSHIFT)
                        self.state = 99
                        self.expression(12)
                        pass

                    elif la_ == 13:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 100
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 101
                        self.match(cpp20Parser.RSHIFT)
                        self.state = 102
                        self.expression(11)
                        pass

                    elif la_ == 14:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 103
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 104
                        self.match(cpp20Parser.LT)
                        self.state = 105
                        self.expression(10)
                        pass

                    elif la_ == 15:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 106
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 107
                        self.match(cpp20Parser.GT)
                        self.state = 108
                        self.expression(9)
                        pass

                    elif la_ == 16:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 109
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 110
                        self.match(cpp20Parser.LEQ)
                        self.state = 111
                        self.expression(8)
                        pass

                    elif la_ == 17:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 112
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 113
                        self.match(cpp20Parser.GEQ)
                        self.state = 114
                        self.expression(7)
                        pass

                    elif la_ == 18:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 115
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 116
                        self.match(cpp20Parser.EQ)
                        self.state = 117
                        self.expression(6)
                        pass

                    elif la_ == 19:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 118
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 119
                        self.match(cpp20Parser.NOT_EQ)
                        self.state = 120
                        self.expression(5)
                        pass

             
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(cpp20Parser.IfStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(cpp20Parser.SwitchStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(cpp20Parser.WhileStatementContext,0)


        def doWhileStatement(self):
            return self.getTypedRuleContext(cpp20Parser.DoWhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(cpp20Parser.ForStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(cpp20Parser.ReturnStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(cpp20Parser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(cpp20Parser.ContinueStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(cpp20Parser.BlockContext,0)


        def declaration(self):
            return self.getTypedRuleContext(cpp20Parser.DeclarationContext,0)


        def SEMI(self):
            return self.getToken(cpp20Parser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp20Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return cpp20Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = cpp20Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cpp20Parser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.ifStatement()
                pass
            elif token in [cpp20Parser.SWITCH]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.switchStatement()
                pass
            elif token in [cpp20Parser.WHILE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.whileStatement()
                pass
            elif token in [cpp20Parser.DO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.doWhileStatement()
                pass
            elif token in [cpp20Parser.FOR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 130
                self.forStatement()
                pass
            elif token in [cpp20Parser.RETURN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 131
                self.returnStatement()
                pass
            elif token in [cpp20Parser.BREAK]:
                self.enterOuterAlt(localctx, 7)
                self.state = 132
                self.breakStatement()
                pass
            elif token in [cpp20Parser.CONTINUE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 133
                self.continueStatement()
                pass
            elif token in [cpp20Parser.LBRACE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 134
                self.block()
                pass
            elif token in [cpp20Parser.BOOL, cpp20Parser.CHAR, cpp20Parser.DOUBLE, cpp20Parser.FLOAT, cpp20Parser.INT, cpp20Parser.LONG, cpp20Parser.SHORT, cpp20Parser.VOID]:
                self.enterOuterAlt(localctx, 10)
                self.state = 135
                self.declaration()
                pass
            elif token in [cpp20Parser.SEMI, cpp20Parser.Identifier, cpp20Parser.Literals]:
                self.enterOuterAlt(localctx, 11)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==cpp20Parser.Identifier or _la==cpp20Parser.Literals:
                    self.state = 136
                    self.expression(0)


                self.state = 139
                self.match(cpp20Parser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(cpp20Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(cpp20Parser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.StatementContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.StatementContext,i)


        def getRuleIndex(self):
            return cpp20Parser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = cpp20Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(cpp20Parser.LBRACE)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & ((1 << (cpp20Parser.LBRACE - 5)) | (1 << (cpp20Parser.SEMI - 5)) | (1 << (cpp20Parser.BOOL - 5)) | (1 << (cpp20Parser.BREAK - 5)) | (1 << (cpp20Parser.CHAR - 5)) | (1 << (cpp20Parser.CONTINUE - 5)) | (1 << (cpp20Parser.DO - 5)) | (1 << (cpp20Parser.DOUBLE - 5)))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (cpp20Parser.FLOAT - 74)) | (1 << (cpp20Parser.FOR - 74)) | (1 << (cpp20Parser.IF - 74)) | (1 << (cpp20Parser.INT - 74)) | (1 << (cpp20Parser.LONG - 74)) | (1 << (cpp20Parser.RETURN - 74)) | (1 << (cpp20Parser.SHORT - 74)) | (1 << (cpp20Parser.SWITCH - 74)) | (1 << (cpp20Parser.VOID - 74)) | (1 << (cpp20Parser.WHILE - 74)) | (1 << (cpp20Parser.Identifier - 74)) | (1 << (cpp20Parser.Literals - 74)))) != 0):
                self.state = 143
                self.statement()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
            self.match(cpp20Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(cpp20Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(cpp20Parser.RPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(cpp20Parser.COMMA)
            else:
                return self.getToken(cpp20Parser.COMMA, i)

        def getRuleIndex(self):
            return cpp20Parser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = cpp20Parser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(cpp20Parser.Identifier)
            self.state = 152
            self.match(cpp20Parser.LPAREN)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.Identifier or _la==cpp20Parser.Literals:
                self.state = 153
                self.expression(0)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cpp20Parser.COMMA:
                    self.state = 154
                    self.match(cpp20Parser.COMMA)
                    self.state = 155
                    self.expression(0)
                    self.state = 160
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 163
            self.match(cpp20Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(cpp20Parser.IF, 0)

        def LPAREN(self):
            return self.getToken(cpp20Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp20Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(cpp20Parser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.StatementContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.StatementContext,i)


        def ELSE(self):
            return self.getToken(cpp20Parser.ELSE, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = cpp20Parser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(cpp20Parser.IF)
            self.state = 166
            self.match(cpp20Parser.LPAREN)
            self.state = 167
            self.expression(0)
            self.state = 168
            self.match(cpp20Parser.RPAREN)
            self.state = 169
            self.statement()
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 170
                self.match(cpp20Parser.ELSE)
                self.state = 171
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(cpp20Parser.CASE, 0)

        def constExpression(self):
            return self.getTypedRuleContext(cpp20Parser.ConstExpressionContext,0)


        def COLON(self):
            return self.getToken(cpp20Parser.COLON, 0)

        def statement(self):
            return self.getTypedRuleContext(cpp20Parser.StatementContext,0)


        def getRuleIndex(self):
            return cpp20Parser.RULE_caseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseStatement" ):
                listener.enterCaseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseStatement" ):
                listener.exitCaseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseStatement" ):
                return visitor.visitCaseStatement(self)
            else:
                return visitor.visitChildren(self)




    def caseStatement(self):

        localctx = cpp20Parser.CaseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_caseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(cpp20Parser.CASE)
            self.state = 175
            self.constExpression()
            self.state = 176
            self.match(cpp20Parser.COLON)
            self.state = 177
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(cpp20Parser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(cpp20Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp20Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(cpp20Parser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(cpp20Parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(cpp20Parser.RBRACE, 0)

        def caseStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.CaseStatementContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.CaseStatementContext,i)


        def getRuleIndex(self):
            return cpp20Parser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStatement" ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)




    def switchStatement(self):

        localctx = cpp20Parser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(cpp20Parser.SWITCH)
            self.state = 180
            self.match(cpp20Parser.LPAREN)
            self.state = 181
            self.expression(0)
            self.state = 182
            self.match(cpp20Parser.RPAREN)
            self.state = 183
            self.match(cpp20Parser.LBRACE)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cpp20Parser.CASE:
                self.state = 184
                self.caseStatement()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 190
            self.match(cpp20Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(cpp20Parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(cpp20Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp20Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(cpp20Parser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(cpp20Parser.StatementContext,0)


        def getRuleIndex(self):
            return cpp20Parser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = cpp20Parser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(cpp20Parser.WHILE)
            self.state = 193
            self.match(cpp20Parser.LPAREN)
            self.state = 194
            self.expression(0)
            self.state = 195
            self.match(cpp20Parser.RPAREN)
            self.state = 196
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(cpp20Parser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(cpp20Parser.StatementContext,0)


        def WHILE(self):
            return self.getToken(cpp20Parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(cpp20Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp20Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(cpp20Parser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(cpp20Parser.SEMI, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_doWhileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStatement" ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStatement" ):
                listener.exitDoWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoWhileStatement" ):
                return visitor.visitDoWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def doWhileStatement(self):

        localctx = cpp20Parser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(cpp20Parser.DO)
            self.state = 199
            self.statement()
            self.state = 200
            self.match(cpp20Parser.WHILE)
            self.state = 201
            self.match(cpp20Parser.LPAREN)
            self.state = 202
            self.expression(0)
            self.state = 203
            self.match(cpp20Parser.RPAREN)
            self.state = 204
            self.match(cpp20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(cpp20Parser.FOR, 0)

        def LPAREN(self):
            return self.getToken(cpp20Parser.LPAREN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(cpp20Parser.SEMI)
            else:
                return self.getToken(cpp20Parser.SEMI, i)

        def RPAREN(self):
            return self.getToken(cpp20Parser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(cpp20Parser.StatementContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return cpp20Parser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = cpp20Parser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(cpp20Parser.FOR)
            self.state = 207
            self.match(cpp20Parser.LPAREN)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.Identifier or _la==cpp20Parser.Literals:
                self.state = 208
                self.expression(0)


            self.state = 211
            self.match(cpp20Parser.SEMI)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.Identifier or _la==cpp20Parser.Literals:
                self.state = 212
                self.expression(0)


            self.state = 215
            self.match(cpp20Parser.SEMI)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.Identifier or _la==cpp20Parser.Literals:
                self.state = 216
                self.expression(0)


            self.state = 219
            self.match(cpp20Parser.RPAREN)
            self.state = 220
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(cpp20Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(cpp20Parser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp20Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return cpp20Parser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = cpp20Parser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(cpp20Parser.RETURN)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.Identifier or _la==cpp20Parser.Literals:
                self.state = 223
                self.expression(0)


            self.state = 226
            self.match(cpp20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(cpp20Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(cpp20Parser.SEMI, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = cpp20Parser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(cpp20Parser.BREAK)
            self.state = 229
            self.match(cpp20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(cpp20Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(cpp20Parser.SEMI, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = cpp20Parser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(cpp20Parser.CONTINUE)
            self.state = 232
            self.match(cpp20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(cpp20Parser.VariableDeclarationContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(cpp20Parser.FunctionDeclarationContext,0)


        def getRuleIndex(self):
            return cpp20Parser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = cpp20Parser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_declaration)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.functionDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.TypeSpecifierContext,0)


        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)

        def SEMI(self):
            return self.getToken(cpp20Parser.SEMI, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = cpp20Parser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.typeSpecifier()
            self.state = 239
            self.match(cpp20Parser.Identifier)
            self.state = 240
            self.match(cpp20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.TypeSpecifierContext,0)


        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(cpp20Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(cpp20Parser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(cpp20Parser.BlockContext,0)


        def functionParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.FunctionParameterContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.FunctionParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(cpp20Parser.COMMA)
            else:
                return self.getToken(cpp20Parser.COMMA, i)

        def getRuleIndex(self):
            return cpp20Parser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = cpp20Parser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.typeSpecifier()
            self.state = 243
            self.match(cpp20Parser.Identifier)
            self.state = 244
            self.match(cpp20Parser.LPAREN)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.BOOL or _la==cpp20Parser.CHAR or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (cpp20Parser.DOUBLE - 66)) | (1 << (cpp20Parser.FLOAT - 66)) | (1 << (cpp20Parser.INT - 66)) | (1 << (cpp20Parser.LONG - 66)) | (1 << (cpp20Parser.SHORT - 66)) | (1 << (cpp20Parser.VOID - 66)))) != 0):
                self.state = 245
                self.functionParameter()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cpp20Parser.COMMA:
                    self.state = 246
                    self.match(cpp20Parser.COMMA)
                    self.state = 247
                    self.functionParameter()
                    self.state = 252
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 255
            self.match(cpp20Parser.RPAREN)
            self.state = 256
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.TypeSpecifierContext,0)


        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_functionParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionParameter" ):
                listener.enterFunctionParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionParameter" ):
                listener.exitFunctionParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionParameter" ):
                return visitor.visitFunctionParameter(self)
            else:
                return visitor.visitChildren(self)




    def functionParameter(self):

        localctx = cpp20Parser.FunctionParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_functionParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.typeSpecifier()
            self.state = 259
            self.match(cpp20Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integerTypeSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.IntegerTypeSpecifierContext,0)


        def realTypeSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.RealTypeSpecifierContext,0)


        def booleanTypeSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.BooleanTypeSpecifierContext,0)


        def charTypeSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.CharTypeSpecifierContext,0)


        def voidTypeSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.VoidTypeSpecifierContext,0)


        def getRuleIndex(self):
            return cpp20Parser.RULE_typeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpecifier" ):
                listener.enterTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpecifier" ):
                listener.exitTypeSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpecifier" ):
                return visitor.visitTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def typeSpecifier(self):

        localctx = cpp20Parser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_typeSpecifier)
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.integerTypeSpecifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.realTypeSpecifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 263
                self.booleanTypeSpecifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 264
                self.charTypeSpecifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 265
                self.voidTypeSpecifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerTypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(cpp20Parser.INT, 0)

        def LONG(self, i:int=None):
            if i is None:
                return self.getTokens(cpp20Parser.LONG)
            else:
                return self.getToken(cpp20Parser.LONG, i)

        def SHORT(self):
            return self.getToken(cpp20Parser.SHORT, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_integerTypeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegerTypeSpecifier" ):
                listener.enterIntegerTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegerTypeSpecifier" ):
                listener.exitIntegerTypeSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerTypeSpecifier" ):
                return visitor.visitIntegerTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def integerTypeSpecifier(self):

        localctx = cpp20Parser.IntegerTypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_integerTypeSpecifier)
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(cpp20Parser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.match(cpp20Parser.LONG)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 270
                self.match(cpp20Parser.SHORT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 271
                self.match(cpp20Parser.LONG)
                self.state = 272
                self.match(cpp20Parser.LONG)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RealTypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(cpp20Parser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(cpp20Parser.DOUBLE, 0)

        def LONG(self):
            return self.getToken(cpp20Parser.LONG, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_realTypeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRealTypeSpecifier" ):
                listener.enterRealTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRealTypeSpecifier" ):
                listener.exitRealTypeSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRealTypeSpecifier" ):
                return visitor.visitRealTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def realTypeSpecifier(self):

        localctx = cpp20Parser.RealTypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_realTypeSpecifier)
        try:
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cpp20Parser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(cpp20Parser.FLOAT)
                pass
            elif token in [cpp20Parser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.match(cpp20Parser.DOUBLE)
                pass
            elif token in [cpp20Parser.LONG]:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.match(cpp20Parser.LONG)
                self.state = 278
                self.match(cpp20Parser.DOUBLE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanTypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(cpp20Parser.BOOL, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_booleanTypeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanTypeSpecifier" ):
                listener.enterBooleanTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanTypeSpecifier" ):
                listener.exitBooleanTypeSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanTypeSpecifier" ):
                return visitor.visitBooleanTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def booleanTypeSpecifier(self):

        localctx = cpp20Parser.BooleanTypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_booleanTypeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(cpp20Parser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharTypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(cpp20Parser.CHAR, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_charTypeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharTypeSpecifier" ):
                listener.enterCharTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharTypeSpecifier" ):
                listener.exitCharTypeSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharTypeSpecifier" ):
                return visitor.visitCharTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def charTypeSpecifier(self):

        localctx = cpp20Parser.CharTypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_charTypeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(cpp20Parser.CHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidTypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(cpp20Parser.VOID, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_voidTypeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoidTypeSpecifier" ):
                listener.enterVoidTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoidTypeSpecifier" ):
                listener.exitVoidTypeSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoidTypeSpecifier" ):
                return visitor.visitVoidTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def voidTypeSpecifier(self):

        localctx = cpp20Parser.VoidTypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_voidTypeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(cpp20Parser.VOID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 4)
         




