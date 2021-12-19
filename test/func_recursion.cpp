int array[10];
int reg[10];
int N;

void merge(int l, int r) {
	int mid = (l + r) / 2;
	int i = l;
	int index1 = l;
	int index2 = mid;
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
	for (k = l;k < r;k++) {
		array[k] = reg[k];
	}
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
	}
}

int print(int x);

int main() {
	array[0] = 5;
	array[1] = 3;
	array[2] = 4;
	array[3] = 2;
	array[4] = 7;
	array[5] = 1;
	array[6] = 8;
	array[7] = 6;
	array[8] = 9;
	array[9] = 0;
	N=10;
	mergeSort(0, N);
	int i;
	for(i=0;i<N;i++){
		print(array[i]);
	}
	return 0;
}