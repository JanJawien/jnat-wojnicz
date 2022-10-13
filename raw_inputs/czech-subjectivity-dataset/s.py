# text source:
# https://github.com/pauli31/czech-subjectivity-dataset

text = open("test.csv", 'r', encoding="utf8").read().split('\n')[1:]
sentences = [line.split('\t')[0] for line in text]

file = open("czech-subjectivity-dataset.txt", "w", encoding="utf8")
for line in sentences[:-1]:
    file.write(line + "\n")
file.write(sentences[-1])
file.close()