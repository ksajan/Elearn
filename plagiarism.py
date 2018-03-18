import Algorithmia

input = {
  "files": [
    [
      "doc1",
      "this is an example input"
    ],
    [
      "doc2",
      "this is another example input"
    ],
    [
      "doc3",
      "the third document is not like the others"
    ]
  ]
}
client = Algorithmia.client('simeIg+RX6DGJbO8d0NmbFy2aAL1')
algo = client.algo('PetiteProgrammer/TextSimilarity/1.0.0')
print(algo.pipe(input).result)