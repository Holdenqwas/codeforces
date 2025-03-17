import math


def op1(val):
    return math.floor(val / 2)

def op2(val):
    return math.ceil(val / 2)
    


def find_min_max_value(val, n, m):
    min_val = val
    max_val = val
    orig_n = n
    orig_m = m

    # find max value
    while n or m:
        print("max", max_val, n, m)
        if max_val % 2:
            if m:
                max_val = op2(max_val)
                m -= 1
            else:
                max_val = op1(max_val)
                n -= 1
        else:
            if n:
                max_val = op1(max_val)
                n -= 1
            else:
                max_val = op2(max_val)
                m -= 1

    n = orig_n
    m = orig_m
    # find min value
    while n or m:
        print("min", min_val, n, m)
        if min_val % 2:
            if n:
                min_val = op1(min_val)
                n -= 1
            else:
                min_val = op2(min_val)
                m -= 1
        else:
            if m:
                min_val = op2(min_val)
                m -= 1
            else:
                min_val = op1(min_val)
                n -= 1

    return min_val, max_val

def main():
    count_test = int(input())
    for _ in range(count_test):
        val, n, m = [int(i) for i in input().split(' ')]

        a, b = find_min_max_value(val, n, m)
        print(a, b)

if __name__ == '__main__':
    main()
    print()
    print("""1 2
3 3
12 12
0 0
88329539 88329539
""")