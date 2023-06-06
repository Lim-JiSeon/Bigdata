# -*- encoding= cp949 -*-

# word2vec를 이용한 유사도 계산 테스트

from gensim.models.word2vec import Word2Vec
from soynlp.tokenizer import RegexTokenizer
import pandas as pd
import re
import utils

class grammar:
    def __init__(self):
        try:
            self.model = Word2Vec.load('word2vec.model')
        except:
            tokenizer = RegexTokenizer()

            lines = None
            tokens= []
            fp, fn = utils.filePaths()
            for p, n in zip(fp, fn): 
                df = utils.readFile(p, n)

                '''
                def preprocessing(text):
                    text = re.sub('\\\\n', ' ', text)
                    text = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z]', ' ', text)
                    return text
                lines = pd.concat(([lines, df['요리명'].apply(preprocessing)]))
                '''
                for l in df:
                    tokens.append(tokenizer.tokenize(l))

            self.model = Word2Vec(tokens, min_count = 0)

            self.model.save('word2vec.model')

    def check(self, word):
        return self.model.wv.most_similar(word)

a = grammar()

print(1)
