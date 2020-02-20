import sys
filename="a_example"
with open(filename+'.in',"r") as i, open(filename+'.out',"w") as o:
	m , n = [int(s) for s in i.readline().split(" ")]
	l = [int(s) for s in i.readline().split(" ")]
	
	#on trie la liste du plus petit au plus grand. Cela permet un travail plus précis par la suite.
	# on devrait utiliser radix
	l.sort()

	'''
	example
	18
	2 4 5 6 8 = 25
	step 1) Un peu comme un masque en réseau on ne garde que les bits qui nous intéressent.
			On passe 1 à 1 les bits jusqu'a ce que la somme des bits passés à 1 dépasse 18.
	1 1 1 1 1
	step 2) étant trop grand, on va retirer le dernier et essayer de retirer un élément plus petit pour repasser en dessous de 18. En espérant tomber sur la solution.
			On fait glisser un 0 de gauche à droite
	0 1 1 1 1 = 23
	1 0 1 1 1 = 21
	1 1 0 1 1 = 20
	1 1 1 0 1 = 19
	1 1 1 1 0 = 17  -> ON EST EN DESSOUS DE 18.
	step 3) on cherche 8-1=7 car le dernier elem de la list (8) dépasse de 1 le résultat cherché.
			Dans le code on simplifie en faisant 25 - 18 = 7 par simplification.
			On cherche donc une combinaison d'élément = à 7.
			Pour cela on prend l'élément le plus à droit et celui le plus à gaucher.
			Ensuite on prend des éléments de plus en plus au milieu jusqu'à trouver ceux qu'il nous fait.
			PS: si on ne trouve pas, on a gardé la meilleur résultat de côté.
	0 1 1 0 1 = 17   et 2 + 6 = 8
	0 1 0 1 1 = 18   et 2 + 5 = 7   => pour diminuer on décale le 0 de droite à gauche
	1 0 1 0 1 = 15   et 4 + 6 = 10  => pour augmenter on décale le 0 de gauche à droite
	'''

	# step 1
	index = 0
	while not sum(l[:index]) >= m:
		index += 1
		#print("step1 :"+str(index))

	if sum(l[:index]) == m:
		tmp = list(range(len(l[:index])))
		o.write(str(len(tmp))+"\n")
		o.write(" ".join(list(map(str, tmp))))
		sys.exit()

	# step 2
	index2 = 0
	#print("step 2:"+str(sum(l[:index])))
	#print(l[index2])
	while sum(l[:index])-l[index2] > m:
		index2 += 1
		#print("step2 :"+str(index2))

	#print("whut:"+str(sum(l[:index])-l[index2]))
	if sum(l[:index])-l[index2] == m:
		tmp = list(range(len(l[:index])))
		tmp.remove(index2)
		o.write(str(len(tmp))+"\n")
		o.write(" ".join(list(map(str, tmp))))
		sys.exit()

	# step 3
	#print("step 3")
	valueToRemove = sum(l[:index]) - m
	leftIndex = 0
	rightIndex = index2 - 1

	bestRightIndex = index2
	bestLeftIndex = index2
	bestSum = sum(l[:index])-l[index2]
	#print(valueToRemove)
	#print(rightIndex)
	#print(leftIndex)
	#print(bestSum)
	while rightIndex != leftIndex:
		#print("step3 r:"+str(rightIndex))
		#print("step3 l:"+str(leftIndex))
		#print("r+l : "+str(l[rightIndex] + l[leftIndex]))
		if l[rightIndex] + l[leftIndex] == valueToRemove:
			bestLeftIndex = leftIndex
			bestRightIndex = rightIndex
			break
		elif l[rightIndex] + l[leftIndex] > valueToRemove:
			# compare with best result
			if l[rightIndex] + l[leftIndex] > bestSum:
				bestSum = l[rightIndex] + l[leftIndex]
				bestRightIndex = rightIndex
				bestLeftIndex = leftIndex

			rightIndex -= 1
		elif l[rightIndex] + l[leftIndex] < valueToRemove:
			leftIndex += 1

	tmp = list(range(len(l[:index])))
	if bestRightIndex == bestLeftIndex:
		tmp.remove(bestRightIndex)
	else:
		tmp.remove(bestRightIndex)
		tmp.remove(bestLeftIndex)
	#print(len(tmp))
	#print(tmp)
	o.write(str(len(tmp))+"\n")
	o.write(" ".join(list(map(str, tmp))))
