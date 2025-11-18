# Day 1 
# Variables

a = 10
b = 5
sum_result = a + b
print("Sum:", sum_result)

# Lists

numbers = [2, 4, 6, 8, 10]
print("First number:", numbers[0])
print("Last number:", numbers[-1])


# Loop
for num in numbers:
    print("Double:", num * 2)


# Function
def average(nums):
    return sum(nums) / len(nums)

print("Average:", average(numbers))
