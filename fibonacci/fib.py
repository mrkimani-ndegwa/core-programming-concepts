import time

print(time.time())
def getNthFib(n):
    # iteratively
    # space O (n)
    # time O (n)
    sequence = [0,1]
    while len(sequence) <= n:
        num = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        sequence.append(num)

    return sequence[n-1]

def getNthFibOption(n):
    sequence = [0,1]
    counter = 3
    while counter <= n:
        nxt = sequence[0] + sequence[1]
        sequence[0] = sequence[1]
        sequence[1] = nxt
        counter+=1
    return sequence[1] if n > 1 else sequence[0]


def getNthFibonnacci(n):
    # Poor time complexity galore
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFibonnacci(n - 1) + getNthFibonnacci(n - 2)

# allow the function to return a value.
# recieive current
print(getNthFib(35)) 
print(getNthFibOption(35))
print(getNthFibonnacci(35))