import sys

class Library:
	def __init__(self, id, nbLivre, sign, speed, books):
		self.id = id
		self.nbLivre = nbLivre
		self.sign = sign
		self.speed = speed
		self.books = books
		self.processedBooks = []
		#print(f"Library created with {nbLivre} {sign} {speed} {books}")

def main():
	filename="a_example"
	#filename="b_read_on"
	#filename="c_incunabula"
	#filename="d_tough_choices"
	#filename="e_so_many_books"
	#filename="f_libraries_of_the_world"
	print(f"reading from {filename}.in and exporting to {filename}.out")

	with open(filename+'.txt',"r") as i, open(filename+'.out',"w") as o:
		nbLivreTot, nbBibli, nbJour = [int(s) for s in i.readline().split(" ")]
		scores = [int(s) for s in i.readline().split(" ")]

		#print(f"context is {nbLivreTot} {nbBibli} {nbJour} {scores}")

		libs = []  # librairies lue
		for id in range(nbBibli):
			nbLivre, sign, speed = [int(s) for s in i.readline().split(" ")]
			books = [int(s) for s in i.readline().split(" ")]
			libs.append(Library(id, nbLivre, sign, speed, books))
		

		# code her
		librairies = [] # processed orderd by sign up

		librairies = libs
		librairies.sort(key=lambda e : e.speed,reverse=True)
		for l in librairies:
			l.processedBooks = l.books


		o.write(str(len(librairies))+"\n")
		for lib in librairies:
			o.write(f"{lib.id} {len(lib.processedBooks)}\n")
			o.write(' '.join(map(str,lib.processedBooks))+"\n")


if __name__ == "__main__":
    # execute only if run as a script
    main()