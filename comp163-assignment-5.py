# === Challenge 1: Collatz Conjecture ===
print("=== Challenge 1: Collatz Conjecture ===")

# Input validation for positive number
current_number = int(input("Enter starting number: "))
while current_number <= 0:
    print("Please enter a positive number.")
    current_number = int(input("Enter starting number: "))

step_count = 0
print("Sequence:", current_number, end=" ")

# Collatz loop
while current_number != 1:
    if current_number % 2 == 0:      # even
        current_number //= 2
    else:                            # odd
        current_number = 3 * current_number + 1
    print(current_number, end=" ")
    step_count += 1

print(f"\nSteps: {step_count}")
print()


# === Challenge 2: Prime Number Checker ===
print("=== Challenge 2: Prime Number Checker ===")

prime_number = int(input("Enter a number: "))
print(f"Testing divisors from 2 to {prime_number - 1}...")

is_prime = True
for i in range(2, prime_number):
    if prime_number % i == 0:
        print(f"{prime_number} is not prime (divisible by {i})")
        is_prime = False
        break

if is_prime:
    print(f"{prime_number} is prime!")
print()

# === Challenge 3: Multiplication Table ===
print("=== Challenge 3: Multiplication Table ===")
print("\nMultiplication Table:")

# Print header row
print("    ", end="")
for col in range(1, 11):
    print(f"{col:4}", end="")
print()

# Print each row with products
# Used chatGPt to explain to me how nested for loop should be used with the appropriate indentation
for row in range(1, 11):
    print(f"{row:2} ", end="")
    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")
    print()


