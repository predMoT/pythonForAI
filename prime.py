def custom_sqrt(num):
    if num <= 0:
        raise ValueError("Number must be positive")
    
    tolerance = 1e-10
    guess = num / 2.0
    
    while abs(guess * guess - num) > tolerance:
        guess = (guess + num / guess) / 2.0
    
    return guess

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    max_divisor = int(custom_sqrt(num))  # Use custom_sqrt function
    divisor = 3
    
    while divisor * divisor <= num:
        if num % divisor == 0:
            return False
        divisor += 2  # Check next odd number
    
    return True

# Get input from the user
user_input = int(input("Enter the integer: "))
print(f"{user_input} is prime: {is_prime(user_input)}")