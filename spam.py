import pyautogui as pag
import time as t

thingToSpam=input("what do you want to spam? keep it short! ")+"\n"
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
	while True:
		startTime=t.perf_counter()
		pag.typewrite(thingToSpam)
		endTime=t.perf_counter()
		if not endTime-startTime<0:
			t.sleep(endTime-startTime)
except KeyboardInterrupt:
	print("\n ^C detected! stopping!")
