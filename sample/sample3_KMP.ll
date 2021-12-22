; ModuleID = ""
target triple = "x86_64-pc-linux"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

@"S" = internal global [100 x i8] zeroinitializer
@"T" = internal global [100 x i8] zeroinitializer
@"next" = internal global [100 x i32] zeroinitializer
@"len" = internal global i32 0
define void @"GetNext"() 
{
__GetNext:
  store i32 0, i32* @"len"
  %".3" = load i32, i32* @"len"
  br label %".4"
.4:
  %".8" = load i32, i32* @"len"
  %".9" = getelementptr inbounds [100 x i8], [100 x i8]* @"T", i32 0, i32 %".8"
  %".10" = load i8, i8* %".9"
  %".11" = sext i8 %".10" to i32
  %".12" = icmp ne i32 %".11", 0
  %".13" = icmp ne i1 %".12", 0
  br i1 %".13", label %".5", label %".6"
.5:
  %".15" = load i32, i32* @"len"
  %".16" = add i32 %".15", 1
  store i32 %".16", i32* @"len"
  %".18" = load i32, i32* @"len"
  br label %".4"
.6:
  %".20" = getelementptr inbounds [100 x i32], [100 x i32]* @"next", i32 0, i32 0
  %".21" = load i32, i32* %".20"
  %".22" = sub i32 0, 1
  store i32 %".22", i32* %".20"
  %".24" = load i32, i32* %".20"
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"k" = alloca i32
  store i32 0, i32* %"k"
  store i32 1, i32* %"i"
  %".28" = load i32, i32* %"i"
  br label %".29"
.29:
  %".34" = load i32, i32* %"i"
  %".35" = load i32, i32* @"len"
  %".36" = icmp slt i32 %".34", %".35"
  %".37" = icmp ne i1 %".36", 0
  br i1 %".37", label %".30", label %".32"
.30:
  %".39" = load i32, i32* %"i"
  %".40" = sub i32 %".39", 1
  %".41" = getelementptr inbounds [100 x i32], [100 x i32]* @"next", i32 0, i32 %".40"
  %".42" = load i32, i32* %".41"
  store i32 %".42", i32* %"k"
  %".44" = load i32, i32* %"k"
  %".45" = load i32, i32* %"i"
  %".46" = getelementptr inbounds [100 x i32], [100 x i32]* @"next", i32 0, i32 %".45"
  %".47" = load i32, i32* %".46"
  store i32 0, i32* %".46"
  %".49" = load i32, i32* %".46"
  br label %".50"
.31:
  %".87" = load i32, i32* %"i"
  %".88" = add i32 %".87", 1
  store i32 %".88", i32* %"i"
  %".90" = load i32, i32* %"i"
  br label %".29"
.32:
  ret void
.50:
  %".54" = load i32, i32* %"k"
  %".55" = icmp sge i32 %".54", 0
  %".56" = icmp ne i1 %".55", 0
  br i1 %".56", label %".51", label %".52"
.51:
  %".61" = load i32, i32* %"i"
  %".62" = sub i32 %".61", 1
  %".63" = getelementptr inbounds [100 x i8], [100 x i8]* @"T", i32 0, i32 %".62"
  %".64" = load i8, i8* %".63"
  %".65" = load i32, i32* %"k"
  %".66" = getelementptr inbounds [100 x i8], [100 x i8]* @"T", i32 0, i32 %".65"
  %".67" = load i8, i8* %".66"
  %".68" = icmp eq i8 %".64", %".67"
  %".69" = icmp ne i1 %".68", 0
  br i1 %".69", label %".58", label %".59"
.52:
  br label %".31"
.58:
  %".71" = load i32, i32* %"i"
  %".72" = getelementptr inbounds [100 x i32], [100 x i32]* @"next", i32 0, i32 %".71"
  %".73" = load i32, i32* %".72"
  %".74" = load i32, i32* %"k"
  %".75" = add i32 %".74", 1
  store i32 %".75", i32* %".72"
  %".77" = load i32, i32* %".72"
  br label %".52"
.59:
  %".79" = load i32, i32* %"k"
  %".80" = getelementptr inbounds [100 x i32], [100 x i32]* @"next", i32 0, i32 %".79"
  %".81" = load i32, i32* %".80"
  store i32 %".81", i32* %"k"
  %".83" = load i32, i32* %"k"
  br label %".60"
.60:
  br label %".50"
}

define void @"KMP"() 
{
__KMP:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"j" = alloca i32
  store i32 0, i32* %"j"
  %"flag" = alloca i32
  store i32 0, i32* %"flag"
  %"pos" = alloca i32
  store i32 0, i32* %"pos"
  br label %".6"
.6:
  %".10" = load i32, i32* %"i"
  %".11" = getelementptr inbounds [100 x i8], [100 x i8]* @"S", i32 0, i32 %".10"
  %".12" = load i8, i8* %".11"
  %".13" = sext i8 %".12" to i32
  %".14" = icmp ne i32 %".13", 0
  %".15" = icmp ne i1 %".14", 0
  br i1 %".15", label %".7", label %".8"
.7:
  %".20" = load i32, i32* %"j"
  %".21" = sub i32 0, 1
  %".22" = icmp eq i32 %".20", %".21"
  %".23" = load i32, i32* %"i"
  %".24" = getelementptr inbounds [100 x i8], [100 x i8]* @"S", i32 0, i32 %".23"
  %".25" = load i8, i8* %".24"
  %".26" = load i32, i32* %"j"
  %".27" = getelementptr inbounds [100 x i8], [100 x i8]* @"T", i32 0, i32 %".26"
  %".28" = load i8, i8* %".27"
  %".29" = icmp eq i8 %".25", %".28"
  %".30" = icmp ne i1 %".22", 0
  %".31" = icmp ne i1 %".29", 0
  %".32" = or i1 %".30", %".31"
  %".33" = icmp ne i1 %".32", 0
  br i1 %".33", label %".17", label %".18"
.8:
  %".73" = load i32, i32* %"flag"
  %".74" = icmp eq i32 %".73", 0
  %".75" = icmp ne i1 %".74", 0
  br i1 %".75", label %".71", label %".72"
.17:
  %".35" = load i32, i32* %"i"
  %".36" = add i32 %".35", 1
  store i32 %".36", i32* %"i"
  %".38" = load i32, i32* %"i"
  %".39" = load i32, i32* %"j"
  %".40" = add i32 %".39", 1
  store i32 %".40", i32* %"j"
  %".42" = load i32, i32* %"j"
  %".45" = load i32, i32* %"j"
  %".46" = getelementptr inbounds [100 x i8], [100 x i8]* @"T", i32 0, i32 %".45"
  %".47" = load i8, i8* %".46"
  %".48" = sext i8 %".47" to i32
  %".49" = icmp eq i32 %".48", 0
  %".50" = icmp ne i1 %".49", 0
  br i1 %".50", label %".43", label %".44"
.18:
  %".64" = load i32, i32* %"j"
  %".65" = getelementptr inbounds [100 x i32], [100 x i32]* @"next", i32 0, i32 %".64"
  %".66" = load i32, i32* %".65"
  store i32 %".66", i32* %"j"
  %".68" = load i32, i32* %"j"
  br label %".19"
.19:
  br label %".6"
.43:
  %".52" = load i32, i32* %"i"
  %".53" = load i32, i32* @"len"
  %".54" = sub i32 %".52", %".53"
  store i32 %".54", i32* %"pos"
  %".56" = load i32, i32* %"pos"
  %".57" = getelementptr inbounds [11 x i8], [11 x i8]* @"__string_0", i32 0, i32 0
  %".58" = load i32, i32* %"pos"
  %".59" = call i32 (i8*, ...) @"printf"(i8* %".57", i32 %".58")
  store i32 1, i32* %"flag"
  %".61" = load i32, i32* %"flag"
  br label %".44"
.44:
  br label %".19"
.71:
  %".77" = getelementptr inbounds [6 x i8], [6 x i8]* @"__string_1", i32 0, i32 0
  %".78" = call i32 (i8*, ...) @"printf"(i8* %".77")
  br label %".72"
.72:
  ret void
}

@"__string_0" = internal global [11 x i8] c"place: %d\0a\00"
@"__string_1" = internal global [6 x i8] c"false\00"
define i32 @"main"() 
{
__main:
  %".2" = getelementptr inbounds [9 x i8], [9 x i8]* @"__string_2", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  %".4" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_3", i32 0, i32 0
  %".5" = getelementptr inbounds [100 x i8], [100 x i8]* @"S", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"scanf"(i8* %".4", i8* %".5")
  %".7" = getelementptr inbounds [9 x i8], [9 x i8]* @"__string_4", i32 0, i32 0
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7")
  %".9" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_5", i32 0, i32 0
  %".10" = getelementptr inbounds [100 x i8], [100 x i8]* @"T", i32 0, i32 0
  %".11" = call i32 (i8*, ...) @"scanf"(i8* %".9", i8* %".10")
  call void @"GetNext"()
  call void @"KMP"()
  ret i32 0
}

@"__string_2" = internal global [9 x i8] c"enter S:\00"
@"__string_3" = internal global [3 x i8] c"%s\00"
@"__string_4" = internal global [9 x i8] c"enter T:\00"
@"__string_5" = internal global [3 x i8] c"%s\00"