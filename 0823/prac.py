arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
subsets = [[]]

def d_sup():
	for sub in subsets:
			if sum(sub) == 10:
				print(sub)

for num in arr:
	for i in range(len(subsets)):
			print(f'subsets[i] : {subsets[i]}, {i} {num} {len(subsets)}')
			subsets.append(subsets[i] + [num])
			#print(f'[num] : {num}')