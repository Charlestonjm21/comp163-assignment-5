current_number = int(input("Enter starting number: "))
step_count = 0
while current_number <= 0:
    print("Please enter a positive number.")
    current_number = int(input("Enter starting number: "))

while current_number != 1:
    if current_number % 2 == 0:
        current_number //= 2
    else:
        current_number = 3 * current_number + 1
    step_count += 1
    print(current_number, end=" ")
    
print(f"\nTotal steps taken: {step_count}")
