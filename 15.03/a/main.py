def apply_xor(arr):
    result = 0
    for item in arr:
        result ^= item
    return result


def count_fix(arr, n, m):
    row_arr = set()
    col_arr = set()

    count_replace = 0
    for row in range(n):
        result = apply_xor(arr[row])
        if result:
            row_arr.add(row)

    for col in range(m):
        result = apply_xor([i[col] for i in arr])
        if result:
            if col in row_arr:
                row_arr.remove(col)
                count_replace += 1
                arr[col][col] = 0 if arr[col][col] == 1 else 1
            else:
                if row_arr:
                    count_replace += 1
                    row = row_arr.pop()
                    arr[row][col] = 0 if arr[row][col] == 1 else 1
                else:
                    col_arr.add(col)
    if row_arr:
        count_replace += len(row_arr)
        for i in row_arr:
            arr[i][0] = 0 if arr[i][0] == 1 else 1
    if col_arr:
        count_replace += len(col_arr)
        for i in col_arr:
            arr[0][i] = 0 if arr[0][i] == 1 else 1
    return count_replace

def main():
    count_test = int(input())
    for _ in range(count_test):
        n, m = [int(i) for i in input().split(' ')]
        arr = []
        for i in range(n):
            row = [elem for elem in map(int, input())]
            arr.append(row)
        # print(count_fix(arr, n, m), end=" ")
        print(count_fix(arr, n, m))

if __name__ == '__main__':
    main()
    # print()
    # print("""2 0 3 3 1 2 2 0 1 2 2 1 1 0 0 2 0 0 1""")