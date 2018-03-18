from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import Algorithmia
from googlesearch import search

import PyPDF2

   
print("***************************RICKX*************************************")
print(" \n")
print(" \n")
print("Choose any of the following:\n1. Extract resources and summary from a pdf document. \n2.  Extract resources and summary from a text document\n 3.Get the theme of the document\n 4.Extract text from immages repeat 1\n 5.Find the amount of plagiarism \n")
print("")
print("")
choice = int(input("Enter your choice here wrt the number: "))
if choice == 1:
    pdfFileObj = open('123.pdf', 'rb') 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader.numPages)
    print('\n' ' \n')

    pageObj = pdfReader.getPage(0)
    print(pageObj.extractText())
    
    inp = pageObj.extractText()
    print(inp)
    
    client = Algorithmia.client('simeIg+RX6DGJbO8d0NmbFy2aAL1')
    algo = client.algo('nlp/Summarizer/0.1.6')
    print(algo.pipe(inp).result)
    print("\n""\n")
    stopWords = set(stopwords.words('english'))
    wordtokens = word_tokenize(inp)
    fil_sent = [w for w in wordtokens if not w in stopWords]
    f = {}
    for word in fil_sent:
        if word not in f:
            f[word]  = 1 
        else :
            f[word] += 1
    client = Algorithmia.client('simeIg+RX6DGJbO8d0NmbFy2aAL1')
    algo = client.algo('cindyxiaoxiaoli/KeywordExtraction/0.3.0')
    key = algo.pipe(inp).result
    for i in  key:
        print("\n")
        print(i)
        print("\n")
        for url in search(i, stop = 2):
            print(url)
            
    pdfFileObj.close()

elif choice == 2:
    import textsum

elif choice == 4:
    import OCRp
elif choice == 5:
    import plagiarism




