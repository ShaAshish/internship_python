#!/usr/bin/python2
import os
import webbrowser
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

print("Press 1 for check date and time")
print("Press 2 to create a new file")
print("Press 3 to create a new directory")
print("Press 4 to serach something on google")
print("Press 5 to logout")
print("Press 6 to shutdown OS")
print("Press 7 to check internet connection")
print("Press 8 to login to whatsapp")		
print("Press 9 to find IP of devices connected to internet of system")
print("Press 0 to exit")

c=int(raw_input("Please enter your choice:"))	
if c==1:
	os.system('date')
elif c==2:
	file_name = raw_input("Enter the file name: ")
	f_path = raw_input("Enter the location where you want to create file: ")
	cmd = 'touch '+f_path+'/'+file_name
	os.system(cmd)
elif c==3:
	dir_name = raw_input("Enter the directory name: ")
	d_path = raw_input("Enter the location where you want to create directory: ")
	cmd='mkdir '+d_path+'/'+dir_name
	os.system(cmd)
elif c==4:
	key = raw_input("Enter the keyword you want to search:")
	webbrowser.open_new_tab('https://www.google.com/search?q='+key)
elif c==5:
	os.system(' gnome-session-quit')
elif c==6:
	os.system('sudo shutdown -h now')
elif c==7:
	if os.system('ping -q -c 1 -W 1 google.com >/dev/null'):
	  print("The internet connection is not working")
	else:
	  print("The internet connection is working")
elif c==8:
	print("logging to whatsapp...")
	driver = webdriver.Firefox()
	driver.get('http://web.whatsapp.com')
	print('Please Scan the QR Code and press enter')
elif c==9:
	print("IP address of computer connected to this computer are ...")
	os.system('nmap -sn 192.168.150.129/24')
else:
	print("Wrong input")

