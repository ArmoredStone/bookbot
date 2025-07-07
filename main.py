from stats import count_words, count_characters, sort_desc
import sys

def get_book_text(filepath: str) -> str:
    try:
        with open(filepath) as f:
            file_contents = f.read()
            return file_contents
    except Exception as e:
        print(e)

def main():
    try:
        file_path = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(file_path)

    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_char_count = sort_desc(char_count)
    
    final_messages = []

    final_messages.append("----------- Word Count ----------")
    final_messages.append(f"Found {word_count} total words")
    final_messages.append("--------- Character Count -------")
    
    for k, v in sorted_char_count.items():
        final_messages.append(f"{k}: {v}")

    final_messages.append("============= END ===============")

    for message in final_messages:
        print(message)


if __name__ == "__main__":
    main()
