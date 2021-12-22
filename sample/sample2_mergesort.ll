; ModuleID = ""
target triple = "x86_64-pc-linux"
target datalayout = ""

@"array" = internal global [100 x i32] zeroinitializer
@"reg" = internal global [100 x i32] zeroinitializer
@"N" = internal global i32 0
declare i32 @"printf"(i8* %".1", ...) 

declare i32 @"scanf"(i8* %".1", ...) 

define void @"merge"(i32 %".1", i32 %".2") 
{
__merge:
  %"l" = alloca i32
  store i32 %".1", i32* %"l"
  %"r" = alloca i32
  store i32 %".2", i32* %"r"
  %".6" = getelementptr inbounds [13 x i8], [13 x i8]* @"__string_0", i32 0, i32 0
  %".7" = load i32, i32* %"l"
  %".8" = load i32, i32* %"r"
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".7", i32 %".8")
  %"mid" = alloca i32
  %".10" = load i32, i32* %"l"
  %".11" = load i32, i32* %"r"
  %".12" = add i32 %".10", %".11"
  %".13" = sdiv i32 %".12", 2
  store i32 %".13", i32* %"mid"
  %"i" = alloca i32
  %".15" = load i32, i32* %"l"
  store i32 %".15", i32* %"i"
  %"index1" = alloca i32
  %".17" = load i32, i32* %"l"
  store i32 %".17", i32* %"index1"
  %"index2" = alloca i32
  %".19" = load i32, i32* %"mid"
  store i32 %".19", i32* %"index2"
  br label %".21"
.21:
  %".25" = load i32, i32* %"index1"
  %".26" = load i32, i32* %"mid"
  %".27" = icmp slt i32 %".25", %".26"
  %".28" = load i32, i32* %"index2"
  %".29" = load i32, i32* %"r"
  %".30" = icmp slt i32 %".28", %".29"
  %".31" = icmp ne i1 %".27", 0
  %".32" = icmp ne i1 %".30", 0
  %".33" = and i1 %".31", %".32"
  %".34" = icmp ne i1 %".33", 0
  br i1 %".34", label %".22", label %".23"
.22:
  %".39" = load i32, i32* %"index1"
  %".40" = getelementptr inbounds [100 x i32], [100 x i32]* @"array", i32 0, i32 %".39"
  %".41" = load i32, i32* %".40"
  %".42" = load i32, i32* %"index2"
  %".43" = getelementptr inbounds [100 x i32], [100 x i32]* @"array", i32 0, i32 %".42"
  %".44" = load i32, i32* %".43"
  %".45" = icmp slt i32 %".41", %".44"
  %".46" = icmp ne i1 %".45", 0
  br i1 %".46", label %".36", label %".37"
.23:
  br label %".79"
.36:
  %".48" = load i32, i32* %"i"
  %".49" = getelementptr inbounds [100 x i32], [100 x i32]* @"reg", i32 0, i32 %".48"
  %".50" = load i32, i32* %".49"
  %".51" = load i32, i32* %"index1"
  %".52" = getelementptr inbounds [100 x i32], [100 x i32]* @"array", i32 0, i32 %".51"
  %".53" = load i32, i32* %".52"
  store i32 %".53", i32* %".49"
  %".55" = load i32, i32* %".49"
  %".56" = load i32, i32* %"i"
  %".57" = add i32 %".56", 1
  store i32 %".57", i32* %"i"
  %".59" = load i32, i32* %"index1"
  %".60" = add i32 %".59", 1
  store i32 %".60", i32* %"index1"
  br label %".38"
.37:
  %".63" = load i32, i32* %"i"
  %".64" = getelementptr inbounds [100 x i32], [100 x i32]* @"reg", i32 0, i32 %".63"
  %".65" = load i32, i32* %".64"
  %".66" = load i32, i32* %"index2"
  %".67" = getelementptr inbounds [100 x i32], [100 x i32]* @"array", i32 0, i32 %".66"
  %".68" = load i32, i32* %".67"
  store i32 %".68", i32* %".64"
  %".70" = load i32, i32* %".64"
  %".71" = load i32, i32* %"i"
  %".72" = add i32 %".71", 1
  store i32 %".72", i32* %"i"
  %".74" = load i32, i32* %"index2"
  %".75" = add i32 %".74", 1
  store i32 %".75", i32* %"index2"
  br label %".38"
.38:
  br label %".21"
.79:
  %".83" = load i32, i32* %"index1"
  %".84" = load i32, i32* %"mid"
  %".85" = icmp slt i32 %".83", %".84"
  %".86" = icmp ne i1 %".85", 0
  br i1 %".86", label %".80", label %".81"
.80:
  %".88" = load i32, i32* %"i"
  %".89" = getelementptr inbounds [100 x i32], [100 x i32]* @"reg", i32 0, i32 %".88"
  %".90" = load i32, i32* %".89"
  %".91" = load i32, i32* %"index1"
  %".92" = getelementptr inbounds [100 x i32], [100 x i32]* @"array", i32 0, i32 %".91"
  %".93" = load i32, i32* %".92"
  store i32 %".93", i32* %".89"
  %".95" = load i32, i32* %".89"
  %".96" = load i32, i32* %"index1"
  %".97" = add i32 %".96", 1
  store i32 %".97", i32* %"index1"
  %".99" = load i32, i32* %"i"
  %".100" = add i32 %".99", 1
  store i32 %".100", i32* %"i"
  br label %".79"
.81:
  br label %".103"
.103:
  %".107" = load i32, i32* %"index2"
  %".108" = load i32, i32* %"r"
  %".109" = icmp slt i32 %".107", %".108"
  %".110" = icmp ne i1 %".109", 0
  br i1 %".110", label %".104", label %".105"
.104:
  %".112" = load i32, i32* %"i"
  %".113" = getelementptr inbounds [100 x i32], [100 x i32]* @"reg", i32 0, i32 %".112"
  %".114" = load i32, i32* %".113"
  %".115" = load i32, i32* %"index2"
  %".116" = getelementptr inbounds [100 x i32], [100 x i32]* @"array", i32 0, i32 %".115"
  %".117" = load i32, i32* %".116"
  store i32 %".117", i32* %".113"
  %".119" = load i32, i32* %".113"
  %".120" = load i32, i32* %"index2"
  %".121" = add i32 %".120", 1
  store i32 %".121", i32* %"index2"
  %".123" = load i32, i32* %"i"
  %".124" = add i32 %".123", 1
  store i32 %".124", i32* %"i"
  br label %".103"
.105:
  %"k" = alloca i32
  store i32 0, i32* %"k"
  %".128" = load i32, i32* %"l"
  store i32 %".128", i32* %"k"
  %".130" = load i32, i32* %"k"
  br label %".131"
.131:
  %".136" = load i32, i32* %"k"
  %".137" = load i32, i32* %"r"
  %".138" = icmp slt i32 %".136", %".137"
  %".139" = icmp ne i1 %".138", 0
  br i1 %".139", label %".132", label %".134"
.132:
  %".141" = load i32, i32* %"k"
  %".142" = getelementptr inbounds [100 x i32], [100 x i32]* @"array", i32 0, i32 %".141"
  %".143" = load i32, i32* %".142"
  %".144" = load i32, i32* %"k"
  %".145" = getelementptr inbounds [100 x i32], [100 x i32]* @"reg", i32 0, i32 %".144"
  %".146" = load i32, i32* %".145"
  store i32 %".146", i32* %".142"
  %".148" = load i32, i32* %".142"
  br label %".133"
.133:
  %".150" = load i32, i32* %"k"
  %".151" = add i32 %".150", 1
  store i32 %".151", i32* %"k"
  br label %".131"
.134:
  ret void
}

@"__string_0" = internal global [13 x i8] c"merge %d %d\0a\00"
define void @"mergeSort"(i32 %".1", i32 %".2") 
{
__mergeSort:
  %"l" = alloca i32
  store i32 %".1", i32* %"l"
  %"r" = alloca i32
  store i32 %".2", i32* %"r"
  %".9" = load i32, i32* %"r"
  %".10" = load i32, i32* %"l"
  %".11" = sub i32 %".9", %".10"
  %".12" = icmp eq i32 %".11", 1
  %".13" = icmp ne i1 %".12", 0
  br i1 %".13", label %".6", label %".7"
.6:
  ret void
.7:
  %"mid" = alloca i32
  %".16" = load i32, i32* %"l"
  %".17" = load i32, i32* %"r"
  %".18" = add i32 %".16", %".17"
  %".19" = sdiv i32 %".18", 2
  store i32 %".19", i32* %"mid"
  %".21" = load i32, i32* %"l"
  %".22" = load i32, i32* %"mid"
  call void @"mergeSort"(i32 %".21", i32 %".22")
  %".24" = load i32, i32* %"mid"
  %".25" = load i32, i32* %"r"
  call void @"mergeSort"(i32 %".24", i32 %".25")
  %".27" = load i32, i32* %"l"
  %".28" = load i32, i32* %"r"
  call void @"merge"(i32 %".27", i32 %".28")
  ret void
.8:
  ret void
}

define i32 @"main"() 
{
__main:
  %".2" = getelementptr inbounds [15 x i8], [15 x i8]* @"__string_1", i32 0, i32 0
  %".3" = call i32 (i8*, ...) @"printf"(i8* %".2")
  %".4" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_2", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"scanf"(i8* %".4", i32* @"N")
  %".6" = getelementptr inbounds [17 x i8], [17 x i8]* @"__string_3", i32 0, i32 0
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6")
  %"i" = alloca i32
  store i32 0, i32* %"i"
  store i32 0, i32* %"i"
  %".10" = load i32, i32* %"i"
  br label %".11"
.11:
  %".16" = load i32, i32* %"i"
  %".17" = load i32, i32* @"N"
  %".18" = icmp slt i32 %".16", %".17"
  %".19" = icmp ne i1 %".18", 0
  br i1 %".19", label %".12", label %".14"
.12:
  %".21" = getelementptr inbounds [3 x i8], [3 x i8]* @"__string_4", i32 0, i32 0
  %".22" = load i32, i32* %"i"
  %".23" = getelementptr inbounds [100 x i32], [100 x i32]* @"array", i32 0, i32 %".22"
  %".24" = load i32, i32* %".23"
  %".25" = call i32 (i8*, ...) @"scanf"(i8* %".21", i32* %".23")
  br label %".13"
.13:
  %".27" = load i32, i32* %"i"
  %".28" = add i32 %".27", 1
  store i32 %".28", i32* %"i"
  br label %".11"
.14:
  %".31" = load i32, i32* @"N"
  call void @"mergeSort"(i32 0, i32 %".31")
  store i32 0, i32* %"i"
  %".34" = load i32, i32* %"i"
  br label %".35"
.35:
  %".40" = load i32, i32* %"i"
  %".41" = load i32, i32* @"N"
  %".42" = icmp slt i32 %".40", %".41"
  %".43" = icmp ne i1 %".42", 0
  br i1 %".43", label %".36", label %".38"
.36:
  %".45" = getelementptr inbounds [4 x i8], [4 x i8]* @"__string_5", i32 0, i32 0
  %".46" = load i32, i32* %"i"
  %".47" = getelementptr inbounds [100 x i32], [100 x i32]* @"array", i32 0, i32 %".46"
  %".48" = load i32, i32* %".47"
  %".49" = call i32 (i8*, ...) @"printf"(i8* %".45", i32 %".48")
  br label %".37"
.37:
  %".51" = load i32, i32* %"i"
  %".52" = add i32 %".51", 1
  store i32 %".52", i32* %"i"
  br label %".35"
.38:
  %".55" = getelementptr inbounds [2 x i8], [2 x i8]* @"__string_6", i32 0, i32 0
  %".56" = call i32 (i8*, ...) @"printf"(i8* %".55")
  ret i32 0
}

@"__string_1" = internal global [15 x i8] c"enter N(<100):\00"
@"__string_2" = internal global [3 x i8] c"%d\00"
@"__string_3" = internal global [17 x i8] c"enter N numbers:\00"
@"__string_4" = internal global [3 x i8] c"%d\00"
@"__string_5" = internal global [4 x i8] c"%d \00"
@"__string_6" = internal global [2 x i8] c"\0a\00"