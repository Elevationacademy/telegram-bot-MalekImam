from my_math import is_prime
from my_math import factorial
from my_math import is_palindrome

def help_bot(*args):
    return "You can use the following commands \n" + str([cmd for cmd in dict_commands.keys()])


dict_commands = {
    "help": help_bot,
    "check": is_prime,
    "factorial": factorial,
    "palindrome" : is_palindrome
}