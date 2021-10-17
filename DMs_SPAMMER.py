import sys, subprocess, random, json, asyncio, os
from discord.ext import commands
try:
    import colorama, pyfade, discord
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'colorama'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyfade'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord.py'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord'])
from colorama import Fore
from datetime import datetime

sys.tracebacklimit = 0
bot = discord.Client()
with open('config.json') as f:
    yamete_kudasai = json.load(f)
token = yamete_kudasai['token']
cooldown = yamete_kudasai['min_cooldown']
cooldown_max = yamete_kudasai['max_cooldown']
message = yamete_kudasai['message']
duplicate = yamete_kudasai['dm_already_dmed_users']
if duplicate == "True":
    munanyo = "True"
elif duplicate == "False":
    munanyo = "False"


print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_cyan, '''
███╗   ███╗ █████╗  ██████╗ ██████╗        ██████╗ ███╗   ███╗
████╗ ████║██╔══██╗██╔════╝██╔════╝        ██╔══██╗████╗ ████║
██╔████╔██║███████║╚█████╗ ╚█████╗         ██║  ██║██╔████╔██║
██║╚██╔╝██║██╔══██║ ╚═══██╗ ╚═══██╗        ██║  ██║██║╚██╔╝██║
██║ ╚═╝ ██║██║  ██║██████╔╝██████╔╝        ██████╔╝██║ ╚═╝ ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝         ╚═════╝ ╚═╝     ╚═╝'''))
print(f'''{Fore.LIGHTWHITE_EX}                                             Made by {Fore.YELLOW}hoemotion 
{Fore.LIGHTWHITE_EX}Check out the github page for updates: {Fore.LIGHTBLUE_EX}https://github.com/hoemotion/mass-dm-discord/  
''')
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle)
    print(f'{Fore.LIGHTGREEN_EX}Logged in as: {Fore.YELLOW}"Example-User#1234" {Fore.LIGHTGREEN_EX}| ID: {Fore.YELLOW}"52525525252134"{Fore.LIGHTGREEN_EX}\nConnected with {Fore.YELLOW}{len(bot.guilds)}{Fore.LIGHTGREEN_EX} Guilds and {Fore.YELLOW}{len(bot.user.friends)} {Fore.LIGHTGREEN_EX}Friends')
    print(f'{Fore.LIGHTYELLOW_EX}[⚡] Started sending DMs to the IDs\n')

    with open("ids.json", "r") as file:
        data = json.load(file)
    with open("blacklistedids.json", "r") as file:
        blcklstdata = json.load(file)
    with open("alreadyusedids.json", "r") as file:
        penis = json.load(file)


    indx = 0
    for i in data:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        indx += 1
        chupapi = await bot.fetch_user(i)
        if chupapi.id in blcklstdata:
            print(f"{Fore.BLUE}{current_time} {Fore.BLACK}[x] Blacklisted User {Fore.YELLOW}{chupapi} {Fore.BLACK}{indx} / {len(data)}")
            await asyncio.sleep(2)
        elif munanyo == "False":
            if chupapi.id in penis:
                print(f"{Fore.BLUE}{current_time} {Fore.LIGHTMAGENTA_EX}[x] Avoiding Duplicates: {Fore.YELLOW}{chupapi} {Fore.BLACK}{indx} / {len(data)}")
                await asyncio.sleep(2)
            else:
                try:
                    await chupapi.send(message)
                    print(
                        f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[+] Sent {message} to {Fore.YELLOW}{chupapi}{Fore.LIGHTGREEN_EX} {indx} / {len(data)}")
                    await asyncio.sleep(random.randint(cooldown, cooldown_max))
                except discord.Forbidden as e:
                    if e.code == 40003:
                        print(
                            f"{Fore.LIGHTYELLOW_EX}You have been Rate Limited\nThe Code will be restarted in 45 seconds - {Fore.RED}{e}")
                        await asyncio.sleep(45)
                        os.execv(sys.executable, ['python'] + sys.argv)
                        continue
                    else:
                        print(
                            f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{chupapi}{Fore.RED} - {e} {indx} / {len(data)}")
                        await asyncio.sleep(random.randint(cooldown, cooldown_max))
                if chupapi.id not in penis:
                    await asyncio.sleep(0.01)
                    penis.append(chupapi.id)

                    with open("alreadyusedids.json", "w") as file:
                        await asyncio.sleep(0.01)
                        json.dump(penis, file)
        else:
            try:
                await chupapi.send(message)
                print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[+] Sent {message} to {Fore.YELLOW}{chupapi}{Fore.LIGHTGREEN_EX} {indx} / {len(data)}")
                await asyncio.sleep(random.randint(cooldown, cooldown_max))
            except discord.Forbidden as e:
                if e.code == 40003:
                    print(f"{Fore.LIGHTYELLOW_EX}You have been Rate Limited\nThe Code will be restarted in 45 seconds - {Fore.RED}{e}")
                    await asyncio.sleep(45)
                    os.execv(sys.executable, ['python'] + sys.argv)
                    continue
                else:
                    print(f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{chupapi}{Fore.RED} - {e} {indx} / {len(data)}")
                    await asyncio.sleep(random.randint(cooldown, cooldown_max))
            if chupapi.id not in penis:
                await asyncio.sleep(0.01)
                penis.append(chupapi.id)

                with open("alreadyusedids.json", "w") as file:
                    await asyncio.sleep(0.01)
                    json.dump(penis, file)
    input(f"{Fore.LIGHTGREEN_EX}Press Enter 5 times to close the program.")
    [input(i) for i in range(4, 0, -1)]

bot.run(token, bot = False)
