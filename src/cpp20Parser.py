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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u0092")
        buf.write("\u0211\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\3\2\3\2\3")
        buf.write("\2\5\2]\n\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\7\7h\n")
        buf.write("\7\f\7\16\7k\13\7\3\7\3\7\3\b\5\bp\n\b\3\b\3\b\3\b\3\b")
        buf.write("\5\bv\n\b\3\b\7\by\n\b\f\b\16\b|\13\b\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\13\3\13\5\13\u0085\n\13\3\f\3\f\3\f\3\f\3\f\7\f")
        buf.write("\u008c\n\f\f\f\16\f\u008f\13\f\5\f\u0091\n\f\3\f\3\f\3")
        buf.write("\f\5\f\u0096\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\7\16\u00a4\n\16\f\16\16\16\u00a7\13\16")
        buf.write("\3\17\3\17\3\17\3\17\5\17\u00ad\n\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00bc\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u00db\n\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\7\22\u0113\n\22\f\22\16\22\u0116\13\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\5\23\u0124\n\23\3\23\5\23\u0127\n\23\3\24\3\24\7\24\u012b")
        buf.write("\n\24\f\24\16\24\u012e\13\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\7\25\u0137\n\25\f\25\16\25\u013a\13\25\5\25")
        buf.write("\u013c\n\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u0147\n\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\7\30\u0154\n\30\f\30\16\30\u0157")
        buf.write("\13\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\5\33")
        buf.write("\u016c\n\33\3\33\3\33\5\33\u0170\n\33\3\33\3\33\5\33\u0174")
        buf.write("\n\33\3\33\3\33\3\33\3\34\3\34\3\34\7\34\u017c\n\34\f")
        buf.write("\34\16\34\u017f\13\34\3\35\3\35\5\35\u0183\n\35\3\35\3")
        buf.write("\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \5 \u0191")
        buf.write("\n \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\7!\u019d\n!\f!\16!\u01a0")
        buf.write("\13!\3!\3!\5!\u01a4\n!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u01af")
        buf.write("\n!\3!\3!\5!\u01b3\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"")
        buf.write("\u01bc\n\"\3#\3#\3#\3#\7#\u01c2\n#\f#\16#\u01c5\13#\3")
        buf.write("#\3#\3$\3$\3$\3$\3$\3$\7$\u01cf\n$\f$\16$\u01d2\13$\5")
        buf.write("$\u01d4\n$\3$\3$\3$\3$\3$\3$\3$\3$\3$\7$\u01df\n$\f$\16")
        buf.write("$\u01e2\13$\5$\u01e4\n$\3$\3$\3$\5$\u01e9\n$\3%\3%\3%")
        buf.write("\3%\3%\3%\3%\5%\u01f2\n%\3&\3&\3&\3&\3&\5&\u01f9\n&\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3(\3(\5(\u0203\n(\3)\3)\3)\3)\5)\u0209")
        buf.write("\n)\3*\3*\3+\3+\3,\3,\3,\2\3\"-\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTV\2")
        buf.write("\4\3\2]_\4\288jj\2\u0242\2\\\3\2\2\2\4^\3\2\2\2\6`\3\2")
        buf.write("\2\2\bb\3\2\2\2\nd\3\2\2\2\fi\3\2\2\2\16o\3\2\2\2\20}")
        buf.write("\3\2\2\2\22\177\3\2\2\2\24\u0084\3\2\2\2\26\u0086\3\2")
        buf.write("\2\2\30\u0099\3\2\2\2\32\u00a5\3\2\2\2\34\u00a8\3\2\2")
        buf.write("\2\36\u00b3\3\2\2\2 \u00bb\3\2\2\2\"\u00da\3\2\2\2$\u0126")
        buf.write("\3\2\2\2&\u0128\3\2\2\2(\u0131\3\2\2\2*\u013f\3\2\2\2")
        buf.write(",\u0148\3\2\2\2.\u014d\3\2\2\2\60\u015a\3\2\2\2\62\u0160")
        buf.write("\3\2\2\2\64\u0168\3\2\2\2\66\u0178\3\2\2\28\u0180\3\2")
        buf.write("\2\2:\u0186\3\2\2\2<\u0189\3\2\2\2>\u0190\3\2\2\2@\u01b2")
        buf.write("\3\2\2\2B\u01bb\3\2\2\2D\u01bd\3\2\2\2F\u01e8\3\2\2\2")
        buf.write("H\u01f1\3\2\2\2J\u01f8\3\2\2\2L\u01fa\3\2\2\2N\u0202\3")
        buf.write("\2\2\2P\u0208\3\2\2\2R\u020a\3\2\2\2T\u020c\3\2\2\2V\u020e")
        buf.write("\3\2\2\2X]\5\4\3\2Y]\5\6\4\2Z]\5\b\5\2[]\5\n\6\2\\X\3")
        buf.write("\2\2\2\\Y\3\2\2\2\\Z\3\2\2\2\\[\3\2\2\2]\3\3\2\2\2^_\7")
        buf.write("\u0088\2\2_\5\3\2\2\2`a\7\u0087\2\2a\7\3\2\2\2bc\7\u0086")
        buf.write("\2\2c\t\3\2\2\2de\7\u0085\2\2e\13\3\2\2\2fh\5> \2gf\3")
        buf.write("\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2jl\3\2\2\2ki\3\2\2")
        buf.write("\2lm\7\2\2\3m\r\3\2\2\2np\5\20\t\2on\3\2\2\2op\3\2\2\2")
        buf.write("pq\3\2\2\2qr\7\u0083\2\2rz\3\2\2\2su\7\16\2\2tv\5\20\t")
        buf.write("\2ut\3\2\2\2uv\3\2\2\2vw\3\2\2\2wy\7\u0083\2\2xs\3\2\2")
        buf.write("\2y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{\17\3\2\2\2|z\3\2\2\2")
        buf.write("}~\t\2\2\2~\21\3\2\2\2\177\u0080\5\20\t\2\u0080\u0081")
        buf.write("\7\21\2\2\u0081\23\3\2\2\2\u0082\u0085\5F$\2\u0083\u0085")
        buf.write("\5D#\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085\25")
        buf.write("\3\2\2\2\u0086\u0087\7\u0083\2\2\u0087\u0090\7\13\2\2")
        buf.write("\u0088\u008d\5H%\2\u0089\u008a\7\16\2\2\u008a\u008c\5")
        buf.write("H%\2\u008b\u0089\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u008b")
        buf.write("\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0091\3\2\2\2\u008f")
        buf.write("\u008d\3\2\2\2\u0090\u0088\3\2\2\2\u0090\u0091\3\2\2\2")
        buf.write("\u0091\u0092\3\2\2\2\u0092\u0095\7\f\2\2\u0093\u0094\7")
        buf.write("\21\2\2\u0094\u0096\5(\25\2\u0095\u0093\3\2\2\2\u0095")
        buf.write("\u0096\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098\5&\24\2")
        buf.write("\u0098\27\3\2\2\2\u0099\u009a\79\2\2\u009a\u009b\7\u0083")
        buf.write("\2\2\u009b\u009c\7\13\2\2\u009c\u009d\7\f\2\2\u009d\u009e")
        buf.write("\5&\24\2\u009e\31\3\2\2\2\u009f\u00a4\5\22\n\2\u00a0\u00a4")
        buf.write("\5\24\13\2\u00a1\u00a4\5\26\f\2\u00a2\u00a4\5\30\r\2\u00a3")
        buf.write("\u009f\3\2\2\2\u00a3\u00a0\3\2\2\2\u00a3\u00a1\3\2\2\2")
        buf.write("\u00a3\u00a2\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3")
        buf.write("\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\33\3\2\2\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a8\u00a9\t\3\2\2\u00a9\u00ac\7\u0083\2\2\u00aa")
        buf.write("\u00ab\7\21\2\2\u00ab\u00ad\5\16\b\2\u00ac\u00aa\3\2\2")
        buf.write("\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af")
        buf.write("\7\7\2\2\u00af\u00b0\5\32\16\2\u00b0\u00b1\7\b\2\2\u00b1")
        buf.write("\u00b2\7\17\2\2\u00b2\35\3\2\2\2\u00b3\u00b4\5\2\2\2\u00b4")
        buf.write("\37\3\2\2\2\u00b5\u00bc\7\u0083\2\2\u00b6\u00b7\7\u0083")
        buf.write("\2\2\u00b7\u00b8\7\t\2\2\u00b8\u00b9\5\"\22\2\u00b9\u00ba")
        buf.write("\7\n\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00b5\3\2\2\2\u00bb")
        buf.write("\u00b6\3\2\2\2\u00bc!\3\2\2\2\u00bd\u00be\b\22\1\2\u00be")
        buf.write("\u00db\5(\25\2\u00bf\u00db\5\2\2\2\u00c0\u00db\7\u0083")
        buf.write("\2\2\u00c1\u00c2\7\13\2\2\u00c2\u00c3\5\"\22\2\u00c3\u00c4")
        buf.write("\7\f\2\2\u00c4\u00db\3\2\2\2\u00c5\u00c6\7W\2\2\u00c6")
        buf.write("\u00db\5\"\22\33\u00c7\u00c8\7\25\2\2\u00c8\u00db\5\"")
        buf.write("\22\32\u00c9\u00ca\7.\2\2\u00ca\u00db\5 \21\2\u00cb\u00cc")
        buf.write("\7\u0083\2\2\u00cc\u00cd\7\t\2\2\u00cd\u00ce\5\"\22\2")
        buf.write("\u00ce\u00cf\7\n\2\2\u00cf\u00db\3\2\2\2\u00d0\u00d1\5")
        buf.write(" \21\2\u00d1\u00d2\7\22\2\2\u00d2\u00d3\5\"\22\5\u00d3")
        buf.write("\u00db\3\2\2\2\u00d4\u00d5\5 \21\2\u00d5\u00d6\7(\2\2")
        buf.write("\u00d6\u00db\3\2\2\2\u00d7\u00d8\5 \21\2\u00d8\u00d9\7")
        buf.write(")\2\2\u00d9\u00db\3\2\2\2\u00da\u00bd\3\2\2\2\u00da\u00bf")
        buf.write("\3\2\2\2\u00da\u00c0\3\2\2\2\u00da\u00c1\3\2\2\2\u00da")
        buf.write("\u00c5\3\2\2\2\u00da\u00c7\3\2\2\2\u00da\u00c9\3\2\2\2")
        buf.write("\u00da\u00cb\3\2\2\2\u00da\u00d0\3\2\2\2\u00da\u00d4\3")
        buf.write("\2\2\2\u00da\u00d7\3\2\2\2\u00db\u0114\3\2\2\2\u00dc\u00dd")
        buf.write("\f\30\2\2\u00dd\u00de\7\27\2\2\u00de\u0113\5\"\22\31\u00df")
        buf.write("\u00e0\f\27\2\2\u00e0\u00e1\7\31\2\2\u00e1\u0113\5\"\22")
        buf.write("\30\u00e2\u00e3\f\26\2\2\u00e3\u00e4\7\33\2\2\u00e4\u0113")
        buf.write("\5\"\22\27\u00e5\u00e6\f\25\2\2\u00e6\u00e7\7\23\2\2\u00e7")
        buf.write("\u0113\5\"\22\26\u00e8\u00e9\f\24\2\2\u00e9\u00ea\7\25")
        buf.write("\2\2\u00ea\u0113\5\"\22\25\u00eb\u00ec\f\23\2\2\u00ec")
        buf.write("\u00ed\7\3\2\2\u00ed\u0113\5\"\22\24\u00ee\u00ef\f\22")
        buf.write("\2\2\u00ef\u00f0\7\4\2\2\u00f0\u0113\5\"\22\23\u00f1\u00f2")
        buf.write("\f\21\2\2\u00f2\u00f3\7$\2\2\u00f3\u0113\5\"\22\22\u00f4")
        buf.write("\u00f5\f\20\2\2\u00f5\u00f6\7%\2\2\u00f6\u0113\5\"\22")
        buf.write("\21\u00f7\u00f8\f\17\2\2\u00f8\u00f9\7!\2\2\u00f9\u0113")
        buf.write("\5\"\22\20\u00fa\u00fb\f\16\2\2\u00fb\u00fc\7X\2\2\u00fc")
        buf.write("\u0113\5\"\22\17\u00fd\u00fe\f\r\2\2\u00fe\u00ff\7/\2")
        buf.write("\2\u00ff\u0113\5\"\22\16\u0100\u0101\f\f\2\2\u0101\u0102")
        buf.write("\7.\2\2\u0102\u0113\5\"\22\r\u0103\u0104\f\13\2\2\u0104")
        buf.write("\u0105\7}\2\2\u0105\u0113\5\"\22\f\u0106\u0107\f\n\2\2")
        buf.write("\u0107\u0108\7[\2\2\u0108\u0113\5\"\22\13\u0109\u010a")
        buf.write("\f\t\2\2\u010a\u010b\7*\2\2\u010b\u0113\5\"\22\n\u010c")
        buf.write("\u010d\f\b\2\2\u010d\u010e\7\35\2\2\u010e\u0113\5\"\22")
        buf.write("\t\u010f\u0110\f\7\2\2\u0110\u0111\7\37\2\2\u0111\u0113")
        buf.write("\5\"\22\b\u0112\u00dc\3\2\2\2\u0112\u00df\3\2\2\2\u0112")
        buf.write("\u00e2\3\2\2\2\u0112\u00e5\3\2\2\2\u0112\u00e8\3\2\2\2")
        buf.write("\u0112\u00eb\3\2\2\2\u0112\u00ee\3\2\2\2\u0112\u00f1\3")
        buf.write("\2\2\2\u0112\u00f4\3\2\2\2\u0112\u00f7\3\2\2\2\u0112\u00fa")
        buf.write("\3\2\2\2\u0112\u00fd\3\2\2\2\u0112\u0100\3\2\2\2\u0112")
        buf.write("\u0103\3\2\2\2\u0112\u0106\3\2\2\2\u0112\u0109\3\2\2\2")
        buf.write("\u0112\u010c\3\2\2\2\u0112\u010f\3\2\2\2\u0113\u0116\3")
        buf.write("\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115#")
        buf.write("\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0127\5*\26\2\u0118")
        buf.write("\u0127\5.\30\2\u0119\u0127\5\60\31\2\u011a\u0127\5\62")
        buf.write("\32\2\u011b\u0127\5\64\33\2\u011c\u0127\58\35\2\u011d")
        buf.write("\u0127\5:\36\2\u011e\u0127\5<\37\2\u011f\u0127\5&\24\2")
        buf.write("\u0120\u0127\5D#\2\u0121\u0127\5@!\2\u0122\u0124\5\"\22")
        buf.write("\2\u0123\u0122\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0125")
        buf.write("\3\2\2\2\u0125\u0127\7\17\2\2\u0126\u0117\3\2\2\2\u0126")
        buf.write("\u0118\3\2\2\2\u0126\u0119\3\2\2\2\u0126\u011a\3\2\2\2")
        buf.write("\u0126\u011b\3\2\2\2\u0126\u011c\3\2\2\2\u0126\u011d\3")
        buf.write("\2\2\2\u0126\u011e\3\2\2\2\u0126\u011f\3\2\2\2\u0126\u0120")
        buf.write("\3\2\2\2\u0126\u0121\3\2\2\2\u0126\u0123\3\2\2\2\u0127")
        buf.write("%\3\2\2\2\u0128\u012c\7\7\2\2\u0129\u012b\5$\23\2\u012a")
        buf.write("\u0129\3\2\2\2\u012b\u012e\3\2\2\2\u012c\u012a\3\2\2\2")
        buf.write("\u012c\u012d\3\2\2\2\u012d\u012f\3\2\2\2\u012e\u012c\3")
        buf.write("\2\2\2\u012f\u0130\7\b\2\2\u0130\'\3\2\2\2\u0131\u0132")
        buf.write("\7\u0083\2\2\u0132\u013b\7\13\2\2\u0133\u0138\5\"\22\2")
        buf.write("\u0134\u0135\7\16\2\2\u0135\u0137\5\"\22\2\u0136\u0134")
        buf.write("\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0138")
        buf.write("\u0139\3\2\2\2\u0139\u013c\3\2\2\2\u013a\u0138\3\2\2\2")
        buf.write("\u013b\u0133\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\3")
        buf.write("\2\2\2\u013d\u013e\7\f\2\2\u013e)\3\2\2\2\u013f\u0140")
        buf.write("\7P\2\2\u0140\u0141\7\13\2\2\u0141\u0142\5\"\22\2\u0142")
        buf.write("\u0143\7\f\2\2\u0143\u0146\5$\23\2\u0144\u0145\7F\2\2")
        buf.write("\u0145\u0147\5$\23\2\u0146\u0144\3\2\2\2\u0146\u0147\3")
        buf.write("\2\2\2\u0147+\3\2\2\2\u0148\u0149\7\62\2\2\u0149\u014a")
        buf.write("\5\36\20\2\u014a\u014b\7\21\2\2\u014b\u014c\5$\23\2\u014c")
        buf.write("-\3\2\2\2\u014d\u014e\7k\2\2\u014e\u014f\7\13\2\2\u014f")
        buf.write("\u0150\5\"\22\2\u0150\u0151\7\f\2\2\u0151\u0155\7\7\2")
        buf.write("\2\u0152\u0154\5,\27\2\u0153\u0152\3\2\2\2\u0154\u0157")
        buf.write("\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156")
        buf.write("\u0158\3\2\2\2\u0157\u0155\3\2\2\2\u0158\u0159\7\b\2\2")
        buf.write("\u0159/\3\2\2\2\u015a\u015b\7|\2\2\u015b\u015c\7\13\2")
        buf.write("\2\u015c\u015d\5\"\22\2\u015d\u015e\7\f\2\2\u015e\u015f")
        buf.write("\5$\23\2\u015f\61\3\2\2\2\u0160\u0161\7C\2\2\u0161\u0162")
        buf.write("\5$\23\2\u0162\u0163\7|\2\2\u0163\u0164\7\13\2\2\u0164")
        buf.write("\u0165\5\"\22\2\u0165\u0166\7\f\2\2\u0166\u0167\7\17\2")
        buf.write("\2\u0167\63\3\2\2\2\u0168\u0169\7M\2\2\u0169\u016b\7\13")
        buf.write("\2\2\u016a\u016c\5\66\34\2\u016b\u016a\3\2\2\2\u016b\u016c")
        buf.write("\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016f\7\17\2\2\u016e")
        buf.write("\u0170\5\"\22\2\u016f\u016e\3\2\2\2\u016f\u0170\3\2\2")
        buf.write("\2\u0170\u0171\3\2\2\2\u0171\u0173\7\17\2\2\u0172\u0174")
        buf.write("\5\66\34\2\u0173\u0172\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175\u0176\7\f\2\2\u0176\u0177\5$\23\2")
        buf.write("\u0177\65\3\2\2\2\u0178\u017d\5\"\22\2\u0179\u017a\7\16")
        buf.write("\2\2\u017a\u017c\5\"\22\2\u017b\u0179\3\2\2\2\u017c\u017f")
        buf.write("\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e")
        buf.write("\67\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0182\7c\2\2\u0181")
        buf.write("\u0183\5\"\22\2\u0182\u0181\3\2\2\2\u0182\u0183\3\2\2")
        buf.write("\2\u0183\u0184\3\2\2\2\u0184\u0185\7\17\2\2\u01859\3\2")
        buf.write("\2\2\u0186\u0187\7\61\2\2\u0187\u0188\7\17\2\2\u0188;")
        buf.write("\3\2\2\2\u0189\u018a\7@\2\2\u018a\u018b\7\17\2\2\u018b")
        buf.write("=\3\2\2\2\u018c\u0191\5@!\2\u018d\u0191\5D#\2\u018e\u0191")
        buf.write("\5F$\2\u018f\u0191\5\34\17\2\u0190\u018c\3\2\2\2\u0190")
        buf.write("\u018d\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u018f\3\2\2\2")
        buf.write("\u0191?\3\2\2\2\u0192\u0193\5J&\2\u0193\u0194\7\u0083")
        buf.write("\2\2\u0194\u0195\7\t\2\2\u0195\u0196\7\u0087\2\2\u0196")
        buf.write("\u01a3\7\n\2\2\u0197\u0198\7\22\2\2\u0198\u0199\7\7\2")
        buf.write("\2\u0199\u019e\5\"\22\2\u019a\u019b\7\16\2\2\u019b\u019d")
        buf.write("\5\"\22\2\u019c\u019a\3\2\2\2\u019d\u01a0\3\2\2\2\u019e")
        buf.write("\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a1\3\2\2\2")
        buf.write("\u01a0\u019e\3\2\2\2\u01a1\u01a2\7\b\2\2\u01a2\u01a4\3")
        buf.write("\2\2\2\u01a3\u0197\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5")
        buf.write("\3\2\2\2\u01a5\u01a6\7\17\2\2\u01a6\u01b3\3\2\2\2\u01a7")
        buf.write("\u01a8\5T+\2\u01a8\u01a9\7\u0083\2\2\u01a9\u01aa\7\t\2")
        buf.write("\2\u01aa\u01ab\7\u0087\2\2\u01ab\u01ae\7\n\2\2\u01ac\u01ad")
        buf.write("\7\22\2\2\u01ad\u01af\5\n\6\2\u01ae\u01ac\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b1\7\17\2")
        buf.write("\2\u01b1\u01b3\3\2\2\2\u01b2\u0192\3\2\2\2\u01b2\u01a7")
        buf.write("\3\2\2\2\u01b3A\3\2\2\2\u01b4\u01bc\7\u0083\2\2\u01b5")
        buf.write("\u01b6\7\u0083\2\2\u01b6\u01b7\7\22\2\2\u01b7\u01bc\5")
        buf.write("\36\20\2\u01b8\u01b9\7\u0083\2\2\u01b9\u01ba\7\22\2\2")
        buf.write("\u01ba\u01bc\5\"\22\2\u01bb\u01b4\3\2\2\2\u01bb\u01b5")
        buf.write("\3\2\2\2\u01bb\u01b8\3\2\2\2\u01bcC\3\2\2\2\u01bd\u01be")
        buf.write("\5J&\2\u01be\u01c3\5B\"\2\u01bf\u01c0\7\16\2\2\u01c0\u01c2")
        buf.write("\5B\"\2\u01c1\u01bf\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3")
        buf.write("\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c6\3\2\2\2")
        buf.write("\u01c5\u01c3\3\2\2\2\u01c6\u01c7\7\17\2\2\u01c7E\3\2\2")
        buf.write("\2\u01c8\u01c9\5J&\2\u01c9\u01ca\7\u0083\2\2\u01ca\u01d3")
        buf.write("\7\13\2\2\u01cb\u01d0\5H%\2\u01cc\u01cd\7\16\2\2\u01cd")
        buf.write("\u01cf\5H%\2\u01ce\u01cc\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0")
        buf.write("\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d4\3\2\2\2")
        buf.write("\u01d2\u01d0\3\2\2\2\u01d3\u01cb\3\2\2\2\u01d3\u01d4\3")
        buf.write("\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d6\7\f\2\2\u01d6\u01d7")
        buf.write("\7\17\2\2\u01d7\u01e9\3\2\2\2\u01d8\u01d9\5J&\2\u01d9")
        buf.write("\u01da\7\u0083\2\2\u01da\u01e3\7\13\2\2\u01db\u01e0\5")
        buf.write("H%\2\u01dc\u01dd\7\16\2\2\u01dd\u01df\5H%\2\u01de\u01dc")
        buf.write("\3\2\2\2\u01df\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0")
        buf.write("\u01e1\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2")
        buf.write("\u01e3\u01db\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e5\3")
        buf.write("\2\2\2\u01e5\u01e6\7\f\2\2\u01e6\u01e7\5&\24\2\u01e7\u01e9")
        buf.write("\3\2\2\2\u01e8\u01c8\3\2\2\2\u01e8\u01d8\3\2\2\2\u01e9")
        buf.write("G\3\2\2\2\u01ea\u01eb\5L\'\2\u01eb\u01ec\7\u0083\2\2\u01ec")
        buf.write("\u01f2\3\2\2\2\u01ed\u01ee\5J&\2\u01ee\u01ef\7\u0083\2")
        buf.write("\2\u01ef\u01f2\3\2\2\2\u01f0\u01f2\7\"\2\2\u01f1\u01ea")
        buf.write("\3\2\2\2\u01f1\u01ed\3\2\2\2\u01f1\u01f0\3\2\2\2\u01f2")
        buf.write("I\3\2\2\2\u01f3\u01f9\5N(\2\u01f4\u01f9\5P)\2\u01f5\u01f9")
        buf.write("\5R*\2\u01f6\u01f9\5T+\2\u01f7\u01f9\5V,\2\u01f8\u01f3")
        buf.write("\3\2\2\2\u01f8\u01f4\3\2\2\2\u01f8\u01f5\3\2\2\2\u01f8")
        buf.write("\u01f6\3\2\2\2\u01f8\u01f7\3\2\2\2\u01f9K\3\2\2\2\u01fa")
        buf.write("\u01fb\5J&\2\u01fb\u01fc\7\27\2\2\u01fcM\3\2\2\2\u01fd")
        buf.write("\u0203\7R\2\2\u01fe\u0203\7S\2\2\u01ff\u0203\7d\2\2\u0200")
        buf.write("\u0201\7S\2\2\u0201\u0203\7S\2\2\u0202\u01fd\3\2\2\2\u0202")
        buf.write("\u01fe\3\2\2\2\u0202\u01ff\3\2\2\2\u0202\u0200\3\2\2\2")
        buf.write("\u0203O\3\2\2\2\u0204\u0209\7L\2\2\u0205\u0209\7D\2\2")
        buf.write("\u0206\u0207\7S\2\2\u0207\u0209\7D\2\2\u0208\u0204\3\2")
        buf.write("\2\2\u0208\u0205\3\2\2\2\u0208\u0206\3\2\2\2\u0209Q\3")
        buf.write("\2\2\2\u020a\u020b\7\60\2\2\u020bS\3\2\2\2\u020c\u020d")
        buf.write("\7\64\2\2\u020dU\3\2\2\2\u020e\u020f\7y\2\2\u020fW\3\2")
        buf.write("\2\2.\\iouz\u0084\u008d\u0090\u0095\u00a3\u00a5\u00ac")
        buf.write("\u00bb\u00da\u0112\u0114\u0123\u0126\u012c\u0138\u013b")
        buf.write("\u0146\u0155\u016b\u016f\u0173\u017d\u0182\u0190\u019e")
        buf.write("\u01a3\u01ae\u01b2\u01bb\u01c3\u01d0\u01d3\u01e0\u01e3")
        buf.write("\u01e8\u01f1\u01f8\u0202\u0208")
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
                      "IntegerSuffix", "StringLiteral", "CharacterLiteral", 
                      "DecimalLiteral", "FloatingLiteral", "DigitSequence", 
                      "DecimalExponent", "SChar", "CChar", "CharTypeSpecificaton", 
                      "Escapesequence", "Simpleescapesequence", "Octalescapesequence", 
                      "Hexadecimalescapesequence", "Universalcharactername" ]

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
    RULE_forExprSet = 26
    RULE_returnStatement = 27
    RULE_breakStatement = 28
    RULE_continueStatement = 29
    RULE_declaration = 30
    RULE_arrayDeclarator = 31
    RULE_variableDeclaration = 32
    RULE_variableDeclarator = 33
    RULE_functionDeclaration = 34
    RULE_functionParameter = 35
    RULE_typeSpecifier = 36
    RULE_pointerTypeSpecifier = 37
    RULE_integerTypeSpecifier = 38
    RULE_realTypeSpecifier = 39
    RULE_booleanTypeSpecifier = 40
    RULE_charTypeSpecifier = 41
    RULE_voidTypeSpecifier = 42

    ruleNames =  [ "literals", "floatingLiteral", "integerLiteral", "characterLiteral", 
                   "stringLiteral", "translationUnit", "baseSpecifierList", 
                   "accessSpecifier", "accessLabel", "memberDeclaration", 
                   "constructorDeclaration", "destructorDeclaration", "memberSpecification", 
                   "classDefinition", "constExpression", "leftExpression", 
                   "expression", "statement", "block", "functionCall", "ifStatement", 
                   "caseStatement", "switchStatement", "whileStatement", 
                   "doWhileStatement", "forStatement", "forExprSet", "returnStatement", 
                   "breakStatement", "continueStatement", "declaration", 
                   "arrayDeclarator", "variableDeclaration", "variableDeclarator", 
                   "functionDeclaration", "functionParameter", "typeSpecifier", 
                   "pointerTypeSpecifier", "integerTypeSpecifier", "realTypeSpecifier", 
                   "booleanTypeSpecifier", "charTypeSpecifier", "voidTypeSpecifier" ]

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
    IntegerSuffix=130
    StringLiteral=131
    CharacterLiteral=132
    DecimalLiteral=133
    FloatingLiteral=134
    DigitSequence=135
    DecimalExponent=136
    SChar=137
    CChar=138
    CharTypeSpecificaton=139
    Escapesequence=140
    Simpleescapesequence=141
    Octalescapesequence=142
    Hexadecimalescapesequence=143
    Universalcharactername=144

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cpp20Parser.FloatingLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.floatingLiteral()
                pass
            elif token in [cpp20Parser.DecimalLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.integerLiteral()
                pass
            elif token in [cpp20Parser.CharacterLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.characterLiteral()
                pass
            elif token in [cpp20Parser.StringLiteral]:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.stringLiteral()
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


    class FloatingLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 92
            self.match(cpp20Parser.FloatingLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DecimalLiteral(self):
            return self.getToken(cpp20Parser.DecimalLiteral, 0)

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
            self.state = 94
            self.match(cpp20Parser.DecimalLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharacterLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CharacterLiteral(self):
            return self.getToken(cpp20Parser.CharacterLiteral, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(cpp20Parser.CharacterLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self):
            return self.getToken(cpp20Parser.StringLiteral, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(cpp20Parser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TranslationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(cpp20Parser.EOF, 0)

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
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.BOOL) | (1 << cpp20Parser.CHAR) | (1 << cpp20Parser.CLASS))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (cpp20Parser.DOUBLE - 66)) | (1 << (cpp20Parser.FLOAT - 66)) | (1 << (cpp20Parser.INT - 66)) | (1 << (cpp20Parser.LONG - 66)) | (1 << (cpp20Parser.SHORT - 66)) | (1 << (cpp20Parser.STRUCT - 66)) | (1 << (cpp20Parser.VOID - 66)))) != 0):
                self.state = 100
                self.declaration()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(cpp20Parser.EOF)
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
        self.enterRule(localctx, 12, self.RULE_baseSpecifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 91)) & ~0x3f) == 0 and ((1 << (_la - 91)) & ((1 << (cpp20Parser.PRIVATE - 91)) | (1 << (cpp20Parser.PROTECTED - 91)) | (1 << (cpp20Parser.PUBLIC - 91)))) != 0):
                self.state = 108
                self.accessSpecifier()


            self.state = 111
            self.match(cpp20Parser.Identifier)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cpp20Parser.COMMA:
                self.state = 113
                self.match(cpp20Parser.COMMA)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 91)) & ~0x3f) == 0 and ((1 << (_la - 91)) & ((1 << (cpp20Parser.PRIVATE - 91)) | (1 << (cpp20Parser.PROTECTED - 91)) | (1 << (cpp20Parser.PUBLIC - 91)))) != 0):
                    self.state = 114
                    self.accessSpecifier()


                self.state = 117
                self.match(cpp20Parser.Identifier)
                self.state = 122
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
        self.enterRule(localctx, 14, self.RULE_accessSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
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
        self.enterRule(localctx, 16, self.RULE_accessLabel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.accessSpecifier()
            self.state = 126
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


        def variableDeclarator(self):
            return self.getTypedRuleContext(cpp20Parser.VariableDeclaratorContext,0)


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
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.functionDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.variableDeclarator()
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
        self.enterRule(localctx, 20, self.RULE_constructorDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(cpp20Parser.Identifier)
            self.state = 133
            self.match(cpp20Parser.LPAREN)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.DOTS) | (1 << cpp20Parser.BOOL) | (1 << cpp20Parser.CHAR))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (cpp20Parser.DOUBLE - 66)) | (1 << (cpp20Parser.FLOAT - 66)) | (1 << (cpp20Parser.INT - 66)) | (1 << (cpp20Parser.LONG - 66)) | (1 << (cpp20Parser.SHORT - 66)) | (1 << (cpp20Parser.VOID - 66)))) != 0):
                self.state = 134
                self.functionParameter()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cpp20Parser.COMMA:
                    self.state = 135
                    self.match(cpp20Parser.COMMA)
                    self.state = 136
                    self.functionParameter()
                    self.state = 141
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 144
            self.match(cpp20Parser.RPAREN)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.COLON:
                self.state = 145
                self.match(cpp20Parser.COLON)
                self.state = 146
                self.functionCall()


            self.state = 149
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
        self.enterRule(localctx, 22, self.RULE_destructorDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(cpp20Parser.COMPL)
            self.state = 152
            self.match(cpp20Parser.Identifier)
            self.state = 153
            self.match(cpp20Parser.LPAREN)
            self.state = 154
            self.match(cpp20Parser.RPAREN)
            self.state = 155
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
        self.enterRule(localctx, 24, self.RULE_memberSpecification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.BOOL) | (1 << cpp20Parser.CHAR) | (1 << cpp20Parser.COMPL))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (cpp20Parser.DOUBLE - 66)) | (1 << (cpp20Parser.FLOAT - 66)) | (1 << (cpp20Parser.INT - 66)) | (1 << (cpp20Parser.LONG - 66)) | (1 << (cpp20Parser.PRIVATE - 66)) | (1 << (cpp20Parser.PROTECTED - 66)) | (1 << (cpp20Parser.PUBLIC - 66)) | (1 << (cpp20Parser.SHORT - 66)) | (1 << (cpp20Parser.VOID - 66)) | (1 << (cpp20Parser.Identifier - 66)))) != 0):
                self.state = 161
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [cpp20Parser.PRIVATE, cpp20Parser.PROTECTED, cpp20Parser.PUBLIC]:
                    self.state = 157
                    self.accessLabel()
                    pass
                elif token in [cpp20Parser.BOOL, cpp20Parser.CHAR, cpp20Parser.DOUBLE, cpp20Parser.FLOAT, cpp20Parser.INT, cpp20Parser.LONG, cpp20Parser.SHORT, cpp20Parser.VOID]:
                    self.state = 158
                    self.memberDeclaration()
                    pass
                elif token in [cpp20Parser.Identifier]:
                    self.state = 159
                    self.constructorDeclaration()
                    pass
                elif token in [cpp20Parser.COMPL]:
                    self.state = 160
                    self.destructorDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 165
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
        self.enterRule(localctx, 26, self.RULE_classDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            _la = self._input.LA(1)
            if not(_la==cpp20Parser.CLASS or _la==cpp20Parser.STRUCT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 167
            self.match(cpp20Parser.Identifier)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cpp20Parser.COLON:
                self.state = 168
                self.match(cpp20Parser.COLON)
                self.state = 169
                self.baseSpecifierList()


            self.state = 172
            self.match(cpp20Parser.LBRACE)
            self.state = 173
            self.memberSpecification()
            self.state = 174
            self.match(cpp20Parser.RBRACE)
            self.state = 175
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
            self.state = 177
            self.literals()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeftExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

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
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(cpp20Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.match(cpp20Parser.Identifier)

                self.state = 181
                self.match(cpp20Parser.LSQUARE)
                self.state = 182
                self.expression(0)
                self.state = 183
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
        __slots__ = 'parser'

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

        def SUB(self):
            return self.getToken(cpp20Parser.SUB, 0)

        def BITAND(self):
            return self.getToken(cpp20Parser.BITAND, 0)

        def leftExpression(self):
            return self.getTypedRuleContext(cpp20Parser.LeftExpressionContext,0)


        def LSQUARE(self):
            return self.getToken(cpp20Parser.LSQUARE, 0)

        def RSQUARE(self):
            return self.getToken(cpp20Parser.RSQUARE, 0)

        def ASSIGN(self):
            return self.getToken(cpp20Parser.ASSIGN, 0)

        def PLUS_PLUS(self):
            return self.getToken(cpp20Parser.PLUS_PLUS, 0)

        def MINUS_MINUS(self):
            return self.getToken(cpp20Parser.MINUS_MINUS, 0)

        def MULT(self):
            return self.getToken(cpp20Parser.MULT, 0)

        def DIV(self):
            return self.getToken(cpp20Parser.DIV, 0)

        def MOD(self):
            return self.getToken(cpp20Parser.MOD, 0)

        def ADD(self):
            return self.getToken(cpp20Parser.ADD, 0)

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

        def BITOR(self):
            return self.getToken(cpp20Parser.BITOR, 0)

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
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 188
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 189
                self.literals()
                pass

            elif la_ == 3:
                self.state = 190
                self.match(cpp20Parser.Identifier)
                pass

            elif la_ == 4:
                self.state = 191
                self.match(cpp20Parser.LPAREN)
                self.state = 192
                self.expression(0)
                self.state = 193
                self.match(cpp20Parser.RPAREN)
                pass

            elif la_ == 5:
                self.state = 195
                self.match(cpp20Parser.NOT)
                self.state = 196
                self.expression(25)
                pass

            elif la_ == 6:
                self.state = 197
                self.match(cpp20Parser.SUB)
                self.state = 198
                self.expression(24)
                pass

            elif la_ == 7:
                self.state = 199
                self.match(cpp20Parser.BITAND)
                self.state = 200
                self.leftExpression()
                pass

            elif la_ == 8:
                self.state = 201
                self.match(cpp20Parser.Identifier)
                self.state = 202
                self.match(cpp20Parser.LSQUARE)
                self.state = 203
                self.expression(0)
                self.state = 204
                self.match(cpp20Parser.RSQUARE)
                pass

            elif la_ == 9:
                self.state = 206
                self.leftExpression()
                self.state = 207
                self.match(cpp20Parser.ASSIGN)
                self.state = 208
                self.expression(3)
                pass

            elif la_ == 10:
                self.state = 210
                self.leftExpression()
                self.state = 211
                self.match(cpp20Parser.PLUS_PLUS)
                pass

            elif la_ == 11:
                self.state = 213
                self.leftExpression()
                self.state = 214
                self.match(cpp20Parser.MINUS_MINUS)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 274
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 272
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 218
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 219
                        self.match(cpp20Parser.MULT)
                        self.state = 220
                        self.expression(23)
                        pass

                    elif la_ == 2:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 221
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 222
                        self.match(cpp20Parser.DIV)
                        self.state = 223
                        self.expression(22)
                        pass

                    elif la_ == 3:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 224
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 225
                        self.match(cpp20Parser.MOD)
                        self.state = 226
                        self.expression(21)
                        pass

                    elif la_ == 4:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 227
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 228
                        self.match(cpp20Parser.ADD)
                        self.state = 229
                        self.expression(20)
                        pass

                    elif la_ == 5:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 230
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 231
                        self.match(cpp20Parser.SUB)
                        self.state = 232
                        self.expression(19)
                        pass

                    elif la_ == 6:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 233
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 234
                        self.match(cpp20Parser.LT)
                        self.state = 235
                        self.expression(18)
                        pass

                    elif la_ == 7:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 236
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 237
                        self.match(cpp20Parser.GT)
                        self.state = 238
                        self.expression(17)
                        pass

                    elif la_ == 8:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 239
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 240
                        self.match(cpp20Parser.LEQ)
                        self.state = 241
                        self.expression(16)
                        pass

                    elif la_ == 9:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 242
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 243
                        self.match(cpp20Parser.GEQ)
                        self.state = 244
                        self.expression(15)
                        pass

                    elif la_ == 10:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 245
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 246
                        self.match(cpp20Parser.EQ)
                        self.state = 247
                        self.expression(14)
                        pass

                    elif la_ == 11:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 248
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 249
                        self.match(cpp20Parser.NOT_EQ)
                        self.state = 250
                        self.expression(13)
                        pass

                    elif la_ == 12:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 251
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 252
                        self.match(cpp20Parser.BITOR)
                        self.state = 253
                        self.expression(12)
                        pass

                    elif la_ == 13:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 254
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 255
                        self.match(cpp20Parser.BITAND)
                        self.state = 256
                        self.expression(11)
                        pass

                    elif la_ == 14:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 257
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 258
                        self.match(cpp20Parser.XOR)
                        self.state = 259
                        self.expression(10)
                        pass

                    elif la_ == 15:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 260
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 261
                        self.match(cpp20Parser.OR)
                        self.state = 262
                        self.expression(9)
                        pass

                    elif la_ == 16:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 263
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 264
                        self.match(cpp20Parser.AND)
                        self.state = 265
                        self.expression(8)
                        pass

                    elif la_ == 17:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 266
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 267
                        self.match(cpp20Parser.LSHIFT)
                        self.state = 268
                        self.expression(7)
                        pass

                    elif la_ == 18:
                        localctx = cpp20Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 269
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 270
                        self.match(cpp20Parser.RSHIFT)
                        self.state = 271
                        self.expression(6)
                        pass

             
                self.state = 276
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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


        def variableDeclarator(self):
            return self.getTypedRuleContext(cpp20Parser.VariableDeclaratorContext,0)


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
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.ifStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.switchStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 279
                self.whileStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 280
                self.doWhileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 281
                self.forStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 282
                self.returnStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 283
                self.breakStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 284
                self.continueStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 285
                self.block()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 286
                self.variableDeclarator()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 287
                self.arrayDeclarator()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.LPAREN) | (1 << cpp20Parser.SUB) | (1 << cpp20Parser.BITAND))) != 0) or ((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (cpp20Parser.NOT - 85)) | (1 << (cpp20Parser.Identifier - 85)) | (1 << (cpp20Parser.StringLiteral - 85)) | (1 << (cpp20Parser.CharacterLiteral - 85)) | (1 << (cpp20Parser.DecimalLiteral - 85)) | (1 << (cpp20Parser.FloatingLiteral - 85)))) != 0):
                    self.state = 288
                    self.expression(0)


                self.state = 291
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
        self.enterRule(localctx, 36, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(cpp20Parser.LBRACE)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & ((1 << (cpp20Parser.LBRACE - 5)) | (1 << (cpp20Parser.LPAREN - 5)) | (1 << (cpp20Parser.SEMI - 5)) | (1 << (cpp20Parser.SUB - 5)) | (1 << (cpp20Parser.BITAND - 5)) | (1 << (cpp20Parser.BOOL - 5)) | (1 << (cpp20Parser.BREAK - 5)) | (1 << (cpp20Parser.CHAR - 5)) | (1 << (cpp20Parser.CONTINUE - 5)) | (1 << (cpp20Parser.DO - 5)) | (1 << (cpp20Parser.DOUBLE - 5)))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (cpp20Parser.FLOAT - 74)) | (1 << (cpp20Parser.FOR - 74)) | (1 << (cpp20Parser.IF - 74)) | (1 << (cpp20Parser.INT - 74)) | (1 << (cpp20Parser.LONG - 74)) | (1 << (cpp20Parser.NOT - 74)) | (1 << (cpp20Parser.RETURN - 74)) | (1 << (cpp20Parser.SHORT - 74)) | (1 << (cpp20Parser.SWITCH - 74)) | (1 << (cpp20Parser.VOID - 74)) | (1 << (cpp20Parser.WHILE - 74)) | (1 << (cpp20Parser.Identifier - 74)) | (1 << (cpp20Parser.StringLiteral - 74)) | (1 << (cpp20Parser.CharacterLiteral - 74)) | (1 << (cpp20Parser.DecimalLiteral - 74)) | (1 << (cpp20Parser.FloatingLiteral - 74)))) != 0):
                self.state = 295
                self.statement()
                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 301
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
        self.enterRule(localctx, 38, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(cpp20Parser.Identifier)
            self.state = 304
            self.match(cpp20Parser.LPAREN)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.LPAREN) | (1 << cpp20Parser.SUB) | (1 << cpp20Parser.BITAND))) != 0) or ((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (cpp20Parser.NOT - 85)) | (1 << (cpp20Parser.Identifier - 85)) | (1 << (cpp20Parser.StringLiteral - 85)) | (1 << (cpp20Parser.CharacterLiteral - 85)) | (1 << (cpp20Parser.DecimalLiteral - 85)) | (1 << (cpp20Parser.FloatingLiteral - 85)))) != 0):
                self.state = 305
                self.expression(0)
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==cpp20Parser.COMMA:
                    self.state = 306
                    self.match(cpp20Parser.COMMA)
                    self.state = 307
                    self.expression(0)
                    self.state = 312
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 315
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
        self.enterRule(localctx, 40, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(cpp20Parser.IF)
            self.state = 318
            self.match(cpp20Parser.LPAREN)
            self.state = 319
            self.expression(0)
            self.state = 320
            self.match(cpp20Parser.RPAREN)
            self.state = 321
            self.statement()
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 322
                self.match(cpp20Parser.ELSE)
                self.state = 323
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
        self.enterRule(localctx, 42, self.RULE_caseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(cpp20Parser.CASE)
            self.state = 327
            self.constExpression()
            self.state = 328
            self.match(cpp20Parser.COLON)
            self.state = 329
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
        self.enterRule(localctx, 44, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(cpp20Parser.SWITCH)
            self.state = 332
            self.match(cpp20Parser.LPAREN)
            self.state = 333
            self.expression(0)
            self.state = 334
            self.match(cpp20Parser.RPAREN)
            self.state = 335
            self.match(cpp20Parser.LBRACE)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cpp20Parser.CASE:
                self.state = 336
                self.caseStatement()
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 342
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
        self.enterRule(localctx, 46, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(cpp20Parser.WHILE)
            self.state = 345
            self.match(cpp20Parser.LPAREN)
            self.state = 346
            self.expression(0)
            self.state = 347
            self.match(cpp20Parser.RPAREN)
            self.state = 348
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
        self.enterRule(localctx, 48, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(cpp20Parser.DO)
            self.state = 351
            self.statement()
            self.state = 352
            self.match(cpp20Parser.WHILE)
            self.state = 353
            self.match(cpp20Parser.LPAREN)
            self.state = 354
            self.expression(0)
            self.state = 355
            self.match(cpp20Parser.RPAREN)
            self.state = 356
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


        def forExprSet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.ForExprSetContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.ForExprSetContext,i)


        def expression(self):
            return self.getTypedRuleContext(cpp20Parser.ExpressionContext,0)


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
            self.state = 358
            self.match(cpp20Parser.FOR)
            self.state = 359
            self.match(cpp20Parser.LPAREN)
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.LPAREN) | (1 << cpp20Parser.SUB) | (1 << cpp20Parser.BITAND))) != 0) or ((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (cpp20Parser.NOT - 85)) | (1 << (cpp20Parser.Identifier - 85)) | (1 << (cpp20Parser.StringLiteral - 85)) | (1 << (cpp20Parser.CharacterLiteral - 85)) | (1 << (cpp20Parser.DecimalLiteral - 85)) | (1 << (cpp20Parser.FloatingLiteral - 85)))) != 0):
                self.state = 360
                self.forExprSet()


            self.state = 363
            self.match(cpp20Parser.SEMI)
            self.state = 365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.LPAREN) | (1 << cpp20Parser.SUB) | (1 << cpp20Parser.BITAND))) != 0) or ((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (cpp20Parser.NOT - 85)) | (1 << (cpp20Parser.Identifier - 85)) | (1 << (cpp20Parser.StringLiteral - 85)) | (1 << (cpp20Parser.CharacterLiteral - 85)) | (1 << (cpp20Parser.DecimalLiteral - 85)) | (1 << (cpp20Parser.FloatingLiteral - 85)))) != 0):
                self.state = 364
                self.expression(0)


            self.state = 367
            self.match(cpp20Parser.SEMI)
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.LPAREN) | (1 << cpp20Parser.SUB) | (1 << cpp20Parser.BITAND))) != 0) or ((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (cpp20Parser.NOT - 85)) | (1 << (cpp20Parser.Identifier - 85)) | (1 << (cpp20Parser.StringLiteral - 85)) | (1 << (cpp20Parser.CharacterLiteral - 85)) | (1 << (cpp20Parser.DecimalLiteral - 85)) | (1 << (cpp20Parser.FloatingLiteral - 85)))) != 0):
                self.state = 368
                self.forExprSet()


            self.state = 371
            self.match(cpp20Parser.RPAREN)
            self.state = 372
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForExprSetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return cpp20Parser.RULE_forExprSet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForExprSet" ):
                listener.enterForExprSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForExprSet" ):
                listener.exitForExprSet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForExprSet" ):
                return visitor.visitForExprSet(self)
            else:
                return visitor.visitChildren(self)




    def forExprSet(self):

        localctx = cpp20Parser.ForExprSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_forExprSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.expression(0)
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cpp20Parser.COMMA:
                self.state = 375
                self.match(cpp20Parser.COMMA)
                self.state = 376
                self.expression(0)
                self.state = 381
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 54, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(cpp20Parser.RETURN)
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.LPAREN) | (1 << cpp20Parser.SUB) | (1 << cpp20Parser.BITAND))) != 0) or ((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (cpp20Parser.NOT - 85)) | (1 << (cpp20Parser.Identifier - 85)) | (1 << (cpp20Parser.StringLiteral - 85)) | (1 << (cpp20Parser.CharacterLiteral - 85)) | (1 << (cpp20Parser.DecimalLiteral - 85)) | (1 << (cpp20Parser.FloatingLiteral - 85)))) != 0):
                self.state = 383
                self.expression(0)


            self.state = 386
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
        self.enterRule(localctx, 56, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(cpp20Parser.BREAK)
            self.state = 389
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
        self.enterRule(localctx, 58, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(cpp20Parser.CONTINUE)
            self.state = 392
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


        def variableDeclarator(self):
            return self.getTypedRuleContext(cpp20Parser.VariableDeclaratorContext,0)


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
        self.enterRule(localctx, 60, self.RULE_declaration)
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.arrayDeclarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.variableDeclarator()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 396
                self.functionDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 397
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


        def getRuleIndex(self):
            return cpp20Parser.RULE_arrayDeclarator

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NormalArrDeclContext(ArrayDeclaratorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cpp20Parser.ArrayDeclaratorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def typeSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.TypeSpecifierContext,0)

        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)
        def LSQUARE(self):
            return self.getToken(cpp20Parser.LSQUARE, 0)
        def DecimalLiteral(self):
            return self.getToken(cpp20Parser.DecimalLiteral, 0)
        def RSQUARE(self):
            return self.getToken(cpp20Parser.RSQUARE, 0)
        def SEMI(self):
            return self.getToken(cpp20Parser.SEMI, 0)
        def ASSIGN(self):
            return self.getToken(cpp20Parser.ASSIGN, 0)
        def LBRACE(self):
            return self.getToken(cpp20Parser.LBRACE, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.ExpressionContext,i)

        def RBRACE(self):
            return self.getToken(cpp20Parser.RBRACE, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(cpp20Parser.COMMA)
            else:
                return self.getToken(cpp20Parser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalArrDecl" ):
                listener.enterNormalArrDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalArrDecl" ):
                listener.exitNormalArrDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalArrDecl" ):
                return visitor.visitNormalArrDecl(self)
            else:
                return visitor.visitChildren(self)


    class StringDeclContext(ArrayDeclaratorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cpp20Parser.ArrayDeclaratorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def charTypeSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.CharTypeSpecifierContext,0)

        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)
        def LSQUARE(self):
            return self.getToken(cpp20Parser.LSQUARE, 0)
        def DecimalLiteral(self):
            return self.getToken(cpp20Parser.DecimalLiteral, 0)
        def RSQUARE(self):
            return self.getToken(cpp20Parser.RSQUARE, 0)
        def SEMI(self):
            return self.getToken(cpp20Parser.SEMI, 0)
        def ASSIGN(self):
            return self.getToken(cpp20Parser.ASSIGN, 0)
        def stringLiteral(self):
            return self.getTypedRuleContext(cpp20Parser.StringLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringDecl" ):
                listener.enterStringDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringDecl" ):
                listener.exitStringDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringDecl" ):
                return visitor.visitStringDecl(self)
            else:
                return visitor.visitChildren(self)



    def arrayDeclarator(self):

        localctx = cpp20Parser.ArrayDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_arrayDeclarator)
        self._la = 0 # Token type
        try:
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                localctx = cpp20Parser.NormalArrDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.typeSpecifier()
                self.state = 401
                self.match(cpp20Parser.Identifier)
                self.state = 402
                self.match(cpp20Parser.LSQUARE)
                self.state = 403
                self.match(cpp20Parser.DecimalLiteral)
                self.state = 404
                self.match(cpp20Parser.RSQUARE)
                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==cpp20Parser.ASSIGN:
                    self.state = 405
                    self.match(cpp20Parser.ASSIGN)
                    self.state = 406
                    self.match(cpp20Parser.LBRACE)
                    self.state = 407
                    self.expression(0)
                    self.state = 412
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==cpp20Parser.COMMA:
                        self.state = 408
                        self.match(cpp20Parser.COMMA)
                        self.state = 409
                        self.expression(0)
                        self.state = 414
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 415
                    self.match(cpp20Parser.RBRACE)


                self.state = 419
                self.match(cpp20Parser.SEMI)
                pass

            elif la_ == 2:
                localctx = cpp20Parser.StringDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.charTypeSpecifier()
                self.state = 422
                self.match(cpp20Parser.Identifier)
                self.state = 423
                self.match(cpp20Parser.LSQUARE)
                self.state = 424
                self.match(cpp20Parser.DecimalLiteral)
                self.state = 425
                self.match(cpp20Parser.RSQUARE)
                self.state = 428
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==cpp20Parser.ASSIGN:
                    self.state = 426
                    self.match(cpp20Parser.ASSIGN)
                    self.state = 427
                    self.stringLiteral()


                self.state = 430
                self.match(cpp20Parser.SEMI)
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


        def getRuleIndex(self):
            return cpp20Parser.RULE_variableDeclaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VarDeclWithConstInitContext(VariableDeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cpp20Parser.VariableDeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)
        def ASSIGN(self):
            return self.getToken(cpp20Parser.ASSIGN, 0)
        def constExpression(self):
            return self.getTypedRuleContext(cpp20Parser.ConstExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclWithConstInit" ):
                listener.enterVarDeclWithConstInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclWithConstInit" ):
                listener.exitVarDeclWithConstInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclWithConstInit" ):
                return visitor.visitVarDeclWithConstInit(self)
            else:
                return visitor.visitChildren(self)


    class VarDeclWithoutInitContext(VariableDeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cpp20Parser.VariableDeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclWithoutInit" ):
                listener.enterVarDeclWithoutInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclWithoutInit" ):
                listener.exitVarDeclWithoutInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclWithoutInit" ):
                return visitor.visitVarDeclWithoutInit(self)
            else:
                return visitor.visitChildren(self)


    class VarDeclWithInitContext(VariableDeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cpp20Parser.VariableDeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)
        def ASSIGN(self):
            return self.getToken(cpp20Parser.ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(cpp20Parser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclWithInit" ):
                listener.enterVarDeclWithInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclWithInit" ):
                listener.exitVarDeclWithInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclWithInit" ):
                return visitor.visitVarDeclWithInit(self)
            else:
                return visitor.visitChildren(self)



    def variableDeclaration(self):

        localctx = cpp20Parser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_variableDeclaration)
        try:
            self.state = 441
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                localctx = cpp20Parser.VarDeclWithoutInitContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.match(cpp20Parser.Identifier)
                pass

            elif la_ == 2:
                localctx = cpp20Parser.VarDeclWithConstInitContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.match(cpp20Parser.Identifier)
                self.state = 436
                self.match(cpp20Parser.ASSIGN)
                self.state = 437
                self.constExpression()
                pass

            elif la_ == 3:
                localctx = cpp20Parser.VarDeclWithInitContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 438
                self.match(cpp20Parser.Identifier)
                self.state = 439
                self.match(cpp20Parser.ASSIGN)
                self.state = 440
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.TypeSpecifierContext,0)


        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cpp20Parser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(cpp20Parser.VariableDeclarationContext,i)


        def SEMI(self):
            return self.getToken(cpp20Parser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(cpp20Parser.COMMA)
            else:
                return self.getToken(cpp20Parser.COMMA, i)

        def getRuleIndex(self):
            return cpp20Parser.RULE_variableDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarator" ):
                listener.enterVariableDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarator" ):
                listener.exitVariableDeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclarator" ):
                return visitor.visitVariableDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclarator(self):

        localctx = cpp20Parser.VariableDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_variableDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.typeSpecifier()
            self.state = 444
            self.variableDeclaration()
            self.state = 449
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cpp20Parser.COMMA:
                self.state = 445
                self.match(cpp20Parser.COMMA)
                self.state = 446
                self.variableDeclaration()
                self.state = 451
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 452
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


        def getRuleIndex(self):
            return cpp20Parser.RULE_functionDeclaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionDeclContext(FunctionDeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cpp20Parser.FunctionDeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def typeSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.TypeSpecifierContext,0)

        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)
        def LPAREN(self):
            return self.getToken(cpp20Parser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(cpp20Parser.RPAREN, 0)
        def SEMI(self):
            return self.getToken(cpp20Parser.SEMI, 0)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)


    class FunctionDefContext(FunctionDeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a cpp20Parser.FunctionDeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDef" ):
                listener.enterFunctionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDef" ):
                listener.exitFunctionDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDef" ):
                return visitor.visitFunctionDef(self)
            else:
                return visitor.visitChildren(self)



    def functionDeclaration(self):

        localctx = cpp20Parser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 486
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                localctx = cpp20Parser.FunctionDeclContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.typeSpecifier()
                self.state = 455
                self.match(cpp20Parser.Identifier)
                self.state = 456
                self.match(cpp20Parser.LPAREN)
                self.state = 465
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.DOTS) | (1 << cpp20Parser.BOOL) | (1 << cpp20Parser.CHAR))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (cpp20Parser.DOUBLE - 66)) | (1 << (cpp20Parser.FLOAT - 66)) | (1 << (cpp20Parser.INT - 66)) | (1 << (cpp20Parser.LONG - 66)) | (1 << (cpp20Parser.SHORT - 66)) | (1 << (cpp20Parser.VOID - 66)))) != 0):
                    self.state = 457
                    self.functionParameter()
                    self.state = 462
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==cpp20Parser.COMMA:
                        self.state = 458
                        self.match(cpp20Parser.COMMA)
                        self.state = 459
                        self.functionParameter()
                        self.state = 464
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 467
                self.match(cpp20Parser.RPAREN)
                self.state = 468
                self.match(cpp20Parser.SEMI)
                pass

            elif la_ == 2:
                localctx = cpp20Parser.FunctionDefContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.typeSpecifier()
                self.state = 471
                self.match(cpp20Parser.Identifier)
                self.state = 472
                self.match(cpp20Parser.LPAREN)
                self.state = 481
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cpp20Parser.DOTS) | (1 << cpp20Parser.BOOL) | (1 << cpp20Parser.CHAR))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (cpp20Parser.DOUBLE - 66)) | (1 << (cpp20Parser.FLOAT - 66)) | (1 << (cpp20Parser.INT - 66)) | (1 << (cpp20Parser.LONG - 66)) | (1 << (cpp20Parser.SHORT - 66)) | (1 << (cpp20Parser.VOID - 66)))) != 0):
                    self.state = 473
                    self.functionParameter()
                    self.state = 478
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==cpp20Parser.COMMA:
                        self.state = 474
                        self.match(cpp20Parser.COMMA)
                        self.state = 475
                        self.functionParameter()
                        self.state = 480
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 483
                self.match(cpp20Parser.RPAREN)
                self.state = 484
                self.block()
                pass


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

        def pointerTypeSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.PointerTypeSpecifierContext,0)


        def Identifier(self):
            return self.getToken(cpp20Parser.Identifier, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.TypeSpecifierContext,0)


        def DOTS(self):
            return self.getToken(cpp20Parser.DOTS, 0)

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
        self.enterRule(localctx, 70, self.RULE_functionParameter)
        try:
            self.state = 495
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self.pointerTypeSpecifier()
                self.state = 489
                self.match(cpp20Parser.Identifier)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 491
                self.typeSpecifier()
                self.state = 492
                self.match(cpp20Parser.Identifier)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 494
                self.match(cpp20Parser.DOTS)
                pass


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
        self.enterRule(localctx, 72, self.RULE_typeSpecifier)
        try:
            self.state = 502
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 497
                self.integerTypeSpecifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
                self.realTypeSpecifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 499
                self.booleanTypeSpecifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 500
                self.charTypeSpecifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 501
                self.voidTypeSpecifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointerTypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(cpp20Parser.TypeSpecifierContext,0)


        def MULT(self):
            return self.getToken(cpp20Parser.MULT, 0)

        def getRuleIndex(self):
            return cpp20Parser.RULE_pointerTypeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointerTypeSpecifier" ):
                listener.enterPointerTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointerTypeSpecifier" ):
                listener.exitPointerTypeSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointerTypeSpecifier" ):
                return visitor.visitPointerTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def pointerTypeSpecifier(self):

        localctx = cpp20Parser.PointerTypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_pointerTypeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.typeSpecifier()
            self.state = 505
            self.match(cpp20Parser.MULT)
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
        self.enterRule(localctx, 76, self.RULE_integerTypeSpecifier)
        try:
            self.state = 512
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.match(cpp20Parser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 508
                self.match(cpp20Parser.LONG)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 509
                self.match(cpp20Parser.SHORT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 510
                self.match(cpp20Parser.LONG)
                self.state = 511
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
        self.enterRule(localctx, 78, self.RULE_realTypeSpecifier)
        try:
            self.state = 518
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [cpp20Parser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 514
                self.match(cpp20Parser.FLOAT)
                pass
            elif token in [cpp20Parser.DOUBLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.match(cpp20Parser.DOUBLE)
                pass
            elif token in [cpp20Parser.LONG]:
                self.enterOuterAlt(localctx, 3)
                self.state = 516
                self.match(cpp20Parser.LONG)
                self.state = 517
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
        self.enterRule(localctx, 80, self.RULE_booleanTypeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
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
        self.enterRule(localctx, 82, self.RULE_charTypeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
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
        self.enterRule(localctx, 84, self.RULE_voidTypeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
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
         




