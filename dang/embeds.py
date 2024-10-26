"""dang$$ Embeds

This module contains Embed Content Handling
Created by: DingoMC
Cores: akka, umbry

"""
import discord
VERSION = "0.3.0"
print('Loaded Python Module: ' + __name__ + ', using version: ' + VERSION)
def PlayerJoined (player: str):
    e_title = player + ' joined'
    e_desc = None
    embed = discord.Embed(title=e_title, description=e_desc, color=0x55ff55)
    return embed
def PlayerLeft (player: str):
    e_title = player + ' left'
    e_desc = None
    embed = discord.Embed(title=e_title, description=e_desc, color=0xff5555)
    return embed
def PlayerDied (message: str):
    e_title = message
    e_desc = None
    embed = discord.Embed(title=e_title, description=e_desc, color=0x121212)
    return embed