def histogram(int_list):
    for num in int_list:
        print('*' * int(num))

if __name__ == "__main__":
    input_str = input("Enter numbers separated by spaces: ")
    int_list = [int(num) for num in input_str.split()]
    histogram(int_list)