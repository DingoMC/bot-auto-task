import subprocess
import select
import asyncio
import re
from dang.jconfig import GetChannel
from dang.embeds import PlayerJoined, PlayerLeft, PlayerDied
VERSION = '0.1.0'
print('Loaded Python Module: ' + __name__ + ', using version: ' + VERSION)

f = subprocess.Popen(['tail', '-F', '/root/minecraft_m/logs/latest.log'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p = select.poll()
p.register(f.stdout)

### Sending ingame chat to Discord chat ###
# Main function to handle updating
async def updater (guild, client):
    if p.poll(1):
        line = f.stdout.readline().decode("utf-8")
        # Do not show warnings or errors on chat
        if line.find('WARN', 0, 31) != -1 or line.find('ERROR', 0, 32) != -1:
            return
        if re.search('(?:[0-9]{1,3}\.){3}[0-9]{1,3}', line) is not None:
            return
        # Remove time
        line = re.sub('\[[0-9]{2}\:[0-9]{2}\:[0-9]{2}\]\s', '', line)
        # Remove debug info
        line = line.replace('[Server thread/INFO]:', '', 1)
        # Remove color coding
        line = re.sub('\u00A7[\dA-Fa-flmno]', '', line)
        is_chat = False
        if re.search('[\<\[]{2}', line) is not None:
            is_chat = True
        channel = client.get_channel(int(GetChannel('ingame_chat')))
        if is_chat == False:
            # Remove joined/left the game
            if re.search('(left|joined)\sthe\sgame', line) is not None:
                return
            # Faster is user authenticator and lost connection
            if line.find('lost connection') != -1:
                playername = line.split(' ')[1]
                await channel.send(content=None, embed=PlayerLeft(playername))
                return
            if line.find('User Authenticator') != -1:
                playername = line.split(' ')[6]
                await channel.send(content=None, embed=PlayerJoined(playername))
                return
            # If someone dies
            death_words = ['pricked', 'drowned', 'died', 'killed', 'blew up', 'blown up', 'hit the ground',
                           'fell from', 'fell off', 'fell while', 'doomed to fall', 'was impaled', 'was squashed',
                           'in flames', 'into fire', 'burned to', 'went off', 'in lava', 'struck by', 'was lava',
                           'danger zone', 'was kileld by', 'froze to', 'was slain by', 'was stung', 'was shot',
                           'was pummeled', 'was fireballed', 'starved to', 'suffocated in', 'was squished',
                           'was poked', 'fell out', 'the same world', 'withered away']
            for d in death_words:
                if line.find(d) != -1:
                    await channel.send(content=None, embed=PlayerDied(line))
                    return
            return
        await channel.send(content=line)

# Task function set interval
async def interval (guild, client):
    while True:
        await updater(guild, client)
        await asyncio.sleep(1)