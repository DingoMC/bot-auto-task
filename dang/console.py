"""dang$$ Console

This module contains Console handling
Created by: DingoMC
Cores: akka, umbry

"""
from datetime import datetime
from requests import get
from dang.jconfig import GetObject, GetVersion

VERSION = "0.19.0"
print('Loaded Python Module: ' + __name__ + ', using version: ' + VERSION)
def CS(text : str, color : str):
    final_text = "\033[0;3"
    if color == "red" or color == "r":
        final_text += "1m"
    elif color == "green" or color == "g":
        final_text += "2m"
    elif color == "yellow" or color == "y":
        final_text += "3m"
    elif color == "blue" or color == "b":
        final_text += "4m"
    elif color == "purple" or color == "p":
        final_text += "5m"
    elif color == "cyan" or color == "c":
        final_text += "6m"
    elif color == "gray":
        final_text += "7m"
    else:
        final_text += "9m"
    final_text += text
    final_text += "\033[0;39m"
    return final_text
# dang$$ Flags
DAT = CS(' > ', "cyan")     # at
DARR = CS(' -> ', "y")      # arrow
COL = CS(' : ',"cyan")      # subseq
ACK = CS('ACK ',"g")        # ACK
RST = CS('RST ',"r")        # Reset
ERR = CS('ERR ',"r")        # Error
WARN = CS('WARN', "y")      # Warning
SET = CS('SET ',"y")        # Setup
INI = CS('INIT',"r")        # Init
DCALL = CS('CALL',"y")      # Call
TASK = CS('TASK',"p")       # Task
LST = CS('LST ',"cyan")     # Listener
LOAD = CS('LOAD',"r")       # Imports
def prtime ():
    ctime = datetime.now()
    cts = ctime.strftime("[%d/%m/%Y][%H:%M:%S]")
    return CS(cts, 'gray')
def prefix ():
    return CS(' dang$$',"r") + DAT
def ACKCommandUsed (cmd : str, executor : str):
    return prtime() + prefix() + ACK + COL + executor + ' used command ' + GetObject('prefix') + cmd
def InitTitleBox ():
    edge = CS('|',"gray")
    final = ''
    lines = []
    lines.append(CS('+====[',"gray")+CS(' dang$$ Auto',"r")+CS(' by',"c")+CS(' DingoMC ',"y")+CS(']====+',"gray"))
    lines.append(edge+CS('       Bot Version',"r")+':'+CS(' ' + GetVersion('Bot Version') + '         ',"y")+edge)
    lines.append(edge+CS('       Bot Core',"c")+':'+CS(' ' + GetVersion('Bot Core') + '              ',"c")+edge)
    lines.append(edge+CS('       dang$$ LWJGL',"r")+':'+CS(' ' + GetVersion('dang$$ LWJGL') + '        ',"r")+edge)
    lines.append(edge+CS('       Python Version',"y")+':'+CS(' ' + GetVersion('Python Version') + '     ',"y")+edge)
    lines.append(CS('+==================================+',"gray"))
    for i in range(0,len(lines),1):
        final += lines[i]
        if i < len(lines)-1:
            final += '\n'
    return final
def ACKCommandsEnabled (am : int):
    return prtime() + prefix() + ACK + COL + 'Successfully enabled ' + str(am)  + ' functions.'
def SetupAutoUpdater (conn : str):
    return prtime() + prefix() + SET + COL + 'Enabling ' + conn + ' Updater ...'
def ACKAutoUpdatersEnabled (am : int):
    return prtime() + prefix() + ACK + COL + 'Successfully enabled ' + str(am)  + ' Auto-Updaters.'
def SetupCustomActivity ():
    return prtime() + prefix() + SET + COL + 'Setting up Custom Activity ...'
def BotOnReady ():
    return prtime() + prefix() + ACK + COL + 'Bot is ready !'
def AutoUpdaterExecuting (listener : str, task : str):
    return prtime() + prefix() + TASK + COL + DCALL + DAT + CS(listener,"p") + COL + task + ' ...'
def AutoUpdaterDone (listener : str):
    return prtime() + prefix() + TASK + COL + ACK + DAT + CS(listener,"p") + COL + 'Done.'
def AutoUpdaterCancelled ():
    return prtime() + prefix() + TASK + COL + RST + DAT + 'Connection reset. Cancelling.'
def GetExternalIP ():
    return get('https://api.ipify.org').text
def ErrorServerInfo ():
    return prtime() + prefix() + TASK + COL + ERR + DAT + CS('dang.tasks.external',"p") + COL + 'Error requesting data for ' + GetObject('dns') + ' - no further information.'
def WarningNotFound (dcid : str):
    return prtime() + prefix() + TASK + COL + WARN + DAT + CS('dang.tasks.roles', "p") + COL + 'Warning: Member not found (ID = ' + dcid + ' )'
def ErrorReadingNBT():
    return prtime() + prefix() + ERR + COL + CS('dang.mccon',"b") + DARR + 'Error while reading NBT file!'
def ErrorAPI():
    return prtime() + prefix() + ERR + COL + CS('dang.mcapi', "b") + DARR + 'Error fetching data from Mojang API!'