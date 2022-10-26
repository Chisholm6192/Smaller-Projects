#The fibonaucci sequence is a series of numbers where each entry is equal to the sum of the previous two
#ex. 0 1 1 2 3 5 8
#0 + 1 = 1,  1 + 1 = 2,  1 + 2 = 3,  2 + 3 = 5,  3 + 5 = 8

def fibonaucci(n): 
    if n == 1 or n == 0:
        return n
    #if the sequence number is one or zero, no calculation is required
    
    elif n < 0:
        return -1
    
    return fibonaucci(n-1) + fibonaucci(n-2)
    #the funciton calls itself to iterate through itself to find the preceding numbers in the sequence

if __name__ == '__main__':
    num = int(input("Fibonaucci: "))
    print(f"fibonaucci({num}) is {fibonaucci(num)}")
