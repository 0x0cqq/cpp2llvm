# Generated from grammar/cpp20Parser.g4 by ANTLR 4.9
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u0090")
        buf.write("\u01dd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\2\3\2\5\2W\n\2\3\3\3\3")
        buf.write("\3\4\3\4\5\4]\n\4\3\5\5\5`\n\5\3\5\3\5\3\5\3\5\3\6\5\6")
        buf.write("g\n\6\3\6\3\6\7\6k\n\6\f\6\16\6n\13\6\3\6\3\6\3\7\7\7")
        buf.write("s\n\7\f\7\16\7v\13\7\3\b\5\by\n\b\3\b\3\b\3\b\3\b\5\b")
        buf.write("\177\n\b\3\b\7\b\u0082\n\b\f\b\16\b\u0085\13\b\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\13\3\13\5\13\u008e\n\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\7\f\u0095\n\f\f\f\16\f\u0098\13\f\5\f\u009a\n\f\3")
        buf.write("\f\3\f\3\f\5\f\u009f\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\7\16\u00ad\n\16\f\16\16\16\u00b0")
        buf.write("\13\16\3\17\3\17\3\17\3\17\5\17\u00b6\n\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\5\21\u00c5\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00d5\n\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\7\22\u0112\n\22\f\22\16\22\u0115\13\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u0123\n\23\3\23\5\23\u0126\n\23\3\24\3\24\7")
        buf.write("\24\u012a\n\24\f\24\16\24\u012d\13\24\3\24\3\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\7\25\u0136\n\25\f\25\16\25\u0139\13")
        buf.write("\25\5\25\u013b\n\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u0146\n\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\7\30\u0153\n\30\f\30\16\30")
        buf.write("\u0156\13\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\5\33\u016b\n\33\3\33\3\33\5\33\u016f\n\33\3\33\3\33\5")
        buf.write("\33\u0173\n\33\3\33\3\33\3\33\3\34\3\34\5\34\u017a\n\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\5\37\u0188\n\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \7")
        buf.write(" \u0194\n \f \16 \u0197\13 \3 \3 \5 \u019b\n \3!\3!\3")
        buf.write("!\3!\5!\u01a1\n!\3!\3!\3!\3!\5!\u01a7\n!\7!\u01a9\n!\f")
        buf.write("!\16!\u01ac\13!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u01b6")
        buf.write("\n\"\f\"\16\"\u01b9\13\"\5\"\u01bb\n\"\3\"\3\"\3\"\3#")
        buf.write("\3#\3#\3$\3$\3$\3$\3$\5$\u01c8\n$\3%\3%\3%\3%\3%\5%\u01cf")
        buf.write("\n%\3&\3&\3&\3&\5&\u01d5\n&\3\'\3\'\3(\3(\3)\3)\3)\2\3")
        buf.write("\"*\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNP\2\4\3\2]_\4\288jj\2\u0209\2V\3")
        buf.write("\2\2\2\4X\3\2\2\2\6Z\3\2\2\2\b_\3\2\2\2\nf\3\2\2\2\ft")
        buf.write("\3\2\2\2\16x\3\2\2\2\20\u0086\3\2\2\2\22\u0088\3\2\2\2")
        buf.write("\24\u008d\3\2\2\2\26\u008f\3\2\2\2\30\u00a2\3\2\2\2\32")
        buf.write("\u00ae\3\2\2\2\34\u00b1\3\2\2\2\36\u00bc\3\2\2\2 \u00c4")
        buf.write("\3\2\2\2\"\u00d4\3\2\2\2$\u0125\3\2\2\2&\u0127\3\2\2\2")
        buf.write("(\u0130\3\2\2\2*\u013e\3\2\2\2,\u0147\3\2\2\2.\u014c\3")
        buf.write("\2\2\2\60\u0159\3\2\2\2\62\u015f\3\2\2\2\64\u0167\3\2")
        buf.write("\2\2\66\u0177\3\2\2\28\u017d\3\2\2\2:\u0180\3\2\2\2<\u0187")
        buf.write("\3\2\2\2>\u0189\3\2\2\2@\u019c\3\2\2\2B\u01af\3\2\2\2")
        buf.write("D\u01bf\3\2\2\2F\u01c7\3\2\2\2H\u01ce\3\2\2\2J\u01d4\3")
        buf.write("\2\2\2L\u01d6\3\2\2\2N\u01d8\3\2\2\2P\u01da\3\2\2\2RW")
        buf.write("\5\4\3\2SW\5\6\4\2TW\5\b\5\2UW\5\n\6\2VR\3\2\2\2VS\3\2")
        buf.write("\2\2VT\3\2\2\2VU\3\2\2\2W\3\3\2\2\2XY\7\u0086\2\2Y\5\3")
        buf.write("\2\2\2Z\\\7\u0085\2\2[]\7\u0083\2\2\\[\3\2\2\2\\]\3\2")
        buf.write("\2\2]\7\3\2\2\2^`\7\u0089\2\2_^\3\2\2\2_`\3\2\2\2`a\3")
        buf.write("\2\2\2ab\7\6\2\2bc\7\u008a\2\2cd\7\6\2\2d\t\3\2\2\2eg")
        buf.write("\7\u0089\2\2fe\3\2\2\2fg\3\2\2\2gh\3\2\2\2hl\7\5\2\2i")
        buf.write("k\7\u0090\2\2ji\3\2\2\2kn\3\2\2\2lj\3\2\2\2lm\3\2\2\2")
        buf.write("mo\3\2\2\2nl\3\2\2\2op\7\5\2\2p\13\3\2\2\2qs\5<\37\2r")
        buf.write("q\3\2\2\2sv\3\2\2\2tr\3\2\2\2tu\3\2\2\2u\r\3\2\2\2vt\3")
        buf.write("\2\2\2wy\5\20\t\2xw\3\2\2\2xy\3\2\2\2yz\3\2\2\2z{\7\u0084")
        buf.write("\2\2{\u0083\3\2\2\2|~\7\16\2\2}\177\5\20\t\2~}\3\2\2\2")
        buf.write("~\177\3\2\2\2\177\u0080\3\2\2\2\u0080\u0082\7\u0084\2")
        buf.write("\2\u0081|\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0081\3\2")
        buf.write("\2\2\u0083\u0084\3\2\2\2\u0084\17\3\2\2\2\u0085\u0083")
        buf.write("\3\2\2\2\u0086\u0087\t\2\2\2\u0087\21\3\2\2\2\u0088\u0089")
        buf.write("\5\20\t\2\u0089\u008a\7\21\2\2\u008a\23\3\2\2\2\u008b")
        buf.write("\u008e\5B\"\2\u008c\u008e\5@!\2\u008d\u008b\3\2\2\2\u008d")
        buf.write("\u008c\3\2\2\2\u008e\25\3\2\2\2\u008f\u0090\7\u0084\2")
        buf.write("\2\u0090\u0099\7\13\2\2\u0091\u0096\5D#\2\u0092\u0093")
        buf.write("\7\16\2\2\u0093\u0095\5D#\2\u0094\u0092\3\2\2\2\u0095")
        buf.write("\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\u009a\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u0091\3")
        buf.write("\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009e")
        buf.write("\7\f\2\2\u009c\u009d\7\21\2\2\u009d\u009f\5(\25\2\u009e")
        buf.write("\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u00a0\u00a1\5&\24\2\u00a1\27\3\2\2\2\u00a2\u00a3\79\2")
        buf.write("\2\u00a3\u00a4\7\u0084\2\2\u00a4\u00a5\7\13\2\2\u00a5")
        buf.write("\u00a6\7\f\2\2\u00a6\u00a7\5&\24\2\u00a7\31\3\2\2\2\u00a8")
        buf.write("\u00ad\5\22\n\2\u00a9\u00ad\5\24\13\2\u00aa\u00ad\5\26")
        buf.write("\f\2\u00ab\u00ad\5\30\r\2\u00ac\u00a8\3\2\2\2\u00ac\u00a9")
        buf.write("\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad")
        buf.write("\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2")
        buf.write("\u00af\33\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b2\t\3")
        buf.write("\2\2\u00b2\u00b5\7\u0084\2\2\u00b3\u00b4\7\21\2\2\u00b4")
        buf.write("\u00b6\5\16\b\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2")
        buf.write("\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\7\7\2\2\u00b8\u00b9")
        buf.write("\5\32\16\2\u00b9\u00ba\7\b\2\2\u00ba\u00bb\7\17\2\2\u00bb")
        buf.write("\35\3\2\2\2\u00bc\u00bd\5\2\2\2\u00bd\37\3\2\2\2\u00be")
        buf.write("\u00c5\7\u0084\2\2\u00bf\u00c0\7\u0084\2\2\u00c0\u00c1")
        buf.write("\7\t\2\2\u00c1\u00c2\5\"\22\2\u00c2\u00c3\7\n\2\2\u00c3")
        buf.write("\u00c5\3\2\2\2\u00c4\u00be\3\2\2\2\u00c4\u00bf\3\2\2\2")
        buf.write("\u00c5!\3\2\2\2\u00c6\u00c7\b\22\1\2\u00c7\u00d5\5(\25")
        buf.write("\2\u00c8\u00d5\5\2\2\2\u00c9\u00d5\7\u0084\2\2\u00ca\u00cb")
        buf.write("\7\13\2\2\u00cb\u00cc\5\"\22\2\u00cc\u00cd\7\f\2\2\u00cd")
        buf.write("\u00d5\3\2\2\2\u00ce\u00cf\7W\2\2\u00cf\u00d5\5\"\22\27")
        buf.write("\u00d0\u00d1\5 \21\2\u00d1\u00d2\7\22\2\2\u00d2\u00d3")
        buf.write("\5\"\22\3\u00d3\u00d5\3\2\2\2\u00d4\u00c6\3\2\2\2\u00d4")
        buf.write("\u00c8\3\2\2\2\u00d4\u00c9\3\2\2\2\u00d4\u00ca\3\2\2\2")
        buf.write("\u00d4\u00ce\3\2\2\2\u00d4\u00d0\3\2\2\2\u00d5\u0113\3")
        buf.write("\2\2\2\u00d6\u00d7\f\26\2\2\u00d7\u00d8\7\27\2\2\u00d8")
        buf.write("\u0112\5\"\22\27\u00d9\u00da\f\25\2\2\u00da\u00db\7\31")
        buf.write("\2\2\u00db\u0112\5\"\22\26\u00dc\u00dd\f\24\2\2\u00dd")
        buf.write("\u00de\7\33\2\2\u00de\u0112\5\"\22\25\u00df\u00e0\f\23")
        buf.write("\2\2\u00e0\u00e1\7\23\2\2\u00e1\u0112\5\"\22\24\u00e2")
        buf.write("\u00e3\f\22\2\2\u00e3\u00e4\7\25\2\2\u00e4\u0112\5\"\22")
        buf.write("\23\u00e5\u00e6\f\21\2\2\u00e6\u00e7\7/\2\2\u00e7\u0112")
        buf.write("\5\"\22\22\u00e8\u00e9\f\20\2\2\u00e9\u00ea\7.\2\2\u00ea")
        buf.write("\u0112\5\"\22\21\u00eb\u00ec\f\17\2\2\u00ec\u00ed\7}\2")
        buf.write("\2\u00ed\u0112\5\"\22\20\u00ee\u00ef\f\16\2\2\u00ef\u00f0")
        buf.write("\7[\2\2\u00f0\u0112\5\"\22\17\u00f1\u00f2\f\r\2\2\u00f2")
        buf.write("\u00f3\7*\2\2\u00f3\u0112\5\"\22\16\u00f4\u00f5\f\f\2")
        buf.write("\2\u00f5\u00f6\7\35\2\2\u00f6\u0112\5\"\22\r\u00f7\u00f8")
        buf.write("\f\13\2\2\u00f8\u00f9\7\37\2\2\u00f9\u0112\5\"\22\f\u00fa")
        buf.write("\u00fb\f\n\2\2\u00fb\u00fc\7\3\2\2\u00fc\u0112\5\"\22")
        buf.write("\13\u00fd\u00fe\f\t\2\2\u00fe\u00ff\7\4\2\2\u00ff\u0112")
        buf.write("\5\"\22\n\u0100\u0101\f\b\2\2\u0101\u0102\7$\2\2\u0102")
        buf.write("\u0112\5\"\22\t\u0103\u0104\f\7\2\2\u0104\u0105\7%\2\2")
        buf.write("\u0105\u0112\5\"\22\b\u0106\u0107\f\6\2\2\u0107\u0108")
        buf.write("\7!\2\2\u0108\u0112\5\"\22\7\u0109\u010a\f\5\2\2\u010a")
        buf.write("\u010b\7X\2\2\u010b\u0112\5\"\22\6\u010c\u010d\f\4\2\2")
        buf.write("\u010d\u010e\7\t\2\2\u010e\u010f\5\"\22\2\u010f\u0110")
        buf.write("\7\n\2\2\u0110\u0112\3\2\2\2\u0111\u00d6\3\2\2\2\u0111")
        buf.write("\u00d9\3\2\2\2\u0111\u00dc\3\2\2\2\u0111\u00df\3\2\2\2")
        buf.write("\u0111\u00e2\3\2\2\2\u0111\u00e5\3\2\2\2\u0111\u00e8\3")
        buf.write("\2\2\2\u0111\u00eb\3\2\2\2\u0111\u00ee\3\2\2\2\u0111\u00f1")
        buf.write("\3\2\2\2\u0111\u00f4\3\2\2\2\u0111\u00f7\3\2\2\2\u0111")
        buf.write("\u00fa\3\2\2\2\u0111\u00fd\3\2\2\2\u0111\u0100\3\2\2\2")
        buf.write("\u0111\u0103\3\2\2\2\u0111\u0106\3\2\2\2\u0111\u0109\3")
        buf.write("\2\2\2\u0111\u010c\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0111")
        buf.write("\3\2\2\2\u0113\u0114\3\2\2\2\u0114#\3\2\2\2\u0115\u0113")
        buf.write("\3\2\2\2\u0116\u0126\5*\26\2\u0117\u0126\5.\30\2\u0118")
        buf.write("\u0126\5\60\31\2\u0119\u0126\5\62\32\2\u011a\u0126\5\64")
        buf.write("\33\2\u011b\u0126\5\66\34\2\u011c\u0126\58\35\2\u011d")
        buf.write("\u0126\5:\36\2\u011e\u0126\5&\24\2\u011f\u0126\5@!\2\u0120")
        buf.write("\u0126\5> \2\u0121\u0123\5\"\22\2\u0122\u0121\3\2\2\2")
        buf.write("\u0122\u0123\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0126\7")
        buf.write("\17\2\2\u0125\u0116\3\2\2\2\u0125\u0117\3\2\2\2\u0125")
        buf.write("\u0118\3\2\2\2\u0125\u0119\3\2\2\2\u0125\u011a\3\2\2\2")
        buf.write("\u0125\u011b\3\2\2\2\u0125\u011c\3\2\2\2\u0125\u011d\3")
        buf.write("\2\2\2\u0125\u011e\3\2\2\2\u0125\u011f\3\2\2\2\u0125\u0120")
        buf.write("\3\2\2\2\u0125\u0122\3\2\2\2\u0126%\3\2\2\2\u0127\u012b")
        buf.write("\7\7\2\2\u0128\u012a\5$\23\2\u0129\u0128\3\2\2\2\u012a")
        buf.write("\u012d\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2")
        buf.write("\u012c\u012e\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u012f\7")
        buf.write("\b\2\2\u012f\'\3\2\2\2\u0130\u0131\7\u0084\2\2\u0131\u013a")
        buf.write("\7\13\2\2\u0132\u0137\5\"\22\2\u0133\u0134\7\16\2\2\u0134")
        buf.write("\u0136\5\"\22\2\u0135\u0133\3\2\2\2\u0136\u0139\3\2\2")
        buf.write("\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013b")
        buf.write("\3\2\2\2\u0139\u0137\3\2\2\2\u013a\u0132\3\2\2\2\u013a")
        buf.write("\u013b\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\7\f\2\2")
        buf.write("\u013d)\3\2\2\2\u013e\u013f\7P\2\2\u013f\u0140\7\13\2")
        buf.write("\2\u0140\u0141\5\"\22\2\u0141\u0142\7\f\2\2\u0142\u0145")
        buf.write("\5$\23\2\u0143\u0144\7F\2\2\u0144\u0146\5$\23\2\u0145")
        buf.write("\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146+\3\2\2\2\u0147")
        buf.write("\u0148\7\62\2\2\u0148\u0149\5\36\20\2\u0149\u014a\7\21")
        buf.write("\2\2\u014a\u014b\5$\23\2\u014b-\3\2\2\2\u014c\u014d\7")
        buf.write("k\2\2\u014d\u014e\7\13\2\2\u014e\u014f\5\"\22\2\u014f")
        buf.write("\u0150\7\f\2\2\u0150\u0154\7\7\2\2\u0151\u0153\5,\27\2")
        buf.write("\u0152\u0151\3\2\2\2\u0153\u0156\3\2\2\2\u0154\u0152\3")
        buf.write("\2\2\2\u0154\u0155\3\2\2\2\u0155\u0157\3\2\2\2\u0156\u0154")
        buf.write("\3\2\2\2\u0157\u0158\7\b\2\2\u0158/\3\2\2\2\u0159\u015a")
        buf.write("\7|\2\2\u015a\u015b\7\13\2\2\u015b\u015c\5\"\22\2\u015c")
        buf.write("\u015d\7\f\2\2\u015d\u015e\5$\23\2\u015e\61\3\2\2\2\u015f")
        buf.write("\u0160\7C\2\2\u0160\u0161\5$\23\2\u0161\u0162\7|\2\2\u0162")
        buf.write("\u0163\7\13\2\2\u0163\u0164\5\"\22\2\u0164\u0165\7\f\2")
        buf.write("\2\u0165\u0166\7\17\2\2\u0166\63\3\2\2\2\u0167\u0168\7")
        buf.write("M\2\2\u0168\u016a\7\13\2\2\u0169\u016b\5\"\22\2\u016a")
        buf.write("\u0169\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016c\u016e\7\17\2\2\u016d\u016f\5\"\22\2\u016e\u016d")
        buf.write("\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\3\2\2\2\u0170")
        buf.write("\u0172\7\17\2\2\u0171\u0173\5\"\22\2\u0172\u0171\3\2\2")
        buf.write("\2\u0172\u0173\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175")
        buf.write("\7\f\2\2\u0175\u0176\5$\23\2\u0176\65\3\2\2\2\u0177\u0179")
        buf.write("\7c\2\2\u0178\u017a\5\"\22\2\u0179\u0178\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\7\17\2")
        buf.write("\2\u017c\67\3\2\2\2\u017d\u017e\7\61\2\2\u017e\u017f\7")
        buf.write("\17\2\2\u017f9\3\2\2\2\u0180\u0181\7@\2\2\u0181\u0182")
        buf.write("\7\17\2\2\u0182;\3\2\2\2\u0183\u0188\5> \2\u0184\u0188")
        buf.write("\5@!\2\u0185\u0188\5B\"\2\u0186\u0188\5\34\17\2\u0187")
        buf.write("\u0183\3\2\2\2\u0187\u0184\3\2\2\2\u0187\u0185\3\2\2\2")
        buf.write("\u0187\u0186\3\2\2\2\u0188=\3\2\2\2\u0189\u018a\5F$\2")
        buf.write("\u018a\u018b\7\u0084\2\2\u018b\u018c\7\t\2\2\u018c\u018d")
        buf.write("\5\"\22\2\u018d\u019a\7\n\2\2\u018e\u018f\7\22\2\2\u018f")
        buf.write("\u0190\7\7\2\2\u0190\u0195\5\"\22\2\u0191\u0192\7\16\2")
        buf.write("\2\u0192\u0194\5\"\22\2\u0193\u0191\3\2\2\2\u0194\u0197")
        buf.write("\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write("\u0198\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u0199\7\7\2\2")
        buf.write("\u0199\u019b\3\2\2\2\u019a\u018e\3\2\2\2\u019a\u019b\3")
        buf.write("\2\2\2\u019b?\3\2\2\2\u019c\u019d\5F$\2\u019d\u01a0\7")
        buf.write("\u0084\2\2\u019e\u019f\7\22\2\2\u019f\u01a1\5\"\22\2\u01a0")
        buf.write("\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01aa\3\2\2\2")
        buf.write("\u01a2\u01a3\7\16\2\2\u01a3\u01a6\7\u0084\2\2\u01a4\u01a5")
        buf.write("\7\22\2\2\u01a5\u01a7\5\"\22\2\u01a6\u01a4\3\2\2\2\u01a6")
        buf.write("\u01a7\3\2\2\2\u01a7\u01a9\3\2\2\2\u01a8\u01a2\3\2\2\2")
        buf.write("\u01a9\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3")
        buf.write("\2\2\2\u01ab\u01ad\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01ae")
        buf.write("\7\17\2\2\u01aeA\3\2\2\2\u01af\u01b0\5F$\2\u01b0\u01b1")
        buf.write("\7\u0084\2\2\u01b1\u01ba\7\13\2\2\u01b2\u01b7\5D#\2\u01b3")
        buf.write("\u01b4\7\16\2\2\u01b4\u01b6\5D#\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3")
        buf.write("\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba\u01b2")
        buf.write("\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("\u01bd\7\f\2\2\u01bd\u01be\5&\24\2\u01beC\3\2\2\2\u01bf")
        buf.write("\u01c0\5F$\2\u01c0\u01c1\7\u0084\2\2\u01c1E\3\2\2\2\u01c2")
        buf.write("\u01c8\5H%\2\u01c3\u01c8\5J&\2\u01c4\u01c8\5L\'\2\u01c5")
        buf.write("\u01c8\5N(\2\u01c6\u01c8\5P)\2\u01c7\u01c2\3\2\2\2\u01c7")
        buf.write("\u01c3\3\2\2\2\u01c7\u01c4\3\2\2\2\u01c7\u01c5\3\2\2\2")
        buf.write("\u01c7\u01c6\3\2\2\2\u01c8G\3\2\2\2\u01c9\u01cf\7R\2\2")
        buf.write("\u01ca\u01cf\7S\2\2\u01cb\u01cf\7d\2\2\u01cc\u01cd\7S")
        buf.write("\2\2\u01cd\u01cf\7S\2\2\u01ce\u01c9\3\2\2\2\u01ce\u01ca")
        buf.write("\3\2\2\2\u01ce\u01cb\3\2\2\2\u01ce\u01cc\3\2\2\2\u01cf")
        buf.write("I\3\2\2\2\u01d0\u01d5\7L\2\2\u01d1\u01d5\7D\2\2\u01d2")
        buf.write("\u01d3\7S\2\2\u01d3\u01d5\7D\2\2\u01d4\u01d0\3\2\2\2\u01d4")
        buf.write("\u01d1\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d5K\3\2\2\2\u01d6")
        buf.write("\u01d7\7\60\2\2\u01d7M\3\2\2\2\u01d8\u01d9\7\64\2\2\u01d9")
        buf.write("O\3\2\2\2\u01da\u01db\7y\2\2\u01dbQ\3\2\2\2,V\\_fltx~")
        buf.write("\u0083\u008d\u0096\u0099\u009e\u00ac\u00ae\u00b5\u00c4")
        buf.write("\u00d4\u0111\u0113\u0122\u0125\u012b\u0137\u013a\u0145")
        buf.write("\u0154\u016a\u016e\u0172\u0179\u0187\u0195\u019a\u01a0")
        buf.write("\u01a6\u01aa\u01b7\u01ba\u01c7\u01ce\u01d4")
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
                      "NEWLINE", "LINE_COMMENT", "COMMENT", "IntegerSuffix", 
                      "Identifier", "DecimalLiteral", "FloatingLiteral", 
                      "DigitSequence", "DecimalExponent", "CharTypeSpecificaton", 
                      "CChar", "Escapesequence", "Simpleescapesequence", 
                      "Octalescapesequence", "Hexadecimalescapesequence", 
                      "Universalcharactername", "SChar" ]

    RULE_literals = 0
    RULE_floatingLiteral = 1
    RULE_integerLiteral = 2
    RULE_characterLiteral = 3
    RULE_stringLiteral = 4
    RULE_translationUnit = 5
    RULE_baseSpecifierList = 6
    RULE_accessSpecifier = 7
    RULE_accessLabel = 8
    RULE_memberDeclaration = 9
    RULE_constructorDeclaration = 10
    RULE_destructorDeclaration = 11
    RULE_memberSpecification = 12
    RULE_classDefinition = 13
    RULE_constExpression = 14
    RULE_leftExpression = 15
    RULE_expression = 16
    RULE_statement = 17
    RULE_block = 18
    RULE_functionCall = 19
    RULE_ifStatement = 20
    RULE_caseStatement = 21
    RULE_switchStatement = 22
    RULE_whileStatement = 23
    RULE_doWhileStatement = 24
    RULE_forStatement = 25
    RULE_returnStatement = 26
    RULE_breakStatement = 27
    RULE_continueStatement = 28
    RULE_declaration = 29
    RULE_arrayDeclarator = 30
    RULE_variableDeclaration = 31
    RULE_functionDeclaration = 32
    RULE_functionParameter = 33
    RULE_typeSpecifier = 34
    RULE_integerTypeSpecifier = 35
    RULE_realTypeSpecifier = 36
    RULE_booleanTypeSpecifier = 37
    RULE_charTypeSpecifier = 38
    RULE_voidTypeSpecifier = 39

    ruleNames =  [ "literals", "floatingLiteral", "integerLiteral", "characterLiteral", 
                   "stringLiteral", "translationUnit", "baseSpecifierList", 
                   "accessSpecifier", "accessLabel", "memberDeclaration", 
                   "constructorDeclaration", "destructorDeclaration", "memberSpecification", 
                   "classDefinition", "constExpression", "leftExpression", 
                   "expression", "statement", "block", "functionCall", "ifStatement", 
                   "caseStatement", "switchStatement", "whileStatement", 
                   "doWhileStatement", "forStatement", "returnStatement", 
                   "breakStatement", "continueStatement", "declaration", 
                   "arrayDeclarator", "variableDeclaration", "functionDeclaration", 
                   "functionParameter", "typeSpecifier", "integerTypeSpecifier", 
                   "realTypeSpecifier", "booleanTypeSpecifier", "charTypeSpecifier", 
                   "voidTypeSpecifier" ]

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
    IntegerSuffix=129
    Identifier=130
    DecimalLiteral=131
    FloatingLiteral=132
    DigitSequence=133
    DecimalExponent=134
    CharTypeSpecificaton=135
    CChar=136
    Escapesequence=137
    Simpleescapesequence=138
    Octalescapesequence=139
    Hexadecimalescapesequence=140
    Universalcharactername=141
    SChar=142

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LiteralsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def floatingLiteral(self):
            return self.getTypedRuleContext(cpp20Parser.FloatingLiteralContext,0)


        def integerLiteral(self):
            return self.getTypedRuleContext(cpp20Parser.IntegerLiteralContext,0)


        def characterLiteral(self):
            return self.getTypedRuleContext(cpp20Parser.CharacterLiteralContext,0)


        def stringLiteral(self):
            return self.getTypedRuleContext(cpp20Parser.StringLiteralContext,0)


        def getRuleIndex(self):
            return cpp20Parser.RULE_literals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiterals" ):
                listener.enterLiterals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiterals" ):
                listener.exitLiterals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = cpp20Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_literals)
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.floatingLiteral()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.integerLiteral()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.characterLiteral()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 83
                self.stringLiteral()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatingLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FloatingLiteral(self):
            return self.getToken(cpp20Parser.FloatingLiteral, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_floatingLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatingLiteral" ):
                listener.enterFloatingLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatingLiteral" ):
                listener.exitFloatingLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatingLiteral" ):
                return visitor.visitFloatingLiteral(self)
            else:
                return visitor.visitChildren(self)




    def floatingLiteral(self):

        localctx = cpp20Parser.FloatingLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_floatingLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(cpp20Parser.FloatingLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DecimalLiteral(self):
            return self.getToken(cpp20Parser.DecimalLiteral, 0)

        def IntegerSuffix(self):
            return self.getToken(cpp20Parser.IntegerSuffix, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_integerLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegerLiteral" ):
                listener.enterIntegerLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegerLiteral" ):
                listener.exitIntegerLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerLiteral" ):
                return visitor.visitIntegerLiteral(self)
            else:
                return visitor.visitChildren(self)




    def integerLiteral(self):

        localctx = cpp20Parser.IntegerLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_integerLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(cpp20Parser.DecimalLiteral)
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 89
                self.match(cpp20Parser.IntegerSuffix)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharacterLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(cpp20Parser.SQUOTE)
            else:
                return self.getToken(cpp20Parser.SQUOTE, i)

        def CChar(self):
            return self.getToken(cpp20Parser.CChar, 0)

        def CharTypeSpecificaton(self):
            return self.getToken(cpp20Parser.CharTypeSpecificaton, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_characterLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCharacterLiteral" ):
                listener.enterCharacterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCharacterLiteral" ):
                listener.exitCharacterLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharacterLiteral" ):
                return visitor.visitCharacterLiteral(self)
            else:
                return visitor.visitChildren(self)




    def characterLiteral(self):

        localctx = cpp20Parser.CharacterLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_characterLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.CharTypeSpecificaton:
                self.state = 92
                self.match(cpp20Parser.CharTypeSpecificaton)


            self.state = 95
            self.match(cpp20Parser.SQUOTE)
            self.state = 96
            self.match(cpp20Parser.CChar)
            self.state = 97
            self.match(cpp20Parser.SQUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(cpp20Parser.DQUOTE)
            else:
                return self.getToken(cpp20Parser.DQUOTE, i)

        def CharTypeSpecificaton(self):
            return self.getToken(cpp20Parser.CharTypeSpecificaton, 0)

        def SChar(self, i:int=None):
            if i is None:
                return self.getTokens(cpp20Parser.SChar)
            else:
                return self.getToken(cpp20Parser.SChar, i)

        def getRuleIndex(self):
            return cpp20Parser.RULE_stringLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)




    def stringLiteral(self):

        localctx = cpp20Parser.StringLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stringLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.CharTypeSpecificaton:
                self.state = 99
                self.match(cpp20Parser.CharTypeSpecificaton)


            self.state = 102
            self.match(cpp20Parser.DQUOTE)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cpp20Parser.SChar:
                self.state = 103
                self.match(cpp20Parser.SChar)
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
            self.match(cpp20Parser.DQUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TranslationUnitContext(ParserRuleContext):

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
        self.enterRule(localctx, 10, self.RULE_translationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.BOOL) | (1 << cpp20Parser.CHAR) | (1 << cpp20Parser.CLASS))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (cpp20Parser.DOUBLE - 66)) | (1 << (cpp20Parser.FLOAT - 66)) | (1 << (cpp20Parser.INT - 66)) | (1 << (cpp20Parser.LONG - 66)) | (1 << (cpp20Parser.SHORT - 66)) | (1 << (cpp20Parser.STRUCT - 66)) | (1 << (cpp20Parser.VOID - 66)))) != 0):
                self.state = 111
                self.declaration()
                self.state = 116
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
        self.enterRule(localctx, 12, self.RULE_baseSpecifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 91)) & ~0x3f) == 0 and ((1 << (_la - 91)) & ((1 << (cpp20Parser.PRIVATE - 91)) | (1 << (cpp20Parser.PROTECTED - 91)) | (1 << (cpp20Parser.PUBLIC - 91)))) != 0):
                self.state = 117
                self.accessSpecifier()


            self.state = 120
            self.match(cpp20Parser.Identifier)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cpp20Parser.COMMA:
                self.state = 122
                self.match(cpp20Parser.COMMA)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 91)) & ~0x3f) == 0 and ((1 << (_la - 91)) & ((1 << (cpp20Parser.PRIVATE - 91)) | (1 << (cpp20Parser.PROTECTED - 91)) | (1 << (cpp20Parser.PUBLIC - 91)))) != 0):
                    self.state = 123
                    self.accessSpecifier()


                self.state = 126
                self.match(cpp20Parser.Identifier)
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


    class AccessSpecifierContext(ParserRuleContext):

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
        self.enterRule(localctx, 14, self.RULE_accessSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
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
        self.enterRule(localctx, 16, self.RULE_accessLabel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.accessSpecifier()
            self.state = 135
            self.match(cpp20Parser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberDeclarationContext(ParserRuleContext):

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
        self.enterRule(localctx, 18, self.RULE_memberDeclaration)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.functionDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
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
        self.enterRule(localctx, 20, self.RULE_constructorDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(cpp20Parser.Identifier)
            self.state = 142
            self.match(cpp20Parser.LPAREN)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.BOOL or _la==cpp20Parser.CHAR or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (cpp20Parser.DOUBLE - 66)) | (1 << (cpp20Parser.FLOAT - 66)) | (1 << (cpp20Parser.INT - 66)) | (1 << (cpp20Parser.LONG - 66)) | (1 << (cpp20Parser.SHORT - 66)) | (1 << (cpp20Parser.VOID - 66)))) != 0):
                self.state = 143
                self.functionParameter()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cpp20Parser.COMMA:
                    self.state = 144
                    self.match(cpp20Parser.COMMA)
                    self.state = 145
                    self.functionParameter()
                    self.state = 150
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 153
            self.match(cpp20Parser.RPAREN)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.COLON:
                self.state = 154
                self.match(cpp20Parser.COLON)
                self.state = 155
                self.functionCall()


            self.state = 158
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorDeclarationContext(ParserRuleContext):

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
        self.enterRule(localctx, 22, self.RULE_destructorDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(cpp20Parser.COMPL)
            self.state = 161
            self.match(cpp20Parser.Identifier)
            self.state = 162
            self.match(cpp20Parser.LPAREN)
            self.state = 163
            self.match(cpp20Parser.RPAREN)
            self.state = 164
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberSpecificationContext(ParserRuleContext):

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
        self.enterRule(localctx, 24, self.RULE_memberSpecification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & ((1 << (cpp20Parser.BOOL - 46)) | (1 << (cpp20Parser.CHAR - 46)) | (1 << (cpp20Parser.COMPL - 46)) | (1 << (cpp20Parser.DOUBLE - 46)) | (1 << (cpp20Parser.FLOAT - 46)) | (1 << (cpp20Parser.INT - 46)) | (1 << (cpp20Parser.LONG - 46)) | (1 << (cpp20Parser.PRIVATE - 46)) | (1 << (cpp20Parser.PROTECTED - 46)) | (1 << (cpp20Parser.PUBLIC - 46)) | (1 << (cpp20Parser.SHORT - 46)))) != 0) or _la==cpp20Parser.VOID or _la==cpp20Parser.Identifier:
                self.state = 170
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [cpp20Parser.PRIVATE, cpp20Parser.PROTECTED, cpp20Parser.PUBLIC]:
                    self.state = 166
                    self.accessLabel()
                    pass
                elif token in [cpp20Parser.BOOL, cpp20Parser.CHAR, cpp20Parser.DOUBLE, cpp20Parser.FLOAT, cpp20Parser.INT, cpp20Parser.LONG, cpp20Parser.SHORT, cpp20Parser.VOID]:
                    self.state = 167
                    self.memberDeclaration()
                    pass
                elif token in [cpp20Parser.Identifier]:
                    self.state = 168
                    self.constructorDeclaration()
                    pass
                elif token in [cpp20Parser.COMPL]:
                    self.state = 169
                    self.destructorDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 174
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
        self.enterRule(localctx, 26, self.RULE_classDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            _la = self._input.LA(1)
            if not(_la==cpp20Parser.CLASS or _la==cpp20Parser.STRUCT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 176
            self.match(cpp20Parser.Identifier)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.COLON:
                self.state = 177
                self.match(cpp20Parser.COLON)
                self.state = 178
                self.baseSpecifierList()


            self.state = 181
            self.match(cpp20Parser.LBRACE)
            self.state = 182
            self.memberSpecification()
            self.state = 183
            self.match(cpp20Parser.RBRACE)
            self.state = 184
            self.match(cpp20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(cpp20Parser.LiteralsContext,0)


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
        self.enterRule(localctx, 28, self.RULE_constExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.literals()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeftExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)

        def LSQUARE(self):
            return self.getToken(cpp20Parser.LSQUARE, 0)

        def expression(self):
            return self.getTypedRuleContext(cpp20Parser.ExpressionContext,0)


        def RSQUARE(self):
            return self.getToken(cpp20Parser.RSQUARE, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_leftExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeftExpression" ):
                listener.enterLeftExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeftExpression" ):
                listener.exitLeftExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeftExpression" ):
                return visitor.visitLeftExpression(self)
            else:
                return visitor.visitChildren(self)




    def leftExpression(self):

        localctx = cpp20Parser.LeftExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_leftExpression)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(cpp20Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(cpp20Parser.Identifier)

                self.state = 190
                self.match(cpp20Parser.LSQUARE)
                self.state = 191
                self.expression(0)
                self.state = 192
                self.match(cpp20Parser.RSQUARE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(cpp20Parser.FunctionCallContext,0)


        def literals(self):
            return self.getTypedRuleContext(cpp20Parser.LiteralsContext,0)


        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(cpp20Parser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(cpp20Parser.RPAREN, 0)

        def NOT(self):
            return self.getToken(cpp20Parser.NOT, 0)

        def leftExpression(self):
            return self.getTypedRuleContext(cpp20Parser.LeftExpressionContext,0)


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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 197
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 198
                self.literals()
                pass

            elif la_ == 3:
                self.state = 199
                self.match(cpp20Parser.Identifier)
                pass

            elif la_ == 4:
                self.state = 200
                self.match(cpp20Parser.LPAREN)
                self.state = 201
                self.expression(0)
                self.state = 202
                self.match(cpp20Parser.RPAREN)
                pass

            elif la_ == 5:
                self.state = 204
                self.match(cpp20Parser.NOT)
                self.state = 205
                self.expression(21)
                pass

            elif la_ == 6:
                self.state = 206
                self.leftExpression()
                self.state = 207
                self.match(cpp20Parser.ASSIGN)
                self.state = 208
                self.expression(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 271
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 212
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 213
                        self.match(cpp20Parser.MULT)
                        self.state = 214
                        self.expression(21)
                        pass

                    elif la_ == 2:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 215
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 216
                        self.match(cpp20Parser.DIV)
                        self.state = 217
                        self.expression(20)
                        pass

                    elif la_ == 3:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 218
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 219
                        self.match(cpp20Parser.MOD)
                        self.state = 220
                        self.expression(19)
                        pass

                    elif la_ == 4:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 221
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 222
                        self.match(cpp20Parser.ADD)
                        self.state = 223
                        self.expression(18)
                        pass

                    elif la_ == 5:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 224
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 225
                        self.match(cpp20Parser.SUB)
                        self.state = 226
                        self.expression(17)
                        pass

                    elif la_ == 6:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 227
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 228
                        self.match(cpp20Parser.BITOR)
                        self.state = 229
                        self.expression(16)
                        pass

                    elif la_ == 7:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 230
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 231
                        self.match(cpp20Parser.BITAND)
                        self.state = 232
                        self.expression(15)
                        pass

                    elif la_ == 8:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 233
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 234
                        self.match(cpp20Parser.XOR)
                        self.state = 235
                        self.expression(14)
                        pass

                    elif la_ == 9:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 236
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 237
                        self.match(cpp20Parser.OR)
                        self.state = 238
                        self.expression(13)
                        pass

                    elif la_ == 10:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 239
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 240
                        self.match(cpp20Parser.AND)
                        self.state = 241
                        self.expression(12)
                        pass

                    elif la_ == 11:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 242
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 243
                        self.match(cpp20Parser.LSHIFT)
                        self.state = 244
                        self.expression(11)
                        pass

                    elif la_ == 12:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 245
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 246
                        self.match(cpp20Parser.RSHIFT)
                        self.state = 247
                        self.expression(10)
                        pass

                    elif la_ == 13:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 248
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 249
                        self.match(cpp20Parser.LT)
                        self.state = 250
                        self.expression(9)
                        pass

                    elif la_ == 14:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 251
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 252
                        self.match(cpp20Parser.GT)
                        self.state = 253
                        self.expression(8)
                        pass

                    elif la_ == 15:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 254
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 255
                        self.match(cpp20Parser.LEQ)
                        self.state = 256
                        self.expression(7)
                        pass

                    elif la_ == 16:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 257
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 258
                        self.match(cpp20Parser.GEQ)
                        self.state = 259
                        self.expression(6)
                        pass

                    elif la_ == 17:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 260
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 261
                        self.match(cpp20Parser.EQ)
                        self.state = 262
                        self.expression(5)
                        pass

                    elif la_ == 18:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 263
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 264
                        self.match(cpp20Parser.NOT_EQ)
                        self.state = 265
                        self.expression(4)
                        pass

                    elif la_ == 19:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 266
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 267
                        self.match(cpp20Parser.LSQUARE)
                        self.state = 268
                        self.expression(0)
                        self.state = 269
                        self.match(cpp20Parser.RSQUARE)
                        pass

             
                self.state = 275
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):

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
        self.enterRule(localctx, 34, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.ifStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.switchStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 278
                self.whileStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 279
                self.doWhileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 280
                self.forStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 281
                self.returnStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 282
                self.breakStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 283
                self.continueStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 284
                self.block()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 285
                self.variableDeclaration()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 286
                self.arrayDeclarator()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.DQUOTE) | (1 << cpp20Parser.SQUOTE) | (1 << cpp20Parser.LPAREN))) != 0) or ((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (cpp20Parser.NOT - 85)) | (1 << (cpp20Parser.Identifier - 85)) | (1 << (cpp20Parser.DecimalLiteral - 85)) | (1 << (cpp20Parser.FloatingLiteral - 85)) | (1 << (cpp20Parser.CharTypeSpecificaton - 85)))) != 0):
                    self.state = 287
                    self.expression(0)


                self.state = 290
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
        self.enterRule(localctx, 36, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(cpp20Parser.LBRACE)
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 3)) & ~0x3f) == 0 and ((1 << (_la - 3)) & ((1 << (cpp20Parser.DQUOTE - 3)) | (1 << (cpp20Parser.SQUOTE - 3)) | (1 << (cpp20Parser.LBRACE - 3)) | (1 << (cpp20Parser.LPAREN - 3)) | (1 << (cpp20Parser.SEMI - 3)) | (1 << (cpp20Parser.BOOL - 3)) | (1 << (cpp20Parser.BREAK - 3)) | (1 << (cpp20Parser.CHAR - 3)) | (1 << (cpp20Parser.CONTINUE - 3)) | (1 << (cpp20Parser.DO - 3)) | (1 << (cpp20Parser.DOUBLE - 3)))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (cpp20Parser.FLOAT - 74)) | (1 << (cpp20Parser.FOR - 74)) | (1 << (cpp20Parser.IF - 74)) | (1 << (cpp20Parser.INT - 74)) | (1 << (cpp20Parser.LONG - 74)) | (1 << (cpp20Parser.NOT - 74)) | (1 << (cpp20Parser.RETURN - 74)) | (1 << (cpp20Parser.SHORT - 74)) | (1 << (cpp20Parser.SWITCH - 74)) | (1 << (cpp20Parser.VOID - 74)) | (1 << (cpp20Parser.WHILE - 74)) | (1 << (cpp20Parser.Identifier - 74)) | (1 << (cpp20Parser.DecimalLiteral - 74)) | (1 << (cpp20Parser.FloatingLiteral - 74)) | (1 << (cpp20Parser.CharTypeSpecificaton - 74)))) != 0):
                self.state = 294
                self.statement()
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 300
            self.match(cpp20Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):

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
        self.enterRule(localctx, 38, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(cpp20Parser.Identifier)
            self.state = 303
            self.match(cpp20Parser.LPAREN)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.DQUOTE) | (1 << cpp20Parser.SQUOTE) | (1 << cpp20Parser.LPAREN))) != 0) or ((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (cpp20Parser.NOT - 85)) | (1 << (cpp20Parser.Identifier - 85)) | (1 << (cpp20Parser.DecimalLiteral - 85)) | (1 << (cpp20Parser.FloatingLiteral - 85)) | (1 << (cpp20Parser.CharTypeSpecificaton - 85)))) != 0):
                self.state = 304
                self.expression(0)
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cpp20Parser.COMMA:
                    self.state = 305
                    self.match(cpp20Parser.COMMA)
                    self.state = 306
                    self.expression(0)
                    self.state = 311
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 314
            self.match(cpp20Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):

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
        self.enterRule(localctx, 40, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(cpp20Parser.IF)
            self.state = 317
            self.match(cpp20Parser.LPAREN)
            self.state = 318
            self.expression(0)
            self.state = 319
            self.match(cpp20Parser.RPAREN)
            self.state = 320
            self.statement()
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 321
                self.match(cpp20Parser.ELSE)
                self.state = 322
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseStatementContext(ParserRuleContext):

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
        self.enterRule(localctx, 42, self.RULE_caseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(cpp20Parser.CASE)
            self.state = 326
            self.constExpression()
            self.state = 327
            self.match(cpp20Parser.COLON)
            self.state = 328
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):

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
        self.enterRule(localctx, 44, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(cpp20Parser.SWITCH)
            self.state = 331
            self.match(cpp20Parser.LPAREN)
            self.state = 332
            self.expression(0)
            self.state = 333
            self.match(cpp20Parser.RPAREN)
            self.state = 334
            self.match(cpp20Parser.LBRACE)
            self.state = 338
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cpp20Parser.CASE:
                self.state = 335
                self.caseStatement()
                self.state = 340
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 341
            self.match(cpp20Parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):

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
        self.enterRule(localctx, 46, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(cpp20Parser.WHILE)
            self.state = 344
            self.match(cpp20Parser.LPAREN)
            self.state = 345
            self.expression(0)
            self.state = 346
            self.match(cpp20Parser.RPAREN)
            self.state = 347
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):

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
        self.enterRule(localctx, 48, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(cpp20Parser.DO)
            self.state = 350
            self.statement()
            self.state = 351
            self.match(cpp20Parser.WHILE)
            self.state = 352
            self.match(cpp20Parser.LPAREN)
            self.state = 353
            self.expression(0)
            self.state = 354
            self.match(cpp20Parser.RPAREN)
            self.state = 355
            self.match(cpp20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):

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
        self.enterRule(localctx, 50, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(cpp20Parser.FOR)
            self.state = 358
            self.match(cpp20Parser.LPAREN)
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.DQUOTE) | (1 << cpp20Parser.SQUOTE) | (1 << cpp20Parser.LPAREN))) != 0) or ((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (cpp20Parser.NOT - 85)) | (1 << (cpp20Parser.Identifier - 85)) | (1 << (cpp20Parser.DecimalLiteral - 85)) | (1 << (cpp20Parser.FloatingLiteral - 85)) | (1 << (cpp20Parser.CharTypeSpecificaton - 85)))) != 0):
                self.state = 359
                self.expression(0)


            self.state = 362
            self.match(cpp20Parser.SEMI)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.DQUOTE) | (1 << cpp20Parser.SQUOTE) | (1 << cpp20Parser.LPAREN))) != 0) or ((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (cpp20Parser.NOT - 85)) | (1 << (cpp20Parser.Identifier - 85)) | (1 << (cpp20Parser.DecimalLiteral - 85)) | (1 << (cpp20Parser.FloatingLiteral - 85)) | (1 << (cpp20Parser.CharTypeSpecificaton - 85)))) != 0):
                self.state = 363
                self.expression(0)


            self.state = 366
            self.match(cpp20Parser.SEMI)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.DQUOTE) | (1 << cpp20Parser.SQUOTE) | (1 << cpp20Parser.LPAREN))) != 0) or ((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (cpp20Parser.NOT - 85)) | (1 << (cpp20Parser.Identifier - 85)) | (1 << (cpp20Parser.DecimalLiteral - 85)) | (1 << (cpp20Parser.FloatingLiteral - 85)) | (1 << (cpp20Parser.CharTypeSpecificaton - 85)))) != 0):
                self.state = 367
                self.expression(0)


            self.state = 370
            self.match(cpp20Parser.RPAREN)
            self.state = 371
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):

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
        self.enterRule(localctx, 52, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(cpp20Parser.RETURN)
            self.state = 375
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.DQUOTE) | (1 << cpp20Parser.SQUOTE) | (1 << cpp20Parser.LPAREN))) != 0) or ((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (cpp20Parser.NOT - 85)) | (1 << (cpp20Parser.Identifier - 85)) | (1 << (cpp20Parser.DecimalLiteral - 85)) | (1 << (cpp20Parser.FloatingLiteral - 85)) | (1 << (cpp20Parser.CharTypeSpecificaton - 85)))) != 0):
                self.state = 374
                self.expression(0)


            self.state = 377
            self.match(cpp20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):

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
        self.enterRule(localctx, 54, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(cpp20Parser.BREAK)
            self.state = 380
            self.match(cpp20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):

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
        self.enterRule(localctx, 56, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(cpp20Parser.CONTINUE)
            self.state = 383
            self.match(cpp20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):

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
        self.enterRule(localctx, 58, self.RULE_declaration)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 385
                self.arrayDeclarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self.variableDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 387
                self.functionDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 388
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
        self.enterRule(localctx, 60, self.RULE_arrayDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.typeSpecifier()
            self.state = 392
            self.match(cpp20Parser.Identifier)
            self.state = 393
            self.match(cpp20Parser.LSQUARE)
            self.state = 394
            self.expression(0)
            self.state = 395
            self.match(cpp20Parser.RSQUARE)
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.ASSIGN:
                self.state = 396
                self.match(cpp20Parser.ASSIGN)
                self.state = 397
                self.match(cpp20Parser.LBRACE)
                self.state = 398
                self.expression(0)
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cpp20Parser.COMMA:
                    self.state = 399
                    self.match(cpp20Parser.COMMA)
                    self.state = 400
                    self.expression(0)
                    self.state = 405
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 406
                self.match(cpp20Parser.LBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):

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
        self.enterRule(localctx, 62, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.typeSpecifier()
            self.state = 411
            self.match(cpp20Parser.Identifier)
            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.ASSIGN:
                self.state = 412
                self.match(cpp20Parser.ASSIGN)
                self.state = 413
                self.expression(0)


            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cpp20Parser.COMMA:
                self.state = 416
                self.match(cpp20Parser.COMMA)
                self.state = 417
                self.match(cpp20Parser.Identifier)
                self.state = 420
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==cpp20Parser.ASSIGN:
                    self.state = 418
                    self.match(cpp20Parser.ASSIGN)
                    self.state = 419
                    self.expression(0)


                self.state = 426
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 427
            self.match(cpp20Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):

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
        self.enterRule(localctx, 64, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.typeSpecifier()
            self.state = 430
            self.match(cpp20Parser.Identifier)
            self.state = 431
            self.match(cpp20Parser.LPAREN)
            self.state = 440
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.BOOL or _la==cpp20Parser.CHAR or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (cpp20Parser.DOUBLE - 66)) | (1 << (cpp20Parser.FLOAT - 66)) | (1 << (cpp20Parser.INT - 66)) | (1 << (cpp20Parser.LONG - 66)) | (1 << (cpp20Parser.SHORT - 66)) | (1 << (cpp20Parser.VOID - 66)))) != 0):
                self.state = 432
                self.functionParameter()
                self.state = 437
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cpp20Parser.COMMA:
                    self.state = 433
                    self.match(cpp20Parser.COMMA)
                    self.state = 434
                    self.functionParameter()
                    self.state = 439
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 442
            self.match(cpp20Parser.RPAREN)
            self.state = 443
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionParameterContext(ParserRuleContext):

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
        self.enterRule(localctx, 66, self.RULE_functionParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.typeSpecifier()
            self.state = 446
            self.match(cpp20Parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):

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
        self.enterRule(localctx, 68, self.RULE_typeSpecifier)
        try:
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.integerTypeSpecifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449
                self.realTypeSpecifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 450
                self.booleanTypeSpecifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 451
                self.charTypeSpecifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 452
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
        self.enterRule(localctx, 70, self.RULE_integerTypeSpecifier)
        try:
            self.state = 460
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(cpp20Parser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.match(cpp20Parser.LONG)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 457
                self.match(cpp20Parser.SHORT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 458
                self.match(cpp20Parser.LONG)
                self.state = 459
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
        self.enterRule(localctx, 72, self.RULE_realTypeSpecifier)
        try:
            self.state = 466
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cpp20Parser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.match(cpp20Parser.FLOAT)
                pass
            elif token in [cpp20Parser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.match(cpp20Parser.DOUBLE)
                pass
            elif token in [cpp20Parser.LONG]:
                self.enterOuterAlt(localctx, 3)
                self.state = 464
                self.match(cpp20Parser.LONG)
                self.state = 465
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
        self.enterRule(localctx, 74, self.RULE_booleanTypeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(cpp20Parser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharTypeSpecifierContext(ParserRuleContext):

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
        self.enterRule(localctx, 76, self.RULE_charTypeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(cpp20Parser.CHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidTypeSpecifierContext(ParserRuleContext):

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
        self.enterRule(localctx, 78, self.RULE_voidTypeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
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
        self._predicates[16] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 2)
         




