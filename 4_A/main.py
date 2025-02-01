def splite(w: int) -> str:
    if w == 2:
        return 'NO'
    if w % 2 == 0:
        return 'YES'
    return 'NO'

def main():
    a = input()
    print(splite(int(a)))

if __name__ == '__main__':
    main()