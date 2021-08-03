import socket
import time
import random
import json
from random import seed
from datetime import datetime
import pytz
# create TCP/IP socket



from tkinter import *

window = Tk()

window.title("Welcome to e-health Tracker")

window.geometry('350x200')

lbl = Label(window, text="Hello",bg="blue")

lbl.grid(column=0, row=0)

def clicked():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    i=0
# retrieve local hostname
    local_hostname = socket.gethostname()

# get fully qualified hostname
    local_fqdn = socket.getfqdn()

# get the according IP address
    ip_address = socket.gethostbyname(local_hostname)

# bind the socket to the port 23456, and connect
    server_address = (ip_address, 9999)
    sock.connect(server_address)
    print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))


    IDi = random.randint(1,100)
    Systolici = random.randint(110,140)
    Diastolici =random.randint(70,120)
    Pulsei= random.randint(60,100)
    Timei= time.asctime(time.localtime(time.time()))
    Tempi= random.randint(34,40)
    Oxygeni=random.randint(90,105)

    records ={
     "ID": 12,
     "Systolic":Systolici,
     "Diastolic":Diastolici,
     "Pulse": Pulsei ,
     "Time": Timei,
     "Temp":Tempi,
     "Oxygen":Oxygeni
     }



  
# Using list comprehension 
# Get values of particular key in list of dictionaries 

    print('mesure',records)
    json_object = json.dumps( records, indent=4)
    print("json",json_object)
    lbl.configure(text=str(json_object))
#for entry in records:
# print (" %s" % records[entry])
#new_data = ( "%s" % records).encode("utf-8")
    new_data = ( "%s" % json_object).encode("utf-8")
    sock.sendall(new_data)
 
    # wait for two seconds
#selfy = sock.recv(1024)
#print(str(selfy))
    time.sleep(2)

# close connection
    sock.close()

   

btn = Button(window, text="New Measurement",bg="yellow", command=clicked)

btn.grid(column=1, row=0)

window.mainloop()
