#!/usr/bin/python2
import os, platform, time, random
sembarang = random.randint(1,3)

err_keyint = "[!] Keyboard Interrupted by User !!!"
err_invld = "[!] Error: Invalid number selected !"
err_invalid = "[!] Error: Invalid option !"
err_blank = "[!] Error: Don't leave it blank !"
err_cantcon = "[!] Error: Can't connect with Target !"
err_cantconp = '''[!] Error: Can't connect to Target's Port !
	Are You sure that Port is opened and allow connection ?
	Try to scan it with Nmap'''
err_cantfind = '''[!] Error: Can't reach Target ! Are You sure Your Target
	is Online ? Are the URL is correct ? Are You Online ?'''
err_cantbck = "[!] Error: Can't go back ! this is the main Modules !"
err_notavai = '''[!] Sorry: This Modules is currently not available right now...
	This Modules maybe Unlocked in the next Version of M-Evil Tools :)
	so...stay with Me :)'''
err_wlist = '''[!] Error: Can't open List File ! The file is too large
	or the File is not exists or corrupted !
	Please Try Again !'''
banner1 = '''
  @@@@@@@@   @@@@@@    @@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@    @@@@@@   @@@  @@@  @@@@@@@@  
  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  
  @@!       @@!  @@@  !@@       @@!       @@!  @@@  @@!  @@@  @@!  @@@  @@!  !@@  @@!       
  !@!       !@!  @!@  !@!       !@!       !@   @!@  !@!  @!@  !@!  @!@  !@!  @!!  !@!       
  @!!!:!    @!@!@!@!  !@!       @!!!:!    @!@!@!@   @!@!!@!   @!@  !@!  @!@@!@!   @!!!:!    
  !!!!!:    !!!@!!!!  !!!       !!!!!:    !!!@!!!!  !!@!@!    !@!  !!!  !!@!!!    !!!!!:    
  !!:       !!:  !!!  :!!       !!:       !!:  !!!  !!: :!!   !!:  !!!  !!: :!!   !!:       
  :!:       :!:  !:!  :!:       :!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:       
   ::       ::   :::   ::: :::   :::::::   :: ::::  ::   :::  ::::: ::   ::  :::   :: ::::  
   :        :    : :   ::  : :    :: ::   :: : ::    :   : :   : :  :    :   :::  : :: ::

             "Okay...who's Next? Your Ex? Your Crush? Your enemy?"

               ---{ FaceBroke v1 }---{ Coded by M-XacT-666 }---
'''
banner2 = '''
MM""""""""`M                            M#"""""""'M                    dP
MM  mmmmmmmM                            ##  mmmm. `M                   88
M'      MMMM .d8888b. .d8888b. .d8888b. #'        .M 88d888b. .d8888b. 88  .dP  .d8888b.
MM  MMMMMMMM 88'  `88 88'  `"" 88ooood8 M#  MMMb.'YM 88'  `88 88'  `88 88888"   88ooood8
MM  MMMMMMMM 88.  .88 88.  ... 88.  ... M#  MMMM'  M 88       88.  .88 88  `8b. 88.  ...
MM  MMMMMMMM `88888P8 `88888P' `88888P' M#       .;M dP       `88888P' dP   `YP `88888P'
MMMMMMMMMMMM                            M#########M

                "Back again for loot? am I right? Mr.Hackers ??"

                ---{ FaceBroke v1 }---{ Coded by M-XacT-666 }---
'''
banner3 = '''
   ,d8888b                         d8b                        d8b
   88P'                            ?88                        ?88
d888888P                            88b                        88b
  ?88'     d888b8b   d8888b d8888b  888888b   88bd88b d8888b   888  d88' d8888b
  88P     d8P' ?88  d8P' `Pd8b_,dP  88P `?8b  88P'  `d8P' ?88  888bd8P' d8b_,dP
 d88      88b  ,88b 88b    88b     d88,  d88 d88     88b  d88 d88888b   88b
d88'      `?88P'`88b`?888P'`?888P'd88'`?88P'd88'     `?8888P'd88' `?88b,`?888P'

    "Remember Your Karma, 'Mr.Hackers...' Use this for good reason... :)"

            ---{ FaceBroke v1 }---{ Coded by M-XacT-666 }---
'''

def clearscreen(x):
	if x == "Windows":
		os.system('CLS')
	else:
		os.system('clear')
def tidur(x):
	time.sleep(x)
def keluar():
	print ""
	print "[*] Closing Tools..."
	tidur(1)
	print "[^] Thanks for using My Tools !"
	exit()
def banner(x):
	if x == 1:
		print banner1
	elif x == 2:
		print banner2
	elif x == 3:
		print banner3
def judul():
	banner(sembarang)