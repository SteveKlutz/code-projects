# Build a program that counts the number of words in a given text file.

# Provide option to print text file before showing word count.

def intro():
    print("Welcome to the word counter!")


def textfile():
    with open("test.rtf", "r") as file:
        contents = file.read()
        words = contents.split()
        num_words = len(words)
        print(f'The file contains {num_words} words.')


intro()
textfile()
