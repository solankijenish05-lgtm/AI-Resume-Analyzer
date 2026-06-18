import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download("stopwords")
nltk.download("wordnet")
def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-z0-9\s]', '', text)

    return text

def remove_stopwords(text):

    stop_words = set(stopwords.words("english"))

    words = text.split()

    filtered_words = []

    for word in words:

        if word not in stop_words:

            filtered_words.append(word)

    return " ".join(filtered_words)
def lemmatize_text(text):

    lemmatizer = WordNetLemmatizer()

    words = text.split()

    result = []

    for word in words:

        result.append(
            lemmatizer.lemmatize(word)
        )

    return " ".join(result)
def preprocess_text(text):

    text = clean_text(text)

    text = remove_stopwords(text)

    text = lemmatize_text(text)

    return text