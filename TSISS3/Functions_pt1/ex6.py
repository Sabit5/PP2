def reverse_sentence(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

if __name__ == "__main__":
    input_string = input("Enter a sentence: ")
    reversed_sentence = reverse_sentence(input_string)
    print("Reversed sentence:", reversed_sentence)
