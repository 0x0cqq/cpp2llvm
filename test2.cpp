int printf(char* s, ...);

int main() {
	int a = 1;
	for(a = 1;a < 10;a++) {
		printf("Hello, world! %d\n",a);
	}
	return 0;
}