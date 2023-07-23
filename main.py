with open("books/frankenstein.txt") as f:
    #Set some global variables for data manipulation
    counter = 0
    blob = ""
    letters = ""
    letters_dictionary = {}
    #Store the content of the book in a variable called "file_content"
    file_content = f.read()
    #Lower the case on all the letters of the content
    lowered_file_content = file_content.lower()
    #Turn the content into a string
    words = lowered_file_content.split()
    #Turn the string into a blob
    for word in words:
        blob += word
    #Remove non alpha characters from the blob
    for ch in blob:
        if ch.isalpha():
            letters += ch
    #Create a dictionary using each letter as a key and start counting them
    for letter in letters:
        if letter in letters_dictionary:
            letters_dictionary[letter] += 1
        elif letter not in letters_dictionary:
            letters_dictionary[letter] = 1
    
    #Create the report
    print("--- Report of books/frankenstein.txt ---")
    #Count the amount of words for display in the report
    amount_of_words = 0
    for word in words:
        amount_of_words += 1
    print(f"{amount_of_words} words in the document")

    #A new dictionary to be used by the recursive function
    new_dict = {}

    #Function to order a dictionary that holds integers as value and sorts them from greatest to least
    def find_and_order(dict):
        #Find and store the greatest integer of a dictionary
        biggest_value = return_the_greatest_value(dict)
        #Store the key that holds the greatest integer in a dictionary
        key_greatest = return_the_greatest_key(dict, biggest_value) 
        #Append that key and value to a new dictionary   
        new_dict[key_greatest] = biggest_value
        #Delete the greatest value from the original dictionary ("dict") in order to use the remaining values..
        #.. to continue to sort the dictionary using recursion.
        del dict[key_greatest]
        #If the dictionary still has values, we turn to recursion.
        if len(dict) > 0:
            find_and_order(dict)
        return new_dict
       
    #Function to be used by the "find_and_order()" function to find the greatest integer from a dictionary values
    def return_the_greatest_value(dicti):
        biggest_value = 0
        for key, value in letters_dictionary.items():
            if value > biggest_value:
                biggest_value = value
        return biggest_value
    
    #Function to store the key that holds the greatest integer in a dictionary, to be used by the "find_and_order()" function toghether with the "return_the_greatest_value()" function.
    def return_the_greatest_key(dicti, number):
        for key, values in dicti.items():
            if values == number:
                return key

        
    #Create a new dictionary that stores the sorted dictionary
    ordered_letters_dictionary = find_and_order(letters_dictionary)
    #Print the content of the dictionary
    for key, value in ordered_letters_dictionary.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End of report ---")

    