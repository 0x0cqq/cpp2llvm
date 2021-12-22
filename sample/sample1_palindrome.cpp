int printf(char* a, ...);
int scanf(char* a, ...);



char str[100];


int check()
{
	printf("please enter your string:\n");
	scanf("%s", str);
	int flag = 1;
	int front = 0;
	int back = 0;
	while(str[back] != '\0')
		back = back + 1;
	back = back - 1;
	while(front < back)
	{
		if(str[ front ] != str[ back ])
			flag = 0;
		front = front + 1;
		back = back - 1;
	}
	if(flag)
		printf("true\n");
	else
		printf("false\n");
	return 0;
}

int main(){
	check();
	return 0;
}