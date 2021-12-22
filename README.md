# cpp2llvm
## Usage

1. Install ANTLR4: [ANTLR4 Installation](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md#installation)[^2]
2. Install ANTLR4 runtime library for python: `pip install -r requirements.txt`
3. Build: `make parser`[^1]
4. Run program: `python3 main.py [source file] [output file]`

Below steps are recommended to be performed in Ubuntu/WSL[^3]: 
5. Install LLVM
6. Run the llvm ir code `lli [target file]`[^3]


[^1]: Maybe you need to install `make` in windows, and change this command to `mingw32-make parser`.
[^2]: For Ubuntu you can `sudo apt install antlr4`, and that will give you a `ANTLR 4.7.2` 。
[^3]: It's hard to find any `lli` or `llc` that can run our LLVM IR on Windows...

**More detail can be viewed in [Doc](doc/doc.md).**

