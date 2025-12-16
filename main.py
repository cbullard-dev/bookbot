from stats import count_words

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents

def main():
  path = "./books/frankenstein.txt"
  book = get_book_text(path)
  wordCount = count_words(book)
  print(f"Found {wordCount} total words")

main()