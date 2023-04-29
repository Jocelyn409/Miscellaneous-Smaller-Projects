file = open("words.txt", "r")
words = file.readlines()
anagram = {}

# Create dictionary with values from text file
for i in words:
    word = ''.join(sorted(i.strip())) # Get sorted word from file
    anagram.update({word: []}) # Add that word to the dictionary with an empty list value

# Fill dictionary values
for i in words:
    word = ''.join(sorted(i.strip())) # Get key
    newList = anagram.get(word) # Get list using key
    newList.append(i.strip()) # Add word to list
    anagram.update({word: newList}) # Update dictionary key value with the new list

# Print all sets of anagrams in descending order
def print_anagram_descending(dictionary):
    for r in range(11, 1, -1):
        print("Anagram list length of:", r)
        for x in dictionary:
            value = dictionary.get(x)
            if len(value) is r and len(value) >= 2:
                print(value)

print_anagram_descending(anagram)

file.close()
