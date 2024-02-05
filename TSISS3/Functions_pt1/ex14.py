from ex12 import histogram
import random 
from ex13 import guess_the_number


if __name__ == "__main__":
    input_str = input("Enter numbers separated by spaces: ")
    int_list = [int(num) for num in input_str.split()]
    histogram(int_list)

    guess_the_number()