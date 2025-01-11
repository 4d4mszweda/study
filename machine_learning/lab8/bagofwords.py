import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import string




nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# Wczytanie artykułu
with open('article.txt', 'r', encoding='utf-8') as file:
    article = file.read()

# Tokenizacja
tokens = word_tokenize(article)

# stop words
stop_words = set(stopwords.words('english'))
additional_stopwords = {'said', 'also', 'would', '“', '”', '’'}
stop_words.update(additional_stopwords)
filtered_tokens = [word for word in tokens if word.lower() not in stop_words and word not in string.punctuation]

lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

# zliczanie
word_freq = Counter(lemmatized_tokens)
common_words = word_freq.most_common(10)

words, counts = zip(*common_words)
plt.bar(words, counts)
plt.xlabel('Słowa')
plt.ylabel('Liczba wystąpień')
plt.title('10 najczęściej występujących słów')
plt.show()


# Chmura tagów
text = ' '.join(lemmatized_tokens)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Chmura tagów')
plt.show()