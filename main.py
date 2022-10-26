
def fibonaucci(n):
    if n == 1 or n == 0:
        return n
    elif n < 0:
        return -1
    return fibonaucci(n-1) + fibonaucci(n-2)

if __name__ == '__main__':
    num = int(input("Fibonaucci: "))
    print(f"fibonaucci({num}) is {fibonaucci(num)}")