# -*- encoding= cp949 -*-

import json
import ast
import os
import utils

print('1. Excel -> json')
print('2. 통합 데이터 구성')
print('입력 : ', end = '')
opt = int(input())
if opt == 1:	# excel -> json
	fp, fn =  utils.filePaths(2)
	for p, n in zip(fp, fn): 
		data = utils.readFile(p, n, 2).values.tolist()

		RECIPE_DS = {}
		for d in data:
			try:	# 데이터 손실이 일어났을 경우를 대비
				# INGR, COND
				INGR, COND = [], []
				for i in ast.literal_eval(d[6]):
					if i[0] == '재료':
						INGR.append(i)
					elif i[0] == '양념':
						COND.append(i)

				# RECP
				RECP = {}
				for rc in ast.literal_eval(d[7]):
					# tip) 제거
					if rc[0] == 't':
						continue
					e = 0
					while rc[e] != '.':
						e += 1
					RECP[int(rc[ : e])] = rc[e + 2 : ]

				# R_PHO
				R_PHO = {}
				for rp in ast.literal_eval(d[8]):
					e = 0
					while rp[e] != '.':
						e += 1
					RECP[int(rp[ : e])] = rp[e + 2 : ]

				data = {
					'M_PHO'	:	d[1],
					'DISH'	:	d[2],
					'QAUN'	:	d[3],
					'TIME'	:	d[4],
					'DIFF'	:	d[5],
					'INGR'	:	INGR,
					'COND'	:	COND,
					'RECP'	:	RECP,
					'R_PHO'	:	R_PHO
				}
				RECIPE_DS[d[0]] = data

			except:
				continue

		name = n.split("_", 1)[1].split(".")[0]
		with open(f'{os.getcwd()}/{name}.json', 'w') as f:
			json.dump(RECIPE_DS, f)

else:
	# RECIPE.json
	RECIPE_ds = {}
	fp, fn =  utils.filePaths(3)
	for p, n in zip(fp, fn): 
		with open(f'{p}/{n}', 'r') as f:
			RECIPE_ds.update(json.load(f))

	RECIPE_ds = dict(sorted(RECIPE_ds.items()))

	classes = utils.readFile(os.getcwd(), 'class.txt')
	'''
	classes_cl = []
	classes_rm = []
	for c in classes:
		temp = c.split()
		classes_cl.append(temp[0])
		if len(temp) == 2:
			classes_rm.append(temp[0])
	'''
	# DISH.json
	DISH_ds = {}
	for KEY, i in RECIPE_ds.items():
		DISH = i['DISH']
		DISH_ds[DISH] = KEY

	RECIPE_new_ds = {}
	CLASS_ds = {}
	for c in classes:
		for KEY, i in RECIPE_ds.items():
			DISH = i['DISH']
			if DISH.find(c) != -1:
				if c in CLASS_ds:
					CLASS_ds[c].append(KEY)
				else:
					CLASS_ds[c] = [KEY]
				RECIPE_new_ds[KEY] = i

	# INGREDIENT.json
	fp, fn = utils.filePaths(2)
	for p, n in zip(fp, fn): 
		df = utils.readFile(p, n, 2)
		ingreds = df['재료'].tolist()
		counts = df['빈도수'].tolist()

	ingreds_d = {}
	for i, c in zip(ingreds, counts):
		if c >= 250:
			ingreds_d[i] = 1

	INGREDIENT_ds = {}
	for KEY, i in RECIPE_new_ds.items():
		for j in i['INGR']:
			ingred = j[1]
			if ingred in ingreds_d:
				if ingred not in INGREDIENT_ds:
					INGREDIENT_ds[ingred] = [KEY]
				else:
					INGREDIENT_ds[ingred].append(KEY)

	for i in list(INGREDIENT_ds.keys()):
		INGREDIENT_ds[i].sort()

	with open('RECIPE.json', 'w') as f:
		json.dump(RECIPE_new_ds, f)
	with open('DISH.json', 'w') as f:
		json.dump(CLASS_ds, f)
	with open('INGREDIENT.json', 'w') as f:
		json.dump(INGREDIENT_ds, f)
	with open('CLASSES.json', 'w') as f:
		json.dump(classes, f)