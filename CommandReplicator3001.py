######################################################
# Windows Command Replicator 3001
######################################################
# Author: Justin Macklin
# Date: 4/8/21
# Description:
#	Tired of typing out windows commands multiple times in a row?
#	Wish you had a not so perfect and incomplete solution for this issue?
#	Look no further!!!
######################################################


import os

#Parameter
command = ""
timesRan = 0

#Ask for input
command = input("Please input your command: \n")
timesRan = int(input("Please input the total times you want the command to be ran: \n"))

#Main Process
def commandRun(command_here, timesRan_here):
	clearConsole() 
	for i in range(1,timesRan_here+1): #run the command x number of times 
		os.system(command_here)
		CommandsLeftToRun = timesRan_here - i
		print(f"-----------------------{CommandsLeftToRun} commands left----------------------")


#clears console (windows only)
def clearConsole():
	os.system("cls")


commandRun(command, timesRan)
