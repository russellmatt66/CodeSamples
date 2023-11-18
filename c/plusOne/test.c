#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int* plusOne(int* digits, int digitsSize) {
    bool addDigit = true;
    for (int i = 0; i < digitsSize; i++){
        if (digits[i] != 9){
            addDigit = false;
            break;
        }
    }

    printArray(digits,digitsSize);
    printf("addDigit = %d\n", addDigit);
    printf("digitsSize = %d\n", digitsSize);

    int plusOneSize; 

    if (addDigit){
        plusOneSize = digitsSize + 1;
    }
    else {
        plusOneSize = digitsSize;
    }

    int* digitsPlusOne = malloc(plusOneSize * sizeof(int));

    printf("%d\n", plusOneSize);

    int carry = 0;
    int id;
    for (int i = digitsSize - 1; i >= 0; i--){
        if (addDigit){
            id = i+1;
        }
        else {
            id = i;
        }

        if (i == digitsSize - 1){
            digitsPlusOne[id] = digits[i] + 1 + carry;
        }
        else{
            digitsPlusOne[id] = digits[i] + carry;
        }

        printf("%d, %d, %d\n", id, digitsPlusOne[id], digits[i]);

        if (digitsPlusOne[id] > 9){
            digitsPlusOne[id] = 0;
            carry = 1;
        }
        else {
            carry = 0;
        }
    }

    if (addDigit && carry){
        digitsPlusOne[0] = carry;
    }

    printArray(digitsPlusOne, plusOneSize);

    return digitsPlusOne;
}

int main() {
    int digits[] = {1,2,3};  // Example input array
    int digitsSize = sizeof(digits) / sizeof(digits[0]);
    // int returnSize;

    // Call plusOne function
    int* result = plusOne(digits, digitsSize);

    // Free the allocated memory
    free(result);

    return 0;
}
