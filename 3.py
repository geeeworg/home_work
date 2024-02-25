def sum_of_elements(numbers, exclude_negative=False):
    if exclude_negative:
        positive_numbers = []
        for num in numbers:
            if num >= 0:
                positive_numbers.append(num)
        return sum(positive_numbers)
    else:
        return sum(numbers)
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
exclude_negative_input = input("Do you want to exclude negative numbers? (yes/no): ")
tf = exclude_negative_input == 'yes'
result = sum_of_elements(numbers, exclude_negative=tf)
print(f"Sum of elements: {result}")

