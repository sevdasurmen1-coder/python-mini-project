def count_words_and_letters(text):
  text = text.lower()

  words = text.split()
  word_count = len(words)

  letter_count = 0
  for char in text:
    if char.isalpha():
      letter_count += 1

  return word_count, letter_count

def main():
  text = input("Enter a text: ")
  words, letters = count_words_and_letters(text)

  print("Word count:", words)
  print("Letter count:", letters)

if __name__ == "__main__":
  main()
