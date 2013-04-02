def binary_print(it,string_length=4):
	it = bin(it)[2:]
	for i in range(string_length-len(it)):
		it = '0'+it
	return it

def pbin(it):
	return binary_print(it)

if __name__ == "__main__":
	a = range(0,16)
	b = [x^2 for x in a]
	for i in a:
		print pbin(2),pbin(i),pbin(b[i]),b[i]
