with open("books/frankenstein.txt") as f:
    file_content = f.read()
    lowered_file_content = file_content.lower()
    words = lowered_file_content.split()
    counter = 0
    for word in words:
        counter += 1
    print(words)