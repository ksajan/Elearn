import Algorithmia

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from googlesearch import search
url = "https://stackoverflow.com/questions/21370298/django-errno-2-no-such-file-or-directory" 
#str(input("Enter the url: "))
input = url 
client = Algorithmia.client('simeIg+RX6DGJbO8d0NmbFy2aAL1')
algo = client.algo('nlp/SummarizeURL/0.1.4')
p = str(algo.pipe(input).result)
print(p)
client = Algorithmia.client('simeIg+RX6DGJbO8d0NmbFy2aAL1')
algo = client.algo('nlp/Summarizer/0.1.6')
print(algo.pipe(p).result)
print("\n""\n")
stopWords = set(stopwords.words('english'))
wordtokens = word_tokenize(p)
fil_sent = [w for w in wordtokens if not w in stopWords]
f = {}
for word in fil_sent:
    if word not in f:
        f[word]  = 1 
    else :
        f[word] += 1
client = Algorithmia.client('simeIg+RX6DGJbO8d0NmbFy2aAL1')
algo = client.algo('cindyxiaoxiaoli/KeywordExtraction/0.3.0')
key = algo.pipe(p).result
for i in  key:
    print("\n")
    print(i)
    print("\n")
    for url in search(i, stop = 2):
        print(url)
