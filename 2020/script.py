import sys

class Library:
	def __init__(self, id, nbL, sign, speed, books):
		self.id = id
		self.nbL = nbL
		self.sign = sign
		self.speed = speed
		self.books = books
		self.processedBooks = []
		print(f"Library created with {nbL} {sign} {speed} {books}")

def main():
	filename="a_example"
	print(f"reading from {filename}.in and exporting to {filename}.out")

	with open(filename+'.txt',"r") as i, open(filename+'.out',"w") as o:
		nbL, nbB, nbJ = [int(s) for s in i.readline().split(" ")]
		scores = [int(s) for s in i.readline().split(" ")]

		print(f"context is {nbL} {nbB} {nbJ} {scores}")

		libs = []
		for id in range(nbB):
			nbL, sign, speed = [int(s) for s in i.readline().split(" ")]
			books = [int(s) for s in i.readline().split(" ")]
			libs.append(Library(id, nbL, sign, speed, books))
		

		# code her
		librairies = [] # orderd by sign up


		o.write(str(len(librairies)))
		for lib in librairies:
			o.write(f"{lib.id} {len(lib.processedBooks)}")
			o.write(' '.join(lib.processedBooks))


if __name__ == "__main__":
    # execute only if run as a script
    main()