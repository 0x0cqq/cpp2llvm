int array[100];
int reg[100];
int N;

int printf(char* s, ...);
int scanf(char* s, ...);


void merge(int l, int r) {
	printf("merge %d %d\n", l, r);
	int mid = (l + r) / 2;
	int i = l, index1 = l, index2 = mid;
	while (index1 < mid && index2 < r) {
		if (array[index1] < array[index2]) {
			reg[i] = array[index1];
			i++;
			index1++;
		}
		else {
			reg[i] = array[index2];
			i++;
			index2++;
		}
	}
	while (index1 < mid) {
		reg[i] = array[index1];
		index1++;
		i++;
	}
	while (index2 < r) {
		reg[i] = array[index2];
		index2++;
		i++;
	}
	int k;
	for (k = l; k < r; k++) {
		array[k] = reg[k];
	}
	return;
}

void mergeSort(int l, int r) {
	if (r - l == 1) {
		return;
	}
	else {
		int mid = (l + r) / 2;
		mergeSort(l, mid);
		mergeSort(mid, r);
		merge(l, r);
		return;
	}
}


int main() {
	printf("enter N(<100):");
	scanf("%d",&N);
	printf("enter N numbers:");
	int i;
	for(i = 0;i < N;i++){
		scanf("%d", &array[i]);
	}	
	mergeSort(0, N);
	for(i = 0;i < N;i++){
		printf("%d ", array[i]);
	}
	printf("\n");
	return 0;
}