# import pandas


def customsplit(string):

	quoteopen = False
	weirdsep = ""
	for char in string:
		if char == '"':

			quoteopen = not quoteopen
		elif char == "," and quoteopen == False:
			weirdsep = weirdsep+"****"
		else:
			weirdsep = weirdsep+char

	return weirdsep.split("****")

def tofloat(val):

	try:
		return float(val)
	except: 
		return(val)


# gplay = pandas.read_csv ("./playStore/googleplaystore.csv")
# print (dir(gplay))
# print (gplay.Rating)

address = "./playStore/googleplaystore.csv"

def convertcsvtolist (address):

	

	table = open(address, "r")
	tb = table.read()
	table.close()

	print(type(tb))

	rows = tb.split("\n")

	headers = rows[0].strip().split(",")
	data = rows[1:]
	print(len(headers))


	lst = []

	for row in data:
		dictn = {}
		rowraw = row.strip()
		row = customsplit(rowraw)

		for col in enumerate(row):
			i,c = col
			# print(headers[i],c)
			try:
				dictn[headers[i]] = tofloat(c)
			except:
				print(len(row),row)
				print(rowraw)
				exit()

		lst.append(dictn)

	return(lst) 




outlop = convertcsvtolist(address)
print(outlop)