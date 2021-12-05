

parser: frontend/cpp20Lexer.g4 frontend/cpp20Parser.g4
	cd frontend && antlr4 cpp20Lexer.g4 cpp20Parser.g4 && javac cpp20*.java
clean:
	del frontend\*.class frontend\*.java frontend\*.interp frontend\*.tokens