import Algorithmia
from googlesearch import search
input = {
  "docsList": [
    "Machine learning is a field of computer science that gives computer systems the ability to learn (i.e., progressively improve performance on a specific task) with data, without being explicitly programmed. The name Machine learning was coined in 1959 by Arthur Samuel.Evolved from the study of pattern recognition and computational learning theory in artificial intelligence,[3] machine learning explores the study and construction of algorithms that can learn from and make predictions on data[4] – such algorithms overcome following strictly static program instructions by making data-driven predictions or decisions,[5]:2 through building a model from sample inputs. Machine learning is employed in a range of computing tasks where designing and programming explicit algorithms with good performance is difficult or infeasible; example applications include email filtering, detection of network intruders or malicious insiders working towards a data breach,[6] optical character recognition (OCR),[7] learning to rank, and computer vision.",
  ],
  "mode": "quality"
}
client = Algorithmia.client('simeIg+RX6DGJbO8d0NmbFy2aAL1')
algo = client.algo('nlp/LDA/1.0.0')
p = algo.pipe(input).result
print(p)
lis = []
max = 0
for i in p:
     for j in i:
        if i[j] > max:
            max = i[j]
            lis.append(j)
for i in lis:
    print(i)
    for url in search(i, stop = 2):
        print(url)
