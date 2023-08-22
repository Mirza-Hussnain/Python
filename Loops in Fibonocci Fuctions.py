def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_num = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_num)
    return fib_sequence

def display_sequence(sequence):
    print("Fibonacci Sequence:")
    for num in sequence:
        print(num, end=", ")

def main():
    num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
    fib_sequence = fibonacci(num_terms)
    display_sequence(fib_sequence)

main()
