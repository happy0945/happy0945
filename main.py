def simplify_digit(num):
    # Helper function to simplify digits
    while num >= 10:
        num = sum(map(int, str(num)))
    return num

def generate_password(decimal_number, name):
    try:
        # Convert decimal number to scientific notation
        scientific_notation = format(decimal_number, '.10e')

        # Extract the coefficient and exponent from scientific notation
        coefficient, exponent = map(float, scientific_notation.split('e'))

        # Simplify digits
        simplified_coefficient = simplify_digit(int(coefficient))
        simplified_exponent = simplify_digit(int(exponent))

        # Convert digits to words
        digit_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

        # Create S1
        s1 = ''.join([digit_words[int(digit)] for digit in str(simplified_coefficient).replace('.', '')[:3]])

        # Create S2
        s2 = ''.join([name[i - 1] for i in range(1, len(name) + 1) if simplified_exponent % 2 != 0])

        # Generate password
        password = f"{s1}@{s2}"
        return password
    except ValueError:
        return "Invalid input"

# Example usage
t = int(input("Enter the number of test cases: "))
for _ in range(t):
    test_case = input("Enter the decimal number and name separated by a space: ").split()
    decimal_number, name = float(test_case[0]), test_case[1]
    password = generate_password(decimal_number, name)
    print(password)
