#Character Count Dictionary

def count_char(input_str):
    char_count = {}
    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        
    return char_count

word = "apple"
print(f"\n The character counts for '{word}' are:")
print(count_char(word))

# sentence = "hello world"
# print(f"\n The character counts for '{sentence}' are:")
# print(count_char(sentence))