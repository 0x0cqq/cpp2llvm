int printf(char* a, ...);
int main()
{
	char str[10] = "aba";
	str[3] = '\0';
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
		printf("flase\n");
	return 0;
}