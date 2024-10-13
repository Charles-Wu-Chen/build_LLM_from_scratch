import os
import re

from ch02.SimpleTokenizer import SimpleTokenizerV2

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path relative to the script location
file_path = os.path.join(script_dir, "the-verdict.txt")

try:
    with open(file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()
        print("Total number of characters:", len(raw_text))
        print(raw_text[:99])
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    print(f"Script directory: {script_dir}")
    print("Please make sure the file exists in the correct location.")


# Next goal is to tokenize this 20,479-character short story into individual words
# and special characters that we can then turn into embeddings for LLM
# training in the upcoming chapters.


preprocessed = re.split(r'([,.?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

print(len(preprocessed))

#  convert these tokens (Strings) to an integer representation to produce the so-called token IDs

all_words = sorted(list(set(preprocessed)))
all_words.extend(["<|endoftext|>", "<|unk|>"])
vocab_size = len(all_words)
print(vocab_size)
vocab = {token:integer for integer,token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i > 50:
        break

# test SimpleTokenizerV2

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2))
print(text)



tokenizer = SimpleTokenizerV2(vocab)
encoded = tokenizer.encode(text)
print(encoded[:10])

print(tokenizer.decode(encoded))

