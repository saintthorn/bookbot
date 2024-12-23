def main():
	with open("books/frankenstein.txt") as f:
		frankenstein = f.read()
		word_count = word_counter(frankenstein)
		#print(frankenstein)
		print(word_count)

def word_counter(text):
	words = text.split()
	count = 0
	for word in words:
		count += 1
	return count

main()