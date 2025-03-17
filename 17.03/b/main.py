
def find_cost(n, k, arr):
    cost = 0
    sort_arr = sorted(arr, reverse=True)
    for i in sort_arr[:k+1]:
       cost += i

    return cost

def main():
    count_test = int(input())
    for _ in range(count_test):
        n, k = [int(i) for i in input().split(' ')]
        arr = [int(i) for i in input().split(' ')]
        print(find_cost(n, k, arr), end=" ")
        # print(find_cost(n, k, arr))

if __name__ == '__main__':
    main()
    print()
    print("5 10 8 7 9 5 3 5 12 12 70 30 2000000000 5 30 11 33")