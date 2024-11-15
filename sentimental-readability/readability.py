from cs50 import get_string

paragraph = get_string("Text: ")

sentence = []  # Initialize empty list to store current sentence
sentences = []  # Initialize empty list to store all sentences
sentence_count = 0  # Initialize counter
word_count = 0
char_count = 0

if paragraph is None:
    print("invalid input")
    exit()

for char in paragraph:  # Fixed typo in 'paragraph'
    sentence.append(char)  # Add character to current sentence
    if char in [".", "?", "!"]:
        sentence_count += 1  # Add 1 to counter (was missing the 1)
        sentences.append(''.join(sentence))  # Join and add complete sentence
        sentence = []  # Reset current sentence

# print("\n")
# print(sentences)


for sentence in sentences:
    words = sentence.split()  # Split sentence into words
    word_count += len(words)  # Count words more accurately
    for char in sentence:
        if char.isalpha():
            char_count += 1

# print(f"sentence_count = {sentence_count}\n word_count = {word_count}\n char_count = {char_count}")

L = 100* char_count / word_count
S = 100 * sentence_count / word_count

grade = round(0.0588 * L - 0.296 * S - 15.8,0)
grade = int(grade)

if 1 <= grade < 16:
    print (f"Grade {grade}")
elif grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
