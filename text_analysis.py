import nltk
from collections import Counter

# Download NLTK stopwords (one-time setup)
nltk.download('stopwords')

# Load stopwords
stopwords = nltk.corpus.stopwords.words('english')

# Read text from file
with open("random_paragraphs.txt", "r") as f:
    text = f.read().lower()  # Convert to lowercase for case-insensitivity

# Remove stop words
processed_text = [word for word in text.split() if word not in stopwords]

# Count word frequencies
word_counts = Counter(processed_text)

# Display word frequencies (top 20 most frequent)
print("Top 20 Most Frequent Words:")
for word, count in word_counts.most_common(20):
    print(f"{word}: {count}")
