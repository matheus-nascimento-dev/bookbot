def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
   result = get_book_text("books/frankenstein.txt")
   list = result.split()
   num_words = len(list)
   #print(f"{num_words} words found in the document")

def get_num_words(text):
    #result = get_book_text(filepath)
    list = text.split()
    num_words = len(list)
    #print(num_words)
    return num_words

def get_char_numb(book):
    text = book.lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0)+1
    #print(char_count)
    return char_count

def sort_dictionary(dict):
    new_list = [{"letter":char,"count":count} for char, count in dict.items() ]
    #print(new_list)
    return new_list


main()