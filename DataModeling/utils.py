from tkinter import filedialog, Tk
from konlpy.tag import Komoran
import pandas as pd
import os, re

class Normalize:    # 정규화 함수
    def __init__(self):
        self.stopwords = readFile(os.getcwd(), '1. Stopwords.txt')
        for i in range(len(self.stopwords)):
            self.stopwords[i] = self.stopwords[i].replace('\n', '')
        self.komoran = Komoran()

    def process(self, text):
        text = self.stripSCharacter(text)
        if text == '':
            return text
        text = self.removeStopword(text)
        if text == '':
            return text
        text = self.lowercase(text)
        if text == '':
            return text
        #text = self.lowercase(text)
        text = self.tagging(text)
        return text

    def stripSCharacter(self, text):        # 특수문자 제거
        return re.sub('[^ㄱ-ㅎ가-힣a-zA-Z0-9\s]', '', text)

    def removeStopword(self, text):         # 불용어 제거
        words = text.split()
        newWords = []
        for word in words:
            keep = True
            for s in self.stopwords:
                if word.find(s) != -1:
                    keep = False
                    break
            if keep:
                newWords.append(word)
        return ' '.join(newWords)
        #return ' '.join([word for word in newWords if word.lower() not in self.stopwords])

    def lowercase(self, text):              # 소문자화
        words = text.split()
        return ' '.join([word.lower() for word in words])
    
    def tagging(self, text):
        words = text.split()
        return ' '.join([word for word in words if self.komoran.pos(word)[0][1] == 'NNP'])

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
        with open(f'{path}/{name}', 'r', encoding = 'cp949') as f:
            data = f.readlines()
        for i in range(len(data)):
            data[i] = data[i].replace('\n', '')
    elif opt == 2:
        data = pd.read_excel(f'{path}/{name}')

    return data

def saveFile(path, name, data, opt = 1, cols = None):
    if opt == 1:
        with open(f'{path}/{name}', 'w', encoding ='cp949') as f:
            for line in data:
                f.write(line + '\n')
    elif opt == 2:
        df = pd.DataFrame(data, columns = cols)
        df.to_excel(f'{path}/{name}', index = False)