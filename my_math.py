
def is_prime(number):
    try:
        number = int(number)
        if number > 1:
            for i in range(2, number//2):
                if number % i == 0:
                    return "Not Prime"
            return "Prime"
        return "Not Prime"
    except:
        return "Invalid Input, must be an integers"


def is_factorial(num):
    i = fact = 1
    while fact < num:
        i += 1
        fact *= i
    return fact == num
    try:
        x = len(num)
        if x <= 2:
            num = int(num)
            if num > 0:
                fact = 1
                for i in range(1, num + 1):
                    fact = fact * i
                return fact
            else:
                return "Invalid Input, must be a positive number."
    except:
        return "Invalid Input, must be an integers"


def is_palindrome(text):
    return text == text[::-1]