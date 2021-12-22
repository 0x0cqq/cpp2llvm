; ModuleID = ""
target triple = "x86_64-pc-linux"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

@"str" = internal global [100 x i8] zeroinitializer
define i32 @"check"() 
{
__check:
  %".2" = getelementptr inbounds [27 x i8], [27 x i8]* @"__string_0", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  %".4" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_1", i32 0, i32 0
  %".5" = getelementptr inbounds [100 x i8], [100 x i8]* @"str", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"scanf"(i8* %".4", i8* %".5")
  %"flag" = alloca i32
  store i32 1, i32* %"flag"
  %"front" = alloca i32
  store i32 0, i32* %"front"
  %"back" = alloca i32
  store i32 0, i32* %"back"
  br label %".10"
.10:
  %".14" = load i32, i32* %"back"
  %".15" = getelementptr inbounds [100 x i8], [100 x i8]* @"str", i32 0, i32 %".14"
  %".16" = load i8, i8* %".15"
  %".17" = icmp ne i8 %".16", 92
  %".18" = icmp ne i1 %".17", 0
  br i1 %".18", label %".11", label %".12"
.11:
  %".20" = load i32, i32* %"back"
  %".21" = add i32 %".20", 1
  store i32 %".21", i32* %"back"
  %".23" = load i32, i32* %"back"
  br label %".10"
.12:
  %".25" = load i32, i32* %"back"
  %".26" = sub i32 %".25", 1
  store i32 %".26", i32* %"back"
  %".28" = load i32, i32* %"back"
  br label %".29"
.29:
  %".33" = load i32, i32* %"front"
  %".34" = load i32, i32* %"back"
  %".35" = icmp slt i32 %".33", %".34"
  %".36" = icmp ne i1 %".35", 0
  br i1 %".36", label %".30", label %".31"
.30:
  %".40" = load i32, i32* %"front"
  %".41" = getelementptr inbounds [100 x i8], [100 x i8]* @"str", i32 0, i32 %".40"
  %".42" = load i8, i8* %".41"
  %".43" = load i32, i32* %"back"
  %".44" = getelementptr inbounds [100 x i8], [100 x i8]* @"str", i32 0, i32 %".43"
  %".45" = load i8, i8* %".44"
  %".46" = icmp ne i8 %".42", %".45"
  %".47" = icmp ne i1 %".46", 0
  br i1 %".47", label %".38", label %".39"
.31:
  %".64" = load i32, i32* %"flag"
  %".65" = icmp ne i32 %".64", 0
  br i1 %".65", label %".61", label %".62"
.38:
  store i32 0, i32* %"flag"
  %".50" = load i32, i32* %"flag"
  br label %".39"
.39:
  %".52" = load i32, i32* %"front"
  %".53" = add i32 %".52", 1
  store i32 %".53", i32* %"front"
  %".55" = load i32, i32* %"front"
  %".56" = load i32, i32* %"back"
  %".57" = sub i32 %".56", 1
  store i32 %".57", i32* %"back"
  %".59" = load i32, i32* %"back"
  br label %".29"
.61:
  %".67" = getelementptr inbounds [6 x i8], [6 x i8]* @"__string_2", i32 0, i32 0
  %".68" = call i32 (i8*, ...) @"printf"(i8* %".67")
  br label %".63"
.62:
  %".70" = getelementptr inbounds [7 x i8], [7 x i8]* @"__string_3", i32 0, i32 0
  %".71" = call i32 (i8*, ...) @"printf"(i8* %".70")
  br label %".63"
.63:
  ret i32 0
}

@"__string_0" = internal global [27 x i8] c"please enter your string:\0a\00"
@"__string_1" = internal global [3 x i8] c"%s\00"
@"__string_2" = internal global [6 x i8] c"true\0a\00"
@"__string_3" = internal global [7 x i8] c"false\0a\00"
define i32 @"main"() 
{
__main:
  %".2" = call i32 @"check"()
  ret i32 0
}
