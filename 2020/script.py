import sys

class Library:
	def __init__(self, nbL, sign, speed, books):
		self.nbL = nbL
		self.sign = sign
		self.speed = speed
		self.books = books
		print(f"Library created with {nbL} {sign} {speed} {books}")

def main():
	filename="a_example"
	print(f"reading from {filename}.in and exporting to {filename}.out")

	with open(filename+'.txt',"r") as i, open(filename+'.out',"w") as o:
		nbL, nbB, nbJ = [int(s) for s in i.readline().split(" ")]
		scores = [int(s) for s in i.readline().split(" ")]

		print(f"context is {nbL} {nbB} {nbJ} {scores}")

		for _ in range(nbB):
			nbL, sign, speed = [int(s) for s in i.readline().split(" ")]
			books = [int(s) for s in i.readline().split(" ")]
			Library(nbL, sign, speed, books)
		
		o.write(str(42))
		o.write(str(42))


if __name__ == "__main__":
    # execute only if run as a script
    main()