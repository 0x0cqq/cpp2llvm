int printf(char* s, ...);

int s[10];

int main() {
	int a = 1;
	for(a = 1;a < 10;a++) {
		s[a] = a;
	}
	for(a = 1;a < 10;a++) {
		printf("%d\n",s[a]);
	}
    int b = 1;
	for(a = 1;a < 10;a++) {
        for(b = 1;b < 10;b++) {
		    printf("Hello, world! %d %d\n", a, b);
	    }
	}
    b = 1;
    while(b < 20){
        b = b + 1;
        printf("b: %d ", b);
    }
    printf("\n");
	return 0;
}