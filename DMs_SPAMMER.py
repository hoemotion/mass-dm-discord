import sys
import subprocess
try:
    import discord
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord.py'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord'])
from discord.ext import commands
import json
try:
    import colorama
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'colorama'])
from colorama import Fore
from datetime import datetime
import asyncio
import time
try:
    import pyfade
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyfade'])

sys.tracebacklimit = 0
bot = discord.Client()

token = input(pyfade.Fade.Horizontal(pyfade.Colors.col, f"Please enter your token>> "))
cooldown = int(input(f"{Fore.LIGHTWHITE_EX}Enter your cooldown>> "))
message = input(f"{Fore.LIGHTWHITE_EX}What Should I Send?>> ")

print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_cyan, '''

███╗   ███╗ █████╗  ██████╗ ██████╗        ██████╗ ███╗   ███╗
████╗ ████║██╔══██╗██╔════╝██╔════╝        ██╔══██╗████╗ ████║
██╔████╔██║███████║╚█████╗ ╚█████╗         ██║  ██║██╔████╔██║
██║╚██╔╝██║██╔══██║ ╚═══██╗ ╚═══██╗        ██║  ██║██║╚██╔╝██║
██║ ╚═╝ ██║██║  ██║██████╔╝██████╔╝        ██████╔╝██║ ╚═╝ ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝         ╚═════╝ ╚═╝     ╚═╝
'''))
print(f'''
{Fore.LIGHTWHITE_EX}                                             Made by {Fore.YELLOW}hoemotion 
{Fore.LIGHTWHITE_EX}Check out the github page for updates: {Fore.LIGHTBLUE_EX}https://github.com/hoemotion/mass-dm-discord/  
''')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle)
    print(f'{Fore.LIGHTGREEN_EX}Logged in as: {Fore.YELLOW}"{bot.user}" {Fore.LIGHTGREEN_EX}| ID: {Fore.YELLOW}"{bot.user.id}"{Fore.LIGHTGREEN_EX}\nConnected with {Fore.YELLOW}{len(bot.guilds)}{Fore.LIGHTGREEN_EX} Guilds and {Fore.YELLOW}{len(bot.user.friends)} {Fore.LIGHTGREEN_EX}Friends')
    print(f'{Fore.LIGHTYELLOW_EX}[⚡] Started sending DMs to the IDs\n')
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    with open("ids.json", "r") as file:
        data = json.load(file)
    with open("blacklistedids.json", "r") as file:
        blcklstdata = json.load(file)


    indx = 0
    for i in data:
        indx += 1
        chupapi = await bot.fetch_user(i)
        if chupapi.id in blcklstdata:
            print(f"{Fore.BLUE}{current_time} {Fore.BLACK}[x] Blacklisted User {Fore.YELLOW}{chupapi} {Fore.BLACK}{indx} / {len(data)}")
            await asyncio.sleep(2)
        else:
            try:
                await chupapi.send(message)
                await asyncio.sleep(cooldown)
                print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[+] Sent DM to {Fore.YELLOW}{chupapi}{Fore.LIGHTGREEN_EX} {indx} / {len(data)}")
            except discord.Forbidden as e:
                if e.code == 40003:
                    print(f"{Fore.LIGHTYELLOW_EX}You have been Rate Limited\nMass DM will be continued in 2 minutes - {Fore.RED}{e}")
                    await asyncio.sleep(120)
                    continue
                else:
                    print(f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{chupapi}{Fore.RED} - {e} {indx} / {len(data)}")
                    await asyncio.sleep(cooldown)

    input("Press Enter 5 times to close the program.")
    [input(i) for i in range(4, 0, -1)]
    raise SystemExit
bot.run(token, bot = False)
