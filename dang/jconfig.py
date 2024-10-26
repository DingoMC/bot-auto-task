"""dang$$ JSON Config

This module contains JSON Config file handling
Created by: DingoMC
Cores: akka, umbry

"""
import json
VERSION = "0.12.0"
print('Loaded Python Module: ' + __name__ + ', using version: ' + VERSION)
def GetList (name : str):
    data = json.load(open('bot-config.json'))
    return data[name]
def GetObject (name : str):
    data = json.load(open('bot-config.json'))
    return str(data[name])
def GetCommandsList ():
    data = json.load(open('bot-config.json'))
    cmd = data['commands']
    command_list : list[str] = []
    for i in cmd:
        command_list.append(str(i['name']))
    return command_list
def GetCommandDescription (command : str):
    data = json.load(open('bot-config.json'))
    cmd = data['commands']
    for i in cmd:
        if str(i['name']) == command: return str(i['description'])
    return None
def GetCommandAliases (command : str):
    data = json.load(open('bot-config.json'))
    cmd = data['commands']
    for i in cmd:
        if str(i['name']) == command: return i['aliases']
    return None
def GetCommandArgs (command : str):
    data = json.load(open('bot-config.json'))
    cmd = data['commands']
    arg_list : list[str] = []
    for i in cmd:
        if str(i['name']) == command:
            if i['arguments'] is None: return None
            for j in i['arguments']:
                arg_list.append(str(j['name']))
    return arg_list
def GetArgumentDescription (command : str, argument : str):
    data = json.load(open('bot-config.json'))
    cmd = data['commands']
    for i in cmd:
        if str(i['name']) == command:
            for j in i['arguments']:
                if str(j['name']) == argument:
                    return str(j['description'])
    return None
def IsArgumentRequired (command : str, argument : str):
    data = json.load(open('bot-config.json'))
    cmd = data['commands']
    for i in cmd:
        if str(i['name']) == command:
            for j in i['arguments']:
                if str(j['name']) == argument:
                    return (j['required'] == "true")
    return False
def CheckCommand (command : str, content : str):
    if content == (GetObject('prefix') + command): return True
    aliases = GetCommandAliases(command)
    if aliases is not None:
        for a in aliases:
            if content == (GetObject('prefix') + a): return True
    return False
def GetVersionNames ():
    data = json.load(open('bot-config.json'))
    cmd = data['versions']
    ver_list : list[str] = []
    for i in cmd:
        ver_list.append(str(i['name']))
    return ver_list
def GetVersion (name : str):
    data = json.load(open('bot-config.json'))
    ver = data['versions']
    for i in ver:
        if str(i['name']) == name: return str(i['type'])
    return None
def GetChannel (name : str):
    data = json.load(open('bot-config.json'))
    return str(data['channels'][name])
