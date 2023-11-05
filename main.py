from os import system
mytitle = "3SP DC-Cloner - Developed by 3spC0d3x"
system("title "+mytitle)
import psutil
import time
import sys
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}

 .d8888b.   .d8888b.  8888888b.       8888888b.   .d8888b.          .d8888b.  888                                    
d88P  Y88b d88P  Y88b 888   Y88b      888  "Y88b d88P  Y88b        d88P  Y88b 888                                    
     .d88P Y88b.      888    888      888    888 888    888        888    888 888                                    
    8888"   "Y888b.   888   d88P      888    888 888               888        888  .d88b.  88888b.   .d88b.  888d888 
     "Y8b.     "Y88b. 8888888P"       888    888 888               888        888 d88""88b 888 "88b d8P  Y8b 888P"   
888    888       "888 888             888    888 888    888 888888 888    888 888 888  888 888  888 88888888 888     
Y88b  d88P Y88b  d88P 888             888  .d88P Y88b  d88P        Y88b  d88P 888 Y88..88P 888  888 Y8b.     888     
 "Y8888P"   "Y8888P"  888             8888888P"   "Y8888P"          "Y8888P"  888  "Y88P"  888  888  "Y8888  888

{Style.RESET_ALL}
                                                {Fore.MAGENTA}Developed by: 3spC0d3x.{Style.RESET_ALL}
        """)
token = input(f'Please enter your token:\n >')
guild_s = input('Please enter guild id you want to copy:\n >')
guild = input('Please enter guild id where you want to copy:\n >')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Logged In as : {client.user}")
    print("Cloning Server")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}


 $$$$$$\  $$\       $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  
$$  __$$\ $$ |     $$  __$$\ $$$\  $$ |$$  _____|$$  __$$\ 
$$ /  \__|$$ |     $$ /  $$ |$$$$\ $$ |$$ |      $$ |  $$ |
$$ |      $$ |     $$ |  $$ |$$ $$\$$ |$$$$$\    $$ |  $$ |
$$ |      $$ |     $$ |  $$ |$$ \$$$$ |$$  __|   $$ |  $$ |
$$ |  $$\ $$ |     $$ |  $$ |$$ |\$$$ |$$ |      $$ |  $$ |
\$$$$$$  |$$$$$$$$\ $$$$$$  |$$ | \$$ |$$$$$$$$\ $$$$$$$  |
 \______/ \________|\______/ \__|  \__|\________|\_______/ 
                                                           
                                                           
                                                           


    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    await client.close()


client.run(token, bot=False)
