import string

def inttostring(num,base):
	digs = string.digits + string.lowercase
	ret = ''
	if num < 0:
		ret = '-'
		num = -num
	num,rem = divmod(num,base)
	while num:
		ret = digs[rem] + ret
		num,rem = divmod(num,base)
	ret = digs[rem] + ret
	return ret

if __name__ == "__main__":
	my_string = ''
	for base in range(2,17):
		my_string += '1'
		a = int(my_string,base)
		print inttostring(a*a,base)
