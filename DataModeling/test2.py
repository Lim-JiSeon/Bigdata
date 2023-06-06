# -*- encoding= cp949 -*-

# 불용어 처리를 통한 요리명 추출

from collections import OrderedDict
import utils
import os

N = utils.useN()

ss = []
tempDT = {}
fp, fn = utils.filePaths()
for p, n in zip(fp, fn): 
	text = utils.readFile(p, n)

	for line in text:
		if line == '':
			continue
		try:
			print(line)
			newLine = N.process(line, 1)
			newLine = ' '.join(list(OrderedDict.fromkeys(newLine.split())))
			for w in newLine.split():
				try:
					tempDT[w] += 1
				except:
					tempDT[w] = 1

			#if len(newLine.split()) <= 3:
			if len(newLine) > 1:
				ss.append(newLine)
				print(newLine)
			print('')
		except:
			pass

ds = []
left = []
for word, count in tempDT.items():
	if count < 2:
		left.append(word)
		continue
	ds.append([word, count])

ds.sort(key = lambda x : x[1], reverse = True)

ds_n = []
ds_c = []
for word, count in ds:
	ds_n.append(word)
	ds_c.append(f'{word} {count}')

utils.saveFile(os.getcwd(), '형태소 모음.txt', ds_n)
utils.saveFile(os.getcwd(), '형태소 모음(수).txt', ds_c)
utils.saveFile(os.getcwd(), '요리명.txt', ss)
utils.saveFile(os.getcwd(), '쩌리.txt', left)