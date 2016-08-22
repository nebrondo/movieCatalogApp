import urllib
def check_text():
	quotes = open("email.txt")
	contents = quotes.read()
	hash1 = hash(contents)
	quotes2 = open("email2.txt")
	contents2 = quotes2.read()
	hash2 = hash(contents2)
	print('Quotes: ' + str(contents))
	print('Quotes2:' + str(contents2))
	if hash1 <> hash2:

		print('Hello!', 'Files are different!!!', 1)
	else:
		print('Hello!', 'Files are equal!!!', 1)
	quotes.close()
	quotes2.close()
	convert_pirate(contents)

def convert_pirate(text_to_check):
        connection = urllib.urlopen("http://isithackday.com/arrpi.php?text=" + text_to_check)
        output = connection.read()
        print(output)
        connection.close()


check_text()
