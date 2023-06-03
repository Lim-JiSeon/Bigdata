import utils

def txtLabels():    # 수동 라벨링 데이터
    fp, fn = utils.filePaths()
    for p, n in zip(fp, fn): 
        text = utils.readFile(p, n)

        newText = []
        for line in text:
            if line == '':
                continue

            token = line.split('/')
            sentense = ' '.join(token[0].split())

            targets, labels = [], []
            for info in token[1 : ]:
                if info == '':
                    continue
                #si = info.split()
                targets.append(info)
                #targets.append(' '.join(si[1 : ]))
                #labels.append(si[0])

            labels.append('DISH')

            newText.append(standard(sentense, targets, labels))
            if newText[-1] == 'x':
                newText.pop()

        utils.saveFile(p, 'norm_' + n, newText)

def standard(origin, target, label):
    if type(target) == str:
        target = [target]
    if type(label) == str:
        label = [label]

    entities = []
    #newOrigin = N.process(origin)
    newOrigin = origin

    for t, l in zip(target, label):
        #nt = N.process(t)
        nt = t
        s = newOrigin.find(nt)
        if s == -1:
            return 'x'
        e = s + len(nt)
        while newOrigin[e] != ' ':
            e += 1
        entities.append((s, e, f'{l}'))

    res = (newOrigin, {'entities' : entities})
    return str(res)

N = utils.Normalize()
txtLabels()