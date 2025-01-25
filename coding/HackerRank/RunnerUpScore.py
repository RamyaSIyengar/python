if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr1 = list(arr)

    lst = list(set(arr1))
    lst.sort()
    print(lst[-2])

