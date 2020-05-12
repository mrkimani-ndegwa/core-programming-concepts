def getNthFib(n):
    # iteratively
    sequence = [0,1]
    while len(sequence) <= n:
        num = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        sequence.append(num)

    return sequence


def getNthFibonnacci(n):
    sequence = [0, 1]
    if n not in sequence:
        ge

# allow the function to return a value.
# recieive current
print(getNthFib(35))