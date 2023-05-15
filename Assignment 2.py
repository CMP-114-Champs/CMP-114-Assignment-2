#Write a program that calculates the sum of numbers in a list

def calculate_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

# Example usage:
numbers = [1, 2, 3, 4, 5]
total_sum = calculate_sum(numbers)
print("The sum of the numbers is:", total_sum)
