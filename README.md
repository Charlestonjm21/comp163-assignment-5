# comp163-assignment-5
# Challenge 1: Collatz Conjecture (While Loop)
A while loop is the best choice here because the number of iterations is unknown. The Collatz sequence continues until the number reaches 1, and we don’t know how many steps this will take in advance.

## How it works:

The program prompts the user for a positive integer.

If the number is even, it is divided by 2.

If the number is odd, it is multiplied by 3 and incremented by 1.

Each new number is printed as part of the sequence, and a counter tracks the total steps.

The loop continues until the number becomes 1, at which point the program displays the total step count.

# Challenge 2: Prime Number Checker (For Loop)

A for loop is appropriate because the range of possible divisors is known in advance: from 2 up to n - 1. This makes iteration predictable and clear.

## How it works:

The program asks the user for a number greater than 1.

It then prints the range of divisors that will be tested.

The for loop checks each number from 2 up to n - 1.

If a divisor evenly divides n, the program declares it not prime and exits early.

If no divisors are found, the number is confirmed as prime.

# Challenge 3: Multiplication Table (Nested Loops)

Two loops are required because we need to generate results for both rows and columns. The outer loop controls the current row, and the inner loop produces each product in that row.

## How it works:

The program first prints a header row of numbers 1 through 10.

The outer loop iterates through each row number (1–10).

For each row, the inner loop iterates through each column number (1–10).

The product of the row and column is calculated and printed with proper formatting.

After finishing one row, the program moves to the next line and continues until the table is complete.
# AI assistance
I  used ChatGPT to help me understand how to debug my code when I faced an error and I was stuck, AI usage was limited to insure understanding of the loop concerts and creation of codes was done myself. 
