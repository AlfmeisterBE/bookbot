def main():

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    report = get_report(character_count,book_path,num_words)
    #print(f"{num_words} words found in the document")
    #print(character_count)
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

def sort_on(dict):
    return dict["count"]

def get_report(character_count, book_path,num_words):
    list_dict = []
    report_strings = []
    report_strings.append(f"--- Begin report of {book_path} ---")
    report_strings.append(f"{num_words} words found in the document")
    report_strings.append("")

    for k,v in character_count.items():
        if k.isalpha() == True:
            list_dict.append({"character": k, "count": v})
    list_dict.sort(reverse=True, key=sort_on )

    for item in list_dict:
            report_strings.append(f"The '{item['character']}' character was found {item['count']} times")
    report_strings.append("--- End report ---")
    
    return "\n".join(report_strings)


if __name__ == "__main__":
    main()