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
        buf.write("\u01a3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2\7\2H\n\2\f\2")
        buf.write("\16\2K\13\2\3\3\5\3N\n\3\3\3\3\3\3\3\3\3\5\3T\n\3\3\3")
        buf.write("\7\3W\n\3\f\3\16\3Z\13\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\5")
        buf.write("\6c\n\6\3\7\3\7\3\7\3\7\3\7\7\7j\n\7\f\7\16\7m\13\7\5")
        buf.write("\7o\n\7\3\7\3\7\3\7\5\7t\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\7\t\u0082\n\t\f\t\16\t\u0085\13")
        buf.write("\t\3\n\3\n\3\n\3\n\5\n\u008b\n\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\5\f\u0098\n\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\7\f\u00d8\n\f\f\f\16\f\u00db\13\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00e9")
        buf.write("\n\r\3\r\5\r\u00ec\n\r\3\16\3\16\7\16\u00f0\n\16\f\16")
        buf.write("\16\16\u00f3\13\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\7\17\u00fc\n\17\f\17\16\17\u00ff\13\17\5\17\u0101\n\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u010c")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\7\22\u0119\n\22\f\22\16\22\u011c\13\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\5\25\u0131\n\25\3\25\3")
        buf.write("\25\5\25\u0135\n\25\3\25\3\25\5\25\u0139\n\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\5\26\u0140\n\26\3\26\3\26\3\27\3\27\3")
        buf.write("\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\5\31\u014e\n\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\7\32")
        buf.write("\u015a\n\32\f\32\16\32\u015d\13\32\3\32\3\32\5\32\u0161")
        buf.write("\n\32\3\33\3\33\3\33\3\33\5\33\u0167\n\33\3\33\3\33\3")
        buf.write("\33\3\33\5\33\u016d\n\33\7\33\u016f\n\33\f\33\16\33\u0172")
        buf.write("\13\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u017c")
        buf.write("\n\34\f\34\16\34\u017f\13\34\5\34\u0181\n\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\5\36\u018e")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u0195\n\37\3 \3 \3")
        buf.write(" \3 \5 \u019b\n \3!\3!\3\"\3\"\3#\3#\3#\2\3\26$\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BD\2\4\3\2]_\4\288jj\2\u01cb\2I\3\2\2\2\4M\3\2\2")
        buf.write("\2\6[\3\2\2\2\b]\3\2\2\2\nb\3\2\2\2\fd\3\2\2\2\16w\3\2")
        buf.write("\2\2\20\u0083\3\2\2\2\22\u0086\3\2\2\2\24\u0091\3\2\2")
        buf.write("\2\26\u0097\3\2\2\2\30\u00eb\3\2\2\2\32\u00ed\3\2\2\2")
        buf.write("\34\u00f6\3\2\2\2\36\u0104\3\2\2\2 \u010d\3\2\2\2\"\u0112")
        buf.write("\3\2\2\2$\u011f\3\2\2\2&\u0125\3\2\2\2(\u012d\3\2\2\2")
        buf.write("*\u013d\3\2\2\2,\u0143\3\2\2\2.\u0146\3\2\2\2\60\u014d")
        buf.write("\3\2\2\2\62\u014f\3\2\2\2\64\u0162\3\2\2\2\66\u0175\3")
        buf.write("\2\2\28\u0185\3\2\2\2:\u018d\3\2\2\2<\u0194\3\2\2\2>\u019a")
        buf.write("\3\2\2\2@\u019c\3\2\2\2B\u019e\3\2\2\2D\u01a0\3\2\2\2")
        buf.write("FH\5\60\31\2GF\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2J")
        buf.write("\3\3\2\2\2KI\3\2\2\2LN\5\6\4\2ML\3\2\2\2MN\3\2\2\2NO\3")
        buf.write("\2\2\2OP\7\u0083\2\2PX\3\2\2\2QS\7\16\2\2RT\5\6\4\2SR")
        buf.write("\3\2\2\2ST\3\2\2\2TU\3\2\2\2UW\7\u0083\2\2VQ\3\2\2\2W")
        buf.write("Z\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y\5\3\2\2\2ZX\3\2\2\2[\\")
        buf.write("\t\2\2\2\\\7\3\2\2\2]^\5\6\4\2^_\7\21\2\2_\t\3\2\2\2`")
        buf.write("c\5\66\34\2ac\5\64\33\2b`\3\2\2\2ba\3\2\2\2c\13\3\2\2")
        buf.write("\2de\7\u0083\2\2en\7\13\2\2fk\58\35\2gh\7\16\2\2hj\58")
        buf.write("\35\2ig\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2lo\3\2\2")
        buf.write("\2mk\3\2\2\2nf\3\2\2\2no\3\2\2\2op\3\2\2\2ps\7\f\2\2q")
        buf.write("r\7\21\2\2rt\5\34\17\2sq\3\2\2\2st\3\2\2\2tu\3\2\2\2u")
        buf.write("v\5\32\16\2v\r\3\2\2\2wx\79\2\2xy\7\u0083\2\2yz\7\13\2")
        buf.write("\2z{\7\f\2\2{|\5\32\16\2|\17\3\2\2\2}\u0082\5\b\5\2~\u0082")
        buf.write("\5\n\6\2\177\u0082\5\f\7\2\u0080\u0082\5\16\b\2\u0081")
        buf.write("}\3\2\2\2\u0081~\3\2\2\2\u0081\177\3\2\2\2\u0081\u0080")
        buf.write("\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0083")
        buf.write("\u0084\3\2\2\2\u0084\21\3\2\2\2\u0085\u0083\3\2\2\2\u0086")
        buf.write("\u0087\t\3\2\2\u0087\u008a\7\u0083\2\2\u0088\u0089\7\21")
        buf.write("\2\2\u0089\u008b\5\4\3\2\u008a\u0088\3\2\2\2\u008a\u008b")
        buf.write("\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\7\7\2\2\u008d")
        buf.write("\u008e\5\20\t\2\u008e\u008f\7\b\2\2\u008f\u0090\7\17\2")
        buf.write("\2\u0090\23\3\2\2\2\u0091\u0092\7\u0084\2\2\u0092\25\3")
        buf.write("\2\2\2\u0093\u0094\b\f\1\2\u0094\u0098\5\34\17\2\u0095")
        buf.write("\u0098\7\u0084\2\2\u0096\u0098\7\u0083\2\2\u0097\u0093")
        buf.write("\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2\2\u0098")
        buf.write("\u00d9\3\2\2\2\u0099\u009a\f\31\2\2\u009a\u009b\7\22\2")
        buf.write("\2\u009b\u00d8\5\26\f\32\u009c\u009d\f\30\2\2\u009d\u009e")
        buf.write("\7\27\2\2\u009e\u00d8\5\26\f\31\u009f\u00a0\f\27\2\2\u00a0")
        buf.write("\u00a1\7\31\2\2\u00a1\u00d8\5\26\f\30\u00a2\u00a3\f\26")
        buf.write("\2\2\u00a3\u00a4\7\33\2\2\u00a4\u00d8\5\26\f\27\u00a5")
        buf.write("\u00a6\f\25\2\2\u00a6\u00a7\7\23\2\2\u00a7\u00d8\5\26")
        buf.write("\f\26\u00a8\u00a9\f\24\2\2\u00a9\u00aa\7\25\2\2\u00aa")
        buf.write("\u00d8\5\26\f\25\u00ab\u00ac\f\23\2\2\u00ac\u00ad\7/\2")
        buf.write("\2\u00ad\u00d8\5\26\f\24\u00ae\u00af\f\22\2\2\u00af\u00b0")
        buf.write("\7.\2\2\u00b0\u00d8\5\26\f\23\u00b1\u00b2\f\21\2\2\u00b2")
        buf.write("\u00b3\7}\2\2\u00b3\u00d8\5\26\f\22\u00b4\u00b5\f\20\2")
        buf.write("\2\u00b5\u00b6\7[\2\2\u00b6\u00d8\5\26\f\21\u00b7\u00b8")
        buf.write("\f\17\2\2\u00b8\u00b9\7*\2\2\u00b9\u00d8\5\26\f\20\u00ba")
        buf.write("\u00bb\f\16\2\2\u00bb\u00bc\7\35\2\2\u00bc\u00d8\5\26")
        buf.write("\f\17\u00bd\u00be\f\r\2\2\u00be\u00bf\7\37\2\2\u00bf\u00d8")
        buf.write("\5\26\f\16\u00c0\u00c1\f\f\2\2\u00c1\u00c2\7\3\2\2\u00c2")
        buf.write("\u00d8\5\26\f\r\u00c3\u00c4\f\13\2\2\u00c4\u00c5\7\4\2")
        buf.write("\2\u00c5\u00d8\5\26\f\f\u00c6\u00c7\f\n\2\2\u00c7\u00c8")
        buf.write("\7$\2\2\u00c8\u00d8\5\26\f\13\u00c9\u00ca\f\t\2\2\u00ca")
        buf.write("\u00cb\7%\2\2\u00cb\u00d8\5\26\f\n\u00cc\u00cd\f\b\2\2")
        buf.write("\u00cd\u00ce\7!\2\2\u00ce\u00d8\5\26\f\t\u00cf\u00d0\f")
        buf.write("\7\2\2\u00d0\u00d1\7X\2\2\u00d1\u00d8\5\26\f\b\u00d2\u00d3")
        buf.write("\f\6\2\2\u00d3\u00d4\7\t\2\2\u00d4\u00d5\5\26\f\2\u00d5")
        buf.write("\u00d6\7\n\2\2\u00d6\u00d8\3\2\2\2\u00d7\u0099\3\2\2\2")
        buf.write("\u00d7\u009c\3\2\2\2\u00d7\u009f\3\2\2\2\u00d7\u00a2\3")
        buf.write("\2\2\2\u00d7\u00a5\3\2\2\2\u00d7\u00a8\3\2\2\2\u00d7\u00ab")
        buf.write("\3\2\2\2\u00d7\u00ae\3\2\2\2\u00d7\u00b1\3\2\2\2\u00d7")
        buf.write("\u00b4\3\2\2\2\u00d7\u00b7\3\2\2\2\u00d7\u00ba\3\2\2\2")
        buf.write("\u00d7\u00bd\3\2\2\2\u00d7\u00c0\3\2\2\2\u00d7\u00c3\3")
        buf.write("\2\2\2\u00d7\u00c6\3\2\2\2\u00d7\u00c9\3\2\2\2\u00d7\u00cc")
        buf.write("\3\2\2\2\u00d7\u00cf\3\2\2\2\u00d7\u00d2\3\2\2\2\u00d8")
        buf.write("\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2")
        buf.write("\u00da\27\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00ec\5\36")
        buf.write("\20\2\u00dd\u00ec\5\"\22\2\u00de\u00ec\5$\23\2\u00df\u00ec")
        buf.write("\5&\24\2\u00e0\u00ec\5(\25\2\u00e1\u00ec\5*\26\2\u00e2")
        buf.write("\u00ec\5,\27\2\u00e3\u00ec\5.\30\2\u00e4\u00ec\5\32\16")
        buf.write("\2\u00e5\u00ec\5\64\33\2\u00e6\u00ec\5\62\32\2\u00e7\u00e9")
        buf.write("\5\26\f\2\u00e8\u00e7\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9")
        buf.write("\u00ea\3\2\2\2\u00ea\u00ec\7\17\2\2\u00eb\u00dc\3\2\2")
        buf.write("\2\u00eb\u00dd\3\2\2\2\u00eb\u00de\3\2\2\2\u00eb\u00df")
        buf.write("\3\2\2\2\u00eb\u00e0\3\2\2\2\u00eb\u00e1\3\2\2\2\u00eb")
        buf.write("\u00e2\3\2\2\2\u00eb\u00e3\3\2\2\2\u00eb\u00e4\3\2\2\2")
        buf.write("\u00eb\u00e5\3\2\2\2\u00eb\u00e6\3\2\2\2\u00eb\u00e8\3")
        buf.write("\2\2\2\u00ec\31\3\2\2\2\u00ed\u00f1\7\7\2\2\u00ee\u00f0")
        buf.write("\5\30\r\2\u00ef\u00ee\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f4\3\2\2\2")
        buf.write("\u00f3\u00f1\3\2\2\2\u00f4\u00f5\7\b\2\2\u00f5\33\3\2")
        buf.write("\2\2\u00f6\u00f7\7\u0083\2\2\u00f7\u0100\7\13\2\2\u00f8")
        buf.write("\u00fd\5\26\f\2\u00f9\u00fa\7\16\2\2\u00fa\u00fc\5\26")
        buf.write("\f\2\u00fb\u00f9\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb")
        buf.write("\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff")
        buf.write("\u00fd\3\2\2\2\u0100\u00f8\3\2\2\2\u0100\u0101\3\2\2\2")
        buf.write("\u0101\u0102\3\2\2\2\u0102\u0103\7\f\2\2\u0103\35\3\2")
        buf.write("\2\2\u0104\u0105\7P\2\2\u0105\u0106\7\13\2\2\u0106\u0107")
        buf.write("\5\26\f\2\u0107\u0108\7\f\2\2\u0108\u010b\5\30\r\2\u0109")
        buf.write("\u010a\7F\2\2\u010a\u010c\5\30\r\2\u010b\u0109\3\2\2\2")
        buf.write("\u010b\u010c\3\2\2\2\u010c\37\3\2\2\2\u010d\u010e\7\62")
        buf.write("\2\2\u010e\u010f\5\24\13\2\u010f\u0110\7\21\2\2\u0110")
        buf.write("\u0111\5\30\r\2\u0111!\3\2\2\2\u0112\u0113\7k\2\2\u0113")
        buf.write("\u0114\7\13\2\2\u0114\u0115\5\26\f\2\u0115\u0116\7\f\2")
        buf.write("\2\u0116\u011a\7\7\2\2\u0117\u0119\5 \21\2\u0118\u0117")
        buf.write("\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a")
        buf.write("\u011b\3\2\2\2\u011b\u011d\3\2\2\2\u011c\u011a\3\2\2\2")
        buf.write("\u011d\u011e\7\b\2\2\u011e#\3\2\2\2\u011f\u0120\7|\2\2")
        buf.write("\u0120\u0121\7\13\2\2\u0121\u0122\5\26\f\2\u0122\u0123")
        buf.write("\7\f\2\2\u0123\u0124\5\30\r\2\u0124%\3\2\2\2\u0125\u0126")
        buf.write("\7C\2\2\u0126\u0127\5\30\r\2\u0127\u0128\7|\2\2\u0128")
        buf.write("\u0129\7\13\2\2\u0129\u012a\5\26\f\2\u012a\u012b\7\f\2")
        buf.write("\2\u012b\u012c\7\17\2\2\u012c\'\3\2\2\2\u012d\u012e\7")
        buf.write("M\2\2\u012e\u0130\7\13\2\2\u012f\u0131\5\26\f\2\u0130")
        buf.write("\u012f\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132\3\2\2\2")
        buf.write("\u0132\u0134\7\17\2\2\u0133\u0135\5\26\f\2\u0134\u0133")
        buf.write("\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write("\u0138\7\17\2\2\u0137\u0139\5\26\f\2\u0138\u0137\3\2\2")
        buf.write("\2\u0138\u0139\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013b")
        buf.write("\7\f\2\2\u013b\u013c\5\30\r\2\u013c)\3\2\2\2\u013d\u013f")
        buf.write("\7c\2\2\u013e\u0140\5\26\f\2\u013f\u013e\3\2\2\2\u013f")
        buf.write("\u0140\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0142\7\17\2")
        buf.write("\2\u0142+\3\2\2\2\u0143\u0144\7\61\2\2\u0144\u0145\7\17")
        buf.write("\2\2\u0145-\3\2\2\2\u0146\u0147\7@\2\2\u0147\u0148\7\17")
        buf.write("\2\2\u0148/\3\2\2\2\u0149\u014e\5\62\32\2\u014a\u014e")
        buf.write("\5\64\33\2\u014b\u014e\5\66\34\2\u014c\u014e\5\22\n\2")
        buf.write("\u014d\u0149\3\2\2\2\u014d\u014a\3\2\2\2\u014d\u014b\3")
        buf.write("\2\2\2\u014d\u014c\3\2\2\2\u014e\61\3\2\2\2\u014f\u0150")
        buf.write("\5:\36\2\u0150\u0151\7\u0083\2\2\u0151\u0152\7\t\2\2\u0152")
        buf.write("\u0153\5\26\f\2\u0153\u0160\7\n\2\2\u0154\u0155\7\22\2")
        buf.write("\2\u0155\u0156\7\7\2\2\u0156\u015b\5\26\f\2\u0157\u0158")
        buf.write("\7\16\2\2\u0158\u015a\5\26\f\2\u0159\u0157\3\2\2\2\u015a")
        buf.write("\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2")
        buf.write("\u015c\u015e\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u015f\7")
        buf.write("\7\2\2\u015f\u0161\3\2\2\2\u0160\u0154\3\2\2\2\u0160\u0161")
        buf.write("\3\2\2\2\u0161\63\3\2\2\2\u0162\u0163\5:\36\2\u0163\u0166")
        buf.write("\7\u0083\2\2\u0164\u0165\7\22\2\2\u0165\u0167\5\26\f\2")
        buf.write("\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0170\3")
        buf.write("\2\2\2\u0168\u0169\7\16\2\2\u0169\u016c\7\u0083\2\2\u016a")
        buf.write("\u016b\7\22\2\2\u016b\u016d\5\26\f\2\u016c\u016a\3\2\2")
        buf.write("\2\u016c\u016d\3\2\2\2\u016d\u016f\3\2\2\2\u016e\u0168")
        buf.write("\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170")
        buf.write("\u0171\3\2\2\2\u0171\u0173\3\2\2\2\u0172\u0170\3\2\2\2")
        buf.write("\u0173\u0174\7\17\2\2\u0174\65\3\2\2\2\u0175\u0176\5:")
        buf.write("\36\2\u0176\u0177\7\u0083\2\2\u0177\u0180\7\13\2\2\u0178")
        buf.write("\u017d\58\35\2\u0179\u017a\7\16\2\2\u017a\u017c\58\35")
        buf.write("\2\u017b\u0179\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u0181\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u0180\u0178\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181\u0182\3\2\2\2\u0182\u0183\7\f\2\2\u0183\u0184\5")
        buf.write("\32\16\2\u0184\67\3\2\2\2\u0185\u0186\5:\36\2\u0186\u0187")
        buf.write("\7\u0083\2\2\u01879\3\2\2\2\u0188\u018e\5<\37\2\u0189")
        buf.write("\u018e\5> \2\u018a\u018e\5@!\2\u018b\u018e\5B\"\2\u018c")
        buf.write("\u018e\5D#\2\u018d\u0188\3\2\2\2\u018d\u0189\3\2\2\2\u018d")
        buf.write("\u018a\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018c\3\2\2\2")
        buf.write("\u018e;\3\2\2\2\u018f\u0195\7R\2\2\u0190\u0195\7S\2\2")
        buf.write("\u0191\u0195\7d\2\2\u0192\u0193\7S\2\2\u0193\u0195\7S")
        buf.write("\2\2\u0194\u018f\3\2\2\2\u0194\u0190\3\2\2\2\u0194\u0191")
        buf.write("\3\2\2\2\u0194\u0192\3\2\2\2\u0195=\3\2\2\2\u0196\u019b")
        buf.write("\7L\2\2\u0197\u019b\7D\2\2\u0198\u0199\7S\2\2\u0199\u019b")
        buf.write("\7D\2\2\u019a\u0196\3\2\2\2\u019a\u0197\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019b?\3\2\2\2\u019c\u019d\7\60\2\2\u019d")
        buf.write("A\3\2\2\2\u019e\u019f\7\64\2\2\u019fC\3\2\2\2\u01a0\u01a1")
        buf.write("\7y\2\2\u01a1E\3\2\2\2&IMSXbkns\u0081\u0083\u008a\u0097")
        buf.write("\u00d7\u00d9\u00e8\u00eb\u00f1\u00fd\u0100\u010b\u011a")
        buf.write("\u0130\u0134\u0138\u013f\u014d\u015b\u0160\u0166\u016c")
        buf.write("\u0170\u017d\u0180\u018d\u0194\u019a")
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
    RULE_baseSpecifierList = 1
    RULE_accessSpecifier = 2
    RULE_accessLabel = 3
    RULE_memberDeclaration = 4
    RULE_constructorDeclaration = 5
    RULE_destructorDeclaration = 6
    RULE_memberSpecification = 7
    RULE_classDefinition = 8
    RULE_constExpression = 9
    RULE_expression = 10
    RULE_statement = 11
    RULE_block = 12
    RULE_functionCall = 13
    RULE_ifStatement = 14
    RULE_caseStatement = 15
    RULE_switchStatement = 16
    RULE_whileStatement = 17
    RULE_doWhileStatement = 18
    RULE_forStatement = 19
    RULE_returnStatement = 20
    RULE_breakStatement = 21
    RULE_continueStatement = 22
    RULE_declaration = 23
    RULE_arrayDeclarator = 24
    RULE_variableDeclaration = 25
    RULE_functionDeclaration = 26
    RULE_functionParameter = 27
    RULE_typeSpecifier = 28
    RULE_integerTypeSpecifier = 29
    RULE_realTypeSpecifier = 30
    RULE_booleanTypeSpecifier = 31
    RULE_charTypeSpecifier = 32
    RULE_voidTypeSpecifier = 33

    ruleNames =  [ "translationUnit", "baseSpecifierList", "accessSpecifier", 
                   "accessLabel", "memberDeclaration", "constructorDeclaration", 
                   "destructorDeclaration", "memberSpecification", "classDefinition", 
                   "constExpression", "expression", "statement", "block", 
                   "functionCall", "ifStatement", "caseStatement", "switchStatement", 
                   "whileStatement", "doWhileStatement", "forStatement", 
                   "returnStatement", "breakStatement", "continueStatement", 
                   "declaration", "arrayDeclarator", "variableDeclaration", 
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

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.DeclarationContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.DeclarationContext,i)


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
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.BOOL) | (1 << cpp20Parser.CHAR) | (1 << cpp20Parser.CLASS))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (cpp20Parser.DOUBLE - 66)) | (1 << (cpp20Parser.FLOAT - 66)) | (1 << (cpp20Parser.INT - 66)) | (1 << (cpp20Parser.LONG - 66)) | (1 << (cpp20Parser.SHORT - 66)) | (1 << (cpp20Parser.STRUCT - 66)) | (1 << (cpp20Parser.VOID - 66)))) != 0):
                self.state = 68
                self.declaration()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseSpecifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(cpp20Parser.Identifier)
            else:
                return self.getToken(cpp20Parser.Identifier, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(cpp20Parser.COMMA)
            else:
                return self.getToken(cpp20Parser.COMMA, i)

        def accessSpecifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.AccessSpecifierContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.AccessSpecifierContext,i)


        def getRuleIndex(self):
            return cpp20Parser.RULE_baseSpecifierList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBaseSpecifierList" ):
                listener.enterBaseSpecifierList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBaseSpecifierList" ):
                listener.exitBaseSpecifierList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseSpecifierList" ):
                return visitor.visitBaseSpecifierList(self)
            else:
                return visitor.visitChildren(self)




    def baseSpecifierList(self):

        localctx = cpp20Parser.BaseSpecifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_baseSpecifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 91)) & ~0x3f) == 0 and ((1 << (_la - 91)) & ((1 << (cpp20Parser.PRIVATE - 91)) | (1 << (cpp20Parser.PROTECTED - 91)) | (1 << (cpp20Parser.PUBLIC - 91)))) != 0):
                self.state = 74
                self.accessSpecifier()


            self.state = 77
            self.match(cpp20Parser.Identifier)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cpp20Parser.COMMA:
                self.state = 79
                self.match(cpp20Parser.COMMA)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 91)) & ~0x3f) == 0 and ((1 << (_la - 91)) & ((1 << (cpp20Parser.PRIVATE - 91)) | (1 << (cpp20Parser.PROTECTED - 91)) | (1 << (cpp20Parser.PUBLIC - 91)))) != 0):
                    self.state = 80
                    self.accessSpecifier()


                self.state = 83
                self.match(cpp20Parser.Identifier)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccessSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUBLIC(self):
            return self.getToken(cpp20Parser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(cpp20Parser.PROTECTED, 0)

        def PRIVATE(self):
            return self.getToken(cpp20Parser.PRIVATE, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_accessSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessSpecifier" ):
                listener.enterAccessSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessSpecifier" ):
                listener.exitAccessSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccessSpecifier" ):
                return visitor.visitAccessSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def accessSpecifier(self):

        localctx = cpp20Parser.AccessSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_accessSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not(((((_la - 91)) & ~0x3f) == 0 and ((1 << (_la - 91)) & ((1 << (cpp20Parser.PRIVATE - 91)) | (1 << (cpp20Parser.PROTECTED - 91)) | (1 << (cpp20Parser.PUBLIC - 91)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccessLabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def accessSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.AccessSpecifierContext,0)


        def COLON(self):
            return self.getToken(cpp20Parser.COLON, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_accessLabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessLabel" ):
                listener.enterAccessLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessLabel" ):
                listener.exitAccessLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccessLabel" ):
                return visitor.visitAccessLabel(self)
            else:
                return visitor.visitChildren(self)




    def accessLabel(self):

        localctx = cpp20Parser.AccessLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_accessLabel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.accessSpecifier()
            self.state = 92
            self.match(cpp20Parser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDeclaration(self):
            return self.getTypedRuleContext(cpp20Parser.FunctionDeclarationContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(cpp20Parser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return cpp20Parser.RULE_memberDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberDeclaration" ):
                listener.enterMemberDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberDeclaration" ):
                listener.exitMemberDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberDeclaration" ):
                return visitor.visitMemberDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def memberDeclaration(self):

        localctx = cpp20Parser.MemberDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_memberDeclaration)
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.functionDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.variableDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorDeclarationContext(ParserRuleContext):
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

        def block(self):
            return self.getTypedRuleContext(cpp20Parser.BlockContext,0)


        def functionParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.FunctionParameterContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.FunctionParameterContext,i)


        def COLON(self):
            return self.getToken(cpp20Parser.COLON, 0)

        def functionCall(self):
            return self.getTypedRuleContext(cpp20Parser.FunctionCallContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(cpp20Parser.COMMA)
            else:
                return self.getToken(cpp20Parser.COMMA, i)

        def getRuleIndex(self):
            return cpp20Parser.RULE_constructorDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorDeclaration" ):
                listener.enterConstructorDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorDeclaration" ):
                listener.exitConstructorDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructorDeclaration" ):
                return visitor.visitConstructorDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def constructorDeclaration(self):

        localctx = cpp20Parser.ConstructorDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_constructorDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(cpp20Parser.Identifier)
            self.state = 99
            self.match(cpp20Parser.LPAREN)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.BOOL or _la==cpp20Parser.CHAR or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (cpp20Parser.DOUBLE - 66)) | (1 << (cpp20Parser.FLOAT - 66)) | (1 << (cpp20Parser.INT - 66)) | (1 << (cpp20Parser.LONG - 66)) | (1 << (cpp20Parser.SHORT - 66)) | (1 << (cpp20Parser.VOID - 66)))) != 0):
                self.state = 100
                self.functionParameter()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cpp20Parser.COMMA:
                    self.state = 101
                    self.match(cpp20Parser.COMMA)
                    self.state = 102
                    self.functionParameter()
                    self.state = 107
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 110
            self.match(cpp20Parser.RPAREN)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.COLON:
                self.state = 111
                self.match(cpp20Parser.COLON)
                self.state = 112
                self.functionCall()


            self.state = 115
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPL(self):
            return self.getToken(cpp20Parser.COMPL, 0)

        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(cpp20Parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(cpp20Parser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(cpp20Parser.BlockContext,0)


        def getRuleIndex(self):
            return cpp20Parser.RULE_destructorDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDestructorDeclaration" ):
                listener.enterDestructorDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDestructorDeclaration" ):
                listener.exitDestructorDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructorDeclaration" ):
                return visitor.visitDestructorDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def destructorDeclaration(self):

        localctx = cpp20Parser.DestructorDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_destructorDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(cpp20Parser.COMPL)
            self.state = 118
            self.match(cpp20Parser.Identifier)
            self.state = 119
            self.match(cpp20Parser.LPAREN)
            self.state = 120
            self.match(cpp20Parser.RPAREN)
            self.state = 121
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberSpecificationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def accessLabel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.AccessLabelContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.AccessLabelContext,i)


        def memberDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.MemberDeclarationContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.MemberDeclarationContext,i)


        def constructorDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.ConstructorDeclarationContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.ConstructorDeclarationContext,i)


        def destructorDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.DestructorDeclarationContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.DestructorDeclarationContext,i)


        def getRuleIndex(self):
            return cpp20Parser.RULE_memberSpecification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberSpecification" ):
                listener.enterMemberSpecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberSpecification" ):
                listener.exitMemberSpecification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberSpecification" ):
                return visitor.visitMemberSpecification(self)
            else:
                return visitor.visitChildren(self)




    def memberSpecification(self):

        localctx = cpp20Parser.MemberSpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_memberSpecification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.BOOL) | (1 << cpp20Parser.CHAR) | (1 << cpp20Parser.COMPL))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (cpp20Parser.DOUBLE - 66)) | (1 << (cpp20Parser.FLOAT - 66)) | (1 << (cpp20Parser.INT - 66)) | (1 << (cpp20Parser.LONG - 66)) | (1 << (cpp20Parser.PRIVATE - 66)) | (1 << (cpp20Parser.PROTECTED - 66)) | (1 << (cpp20Parser.PUBLIC - 66)) | (1 << (cpp20Parser.SHORT - 66)) | (1 << (cpp20Parser.VOID - 66)) | (1 << (cpp20Parser.Identifier - 66)))) != 0):
                self.state = 127
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [cpp20Parser.PRIVATE, cpp20Parser.PROTECTED, cpp20Parser.PUBLIC]:
                    self.state = 123
                    self.accessLabel()
                    pass
                elif token in [cpp20Parser.BOOL, cpp20Parser.CHAR, cpp20Parser.DOUBLE, cpp20Parser.FLOAT, cpp20Parser.INT, cpp20Parser.LONG, cpp20Parser.SHORT, cpp20Parser.VOID]:
                    self.state = 124
                    self.memberDeclaration()
                    pass
                elif token in [cpp20Parser.Identifier]:
                    self.state = 125
                    self.constructorDeclaration()
                    pass
                elif token in [cpp20Parser.COMPL]:
                    self.state = 126
                    self.destructorDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)

        def LBRACE(self):
            return self.getToken(cpp20Parser.LBRACE, 0)

        def memberSpecification(self):
            return self.getTypedRuleContext(cpp20Parser.MemberSpecificationContext,0)


        def RBRACE(self):
            return self.getToken(cpp20Parser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(cpp20Parser.SEMI, 0)

        def CLASS(self):
            return self.getToken(cpp20Parser.CLASS, 0)

        def STRUCT(self):
            return self.getToken(cpp20Parser.STRUCT, 0)

        def COLON(self):
            return self.getToken(cpp20Parser.COLON, 0)

        def baseSpecifierList(self):
            return self.getTypedRuleContext(cpp20Parser.BaseSpecifierListContext,0)


        def getRuleIndex(self):
            return cpp20Parser.RULE_classDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDefinition" ):
                listener.enterClassDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDefinition" ):
                listener.exitClassDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDefinition" ):
                return visitor.visitClassDefinition(self)
            else:
                return visitor.visitChildren(self)




    def classDefinition(self):

        localctx = cpp20Parser.ClassDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_classDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            _la = self._input.LA(1)
            if not(_la==cpp20Parser.CLASS or _la==cpp20Parser.STRUCT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 133
            self.match(cpp20Parser.Identifier)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.COLON:
                self.state = 134
                self.match(cpp20Parser.COLON)
                self.state = 135
                self.baseSpecifierList()


            self.state = 138
            self.match(cpp20Parser.LBRACE)
            self.state = 139
            self.memberSpecification()
            self.state = 140
            self.match(cpp20Parser.RBRACE)
            self.state = 141
            self.match(cpp20Parser.SEMI)
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
        self.enterRule(localctx, 18, self.RULE_constExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
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

        def LSQUARE(self):
            return self.getToken(cpp20Parser.LSQUARE, 0)

        def RSQUARE(self):
            return self.getToken(cpp20Parser.RSQUARE, 0)

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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 146
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 147
                self.match(cpp20Parser.Literals)
                pass

            elif la_ == 3:
                self.state = 148
                self.match(cpp20Parser.Identifier)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 213
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 151
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 152
                        self.match(cpp20Parser.ASSIGN)
                        self.state = 153
                        self.expression(24)
                        pass

                    elif la_ == 2:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 154
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 155
                        self.match(cpp20Parser.MULT)
                        self.state = 156
                        self.expression(23)
                        pass

                    elif la_ == 3:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 157
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 158
                        self.match(cpp20Parser.DIV)
                        self.state = 159
                        self.expression(22)
                        pass

                    elif la_ == 4:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 160
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 161
                        self.match(cpp20Parser.MOD)
                        self.state = 162
                        self.expression(21)
                        pass

                    elif la_ == 5:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 163
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 164
                        self.match(cpp20Parser.ADD)
                        self.state = 165
                        self.expression(20)
                        pass

                    elif la_ == 6:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 166
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 167
                        self.match(cpp20Parser.SUB)
                        self.state = 168
                        self.expression(19)
                        pass

                    elif la_ == 7:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 169
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 170
                        self.match(cpp20Parser.BITOR)
                        self.state = 171
                        self.expression(18)
                        pass

                    elif la_ == 8:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 172
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 173
                        self.match(cpp20Parser.BITAND)
                        self.state = 174
                        self.expression(17)
                        pass

                    elif la_ == 9:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 175
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 176
                        self.match(cpp20Parser.XOR)
                        self.state = 177
                        self.expression(16)
                        pass

                    elif la_ == 10:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 178
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 179
                        self.match(cpp20Parser.OR)
                        self.state = 180
                        self.expression(15)
                        pass

                    elif la_ == 11:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 181
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 182
                        self.match(cpp20Parser.AND)
                        self.state = 183
                        self.expression(14)
                        pass

                    elif la_ == 12:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 184
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 185
                        self.match(cpp20Parser.LSHIFT)
                        self.state = 186
                        self.expression(13)
                        pass

                    elif la_ == 13:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 187
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 188
                        self.match(cpp20Parser.RSHIFT)
                        self.state = 189
                        self.expression(12)
                        pass

                    elif la_ == 14:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 190
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 191
                        self.match(cpp20Parser.LT)
                        self.state = 192
                        self.expression(11)
                        pass

                    elif la_ == 15:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 193
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 194
                        self.match(cpp20Parser.GT)
                        self.state = 195
                        self.expression(10)
                        pass

                    elif la_ == 16:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 196
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 197
                        self.match(cpp20Parser.LEQ)
                        self.state = 198
                        self.expression(9)
                        pass

                    elif la_ == 17:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 199
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 200
                        self.match(cpp20Parser.GEQ)
                        self.state = 201
                        self.expression(8)
                        pass

                    elif la_ == 18:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 202
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 203
                        self.match(cpp20Parser.EQ)
                        self.state = 204
                        self.expression(7)
                        pass

                    elif la_ == 19:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 205
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 206
                        self.match(cpp20Parser.NOT_EQ)
                        self.state = 207
                        self.expression(6)
                        pass

                    elif la_ == 20:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 208
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 209
                        self.match(cpp20Parser.LSQUARE)
                        self.state = 210
                        self.expression(0)
                        self.state = 211
                        self.match(cpp20Parser.RSQUARE)
                        pass

             
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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


        def variableDeclaration(self):
            return self.getTypedRuleContext(cpp20Parser.VariableDeclarationContext,0)


        def arrayDeclarator(self):
            return self.getTypedRuleContext(cpp20Parser.ArrayDeclaratorContext,0)


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
        self.enterRule(localctx, 22, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.ifStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.switchStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.whileStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 221
                self.doWhileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 222
                self.forStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 223
                self.returnStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 224
                self.breakStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 225
                self.continueStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 226
                self.block()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 227
                self.variableDeclaration()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 228
                self.arrayDeclarator()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==cpp20Parser.Identifier or _la==cpp20Parser.Literals:
                    self.state = 229
                    self.expression(0)


                self.state = 232
                self.match(cpp20Parser.SEMI)
                pass


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
        self.enterRule(localctx, 24, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(cpp20Parser.LBRACE)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & ((1 << (cpp20Parser.LBRACE - 5)) | (1 << (cpp20Parser.SEMI - 5)) | (1 << (cpp20Parser.BOOL - 5)) | (1 << (cpp20Parser.BREAK - 5)) | (1 << (cpp20Parser.CHAR - 5)) | (1 << (cpp20Parser.CONTINUE - 5)) | (1 << (cpp20Parser.DO - 5)) | (1 << (cpp20Parser.DOUBLE - 5)))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (cpp20Parser.FLOAT - 74)) | (1 << (cpp20Parser.FOR - 74)) | (1 << (cpp20Parser.IF - 74)) | (1 << (cpp20Parser.INT - 74)) | (1 << (cpp20Parser.LONG - 74)) | (1 << (cpp20Parser.RETURN - 74)) | (1 << (cpp20Parser.SHORT - 74)) | (1 << (cpp20Parser.SWITCH - 74)) | (1 << (cpp20Parser.VOID - 74)) | (1 << (cpp20Parser.WHILE - 74)) | (1 << (cpp20Parser.Identifier - 74)) | (1 << (cpp20Parser.Literals - 74)))) != 0):
                self.state = 236
                self.statement()
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242
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
        self.enterRule(localctx, 26, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(cpp20Parser.Identifier)
            self.state = 245
            self.match(cpp20Parser.LPAREN)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.Identifier or _la==cpp20Parser.Literals:
                self.state = 246
                self.expression(0)
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cpp20Parser.COMMA:
                    self.state = 247
                    self.match(cpp20Parser.COMMA)
                    self.state = 248
                    self.expression(0)
                    self.state = 253
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 256
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
        self.enterRule(localctx, 28, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(cpp20Parser.IF)
            self.state = 259
            self.match(cpp20Parser.LPAREN)
            self.state = 260
            self.expression(0)
            self.state = 261
            self.match(cpp20Parser.RPAREN)
            self.state = 262
            self.statement()
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 263
                self.match(cpp20Parser.ELSE)
                self.state = 264
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
        self.enterRule(localctx, 30, self.RULE_caseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(cpp20Parser.CASE)
            self.state = 268
            self.constExpression()
            self.state = 269
            self.match(cpp20Parser.COLON)
            self.state = 270
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
        self.enterRule(localctx, 32, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(cpp20Parser.SWITCH)
            self.state = 273
            self.match(cpp20Parser.LPAREN)
            self.state = 274
            self.expression(0)
            self.state = 275
            self.match(cpp20Parser.RPAREN)
            self.state = 276
            self.match(cpp20Parser.LBRACE)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cpp20Parser.CASE:
                self.state = 277
                self.caseStatement()
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 283
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
        self.enterRule(localctx, 34, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(cpp20Parser.WHILE)
            self.state = 286
            self.match(cpp20Parser.LPAREN)
            self.state = 287
            self.expression(0)
            self.state = 288
            self.match(cpp20Parser.RPAREN)
            self.state = 289
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
        self.enterRule(localctx, 36, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(cpp20Parser.DO)
            self.state = 292
            self.statement()
            self.state = 293
            self.match(cpp20Parser.WHILE)
            self.state = 294
            self.match(cpp20Parser.LPAREN)
            self.state = 295
            self.expression(0)
            self.state = 296
            self.match(cpp20Parser.RPAREN)
            self.state = 297
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
        self.enterRule(localctx, 38, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(cpp20Parser.FOR)
            self.state = 300
            self.match(cpp20Parser.LPAREN)
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.Identifier or _la==cpp20Parser.Literals:
                self.state = 301
                self.expression(0)


            self.state = 304
            self.match(cpp20Parser.SEMI)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.Identifier or _la==cpp20Parser.Literals:
                self.state = 305
                self.expression(0)


            self.state = 308
            self.match(cpp20Parser.SEMI)
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.Identifier or _la==cpp20Parser.Literals:
                self.state = 309
                self.expression(0)


            self.state = 312
            self.match(cpp20Parser.RPAREN)
            self.state = 313
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
        self.enterRule(localctx, 40, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(cpp20Parser.RETURN)
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.Identifier or _la==cpp20Parser.Literals:
                self.state = 316
                self.expression(0)


            self.state = 319
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
        self.enterRule(localctx, 42, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(cpp20Parser.BREAK)
            self.state = 322
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
        self.enterRule(localctx, 44, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(cpp20Parser.CONTINUE)
            self.state = 325
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

        def arrayDeclarator(self):
            return self.getTypedRuleContext(cpp20Parser.ArrayDeclaratorContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(cpp20Parser.VariableDeclarationContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(cpp20Parser.FunctionDeclarationContext,0)


        def classDefinition(self):
            return self.getTypedRuleContext(cpp20Parser.ClassDefinitionContext,0)


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
        self.enterRule(localctx, 46, self.RULE_declaration)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.arrayDeclarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.variableDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 329
                self.functionDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 330
                self.classDefinition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.TypeSpecifierContext,0)


        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)

        def LSQUARE(self):
            return self.getToken(cpp20Parser.LSQUARE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.ExpressionContext,i)


        def RSQUARE(self):
            return self.getToken(cpp20Parser.RSQUARE, 0)

        def ASSIGN(self):
            return self.getToken(cpp20Parser.ASSIGN, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(cpp20Parser.LBRACE)
            else:
                return self.getToken(cpp20Parser.LBRACE, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(cpp20Parser.COMMA)
            else:
                return self.getToken(cpp20Parser.COMMA, i)

        def getRuleIndex(self):
            return cpp20Parser.RULE_arrayDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayDeclarator" ):
                listener.enterArrayDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayDeclarator" ):
                listener.exitArrayDeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDeclarator" ):
                return visitor.visitArrayDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def arrayDeclarator(self):

        localctx = cpp20Parser.ArrayDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_arrayDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.typeSpecifier()
            self.state = 334
            self.match(cpp20Parser.Identifier)
            self.state = 335
            self.match(cpp20Parser.LSQUARE)
            self.state = 336
            self.expression(0)
            self.state = 337
            self.match(cpp20Parser.RSQUARE)
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.ASSIGN:
                self.state = 338
                self.match(cpp20Parser.ASSIGN)
                self.state = 339
                self.match(cpp20Parser.LBRACE)
                self.state = 340
                self.expression(0)
                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cpp20Parser.COMMA:
                    self.state = 341
                    self.match(cpp20Parser.COMMA)
                    self.state = 342
                    self.expression(0)
                    self.state = 347
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 348
                self.match(cpp20Parser.LBRACE)


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


        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(cpp20Parser.Identifier)
            else:
                return self.getToken(cpp20Parser.Identifier, i)

        def SEMI(self):
            return self.getToken(cpp20Parser.SEMI, 0)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(cpp20Parser.ASSIGN)
            else:
                return self.getToken(cpp20Parser.ASSIGN, i)

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
        self.enterRule(localctx, 50, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.typeSpecifier()
            self.state = 353
            self.match(cpp20Parser.Identifier)
            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.ASSIGN:
                self.state = 354
                self.match(cpp20Parser.ASSIGN)
                self.state = 355
                self.expression(0)


            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cpp20Parser.COMMA:
                self.state = 358
                self.match(cpp20Parser.COMMA)
                self.state = 359
                self.match(cpp20Parser.Identifier)
                self.state = 362
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==cpp20Parser.ASSIGN:
                    self.state = 360
                    self.match(cpp20Parser.ASSIGN)
                    self.state = 361
                    self.expression(0)


                self.state = 368
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 369
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
        self.enterRule(localctx, 52, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.typeSpecifier()
            self.state = 372
            self.match(cpp20Parser.Identifier)
            self.state = 373
            self.match(cpp20Parser.LPAREN)
            self.state = 382
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.BOOL or _la==cpp20Parser.CHAR or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (cpp20Parser.DOUBLE - 66)) | (1 << (cpp20Parser.FLOAT - 66)) | (1 << (cpp20Parser.INT - 66)) | (1 << (cpp20Parser.LONG - 66)) | (1 << (cpp20Parser.SHORT - 66)) | (1 << (cpp20Parser.VOID - 66)))) != 0):
                self.state = 374
                self.functionParameter()
                self.state = 379
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cpp20Parser.COMMA:
                    self.state = 375
                    self.match(cpp20Parser.COMMA)
                    self.state = 376
                    self.functionParameter()
                    self.state = 381
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 384
            self.match(cpp20Parser.RPAREN)
            self.state = 385
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
        self.enterRule(localctx, 54, self.RULE_functionParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.typeSpecifier()
            self.state = 388
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
        self.enterRule(localctx, 56, self.RULE_typeSpecifier)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.integerTypeSpecifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.realTypeSpecifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 392
                self.booleanTypeSpecifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 393
                self.charTypeSpecifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 394
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
        self.enterRule(localctx, 58, self.RULE_integerTypeSpecifier)
        try:
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.match(cpp20Parser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.match(cpp20Parser.LONG)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 399
                self.match(cpp20Parser.SHORT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 400
                self.match(cpp20Parser.LONG)
                self.state = 401
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
        self.enterRule(localctx, 60, self.RULE_realTypeSpecifier)
        try:
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cpp20Parser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.match(cpp20Parser.FLOAT)
                pass
            elif token in [cpp20Parser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.match(cpp20Parser.DOUBLE)
                pass
            elif token in [cpp20Parser.LONG]:
                self.enterOuterAlt(localctx, 3)
                self.state = 406
                self.match(cpp20Parser.LONG)
                self.state = 407
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
        self.enterRule(localctx, 62, self.RULE_booleanTypeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
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
        self.enterRule(localctx, 64, self.RULE_charTypeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
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
        self.enterRule(localctx, 66, self.RULE_voidTypeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
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
        self._predicates[10] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 4)
         



