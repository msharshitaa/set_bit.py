def set_bit(A, B):
    result=0
    result |= (1 << A)
    result |= (1 << B)
    return result
A = int(input())
B = int(input())
print(set_bit(A, B))
