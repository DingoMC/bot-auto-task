import asyncio
from dang.console import AutoUpdaterDone, AutoUpdaterExecuting, ErrorServerInfo
from dang.jconfig import GetChannel
from dang.models.mcserverinfo import MCServerInfo
VERSION = '0.2.3'
print('Loaded Python Module: ' + __name__ + ', using version: ' + VERSION)
### Updating External Info (TCP --> Discord) ###
# Main function to handle updating
async def updater (client):
    data = MCServerInfo.select(['latency', 'players', 'players_max', 'version'], {"dns": "dingo-mc.net"})
    if len(data) == 0:
        print(ErrorServerInfo())
        return
    channel_name = 'Version: ' + str(data[0][3])
    channel = client.get_channel(int(GetChannel('version')))
    await channel.edit(name=channel_name)
    channel_name = 'Players: ' + str(data[0][1]) + ' / ' + str(data[0][2])
    channel = client.get_channel(int(GetChannel('players')))
    await channel.edit(name=channel_name)
    channel_name = 'Ping: ' + str(data[0][0]) + 'ms'
    channel = client.get_channel(int(GetChannel('ping')))
    await channel.edit(name=channel_name)
    print(AutoUpdaterDone('TCP->DC'))
        
# Task function set interval
async def interval (client):
    while True:
        print(AutoUpdaterExecuting('TCP->DC','Updating info channels'))
        await updater(client)
        await asyncio.sleep(600)