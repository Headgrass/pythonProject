'''
1. arr = [1, 0, -6, 2, 5, 3, 2]
2. pivot = arr[6] (опорный элемент)
3. Вызвать шаги 1-2 для подмассива слева от pivot и справа от pivot
'''

arr = [0, -5, 2, 3, 5, 9, -1, 7]
res = []


def QuickSort(inputArray, minIndex, maxIndex):

    pivot = 0
    QuickSort(inputArray, minIndex, pivot - 1)
    QuickSort(inputArray, pivot + 1, maxIndex)

    return inputArray


def GetPivotIndex(inputArray, minIndex, maxIndex):

    pivotIndex = minIndex -1
    for i in range(len(maxIndex - 1)):
        if (inputArray[i] < inputArray[maxIndex]):
            pivotIndex = pivotIndex + pivotIndex
            swap()


def swap(inputArray[], leftValue, rightValue):
    temp = inputArray[leftValue]
    leftValue = rightValue
    rightValue = temp

