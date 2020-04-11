import requests
from bs4 import BeautifulSoup
import math
import re
from collections import Counter


URL = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='PageContent_C002_Col01')

results = results.text.split("\n")
facts = []

for i in results:
	if(i != "" and i != "Download and share the graphic" and i!= " "):
		facts.append(i)

WORD = re.compile(r"\w+")

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


facts_vec = []
for i in facts:
	facts_vec.append(text_to_vector(i))


userText = "what are the symptoms of corona virus"
userText_vec = text_to_vector(userText)
get_cosine_score = []

for i in facts_vec:
	get_cosine_score.append(get_cosine(i,userText_vec))

print(get_cosine_score.index(max(get_cosine_score)))

print(facts[get_cosine_score.index(max(get_cosine_score))])

