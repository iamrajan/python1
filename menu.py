#!/usr/bin/python

import time
import webbrowser
import os
menu='''
press 1 to check current time and date:
press 2 to scan all your mac address in your current connection networks:
press 3 to shutdown the system:
press 4 to search something on google:
press 5 to logout your current machine:
press 6 to shutdown all connected system in your current network:
press 7 to update status on fb;
press 8 to list ip address of given website:
'''
print menu
choice=raw_input()

if choice == '1' :
	print "current date and time is: " , time.ctime()  
elif choice == '2' :
	print "mac address is: " 
elif choice == '3' :
	print "byeeeee"
elif choice == '4' :
	find=raw_input("enter query:")
	webbrowser.open_new_tab("http://www.google.com/search?q="+find)
