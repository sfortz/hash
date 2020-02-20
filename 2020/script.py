import sys

class Library:
	def __init__(self, id, nbLivre, sign, speed, books, scores,prior):
		self.id = id
		self.nbLivre = nbLivre
		self.sign = sign
		self.speed = speed
		self.books = books
		self.processedBooks = []
		self.scores = scores
		self.prior = prior
		#print(f"Library created with {nbLivre} {sign} {speed} {books}")

def main(filename):
	print(f"reading from {filename}.in and exporting to {filename}.out")

	with open(filename+'.txt',"r") as i, open(filename+'.out',"w") as o:
		nbLivreTot, nbBibli, nbJour = [int(s) for s in i.readline().split(" ")]
		scoresTot = [int(s) for s in i.readline().split(" ")]

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

			prior = (sum(scores[:]) / speed) / sign

			libs.append(Library(id, nbLivre, sign, speed, books, scores,prior))
		
		librairies = [] # processed orderd by sign up

		librairies = libs
		librairies.sort(key=lambda e : e.prior,reverse=True)
		dejaVu = dict()
		for l in librairies:
			for b in l.books:
				if not dejaVu.get(b,False) :
					l.processedBooks.append(b)
					dejaVu[b] = True

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
