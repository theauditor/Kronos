# -*- coding: utf-8 -*-
#Kronos - 0.1 [Abstract Anion] - Alpha
#Copyright Blaise M Crowly 2014 - All rights reserved
#Created at Xincoz [xincoz.com]
#GPL v3

"""This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.)"""

"""This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details."""

#Import required modules
import platform
import os
import psutil
import time
import datetime
import subprocess

#General class to handle generala operation
class General:
    #Ping handles the PING request
    def ping(self):
      #Ping responds with the platform information
      return platform.platform()


    #Execute executes the given command
    def Execute(self,Com):
      if os.system(Com) == 0:
          return "Succesful"
      else:
          return "Failed"

#Config class contains tools to edit the system configurations
class Config:
    #SetDNS sets the DNS values in resolv.conf
    def SetDNS(self,DNS):
      DNS = DNS.split(',')
      Conf = ""
      for each in DNS:
          Conf = Conf+"nameserver  "+each
          Conf = Conf + "\n"

      try:
        ResolvFile = open('/etc/resolv.conf','w')
        ResolvFile.write(Conf)
        ResolvFile.close()
        return "Done"
      except:
         return "ERROR : Could not update resolv file"

#Maintenance class contain tools related to system maintenance
class Maintain():
     #Shutsdown the system
     def Off(self):
       os.system('poweroff')
       return "Shutting Down"

     #Gets system information using psutil and return it
     def GetStatus(self):
         Response = ""
         Response = Response + "OS->  " + platform.platform() + "\n"
         Response = Response + "TIME->  " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "\n"
         Response = Response + "CPU-> CORES:" + str(psutil.cpu_count()) + "  USAGE:"+str(psutil.cpu_percent())
         Response = Response + "%  PROC:" + str(len(psutil.pids())) + "\n"
         Tem = psutil.virtual_memory() 
         Response = Response + "MEMORY->  TOTAL:" + str(Tem.used+Tem.free)+"    USED:" + str(Tem.used) + "   FREE:" + str(Tem.free)
         Response = Response + "    USAGE:" + str(Tem.percent) + "%\n"
         Tem = psutil.disk_usage('/')
         Response = Response + "DISK->  TOTAL:" + str(Tem.total) + "  USED:" + str(Tem.used)  + "  FREE:" + str(Tem.free)
         Response = Response + "  USAGE:" + str(Tem.percent) + "%\n"
         return Response

      #Start a service
     def StartService(self,Service):
         Command = "/usr/sbin/service "
         Arg     = Service  + " start"
         Execute = Command + Arg
         if os.system(Execute) == 0:
           return "Executed"
         else:
             return "System returned an error, check the command or use ssh"

     #Stop a service
     def StopService(self,Service):
         Command = "/usr/sbin/service "
         Arg     = Service  + " stop"
         Execute = Command + Arg
         if os.system(Execute) == 0:
           return "Executed"
         else:
             return "System returned an error, check the command or use ssh"
         
     #Restart a service
     def ReStartService(self,Service):
         Command = "/usr/sbin/service "
         Arg     = Service  + " restart"
         Execute = Command + Arg
         if os.system(Execute) == 0:
           return "Executed"
         else:
             return "System returned an error, check the command or use ssh"


    #Reboot the system
     def Reboot(self):
         os.system('reboot')
         return "Rebooting"

#Processes class contain tools to manage the processes
class Processes:
    #Responds after checking is a said process is runnign on the system
    def IsRunning(self,Service):
        for each in psutil.process_iter():
            if str(each.name()).lower() == Service.lower():
                return "Running @ " + each.pid
        return "Not Running"


    #responds with a list of all running processes
    def ListPS(self):
        Procs = ""
        for each in psutil.process_iter():
            Procs = Procs + each.name() + " ........................ " + str(each.pid) + "\n"
        return Procs

    #Kills the process with the given PID
    def KillPID(self,Pid):
        for each in psutil.process_iter():
            if each.pid == int(Pid):
                each.kill()
                return "Killed"
        return "No Process Found"
   #Kills all instances of the process with the given name
    def KillPS(self,Process):
        Flag = "No Such Process"
        for each in psutil.process_iter():
            if each.name().lower() == Process.lower():
                each.kill()
                Flag = "Killed"
        return Flag
