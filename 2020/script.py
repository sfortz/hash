import sys

filename="a_example"

with open(filename+'.in',"r") as i, open(filename+'.out',"w") as o:
	m , n = [int(s) for s in i.readline().split(" ")]
	l = [int(s) for s in i.readline().split(" ")]
	
	o.write(str(42))
	o.write(str(42))
