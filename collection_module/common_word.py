import os
import string
import urllib.request
from collections import Counter

tmp = os.getenv("TMP", "/tmp")


def _resolve_data_files():
    base_dir = os.path.dirname(__file__)
    local_stopwords = os.path.join(base_dir, 'stop_words.txt')
    local_harry = os.path.join(base_dir, 'harry_text.txt')

    if os.path.exists(local_stopwords) and os.path.exists(local_harry):
        return local_stopwords, local_harry

    stopwords_path = os.path.join(tmp, 'stopwords.txt')
    harry_path = os.path.join(tmp, 'harry.txt')
    urllib.request.urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
        stopwords_path,
    )
    urllib.request.urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
        harry_path,
    )
    return stopwords_path, harry_path

def get_harry_most_common_word():
    stopwords_file, harry_text = _resolve_data_files()

    with open(stopwords_file, encoding='utf-8') as f:
        stopwords = {word.strip().lower() for word in f if word.strip()}

    with open(harry_text, encoding='utf-8') as f:
        text = f.read().lower()

    words = [w.strip(string.punctuation) for w in text.split()]
    filtered_words = [w for w in words if w and w not in stopwords]
    return Counter(filtered_words).most_common(1)[0]

get_harry_most_common_word()