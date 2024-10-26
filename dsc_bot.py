# Code made originally by Elektroteleinformatyko master v.4
# Import neccessary libraries
import os
import sys
from types import coroutine
try:
    # import necessary libs
    import discord
    from discord.ext import commands
    import asyncio
    from dotenv import load_dotenv
    from random import seed
    from random import randint
    # import dang$$ basic modules
    import dang.commands
    import dang.console as dcon
    import dang.jconfig as djc
    # import tasks
    from dang.tasks import *
    # import commands
    from dang.commands import *
except ImportError or ModuleNotFoundError:
    print("dang$$ > ERR  : Python -> At least 1 required module could not be found! Exiting...")
    sys.exit(1)
# Discord Token and Discord Server Name is located in .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GUILD_ID = 571982328759582741
# Login as a discord user
intents = discord.Intents.all()
client = commands.Bot(intents=intents)
# Tasks class
class BotTask:
    def __init__ (self, name : str, coro : coroutine, task : asyncio.Task):
        self.name = name
        self.coro = coro
        self.task = task
### MAIN BOT PART ###
# Slash commands
@client.slash_command(name="version",description=djc.GetCommandDescription('version'))
async def version (message):
    await dang.commands.version.main(message)
    print(dcon.ACKCommandUsed('version', str(message.author)))

# Start listening to the chat ...
@client.event
async def on_message (message : discord.Message):
    for guild in client.guilds:
        g_id = guild.id
    c_guild = client.get_guild(g_id)
    # Prevent bot from responding to his own messages
    if message.author == client.user: return

# Run when bot is initializing ...
@client.event
async def on_ready():
    # Stop tasks if there were any
    init_tasks = asyncio.all_tasks()
    for task in init_tasks:
        name = task.get_name()
        if not 'pycord' in name and name != 'Task-1':
            print(dcon.AutoUpdaterCancelled())
            task.cancel()
    seed(randint(0,255))
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(dcon.InitTitleBox())
    print(dcon.prtime() + dcon.prefix() + dcon.INI + dcon.COL + f'Server found: {guild.name} (id: {guild.id})')
    reg_functions = djc.GetCommandsList()
    print(dcon.ACKCommandsEnabled(len(reg_functions)))
    tasks : list[BotTask] = []
    tasks.append(BotTask(dang.tasks.roles.__name__, dang.tasks.roles.interval(guild), None))
    tasks.append(BotTask(dang.tasks.external.__name__, dang.tasks.external.interval(client), None))
    tasks.append(BotTask(dang.tasks.events.__name__, dang.tasks.events.interval(client), None))
    tasks.append(BotTask(dang.tasks.chat.__name__, dang.tasks.chat.interval(guild, client), None))
    for t in tasks:
        print(dcon.SetupAutoUpdater(t.name))
        t.task = asyncio.create_task(t.coro, name=t.name)
    print(dcon.ACKAutoUpdatersEnabled(len(tasks)))
    print(dcon.SetupCustomActivity())
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Automating tasks"))
    print(dcon.BotOnReady())
client.run(TOKEN)