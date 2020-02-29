import sys

"""
L'idée est de donner un score à chaque librairie et de les trier sur base de ce score.
Les livres de chaque librairie son uniquement trié par ordre de va décroissane et les doublon sont retiré sur les dernier livres.
"""

class Library:
	def __init__(self, id, nbLivre, sign, speed, books, scores,prior):
		self.id = id
		self.nbLivre = nbLivre
		self.sign = sign
		self.speed = speed
		self.books = books
		self.processedBooks = []
		self.processedBooksScores = []
		self.scores = scores
		self.prior = prior
		#print(f"Library created with {nbLivre} {sign} {speed} {books}")

def genPriority(scores,speed,sign):
	return (sum(scores[:]) / speed) / sign
	#return sum(scores[:]) + (1/speed) * 1000 + (1/sign) * 1000000

def main(filename):
	print(f"reading from {filename}.in and exporting to {filename}.out")

	with open(filename+'.txt',"r") as i, open(filename+'.out',"w") as o:
		nbLivreTot, nbBibli, nbJour = [int(s) for s in i.readline().split(" ")]
		scoresTot = [int(s) for s in i.readline().split(" ")]
		print(sum(scoresTot))
		maxScore = max(scoresTot)
		minScore = min(scoresTot)

		#print(f"context is {nbLivreTot} {nbBibli} {nbJour} {scoresTot}")

		libs = []  # librairies lue
		for id in range(nbBibli):
			nbLivre, sign, speed = [int(s) for s in i.readline().split(" ")]
			books = [int(s) for s in i.readline().split(" ")]
			scores = [0] * nbLivre
			for z in range(nbLivre):
				scores[z] = scoresTot[books[z]]

			orderedZipped = list(zip(books,scores))
			orderedZipped.sort(key=lambda e : e[1],reverse=True)
			oredered = list(zip(*orderedZipped))
			books = list(oredered[0])
			scores = list(oredered[1])

			#nbLivresProcessed = min((nbJour - sign), nbLivre) * speed
			#prior = sum(scores[:nbLivresProcessed])

			#w = [x ** 0.2 for x in range(len(scores))] #weights
			#prior = (sum([ _x * _w for _x, _w in zip( scores, w[::-1] ) ]) / speed) / sign 
			
			prior = genPriority(scores,speed,sign)
			
			libs.append(Library(id, nbLivre, sign, speed, books, scores,prior))
		
		librairies = [] # processed orderd by sign up

		librairies = libs
		librairies.sort(key=lambda e : e.prior,reverse=True)
		dejaVu = dict()
		for l in librairies:
			for idx,b in enumerate(l.books):
				if not dejaVu.get(b,False) :
					l.processedBooks.append(b)
					l.processedBooksScores.append(l.scores[idx])
					dejaVu[b] = True
			l.prior = genPriority(l.processedBooksScores,speed,sign)

		#retirer les librairies qui n'ont pas de livres.
		librairies = list(filter(lambda l: len(l.processedBooks) != 0, librairies))

		o.write(str(len(librairies))+"\n")
		for lib in librairies:
			o.write(f"{lib.id} {len(lib.processedBooks)}\n")
			o.write(' '.join(map(str,lib.processedBooks))+"\n")


if __name__ == "__main__":
    # execute only if run as a script
	for filename in ["a_example","b_read_on","c_incunabula","d_tough_choices","e_so_many_books","f_libraries_of_the_world"]:
		main(filename)
