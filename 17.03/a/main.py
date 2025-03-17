import math
def find_count_op(n, k):
    count = 0
    if n % 2 == 0:
        if k % 2 == 0:
            count = n / k
        else:
            count = n / (k - 1)
    else:
        if k % 2 == 0:
            count = (n - k - 1) / k + 1
        else:
            count = (n - k) / (k - 1) + 1

    return math.ceil(count)

def main():
    count_test = int(input())
    for _ in range(count_test):
        n, k = [int(i) for i in input().split(' ')]
        # print(find_count_op(n, k), end=" ")
        print(find_count_op(n, k))

if __name__ == '__main__':
    main()
    # print()
    # print("7 4 3 499983901 1 2 499999999 500000000 1")