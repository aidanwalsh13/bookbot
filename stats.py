# word count of book
def get_word_count(filepath):
        with open(filepath) as f:
                return f.read()

def count_words(text):
        words = text.split()
        return len(words)

# a tally of every symbol and letter
def get_character_count(filepath):
        with open(filepath) as f:
                return f.read()

def count_characters(text):
	text = text.lower()
	c_count = {}
	for c in text:
		if c in c_count:
			c_count[c] += 1
		else:
			c_count[c] = 1
	return c_count

# sorting the frankenstein dictionary into mulitple dictionaries
def sort_on(characters):
	return characters["num"]


def split_dictionary(c_count):
	list_of_dict = []
	for c, count in c_count.items():
		if c.isalpha():
			list_of_dict.append({"char": c, "num": count})
	list_of_dict.sort(reverse=True, key=sort_on)
	return list_of_dict

