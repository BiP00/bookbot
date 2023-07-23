with open("books/frankenstein.txt") as f:
    file_content = f.read()
    lowered_file_content = file_content.lower()
    words = lowered_file_content.split()
    counter = 0
    blob = ""
    letters = ""
    letters_dictionary = {}
    for word in words:
        blob += word
    for ch in blob:
        if ch.isalpha():
            letters += ch
    for letter in letters:
        if letter in letters_dictionary:
            letters_dictionary[letter] += 1
        elif letter not in letters_dictionary:
            letters_dictionary[letter] = 1
    print(letters_dictionary)