a = int(input("m? "))
b = int(input("n? "))
if a < 0 or b < 0:
    print("Negative numbers not allowed")
def Ack(m, n):
    if m >= 0 and n >= 0:
        if m == 0:
            return n + 1
        elif m == 1:
            return n + 2
        elif m == 2:
            return (2 * n) + 3
        elif m == 3:
            return (2 ** (n + 3)) - 3
        else:
            if n == 0:
                return Ack(m - 1, 1)
            else:
                return Ack(m - 1, Ack(m, n - 1)) 
print(Ack(a, b))
