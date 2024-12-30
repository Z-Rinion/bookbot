with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    word_contents = file_contents.split()
    lower_contents = file_contents.lower()
    alphabet = {}
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_contents.count} words found in the document\n\n")
    for letter in lower_contents:
        if not letter in alphabet.keys():
            alphabet[letter] = 0            
        alphabet[letter] += 1
    for key in alphabet.keys():
        print(f"The \'{key}\' character was found {alphabet[key]} times")
    print("--- End of report ---")