from tkinter import filedialog, Tk
#from konlpy.tag import Komoran
from pykospacing import Spacing
import pandas as pd
import os, re

class Normalize:    # 정규화 함수
    def __init__(self):
        self.stopwords_1 = readFile(os.getcwd(), 'Stopwords_1.txt')
        self.stopwords_2 = readFile(os.getcwd(), 'Stopwords_2.txt')
        for i in range(len(self.stopwords_1)):
            self.stopwords_1[i] = self.stopwords_1[i].replace('\n', '')
        for i in range(len(self.stopwords_2)):
            self.stopwords_2[i] = self.stopwords_2[i].replace('\n', '')
        #self.komoran = Komoran()
        self.spacing = Spacing()

    def process(self, text):
        text = self.stripSCharacter(text)
        if text == '':
            return text
        text = self.resentense(text)
        if text == '':
            return text
        text = self.removeStopword(text)
        if text == '':
            return text
        text = self.removeStopword(text, 1)
        return text

    def stripSCharacter(self, text):                # 한글만 남기기
        return re.sub('[^가-힣\s]', '', text)       

    def removeStopword(self, text, opt = 0):        # 불용어 제거
        if opt == 0:
            words = text.split()
            newWords = []
            for word in words:
                keep = True
                for s in self.stopwords_1:
                    if word == s:
                        keep = False
                        break
                if keep:
                    newWords.append(word)
            return ' '.join(newWords)
        else:
            words = text.split()
            newWords = []
            for word in words:
                keep = True
                for s in self.stopwords_2:
                    if word.find(s) != -1:
                        keep = False
                        break
                if keep:
                    newWords.append(word)
            return ' '.join(newWords)

    def resentense(self, text):
        return self.spacing(text) 

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