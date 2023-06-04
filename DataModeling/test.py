# -*- encoding= cp949 -*-

from gensim.models.word2vec import Word2Vec
from soynlp.tokenizer import RegexTokenizer
import pandas as pd
import re
import utils

class similarity:
    def __init__(self):
        try:
            self.model = Word2Vec.load('word2vec.model')
        except:
            tokenizer = RegexTokenizer()

            lines = None
            fp, fn = utils.filePaths(2)
            for p, n in zip(fp, fn): 
                df = utils.readFile(p, n, 2)

                def preprocessing(text):
                    text = re.sub('\\\\n', ' ', text)
                    text = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z]', ' ', text)
                    return text
                lines = pd.concat(([lines, df['요리명'].apply(preprocessing)]))

            tokens = lines.apply(tokenizer.tokenize)
            self.model = Word2Vec(tokens, min_count = 0)

            self.model.save('word2vec.model')

    def check(self, word):
        return self.model.wv.most_similar(word)