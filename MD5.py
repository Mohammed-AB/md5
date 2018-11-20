# you can import any word list you want and it has to be hash.txt file name

import md5

counter = 1

hash = raw_input("[+] Enter the MD5 hash: ")
default = raw_input("[+] Want to use wordlist? [y/n]: ")
if default in ['y', 'yes']:
	passList = 'hash.txt'
else:
	passList = raw_input("[+] Please enter the name of wordlist to use: ")

try:
	passList = open(passList, "r")
except:
	print "\nFile Not Found."
	quit()

print "Trying password number "
for password in passList:
	filemd5 = md5.new(password.strip()).hexdigest()
	print "[%d]--> %s" % (counter, password.strip())
	counter += 1
	
	if hash == filemd5:
		print "\n[+] Match Found! \nPassword is: %s" % password
		break
	else: print "\nPassword Not Found."