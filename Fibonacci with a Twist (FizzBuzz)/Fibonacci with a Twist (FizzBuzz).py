#Fibonacci with a Twist (FizzBuzz)
def fibonacci_with_fizzbuzz(n):
    
    if n <= 0:
        return[]
    if n == 1:
        return[0]
    
    fib_list = [0,1]
    
    while len(fib_list) < n:
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)
        
    result_list = []
    for number in fib_list:
        if number % 15 == 0 and number != 0:
            result_list.append("FizzBuzz")
        elif number % 3 == 0 and number != 0:
            result_list.append("Fizz")
        elif number % 5 == 0 and number != 0:
            result_list.append("Buzz")
        else:
            result_list.append(number)
    
    return result_list        
    
n = 8
print(f"The first {n} Fibonacci number with FizzBuzz are: ")
print(fibonacci_with_fizzbuzz(n))
