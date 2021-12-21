int printf(char* a, ...);
char S[100]="babacdacabcabbdeabacdaaa";
char T[100]="abacd";
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
				printf("%d\n",pos);
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
	GetNext();
	KMP();
	return 0;
}