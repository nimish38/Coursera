import random


def bernoulli(p=0.5):
    return random.random() < p


sChampionWord = ''
iChampionValue = 0
sWordList = list(input().split())
for i in range(len(sWordList)):
    iCurrValue = bernoulli(1/(i+1))
    if iCurrValue > iChampionValue:
        iChampionValue = iCurrValue
        sChampionWord = sWordList[i]

print(sChampionWord)
