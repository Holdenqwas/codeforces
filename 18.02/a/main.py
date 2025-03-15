def is_arr_exist(arr):
    cur_position = 0
    pattern = [1,0,1]
    for elem in arr:
        if elem == pattern[cur_position]:
            cur_position+=1
        else:
            cur_position =0
        if cur_position >= 3:
            return 'NO'
        
    if len(arr)>=3:
        if arr[-1] == 1 and arr[-2] == 0: 
            if arr[-3] == 0:
                return 'YES'
            else:
                return 'NO'
        
    return 'YES'

def main():
    # a = input()
    # print(a)
    count_test = int(input())
    for test_case in range(count_test):
        count = int(input())
        arr = [elem for elem in map(int, input().split(' '))]
        print(is_arr_exist(arr))

if __name__ == '__main__':
    main()