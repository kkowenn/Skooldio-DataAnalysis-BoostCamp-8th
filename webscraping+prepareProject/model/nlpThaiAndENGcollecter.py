from pythainlp import word_tokenize
from collections import Counter
import pandas as pd

df = pd.read_excel("myPrivateData.xlsx")

# Function to split English and Thai words
def split_words(sentence):
    english_words = []
    thai_words = []
    for word in sentence.split():
        if any(char.isalpha() for char in word) and all(char.isascii() for char in word):
            english_words.extend(word.split())
        else:
            thai_words.extend(word_tokenize(word))
    return english_words + thai_words

# Split words for each title in the aboutTitle['title']
all_words = []
for title in df['title']:
    all_words.extend(split_words(title))

# Count the frequency of each word
word_counts = Counter(all_words)

# Sort the words by frequency and get the top 100 words with their counts
top_100_words = word_counts.most_common(100)

# Create a DataFrame from the top 100 words
df_top_100 = pd.DataFrame(top_100_words, columns=['Word', 'Count'])

# Save the DataFrame to an Excel file
output_file = "top_100_famous_words.xlsx"
df_top_100.to_excel(output_file, index=False, engine='openpyxl')

print(f"Top 100 famous words have been saved to {output_file}")
