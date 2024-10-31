def main():
    # Read from file
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    create_book_report(book_path, count_words(text), count_chars(text))
    

def get_text(book):
    with open(book) as f:
        book_text = f.read()
        return book_text

def count_words(text):
    split_text = text.split()
    return len(split_text)

def count_chars(text):
    char_count_dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char.isalpha():
            if lower_char in char_count_dict:
                char_count_dict[lower_char] += 1
            else:
                char_count_dict[lower_char] = 1
    return char_count_dict

def create_book_report(book_name, count_of_words, count_of_chars):
    print(f"--- Begin report of {book_name} ---")
    print(f"{count_of_words} words found in the document")
    print("")
    new_list = count_of_chars.items()
    sorted_new_list = sorted(new_list, key=lambda x: x[1], reverse=True)
    for char in sorted_new_list:
        print(f"The '{char[0]}' character was found {char[1]} times")
    print("--- End report ---")
    

main()