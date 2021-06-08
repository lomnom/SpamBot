import pyautogui as pag
import time as t

try:
	fromFile=False
	thingToSpam=input("what do you want to spam? keep it short! (ctrl+c to specify text file)")+"\n"
except KeyboardInterrupt:
	fromFile=True
	thingToSpam=open(input("\nEnter the path to the text file, the file will be sent line by line! ").strip(), "r").read().split("\n")
	print(thingToSpam)
	quit()
print("starting keyboard control and spamming in 5")
t.sleep(1)
print("4")
t.sleep(1)
print("3")
t.sleep(1)
print("2")
t.sleep(1)
print("1")
t.sleep(1)

print("spamming! delay: 1s because whatsapp refuses to work with paster spam rates")
try:
	if fromFile:
		for line in thingToSpam:
			startTime=t.perf_counter()
			pag.typewrite(line+"\n")
			endTime=t.perf_counter()
			if not endTime-startTime<0:
				t.sleep(endTime-startTime)
	else:
		while True:
			startTime=t.perf_counter()
			pag.typewrite(thingToSpam)
			endTime=t.perf_counter()
			if not endTime-startTime<0:
				t.sleep(endTime-startTime)
except KeyboardInterrupt:
	print("\n ^C detected! stopping!")
