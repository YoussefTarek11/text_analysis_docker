import nltk
from collections import Counter
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')

with open("random_paragraphs.txt", "r") as f:
    text = f.read().lower()  

processed_text = [word for word in text.split() if word not in stopwords]
word_counts = Counter(processed_text)

print("Top 20 Most Frequent Words:")
for word, count in word_counts.most_common(20):
    print(f"{word}: {count}")
