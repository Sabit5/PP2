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

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
    

if __name__ == "__main__":
    num_list = input("Enter a list of numbers separated by spaces: ").split()
    num_list = list(map(int, num_list))

    prime_numbers = filter_prime(num_list)
    print("Prime numbers:", prime_numbers)