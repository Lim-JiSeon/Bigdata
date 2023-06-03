import spacy
from spacy.training.example import Example
import utils

#-------------------------------------------------------------------------------------
# 모델명(경로), 추후에 유동적으로 선택 가능하게끔 바꿀 여지 있음
modelName = 'ner_model'
# 하이퍼파라미터
HP = {
    'dropout'   :   0.5,
    'minBatch'  :   32,
    'maxBatch'  :   50,
    'learnRate' :   0.001,
    'epochs'    :   100,
    'patience'  :   100
}
# 라벨
labels = ['DISH']
# 확률(predict)
#probability = 0.5
#-------------------------------------------------------------------------------------

def extract(model, fp = None, fn = None):
    if fn == None:    # 테스트용
        print('음식명 읽기')
        fp, fn = utils.filePaths()
    else:
        fp, fn = [fp], [fn]

    dishes = []
    for p, n in zip(fp, fn): 
        text = utils.readFile(p, n)

        dish = []
        for line in text[1 : ]:
            if line != '':
                doc = model(line)

                for entity in doc.ents:
                    if entity.label_ == 'DISH':
                        dish.append(entity.text)

        dishes.append(dish)

        print('\n=======================================================')
        print('음식명:')
        print('\n'.join(dish))

    return dishes

def setModel():
    from spacy.util import minibatch, compounding
    import random

    trainData = []
    print('학습용 데이터 읽기')
    fp, fn = utils.filePaths()
    for p, n in zip(fp, fn): 
        text = utils.readFile(p, n)
        for line in text:
            trainData.append(eval(line))

    config = {"nlp": {"tokenizer": {"@tokenizers": "spacy.Tokenizer.v1"}}}
    nlp = spacy.blank("ko", config = config)
    nlp.add_pipe('sentencizer')
    ner = nlp.create_pipe('ner')
    for label in labels:
        ner.add_label(label)
    nlp.add_pipe('ner')

    notImp = 0
    bestLoss = 10000

    print('학습 시작\n')
    optimizer = nlp.begin_training()
    for itn in range(HP['epochs']):
        random.shuffle(trainData)
        losses = {}
        batches = minibatch(
            trainData,
            size = compounding(HP['minBatch'], HP['maxBatch'], HP['learnRate'])
        )
        for batch in batches:
            example = []
            texts, annotations = zip(*batch)
            for text, annotation in zip(texts, annotations):
                doc = nlp.make_doc(text)
                tags = spacy.training.offsets_to_biluo_tags(doc, annotation['entities'])
                example.append(Example.from_dict(doc, {'entities': tags}))
            nlp.update(example, drop = HP['dropout'], losses = losses, sgd = optimizer)

        print(f"{itn + 1} Losses: {losses['ner']:.3f}")

        if bestLoss > losses['ner']:
            bestLoss = losses['ner']
            notImp = 0
        else:
            notImp += 1
            if notImp >= HP['patience']:
                print(f"No improvement for {notImp} epochs. Early stopping.")
                break

    global modelName
    nlp.to_disk(modelName)

    print('\n모델 저장 완료')

    extract(nlp)   # for test

setModel()