# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# PART A: Function to print first N Fibonacci terms
def generate_fibonacci(n):
    # Check if N is positive
    if n <= 0:
        print("Error: Number of terms must be a positive integer.")
        return

    fibonacci = []

    first = 0
    second = 1

    for i in range(n):
        fibonacci.append(first)

        # Calculate next Fibonacci number
        next_number = first + second
        first = second
        second = next_number

    print("Fibonacci sequence:", *fibonacci)


# PART B: Function to check if a number is a Fibonacci number
def is_fibonacci(number):

    first = 0
    second = 1

    # Check first two Fibonacci numbers
    if number == first or number == second:
        return True

    # Generate Fibonacci sequence using a loop
    while second <= number:
        next_number = first + second
        first = second
        second = next_number

        if second == number:
            return True

    return False


# Main function
def main():

    # Part A
    terms = int(input("How many terms? "))
    generate_fibonacci(terms)


    # Part B
    number = int(input("\nEnter a number to check: "))

    if is_fibonacci(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


# Run program
if __name__ == "__main__":
    main()