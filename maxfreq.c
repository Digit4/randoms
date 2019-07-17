#include <stdio.h>

void bubbleSort(int arr[], int n)
{
	int i, j, temp;
	for (i = 0; i < n - 1; i++)
		for (j = 0; j < n - i - 1; j++)
			if (arr[j] > arr[j + 1])
			{
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
}

int maximumFrequency(int arr[]) {
	int freq = 0, maxfreq = 0,retval;
	for (int i = 0; i < 10; i++) {
		freq++;
		if (i>=1) {
			if (arr[i]!= arr[i-1]) {
				if (freq > maxfreq) {
					maxfreq = freq;
					retval = arr[i - 1];
				}
				freq = 1;
			}
		}
	}
	return( retval);
}

int main() {
	int arr[10] = {1,1,1,2,2,1,1,1,3,3};
	int arr1[10] = {9, 9, 9, 2, 2, 3, 3, 9, 3, 3};
	int arr2[10] = {1,2,3,4,5,6,7,8,9,0};
	int arr3[10] = {1, 2, 3, 4, 5, 6, -7, 8, 9, 0};
	bubbleSort(arr3, 10);
	int final = maximumFrequency(arr3);
	printf("MaxFreq: %d\n", final);
}