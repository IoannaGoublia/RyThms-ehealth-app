from tkinter import *   
from threading import Thread
from time import sleep,time
import socket
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import codecs
from io import BytesIO
import pyodbc
import socket
import sys
import argparse
port = 9999

def server(port):
 print("thread started..")
 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
 sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 sock.bind(('', port))
 print("Server listening on port %s" %port)
 sock.listen(2)
 conn, addr = sock.accept()

 rc = conn.recv(1000).decode('utf-8')
 conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=USER-PC\SQLEXPRESS;'
                        'Database=TestDB;'
                        'Trusted_Connection=yes;')
 cursor = conn.cursor()
 cursor.execute('SELECT * FROM TestDB.dbo.apdata')
 result = cursor.fetchall()
                       
  
# loop through the rows 
 for row in result: 
  print(row, '\n')
                          

 json_object = json.dumps( rc,ensure_ascii=False, indent=4)
 data = json.loads(rc)
                       # json_object_1=json.dumps(self.rc, sort_keys=True, indent=4)
 print(json_object)
                       # print(json_object_1)
                        


                        #with open("self_rc.json", "w") as outfile:  
                         #json.dump(self.rc,outfile, ensure_ascii=False ) 
                       
 with open('self_rc.json', 'w') as outfile:
  outfile.write("[")

  outfile.write(rc)
  outfile.write("]")
  outfile.close()
 with open('self_rc.json', 'r') as f:
              
                distros_dict = json.load(f)

                for distro in distros_dict:
                 print("TIME:",distro["Time"])
               # print("Systolic:",distro["Systolic"])
               # print("Diastolic:",distro["Diastolic"])
               # print("Pulse:",distro["Pulse"])
    
                conni = pyodbc.connect('Driver={SQL Server};'
                      'Server=USER-PC\SQLEXPRESS;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')

                cursor = conni.cursor()
                cursor.execute('SELECT * FROM TestDB.dbo.apdata')



                cursor.execute(
                 "INSERT INTO TestDB.dbo.apdata (ID, Systolic,Diastolic,Pulse, Time,Temp,Oxygen) VALUES(?,?,?,?,?,?,?)",
                    distro["ID"],distro["Systolic"],distro["Diastolic"],distro["Pulse"],distro["Time"],distro["Temp"],distro["Oxygen"]
               
                 )
                
                i=0
                if (distro["Systolic"] <120 and distro["Diastolic"] <85 and distro["Temp"] < 38 and distro["Oxygen"]>95):
                  cursor.execute("DELETE FROM TestDB.dbo.Number")
                  i=5
                  cursor.execute(
                     "INSERT INTO TestDB.dbo.Number (Number) VALUES(?)",
                      i )
                  cursor.execute('SELECT * FROM TestDB.dbo.Number')
                elif (distro["Systolic"] >120 and distro["Diastolic"] >85 and distro["Temp"] >37 and distro["Oxygen"]<95):
                  cursor.execute("DELETE FROM TestDB.dbo.Number")
                  i=9
                  cursor.execute(
                     "INSERT INTO TestDB.dbo.Number (Number) VALUES(?)",
                      i )
                  cursor.execute('SELECT * FROM TestDB.dbo.Number')
                else:
                  cursor.execute("DELETE FROM TestDB.dbo.Number")
                  i=7
                  cursor.execute(
                     "INSERT INTO TestDB.dbo.Number (Number) VALUES(?)",
                      i )
                  cursor.execute('SELECT * FROM TestDB.dbo.Number')
                conni.commit()
            
                 
              
 conn.close()
if __name__ == '__main__':
       
      
        
        server(port)
  
                        
