def findSublists(A):
    for i in range(len(A)):


        for j in range(i, len(A)):
            print(A[i:j + 1])

def rotate(arr, n):
    x = arr[n - 1]  #last element

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = x
    print(arr)



if __name__ == '__main__':
    A = [2, 7, 5]
    B=[1, 4, 6, 8, 7]# [7, 1, 4, 6, 8]


    findSublists(A)
    rotate(B, len(B))







