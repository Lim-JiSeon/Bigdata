import pandas as pd
import numpy as np
import re
from soynlp.tokenizer import RegexTokenizer
from gensim.models import word2vec

def replace_similar_words(text):
    model = word2vec.Word2Vec.load('word2vec_syn.model')

    # 재료 한 번에 입력 가능(\n으로 구분) ex) 소금\n양파\n설탕\n다진마늘\n참기름
    ingredients = text.split('\n')
    for i in range(len(ingredients)):
        try:
            ingredient = ingredients[i]
            result = model.wv.most_similar(ingredient)
            similar_words = [word[0] for word in result if word[1] >= 0.8]   # 유사도 0.8 이상인 단어 중 첫번째 값(유사도가 가장 큰 값)을 유사어로 대체
            for j in range(i + 1, len(ingredients)):
                if ingredients[j] in similar_words:
                    print('--> {0} replaced with {1}'.format(ingredients[j], ingredients[i]))
                    ingredients[j] = ingredients[i]
        except KeyError:
            pass

    return '\n'.join(ingredients)

