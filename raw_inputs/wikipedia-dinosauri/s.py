# text source:
# https://cs.wikipedia.org/wiki/Dinosau%C5%99i

import re

text = open("dinosauri.txt", 'r', encoding="utf8").read().replace("\n", " ")

text = re.sub("\[[0-9]+\]", "", text)

file = open("dinosauri-clean.txt", "w", encoding="utf8")
file.write(text)
file.close()