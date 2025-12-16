from stats import count_words, count_characters, sort_counts

TITLE = "============ BOOKBOT ============"
WORD_COUNT_HEADER = "----------- Word Count ----------"
CHARACTER_COUNT_HEADER = "--------- Character Count -------"
END = "============= END ==============="


def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents

def main():
  path = "books/frankenstein.txt"

  # Complete the collections and calculations
  book = get_book_text(path)
  wordCount = count_words(book)
  chars = count_characters(book)
  sortCount = sort_counts(chars)

  # Print the message body
  print(TITLE)
  print(f"Analyzing book found at {path}...")
  print(WORD_COUNT_HEADER)
  print(f"Found {wordCount} total words")
  print(CHARACTER_COUNT_HEADER)
  for item in sortCount:
    char = item["name"]
    if not char.isalpha():
      continue
    count = item["num"]
    print(f"{char}: {count}")

  print(END)


main()