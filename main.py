def main():

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    report = get_report(character_count,book_path,num_words)
    print(f"{num_words} words found in the document")
    print(character_count)
    print(report)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    character_dict = {}
    for character in text:
        lowered = character.lower()
        if lowered in character_dict:
            character_dict[lowered] += 1
        else:
            character_dict[lowered] = 1
    return character_dict

def get_report(character_count, book_path,num_words):
    list_dict = []
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for k,v in character_count.sort(reverse=True, key=v):
        if k.isalpha() == True:
            print(f"Key is {k} and value is {v}")


if __name__ == "__main__":
    main()