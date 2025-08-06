#Reverse Words in a String

def reverse_word(input_str):
    
    words = input_str.split()
    words.reverse()
    reversed_str = " ".join(words)
    return reversed_str

s = input("Please enter: ")
print(f"The original string is: '{s}'")
print(f"The reversed string is: '{reverse_word(s)}'")