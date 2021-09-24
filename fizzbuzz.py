def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizz_buzz(8))
print(fizz_buzz(10))
print(fizz_buzz(6))
print(fizz_buzz(15))
print(fizz_buzz(2))
print(fizz_buzz(5))