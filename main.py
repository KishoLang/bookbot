def main():
    # Read from file
    print(get_text())
    print(count_words())

def get_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words():
    text = get_text()
    split_text = text.split()
    # count = 0
    # for word in split_text:
    #     count += 1
    # return count
    return len(split_text)

main()