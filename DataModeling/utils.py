from tkinter import filedialog, Tk
import pandas as pd
import os, re

class Normalize:    # 정규화 함수
    def __init__(self):
        self.stopwords = readFile(os.getcwd(), 'Stopwords')
        for i in range(len(self.stopwords)):
            self.stopwords[i] = self.stopwords[i].replace('\n', '')

    def process(self, text):
        text = self.stripSCharacter(text)
        text = self.removeStopword(text)
        #text = self.lowercase(text)
        return text

    def stripSCharacter(self, text):        # 특수문자 제거
        #return re.sub('[^a-zA-Z0-9\s]', '', text)
        return re.sub('[^a-zA-Z0-9+\s\'&-]', '', text)  # +, -, ', & 기호 살림

    def removeStopword(self, text):         # 불용어 제거
        words = text.split()
        return ' '.join([word for word in words if word not in self.stopwords])

    def lowercase(self, text):              # 소문자화
        words = text.split()
        return ' '.join([word.lower() for word in words])

def filePaths(opt = 1):
    root = Tk()
    root.withdraw()

    if opt == 1:
        fullPaths = filedialog.askopenfilenames(title = 'Select txt Files', initialdir = os.getcwd(), filetypes = [("Text files", "*.txt"), ("All files", "*.*")])
    elif opt == 2:
        fullPaths = filedialog.askopenfilenames(title = 'Select Excel File', initialdir = os.getcwd(), filetypes=[('Excel files',('*.csv', '*.xlsx')), ("All files", "*.*")])

    paths, names = [], []
    for p in fullPaths:
        temp = p.split('/')
        paths.append('/'.join(temp[ : -1]))
        names.append(temp[-1])
    
    return paths, names

def readFile(path, name, opt = 1):
    if opt == 1:
        with open(f'{path}/{name}', 'r', encoding ='UTF8') as f:
            data = f.readlines()
        for i in range(len(data)):
            data[i] = data[i].replace('\n', '')
    elif opt == 2:
        data = pd.read_excel(f'{path}/{name}')

    return data

def saveFile(path, name, data, opt = 1, cols = None):
    if opt == 1:
        with open(f'{path}/{name}', 'w', encoding ='UTF8') as f:
            for line in data:
                f.write(line + '\n')
    elif opt == 2:
        df = pd.DataFrame(data, columns = cols)
        df.to_excel(f'{path}/{name}', index = False)