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
			try:
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

	print('재료사전 선택')
	fp, fn =  utils.filePaths(2)	# 재료사전
	for p, n in zip(fp, fn): 
		data = utils.readFile(p, n, 2).values.tolist()

		ingreds = []
		for d in data:
			ingreds.append(d[0])

	# INGREDIENT.json
	INGREDIENT_ds = {}
	

	# DISH.json
	DISH_ds = {}

	with open('RECIPE.json', 'w') as f:
		json.dump(RECIPE_ds, f)
	with open('INGREDIENT.json', 'w') as f:
		json.dump(INGREDIENT_ds, f)
	with open('DISH.json', 'w') as f:
		json.dump(DISH_ds, f)