import time
def compute():
	max_value = 0
	
	for x in range(999, 100, -1):
		for y in range(999, 100, -1):
			z = x * y
			z_string = str(z)
			z_r = z_string[::-1]
			if z_r == z_string and z > max_value:
				max_value = z				
	print max_value		
if __name__ == "__main__":
	
	start = time.time()
	compute()
	end = time.time()
	print str("%.4f ms" % ((end - start) * 1000))	
