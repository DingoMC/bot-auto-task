import asyncio
import discord
import math
from dang.console import AutoUpdaterDone, AutoUpdaterExecuting
from dang.jconfig import GetChannel
from datetime import datetime
from dang.models.event import Event
VERSION = '0.2.0'
print('Loaded Python Module: ' + __name__ + ', using version: ' + VERSION)
### Sending Event Data every day once between 8am and 10am ###
def isLeap (year : int):
    if (year % 4 == 0 and year % 100 > 0) or year % 400 == 0:
        return True
    return False

def maxMonthDays (month : int, year : int):
    if isLeap(year):
        md = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return md[month - 1]
    md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return md[month - 1]

def getEaster (date: datetime):
    c_year = date.year
    a : int = c_year % 19
    b : int = math.floor(c_year / 100)
    c : int = c_year % 100
    d : int = math.floor(b / 4)
    e : int = b % 4
    f : int = math.floor((b + 8) / 25)
    g : int = math.floor((b - f + 1) / 3)
    h : int = ((19 * a) + b - d - g + 15) % 30
    i : int = math.floor(c / 4)
    k : int = c % 4
    l : int = (32 + (2 * e) + (2 * i) - h - k) % 7
    m : int = math.floor((a + (11 * h) + (22 * l)) / 451)
    p : int = (h + l - (7 * m) + 114) % 31
    return {"day": p + 1, "month": math.floor((h + l - (7 * m) + 114) / 31)}

def getPalmSunday (date: datetime, easter: dict[str, int]):
    mmd = maxMonthDays(date.month - 1, date.year)
    if easter["day"] - 7 < 1:
        return {"day": (mmd + easter["day"] - 7), "month": (easter["month"] - 1)}
    return {"day": (easter["day"] - 7), "month": easter["month"]}

def getBigThursday (date: datetime, easter: dict[str, int]):
    mmd = maxMonthDays(date.month - 1, date.year)
    if easter["day"] - 3 < 1:
        return {"day": (mmd + easter["day"] - 3), "month": (easter["month"] - 1)}
    return {"day": (easter["day"] - 3), "month": easter["month"]}

def getBigFriday (date: datetime, easter: dict[str, int]):
    mmd = maxMonthDays(date.month - 1, date.year)
    if easter["day"] - 2 < 1:
        return {"day": (mmd + easter["day"] - 2), "month": (easter["month"] - 1)}
    return {"day": (easter["day"] - 2), "month": easter["month"]}

def getBigSaturday (date: datetime, easter: dict[str, int]):
    mmd = maxMonthDays(date.month - 1, date.year)
    if easter["day"] - 1 < 1:
        return {"day": (mmd + easter["day"] - 1), "month": (easter["month"] - 1)}
    return {"day": (easter["day"] - 1), "month": easter["month"]}

def getEasterMonday (date: datetime, easter: dict[str, int]):
    mmd = maxMonthDays(date.month, date.year)
    if easter["day"] + 1 > mmd:
        return {"day": 1, "month": (easter["month"] + 1)}
    return {"day": (easter["day"] + 1), "month": easter["month"]}   

def getCorpusChristi (date: datetime, easter: dict[str, int]):
    dayValue = 60
    cm = easter["month"]
    dayValue -= (maxMonthDays(cm, date.year) - easter["day"])
    d = dayValue
    while d > 0:
        cm += 1
        d -= maxMonthDays(cm, date.year)
        if d > 0:
            dayValue = d
    return {"day": dayValue, "month": cm}

def getMovingEvents (date: datetime):
    moving_events = []
    day = date.day
    month = date.month
    easter = getEaster(date)
    palmSunday = getPalmSunday(date, easter)
    bigThursday = getBigThursday(date, easter)
    bigFriday = getBigFriday(date, easter)
    bigSaturday = getBigSaturday(date, easter)
    easterMonday = getEasterMonday(date, easter)
    corpusChristi = getCorpusChristi(date, easter)
    if easter["day"] == day and easter["month"] == month:
        moving_events.append(['moving', 'Wielkanoc'])
    if palmSunday["day"] == day and palmSunday["month"] == month:
        moving_events.append(['moving', 'Niedziela Palmowa'])
    if bigThursday["day"] == day and bigThursday["month"] == month:
        moving_events.append(['moving', 'Wielki Czwartek'])
    if bigFriday["day"] == day and bigFriday["month"] == month:
        moving_events.append(['moving', 'Wielki Piątek'])
    if bigSaturday["day"] == day and bigSaturday["month"] == month:
        moving_events.append(['moving', 'Wielka Sobota'])
    if easterMonday["day"] == day and easterMonday["month"] == month:
        moving_events.append(['moving', 'Poniedziałek Wielkanocny'])
    if corpusChristi["day"] == day and corpusChristi["month"] == month:
        moving_events.append(['moving', 'Boże Ciało'])
    return moving_events

# Main function
async def handler (client):
    d = datetime.now()
    h = d.hour
    day = d.day
    month = d.month
    if h >= 8 and h <= 10:
        print(AutoUpdaterExecuting('EVU','Sending Event info'))
        events : list = Event.select(['class', '"desc"'], {"day": day, "month": month})
        events.extend(getMovingEvents(d))
        if len(events) > 0:
            embed = discord.Embed(title='Event Notifier', description='Today\'s Events', color=0xffdd77)
            should_ping = False
            for e in events:
                if not should_ping and (str(e[0]) == 'birthday' or str(e[0]) == 'nameday'):
                    should_ping = True
                embed.add_field(name=str(e[1]), value=str(e[0]), inline=False)
            channel = client.get_channel(int(GetChannel('events')))
            content = '<@&890189861435342868>' if should_ping else None
            await channel.send(content=content, embed=embed)
        print(AutoUpdaterDone('EVU'))
        
# Task function set interval
async def interval (client):
    while True:
        await handler(client)
        await asyncio.sleep(10800)