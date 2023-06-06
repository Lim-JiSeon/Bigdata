from tkinter import filedialog, Tk
from konlpy.tag import Komoran
from pykospacing import Spacing
import pandas as pd
import os, re

class Normalize:    # 정규화 함수
    def __init__(self):
        stopwords = readFile(os.getcwd(), 'Stopwords.txt')

        self.stopwords = {}
        for s in stopwords:
            self.stopwords[s] = 0
        self.komoran = Komoran()
        self.spacing = Spacing()

    def process(self, text, opt = 0):
        text = self.stripSCharacter(text)
        if text == '':
            return text
        text = self.resentense(text)
        if opt == 1:
            text = self.tagging(text)
        text = self.removeStopword(text)
        return text

    def stripSCharacter(self, text):        # 한글만 남기기
        return re.sub('[^가-힣\s]', '', text)       

    def removeStopword(self, text):         # 불용어 제거
        words = text.split()
        newWords = []
        for word in words:
            if word in self.stopwords:
                continue
            newWords.append(word)
        return ' '.join(newWords)

    def resentense(self, text):
        text = text.replace(' ', '')
        return self.spacing(text) 

    def tagging(self, text):
        return ' '.join(self.komoran.nouns(text))

def filePaths(opt = 1):
    root = Tk()
    root.withdraw()

    if opt == 1:
        fullPaths = filedialog.askopenfilenames(title = 'Select txt Files', initialdir = os.getcwd(), filetypes = [("Text files", "*.txt"), ("All files", "*.*")])
    elif opt == 2:
        fullPaths = filedialog.askopenfilenames(title = 'Select Excel File', initialdir = os.getcwd(), filetypes=[('Excel files',('*.csv', '*.xlsx')), ("All files", "*.*")])
    elif opt == 3:
        fullPaths = filedialog.askopenfilenames(title = 'Select Excel File', initialdir = os.getcwd(), filetypes=[('JSON files', ('*.json')), ("All files", "*.*")])

    paths, names = [], []
    for p in fullPaths:
        temp = p.split('/')
        paths.append('/'.join(temp[ : -1]))
        names.append(temp[-1])
    
    return paths, names

def readFile(path, name, opt = 1):
    if opt == 1:
        with open(f'{path}/{name}', 'r', encoding = 'utf8') as f:
            data = f.readlines()
        for i in range(len(data)):
            data[i] = data[i].replace('\n', '')
    elif opt == 2:
        data = pd.read_excel(f'{path}/{name}')

    return data

def saveFile(path, name, data, opt = 1, cols = None):
    if opt == 1:
        with open(f'{path}/{name}', 'w', encoding ='utf8') as f:
            for line in data:
                f.write(line + '\n')
    elif opt == 2:
        df = pd.DataFrame(data, columns = cols)
        df.to_excel(f'{path}/{name}', index = False)

def useN():
    return Normalize()