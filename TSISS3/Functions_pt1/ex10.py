def unique_elements(input_list):
    unique_list = []
    for elem in input_list:
        if elem not in unique_list:
            unique_list.append(elem)
    return unique_list

if __name__ == "__main__":
    input_list = input("Enter a list of elements separated by spaces: ").split()
    unique_list = unique_elements(input_list)
    print("Unique elements:", unique_list)

