def main():
	book_path = "books/frankenstein.txt"
	text = get_path(book_path)
	word_count = word_counter(text)
	char_count = char_counter(text)
	print(text)
	print(word_count)
	print(char_count)

def get_path(path):
	with open(path) as f:
		path = f.read()
		return path

def word_counter(text):
	words = text.split()
	count = 0
	for word in words:
		count += 1
	return count

def char_counter(text):
	char_dict = {
		'a': 0,
		'b': 0,
		'c': 0,
		'd': 0,
		'e': 0,
		'f': 0,
		'g': 0,
		'h': 0,
		'i': 0,
		'j': 0,
		'k': 0,
		'l': 0,
		'm': 0,
		'n': 0,
		'o': 0,
		'p': 0,
		'q': 0,
		'r': 0,
		's': 0,
		't': 0,
		'u': 0,
		'v': 0,
		'w': 0,
		'x': 0,
		'y': 0,
		'z': 0
	}
	words = text.split()
	for word in words:
		word = word.lower()
		for char in word:
			if char in char_dict:
				char_dict[char] += 1
			else:
				char_dict[char] = 1
	return char_dict

main()