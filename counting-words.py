print("Welcome to Counting Words!")

usr_input = input("Enter a word: ")

letters = dict()

def counting_words(arg):
    arg = arg.lower()
    for i in arg:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters 

counting_words(usr_input)

print("We have analysed your word!")

for letter, num in letters.items():
    print("We have found the letter '" + letter + "' " + str(num) + " times.")             
