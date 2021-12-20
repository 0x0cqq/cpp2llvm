


parser: grammar/cpp20Lexer.g4 grammar/cpp20Parser.g4
	antlr4 -Dlanguage=Python3 grammar/cpp20Parser.g4 grammar/cpp20Lexer.g4 -visitor -o src

build: 
	antlr4 .\cpp20Lexer.g4 .\cpp20Parser.g4; javac cpp20*.java	
	cat ..\test.cpp | grun cpp20 translationUnit -gui


ifdef OS
   RM = del /Q
   FixPath = $(subst /,\,$1)
else
   ifeq ($(shell uname), Linux)
      RM = rm -f
      FixPath = $1
   endif
endif

clean:
	-$(RM) src
   