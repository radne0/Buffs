import time
import os
import re
import pydirectinput as kb
import pyperclip as cb
import datetime as dt
from boltons.setutils import IndexedSet



''' A basic buff bot.
logfile - path to eq log file to monitor for buff requests. eg:  /Everquest/logs/eqlog_Fluffy_mangler.txt
buffs - dictionary  in the form:  "bufftriggertext":(gem_slot,casttime)
regex - buff request format.  player_name requesting buff and buff text should be grouped in that order.
'''

class BuffBot:
    #configure buff bot
    def __init__(self, logfile,buffs,regex):
       print(regex)
       self.logfile = logfile
       self.bufflist = buffs
       self.rx = re.compile(regex)
       self.buffq = IndexedSet()      # Actual QUEUE.
       self.windowName = "EverQuest"

    #display configuration   
    def displayconfig(self):
        print("Bot Configuration")
        print("Reading Log file: ", self.logfile)
        print("Current Buff list")
        for key in self.bufflist:
            print("buff trigger:",key,"\tgem slot: ",self.bufflist[key][0],'\tcast time:',self.bufflist[key][1])
            
    #def checkWindow(self):
    #    hwnd = w32.GetForegroundWindow()
    #    name = w32.GetWindowText(hwnd)
    #    return self.windowName == name
     
    def MatchFound(self,name,request):

           try:
               print(str(dt.datetime.now())[0:19], name, "requested", request)
               self.ProcessRequest(name,request,self.bufflist[request])
                                                   
           except KeyError:   #ignore non-buff requests.
               print(str(dt.datetime.now())[0:19],"Unknown request from",name, "ignored:", request)
               pass
       
   # build the macro for this buff and execute it.            
    def ProcessRequest(self,name,request,spellinfo):
        gem = spellinfo[0]
        casttime = spellinfo[1]
        castline =["/tar " + name, "/cast " + str(gem), "/cast " + str(gem),"/cast " + str(gem),"/cast " + str(gem)]
        print(str(dt.datetime.now())[0:19],'casting',request,'on',name,'from spell slot',gem, 'with cast time ',casttime,'seconds.')            
        
        for lines in castline:
            print(lines)
            self.enterline(lines)               
            time.sleep(0.5)
        time.sleep(float(casttime))
        self.enterline("/sit")
        print(str(dt.datetime.now())[0:19],"Request completed.")
       
    # copy each line to clipboard and paste into EQ.
    def enterline(self,cmd):
        cb.copy(cmd)
        kb.press("enter", _pause=False)
        kb.keyDown("ctrl", _pause=False)
        kb.press("v", _pause=False)
        kb.keyUp("ctrl", _pause=False)
        kb.press("enter", _pause=False)


   # wait for a valid buff request from a player.          
    def listen(self):
       with open(self.logfile) as f:
             f.seek(0, os.SEEK_END)
             time.sleep(2)
             print("Listening for buff requests")
             while True:
                 txt=''
                 line = f.readline()

                 if line:
                     #print("raw line: " + line)
                     s = line.split()       # get rid of time stamps
                     txt = " ".join(s[5:])
                     txt = txt.lower()
                     m = self.rx.match(txt)
                     if m:
                         self.MatchFound(m.group(1),m.group(2))
                 time.sleep(0.3)






  
