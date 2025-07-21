import sys
from stats import get_word_count, count_words, get_character_count, count_characters, split_dictionary

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	path = sys.argv[1]

    # Get word count
	book_text = get_word_count(path)
	total_words = count_words(book_text)
    
    # Get character count
	character_count = count_characters(book_text)
    
    # Get sorted character list (only alphabetical
	sorted_chars = split_dictionary(character_count)
    
    # Print the report
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print(f"Found {total_words} total words")
	print("--------- Character Count -------")
	for item in sorted_chars:
		print(f"{item['char']}: {item['num']}")
		print("============= END ===============")

main()
