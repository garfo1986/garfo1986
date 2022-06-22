
import time


hora = time.strftime('%H') 
minutos = time.strftime('%M') 


if int(hora) >= 19:
	print ("Time to go home") 
else:
	print (f"there are {18- int(hora)} hours and { 59-int(minutos)} minutes to go home")