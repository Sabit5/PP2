from itertools import permutations

def print_permutations(input_string):
    input_list = input_string.split()
    perms = permutations(input_list)
    for i in perms:
        print(" ".join(i))

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    print("Permutations of the string:")
    print_permutations(input_string)