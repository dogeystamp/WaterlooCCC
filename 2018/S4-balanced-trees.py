def main():
    n = int(input())
    mem = {}
    def balance(w):
        if w == 1:
            return 1
        if mem.get(w,None):
            return mem[w]
        ways = 0
        for nT in range(2,w+1):
            ways += balance(w//nT)
        mem[w]=ways
        return ways
    print(balance(n))
main()