if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    arr = [int(ele) for ele in arr]
    arr.sort()
    first = arr.pop()
    i = len(arr)-1
    while i >= 0:
        if arr[i] < first:
            print(arr[i])
            break
        i -= 1
