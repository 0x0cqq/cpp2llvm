int printf(char* a, ...);
int scanf(char* a, ...);

char S[100];
char T[100];
int next[100];
int len;
void GetNext()
{
	len = 0;
	while(T[len] != 0)
		len = len + 1;
	next[0] = -1;
	int i;
	int k;
	for(i = 1; i < len; i = i + 1)
	{
		k = next[i - 1];
		next[i] = 0;
		while(k >= 0)
		{
			if(T[i - 1] == T[k])
			{
				next[i] = k+1;
				break;
			}
			else
				k = next[k];
		}
	}
}
void KMP()
{
	int i = 0;
	int j = 0;
	int flag = 0;
	int pos;
	while(S[i] != 0)
	{
		if(j == -1 || S[i] == T[j])
		{
			i = i + 1; 
			j = j + 1; 
			if(T[j] == 0)
			{
				pos = i - len;
				printf("place: %d\n",pos);
				flag = 1;
			}
		}
		else j = next[j];
	}
	if(flag == 0)
		printf("false");
}
int main()
{
	printf("enter S:");
	scanf("%s",S);
	printf("enter T:");
	scanf("%s",T);

	GetNext();
	KMP();
	return 0;
}