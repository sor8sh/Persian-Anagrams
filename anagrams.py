# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

realWords = []
fakeWords = []
allPerms = []
bigPersianNum = ['۵', '۶', '۷', '۸', '۹']


def permutations(head, tail=''):
    if len(head) == 0 and tail not in allPerms:
        allPerms.append(tail)
        url = "https://www.vajehyab.com/?q=" + tail + "&d=en"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        result = soup.find_all('span')[2]
        print(tail + ' ==> ' + result.text)

        text = result.text
        l = text.split(' ')
        if len(l[0]) == 2 or len(l[0]) == 3 or len(l[0]) == 4 or l[0] in bigPersianNum:
            if tail not in realWords and 'هم‌آوا' not in result.text:
                realWords.append(tail)
        elif len(l[0]) == 1 and l[0] != '۰':
            fakeWords.append(tail)

    else:
        for i in range(len(head)):
            permutations(head[0:i] + head[i + 1:], tail + head[i])


word = input("Enter a farsi word: ")
permutations(word)
print('100% Words: ', realWords)
print('50/50 Words: ', fakeWords)
