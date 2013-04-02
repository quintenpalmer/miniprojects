import sys

def print_array(array,max_length=2):
	for entry in array:
		for empty in range(2-len(str(entry))):
			sys.stdout.write(' ')
		sys.stdout.write(str(entry)+', ')
	sys.stdout.write('\n')

if __name__ == "__main__":
	print_array(range(20))
	print_array(range(20-1,-1,-1))
