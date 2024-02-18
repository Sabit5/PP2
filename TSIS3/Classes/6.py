def is_prime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False



numbers = input("Enter a list of numbers: ").split()
numbers = [int(num) for num in numbers]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", prime_numbers)