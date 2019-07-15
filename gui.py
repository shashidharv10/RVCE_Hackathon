from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
import Tkinter as tk
top=tk.Tk()
F=tk.Frame(top)
F.pack(fill="both")

fEntry=tk.Frame(F,border=1)
#eHello=tk.Entry(fEntry)
#eHello.pack(side="left")
#lHistory=tk.Label(fEntry,text="",foreground="steelblue")
#lHistory.pack(side="bottom",fill="x")
fEntry.pack(side="top")

#def evClear():
#    lHistory['text']=eHello.get()
#    eHello.delete(0,tk.END)

def evYT():
	driver = webdriver.Chrome('/usr/local/bin/chromedriver') 
	driver.get("https://www.youtube.com/") 
	wait = WebDriverWait(driver, 600)
def evGoo():
	driver = webdriver.Chrome('/usr/local/bin/chromedriver') 
	driver.get("https://www.google.com/") 
	wait = WebDriverWait(driver, 600)

fButtons=tk.Frame(F,relief="sunken",border=1)
bYoutube=tk.Button(fButtons,text="Youtube",command=evYT)
bYoutube.pack(side="left",padx=5,pady=2)
bGoogle=tk.Button(fButtons,text="Google",command=evGoo)
bGoogle.pack(side="left",padx=5,pady=2)
bSMS=tk.Button(fButtons,text="SMS",command=F.quit)
bSMS.pack(side="left",padx=5,pady=2)
fButtons.pack(side="top",fill="x")

F.mainloop()
