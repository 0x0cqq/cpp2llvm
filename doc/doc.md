# 编译原理大作业：C到LLVM的编译器

小组成员：陈启乾、潘首安、谭弈凡



## 一、使用说明

### 1. 环境配置

- 系统：Windows 10
- 语言：Python 3.9
- 安装 ANTLR4: [ANTLR4 Installation](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md#installation)

- 安装 ANTLR4 runtime library for python: `pip install antlr4-python3-runtime`



### 2. 编译与运行

1. 编译: `make parser`[^1]
2. 运行程序: `python3 main.py`
3. 编译test文件夹下的代码：
4. 运行llvm代码：

[^1]: Maybe you need to install `make` in windows, and change this command to `mingw32-make parser`.



## 二、文件结构



## 三、实现语法及原理

### 1. 变量与数组

#### 1.1 符号表

我们在 `tables.py` 中定义了符号属性类`NameProperty`和符号表类 `NameTable` 。`NameProperty`类定义了一个符号的所有属性，包括类型`type`，值/地址`value`，是否为有符号数`signed`。`NameTable`类的实例保存程序中声明所有符号（包括变量名，数组名与函数名）。其中定义了列表`table`和当前作用域深度`currunt_scope_level` ，以栈的形式逐层保存符号。

符号表的使用：当程序进入一段新的作用域时，调用符号表的类函数`enterScope`，将当前作用域深度+1，同时在列表`table`中加入一段新的词典。如果有临时变量/数组符号被声明，那么将该符号的相关属性添加至`table`列表的最后一段词典中；如果有全局变量/函数被声明，那么将该符号的相关属性添加至`table`列表的第一段词典中。当变量离开一段作用域时，调用符号表的类函数`exitScope`，将当前作用域-1，同时弹出`table`列表的最后一段词典，释放这个作用域中的所有临时变量。

符号的调用：这部分定义在类函数`getProperty`中。在程序中识别到一标识符后，在`table`列表中从后向前搜索各个词典，返回第一个命中符号的`NameProperty`。如果没有找到该标识符，则报错。

#### 1.2 变量的初始化与访问

变量的声明并不显式地表示在生成的llvm代码中，主要通过符号表实现。具体的实现方式为：判断当前作用域深度，选择以全局变量/临时变量的形式将变量的标识符及其属性加入到符号表。这里保存的变量值实际为其值所在的虚拟寄存器，并非其实际的地址，没有调用llvm的全局/临时变量分配接口，因此不显式地生成llvm代码。

变量的访问通过调用符号表的`getProperty`接口实现，返回的是当前保存变量值的虚拟寄存器。当对变量进行赋值/更新后，再调用符号表的`setProperty`接口更新变量的值为新的虚拟寄存器即可。

#### 1.3 数组的初始化与访问

数组的声明通过`llvmlite`模块中添加全局变量与临时变量的方式实现。首先判断当前变量作用域深度`currunt_scope_level`，选择调用`ir.GlobalVarible`或`Builder.alloca`接口，再将该变量加入符号表。如果在声明的同时对数组进行了初始化，则通过如下数组访问的方式进行值的更新即可。

```python
ir.GlobalVariable(Module, Type, name = CName)
IRBuilder.alloca(Type, name = CName)
```

数组的访问通过`llvmlite`模块中加载指针指向变量值和保存变量值到指针的方式实现。先调用`IRBuilder.gep`获取待访问数组元素的地址，再调用`IRBuilder.load`加载地址到本地，运算结束后调用`IRBuilder.store`保存新的值到地址。

```python
IRBuilder.gep(ptr, indices, inbounds=False, name='')
IRBuilder.load(ptr, name='', align=None)
IRBuilder.store(value, ptr, align=None)
```

### 2. 表达式

表达式分为函数调用，标识符，立即数，判断式，运算式，赋值式等。我们重写了`visitExpression`类，访问表达式时先递归地处理每个子表达式，将他们的类型统一，然后调用`llvmlite`中的表达式处理接口，最后返回一个包括表达式结果类型`type`，表达式结果符号标志`signed`，表达式结果的llvm值`value`的词典，以便使用。

#### 2.1 运算表达式

运算表达式支持的符号包括 '+'|'-'|'*'|'/'|'%'|'>>'|'<<'。实现的方式为：先递归地处理左、右子表达式，将他们转换为同一类型，记录为`exprType`,再调用`llvmlite`处理表达式的接口，保存值到LLVMValue。最终返回的结果为`{exprType,True,LLVMValue}`

```python
IRBuilder.add(lhs, rhs, name='', flags=())
IRBuilder.sub(lhs, rhs, name='', flags=())
IRBuilder.mul(lhs, rhs, name='', flags=())
IRBuilder.sdiv(lhs, rhs, name='', flags=())
IRBuilder.srem(lhs, rhs, name='', flags=())
IRBuilder.shl(lhs, rhs, name='', flags=())
IRBuilder.lshr(lhs, rhs, name='', flags=())
```

#### 2.2 判断表达式

判断表达式支持的符号包括'==' | '!=' | '<' | '<=' | '>' | '>='。实现的方式为：先递归地处理左、右子表达式，将之转换为同一类型，根据数据类型选择调用`llvmlite`的接口，保存值到LLVMValue。最终返回的结果为`{ir.IntType(1),True,LLVMValue}`

```python
IRBuilder.icmp_signed(cmpop, lhs, rhs, name='')
IRBuilder.icmp_unsigned(cmpop, lhs, rhs, name='')
IRBuilder.fcmp_ordered(cmpop, lhs, rhs, name='', flags=[])
```

#### 2.3 赋值表达式

赋值表达式支持对数组和变量进行赋值，具体的方法与数组/变量初始化的方式一致，这里不再赘述。

### 3. 函数

#### 3.1 函数的声明



#### 3.2 函数的调用



#### 3.3 函数返回值



#### 3.4 自定义函数



### 4. 程序结构

程序结构主要通过`llvmlite`中的跳转和条件跳转语句接口实现：

```python
IRBuilder.branch(target)
IRBuilder.cbranch(cond, truebr, falsebr)
```

#### 4.1 选择结构



#### 4.2 循环结构

程序支持的循环结构有while,dowhile,for。

while和dowhile循环都分为三个块，分别保存判断表达式，循环部分和循环结束部分的语句。声明这三个块后，程序首先在当前`IRBuilder`输出指令跳转到判断表达式，然后输出判断表达式对应的语句，再调用`IRBuilder.cbranch`选择进入循环部分或循环结束部分，在循环部分结束后，判断当前块没被break/continue语句插入br语句时，调用`IRBuilder.branch`进入表达式判断语句块。

for循环结构为`for(forExprSet;expression;forExpr){ }`，括号内的三个部分都可以为空，目前不支持在`forExprSet`中进行变量的声明，但可以对已有的变量进行赋值。具体的实现中，for循环分为四个块，相比while和dowhile循环，在循环语句块后增加了更新语句块，逻辑基本一致。

#### 4.3 跳转结构

程序支持的跳转结构有break和continue。程序在`visitor`中定义列表`blockToBreak`和`blockToContinue`，以栈的形式保存语句块。在进入一段循环结构时，将该循环结构中调用break和continue时跳转至的语句块加入对应列表中。识别到break和continue语句时，调用LLVM的接口，输出跳转语句。

break语句的功能为跳转到当前所在循环体的结束块。continue语句的功能为跳转到当前所在循环体的表达式判断块。特别地，对于for循环，continue语句会跳转到更新语句块，再继续进行表达式判断。

## 四、难点与创新点

1. 对一些需要嵌套的语法（表达式，循环结构）进行中间代码生成时，需要递归地进行处理。这个过程需要对返回值进行类型定义，重组等操作，确定输出跳转的语句块，逻辑相对复杂。
2. 

## 五、小组分工

