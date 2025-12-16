def count_words(book):
  words = book.split()
  return len(words)

def count_characters(book):
  lower_book = book.lower()
  chars = {}
  for char in lower_book:
    if char not in chars:
      chars[char] = 1
      continue
    chars[char] += 1
  return chars

def sort_counts(count_dictionary):
  count_list = []
  for key in count_dictionary:
    element = {"name": key,
              "num": count_dictionary[key]}
    count_list.append(element)
  count_list.sort(reverse=True, key=sort_on)
  return count_list

def sort_on(items):
  return items["num"]