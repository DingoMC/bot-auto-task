import discord
import asyncio
from dang.console import AutoUpdaterDone, AutoUpdaterExecuting, WarningNotFound
from dang.mcapi import GetNameByUUID
from dang.mccon import GetScore
from dang.models.mcuser import MCUser
from dang.models.mcrank import MCRank
from dang.models.parkour_rank import ParkourRank
from dang.models.etv_rank import ETVRank
VERSION = '0.2.2'
print('Loaded Python Module: ' + __name__ + ', using version: ' + VERSION)
ranks = MCRank.select(['id', 'name'])
parkour_ranks = ParkourRank.select(['id','name','min','max'])
etv_ranks = ETVRank.select(['id', 'name', 'min', 'max'])
### Updating Discord Roles (Database --> Discord) ###
# Main function to handle updating
async def updater (guild):
    data = MCUser.select(['u.dcid', 'r.id', 'u.mcuuid', 'r.name', 'u.name'], join=['MCRank'])
    for p in data:
        # Clear all roles first
        try:
            member = await guild.fetch_member(int(p[0]))
        except:
            print(WarningNotFound(p[0]))
        else:
            rank = int(p[1])
            roles = []
            for j in ranks:
                if rank != int(j[0]) and int(j[0]) > 0:
                    role = discord.utils.get(guild.roles, name=j[1])
                    if role in member.roles: roles.append(role)           
            if len(roles) > 0:
                await discord.Member.remove_roles(member, *roles)
            if rank > 0:
                rname = p[3]
                role = discord.utils.get(guild.roles, name=rname)
                if not role in member.roles: await discord.Member.add_roles(member, role)
            # Parkour Roles
            roles = []
            pa_score = GetScore('/root/minecraft_m/minigames/data/scoreboard.dat', p[4], 'parkour')
            for j in parkour_ranks:
                # Add role if needed
                if pa_score >= int(j[2]) and pa_score <= int(j[3]):
                    rname = 'Parkour ' + j[1]
                    role = discord.utils.get(guild.roles, name=rname)
                    if not role in member.roles: await discord.Member.add_roles(member, role)
                else:
                    rname = 'Parkour ' + j[1]
                    role = discord.utils.get(guild.roles, name=rname)
                    if role in member.roles: roles.append(role)   
            if len(roles) > 0:
                await discord.Member.remove_roles(member, *roles)
            # EtV Roles
            roles = []
            etv_score = GetScore('/root/minecraft_m/minigames/data/scoreboard.dat', p[4], 'ETVScore')
            for j in etv_ranks:
                # Add role if needed
                if etv_score >= int(j[2]) and etv_score <= int(j[3]):
                    rname = 'EtV ' + j[1]
                    role = discord.utils.get(guild.roles, name=rname)
                    if not role in member.roles: await discord.Member.add_roles(member, role)
                else:
                    rname = 'EtV ' + j[1]
                    role = discord.utils.get(guild.roles, name=rname)
                    if role in member.roles: roles.append(role)   
            if len(roles) > 0:
                await discord.Member.remove_roles(member, *roles)
# Task function set interval
async def interval (guild):
    while True:
        print(AutoUpdaterExecuting('DB->DC','Updating roles'))
        await updater(guild)
        print(AutoUpdaterDone('DB->DC'))
        await asyncio.sleep(600)