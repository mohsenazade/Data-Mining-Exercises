import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from os import listdir
from collections import Counter
from math import log
from matplotlib import pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

def cleanText(sen):
    sen = sen.lower()
    sentence = re.sub(r'<[^>]+>', ' ', sen) #remove html tags
    sentence = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%|-)*\b', '', sentence) #remove urls
    sentence = re.sub(r'[^a-zA-Z]', ' ', sentence) #remove symbols and numbers
    sentence = re.sub(r'\s+[a-zA-Z]\s+', ' ', sentence) #remove single char
    sentence = re.sub(r'\s+', ' ', sentence) #remove more than one whiteSpaces
    return sentence

def preprocess(text):
    sent_token = sent_tokenize(text)
    filtered = list(map(cleanText, sent_token))  
    word_token = []
    for sen in filtered:
        word_token.extend(word_tokenize(sen))
    stop_w = set(stopwords.words('english'))
    wordlist = [word for word in word_token if not word in stop_w]
    stemed = list(map(PorterStemmer().stem, wordlist))
    lem = WordNetLemmatizer()
    lem_word = list(map(lem.lemmatize, stemed))
    return lem_word

def entropy(string):
    prob = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]
    entropy = sum([ p * log(p) / log(2.0) for p in prob ])
    return 0 - entropy

def wcloud(text,title):
    wcloud = WordCloud(max_font_size=50, max_words=100, background_color='white').generate(text)
    plt.figure()
    plt.imshow(wcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()

def matrix(wordlist):
    tword = []
    for text in wordlist:
        for word in text:
            if word not in tword:
                tword.append(word)
            else:
                continue
    first_row = ' '.join(tword)
    rows = ''
    for text in wordlist:
        for word in tword:
            rows += ' ' + str(text.count(word))
        rows += '\n'    
    return first_row + '\n' +rows    

if __name__ == '__main__':
    dirlist = listdir('data')
    dirlist.sort()
    words = []
    for txt in dirlist: 
        f = open(f'data/{txt}', 'r')
        text = f.read()
        f.close()
        wordlist = preprocess(text)
        count = Counter(wordlist)
        wcloud(text, txt)
        words.append(wordlist)
    
    matrix = matrix(words)   
