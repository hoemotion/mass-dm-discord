import sys, subprocess, random, json, asyncio, os, time
try:
    import colorama, pyfade, discord
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'colorama'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyfade'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord.py'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord'])
from colorama import Fore
from datetime import datetime
from discord.ext import commands
def error_msg():
    print(pyfade.Fade.Horizontal(pyfade.Colors.purple_to_red, """Bruhhhh\nSeems like you\'re new to Python and/or JSON..\nJoin the Support-Server and lemme help you :)\nhttps://discord.gg/verQuxaBqy"""))
    time.sleep(10)
    input(f"{Fore.YELLOW}Press Enter to exit the script")
    raise SystemExit
sys.tracebacklimit = 0
bot = discord.Client()
with open("tokens.json", "r") as file:
    tokens = json.load(file)
with open("alrdyusedtokens.json", "r") as file:
    tokenscheck = json.load(file)
unused_tokens = []
if len(tokens) == 0:
    print("No Tokens were found\nScript is closing")
    raise SystemExit
for tkn in tokens:
    if tkn in tokenscheck:
        pass
    else:
        unused_tokens.append(tkn)
if len(unused_tokens) != 0:
    token = random.choice(unused_tokens)
    tokenscheck.append(token)
    with open("./alrdyusedtokens.json", "w", encoding='utf-8') as file:
        json.dump(tokenscheck, file)
else:
    reset = []
    with open('./alrdyusedtokens.json', 'w', encoding='utf-8') as f:
        json.dump(reset, f, ensure_ascii=False, indent=4)
    print("Resetting already used tokens")
    time.sleep(5)
    os.execv(sys.executable, ['python'] + sys.argv)

with open('config.json') as f:
    yamete_kudasai = json.load(f)
cooldown = yamete_kudasai['min_cooldown']
cooldown_max = yamete_kudasai['max_cooldown']
display_sleep = yamete_kudasai['display_sleep']
message = yamete_kudasai['message']
dm_limit = yamete_kudasai['dm_each_token']
always_sleep = yamete_kudasai['sleep_on_exception']
duplicate = yamete_kudasai['dm_already_dmed_users']
fetch_users = yamete_kudasai['always_fetch_users']
send_embed = yamete_kudasai['send_embed']
embed_title = yamete_kudasai['embed_title']
embed_description = yamete_kudasai['embed_description']
embed_author = yamete_kudasai['embed_author']
embed_footer = yamete_kudasai['embed_footer']
embed_footer_icon_url = yamete_kudasai['embed_footer_icon_url']
embed_thumbnail_url = yamete_kudasai['embed_thumbnail_url']
embed_image_url = yamete_kudasai['embed_image_url']
embed_author_icon_url = yamete_kudasai['embed_author_icon_url']
if duplicate == "True":
    munanyo = "True"
elif duplicate == "False":
    munanyo = "False"
else:
    munanyo = "False"
async def mass_dm():
    with open("ids.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    with open("blacklistedids.json", "r", encoding='utf-8') as file:
        blcklstdata = json.load(file)
    indx = 0
    success = 0
    for i in data:
        with open("alreadyusedids.json", "r", encoding='utf-8') as file:
            penis = json.load(file)
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        indx += 1
        if int(i) in blcklstdata:
            if fetch_users == "False":
                print(f"{Fore.BLUE}{current_time} {Fore.BLACK}[x] Blacklisted User {Fore.YELLOW}{i} {Fore.BLACK}{indx} / {len(data)}")
            elif fetch_users == "True":
                chupapi = await bot.fetch_user(i)
                print(f"{Fore.BLUE}{current_time} {Fore.BLACK}[x] Blacklisted User {Fore.YELLOW}{chupapi} {Fore.BLACK}{indx} / {len(data)}")
                print(f"{Fore.YELLOW}Sleeping 2 seconds")
                await asyncio.sleep(2)
            else:
                print(f"{Fore.RED}[FETCH USERS ERROR]")
                error_msg()
        elif munanyo == "False":
            if int(i) in penis:
                if fetch_users == "False":
                    print(f"{Fore.BLUE}{current_time} {Fore.LIGHTMAGENTA_EX}[x] Avoiding Duplicates: {Fore.YELLOW}{i} {Fore.BLACK}{indx} / {len(data)}")
                elif fetch_users == "True":
                    chupapi = await bot.fetch_user(i)
                    print(f"{Fore.BLUE}{current_time} {Fore.LIGHTMAGENTA_EX}[x] Avoiding Duplicates: {Fore.YELLOW}{chupapi} {Fore.BLACK}{indx} / {len(data)}")
                    print(f"{Fore.YELLOW}Sleeping 2 seconds")
                    await asyncio.sleep(2)
                else:
                    print(f"{Fore.RED}[FETCH USERS ERROR]")
                    error_msg()
            else:
                chupapi = await bot.fetch_user(i)
                try:
                    await chupapi.send(message.replace('user_id', f'{chupapi.id}').replace('user_name', f'{chupapi.name}').replace('user_mention', f'<@{chupapi.id}>').replace('user_discriminator', f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'))
                    print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[+] Sent {message} to {Fore.YELLOW}{chupapi}{Fore.LIGHTGREEN_EX} {indx} / {len(data)}")
                    pablo = random.randint(cooldown, cooldown_max)
                    success += 1
                    if success >= dm_limit:
                        print(f"{Fore.BLUE}{current_time} {Fore.LIGHTCYAN_EX}[?] DM Limit has been reached: {Fore.YELLOW}{dm_limit} DMs {Fore.LIGHTCYAN_EX}(Switching the token in 1 second)")
                        await asyncio.sleep(1)
                        os.execv(sys.executable, ['python'] + sys.argv)
                    if display_sleep == "True":
                          print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                    else:
                        pass
                    await asyncio.sleep(pablo)
                except discord.Forbidden as e:
                    if e.code == 40003:
                        print(
                            f"{Fore.LIGHTYELLOW_EX}You have been Rate Limited\nThe Code will be restarted in 90 seconds - {Fore.RED}{e}")
                        await asyncio.sleep(90)
                        os.execv(sys.executable, ['python'] + sys.argv)
                        continue
                    else:
                        print(
                            f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{chupapi}{Fore.RED} - {e} {indx} / {len(data)}")
                        pablo = random.randint(cooldown, cooldown_max)
                        if always_sleep == "True":
                            if display_sleep == "True":
                                print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                            await asyncio.sleep(pablo)
                except discord.HTTPException as e:
                    print(f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t fetch {Fore.YELLOW}{i}{Fore.RED} - {e} {indx} / {len(data)}")
                if chupapi.id not in penis:
                    await asyncio.sleep(0.01)
                    penis.append(chupapi.id)
                    with open("alreadyusedids.json", "w") as file:
                        await asyncio.sleep(0.01)
                        json.dump(penis, file)
        else:
            try:
                chupapi = await bot.fetch_user(i)
                await chupapi.send(message.replace('user_id', f'{chupapi.id}').replace('user_name', f'{chupapi.name}').replace('user_mention', f'<@{chupapi.id}>').replace('user_discriminator', f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'))
                print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[+] Sent {message} to {Fore.YELLOW}{chupapi}{Fore.LIGHTGREEN_EX} {indx} / {len(data)}")
                pablo = random.randint(cooldown, cooldown_max)
                success += 1
                if success >= dm_limit:
                    print(f"{Fore.BLUE}{current_time} {Fore.LIGHTCYAN_EX}[?] DM Limit has been reached: {Fore.YELLOW}{dm_limit} DMs {Fore.LIGHTCYAN_EX}(Switching the token in 1 second)")
                    await asyncio.sleep(1)
                    os.execv(sys.executable, ['python'] + sys.argv)
                if display_sleep == "True":
                    print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                else:
                    pass
                await asyncio.sleep(pablo)
            except discord.Forbidden as e:
                if e.code == 40003:
                    print(f"{Fore.LIGHTYELLOW_EX}You have been Rate Limited\nThe Code will be restarted in 90 seconds - {Fore.RED}{e}")
                    await asyncio.sleep(90)
                    os.execv(sys.executable, ['python'] + sys.argv)
                    continue
                else:
                    print(f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{chupapi}{Fore.RED} - {e} {indx} / {len(data)}")
                    pablo = random.randint(cooldown, cooldown_max)
                    if always_sleep == "True":
                        if display_sleep == "True":
                            print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                        await asyncio.sleep(pablo)
            except discord.HTTPException as e:
                print(f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t fetch {Fore.YELLOW}{i}{Fore.RED} - {e} {indx} / {len(data)}")
            if chupapi.id not in penis:
                penis.append(chupapi.id)
                with open("alreadyusedids.json", "w") as file:
                    json.dump(penis, file)
    input(f"{Fore.LIGHTGREEN_EX}Press Enter 5 times to close the program.")
    [input(i) for i in range(4, 0, -1)]
    print("Goodbye!\nhttps://github.com/hoemotion/mass-dm-discord Don\'t forget to leave a star!!")
    await sys.exit()
async def mass_dm_embed():
    with open("ids.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    with open("blacklistedids.json", "r", encoding='utf-8') as file:
        blcklstdata = json.load(file)
    indx = 0
    success = 0
    for i in data:
        with open("alreadyusedids.json", "r", encoding='utf-8') as file:
            penis = json.load(file)
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        indx += 1
        if int(i) in blcklstdata:
            if fetch_users == "False":
                print(f"{Fore.BLUE}{current_time} {Fore.BLACK}[x] Blacklisted User {Fore.YELLOW}{i} {Fore.BLACK}{indx} / {len(data)}")
            elif fetch_users == "True":
                chupapi = await bot.fetch_user(i)
                print(f"{Fore.BLUE}{current_time} {Fore.BLACK}[x] Blacklisted User {Fore.YELLOW}{chupapi} {Fore.BLACK}{indx} / {len(data)}")
                print(f"{Fore.YELLOW}Sleeping 2 seconds")
                await asyncio.sleep(2)
            else:
                print(f"{Fore.RED}[FETCH USERS ERROR]")
                error_msg()
        elif munanyo == "False":
            if int(i) in penis:
                if fetch_users == "False":
                    print(f"{Fore.BLUE}{current_time} {Fore.LIGHTMAGENTA_EX}[x] Avoiding Duplicates: {Fore.YELLOW}{i} {Fore.BLACK}{indx} / {len(data)}")
                elif fetch_users == "True":
                    chupapi = await bot.fetch_user(i)
                    print(f"{Fore.BLUE}{current_time} {Fore.LIGHTMAGENTA_EX}[x] Avoiding Duplicates: {Fore.YELLOW}{chupapi} {Fore.BLACK}{indx} / {len(data)}")
                    print(f"{Fore.YELLOW}Sleeping 2 seconds")
                    await asyncio.sleep(2)
                else:
                    print(f"{Fore.RED}[FETCH USERS ERROR]")
                    error_msg()
            else:
                chupapi = await bot.fetch_user(i)
                embed_skrr = discord.Embed(title=f"{embed_title}".replace('user_id', f'{chupapi.id}').replace('user_name', f'{chupapi.name}').replace('user_discriminator', f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'),icon_url=embed_footer_icon_url.replace('user_avatar', f'{chupapi.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}'),description=f"{embed_description}".replace('user_id', f'{chupapi.id}').replace('user_name',f'{chupapi.name}').replace('user_mention', f'<@{chupapi.id}>').replace('user_discriminator',f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'), color=discord.Colour.random())
                embed_skrr.set_thumbnail(url=f"{embed_thumbnail_url}"), embed_skrr.set_image(url=f"{embed_image_url}"), embed_skrr.set_author(name=f"{embed_author}".replace('user_id', f'{chupapi.id}').replace('user_name',f'{chupapi.name}').replace('user_mention', f'<@{chupapi.id}>').replace('user_discriminator',f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'), icon_url=embed_author_icon_url.replace('user_avatar',f'{chupapi.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}')), embed_skrr.set_footer(text=f"{embed_footer}".replace('user_id', f'{chupapi.id}').replace('user_name',f'{chupapi.name}').replace('user_mention', f'<@{chupapi.id}>').replace('user_discriminator',f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'),icon_url=embed_footer_icon_url.replace('user_avatar',f'{chupapi.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}'))
                try:
                    await chupapi.send(embed=embed_skrr)
                    print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[+] Sent the embed to {Fore.YELLOW}{chupapi}{Fore.LIGHTGREEN_EX} {indx} / {len(data)}")
                    pablo = random.randint(cooldown, cooldown_max)
                    success += 1
                    if success >= dm_limit:
                        print(f"{Fore.BLUE}{current_time} {Fore.LIGHTCYAN_EX}[?] DM Limit has been reached: {Fore.YELLOW}{dm_limit} DMs {Fore.LIGHTCYAN_EX}(Switching the token in 1 second)")
                        await asyncio.sleep(1)
                        os.execv(sys.executable, ['python'] + sys.argv)
                    if display_sleep == "True":
                          print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                    else:
                        pass
                    await asyncio.sleep(pablo)
                except discord.Forbidden as e:
                    if e.code == 40003:
                        print(f"{Fore.LIGHTYELLOW_EX}You have been Rate Limited\nThe Code will be restarted in 90 seconds - {Fore.RED}{e}")
                        await asyncio.sleep(90)
                        os.execv(sys.executable, ['python'] + sys.argv)
                        continue
                    else:
                        print(
                            f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{chupapi}{Fore.RED} - {e} {indx} / {len(data)}")
                        pablo = random.randint(cooldown, cooldown_max)
                        if always_sleep == "True":
                            if display_sleep == "True":
                                print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                            await asyncio.sleep(pablo)
                except discord.HTTPException as e:
                    print(f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t fetch {Fore.YELLOW}{i}{Fore.RED} - {e} {indx} / {len(data)}")
                if chupapi.id not in penis:
                    penis.append(chupapi.id)
                    with open("alreadyusedids.json", "w") as file:
                        json.dump(penis, file)
        else:
            try:
                chupapi = await bot.fetch_user(i)
                embed_skrr = discord.Embed(title=f"{embed_title}".replace('user_id', f'{chupapi.id}').replace('user_name',f'{chupapi.name}').replace('user_discriminator', f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'),icon_url=embed_footer_icon_url.replace('user_avatar',f'{chupapi.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}'), description=f"{embed_description}".replace('user_id', f'{chupapi.id}').replace('user_name',f'{chupapi.name}').replace('user_mention', f'<@{chupapi.id}>').replace('user_discriminator', f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'), color=discord.Colour.random())
                embed_skrr.set_thumbnail(url=f"{embed_thumbnail_url}"), embed_skrr.set_image(url=f"{embed_image_url}"), embed_skrr.set_author(name=f"{embed_author}".replace('user_id', f'{chupapi.id}').replace('user_name',f'{chupapi.name}').replace('user_mention', f'<@{chupapi.id}>').replace('user_discriminator',f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'), icon_url=embed_author_icon_url.replace('user_avatar',f'{chupapi.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}')), embed_skrr.set_footer(text=f"{embed_footer}".replace('user_id', f'{chupapi.id}').replace('user_name',f'{chupapi.name}').replace('user_mention', f'<@{chupapi.id}>').replace('user_discriminator',f'{chupapi.discriminator}').replace('selfbot_id',f'{bot.user.id}').replace('selfbot_name', f'{bot.user.name}').replace('selfbot_mention', f'<@{bot.user.id}>').replace('selfbot_discriminator', f'{bot.user.discriminator}'),icon_url=embed_footer_icon_url.replace('user_avatar',f'{chupapi.avatar_url}').replace('selfbot_avatar', f'{bot.user.avatar_url}'))
                await chupapi.send(embed=embed_skrr)
                print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[+] Sent the embed to {Fore.YELLOW}{chupapi}{Fore.LIGHTGREEN_EX} {indx} / {len(data)}")
                success +=1
                if success >= dm_limit:
                    print(f"{Fore.BLUE}{current_time} {Fore.LIGHTCYAN_EX}[?] DM Limit has been reached: {Fore.YELLOW}{dm_limit} DMs {Fore.LIGHTCYAN_EX}(Switching the token in 1 second)")
                    await asyncio.sleep(1)
                    os.execv(sys.executable, ['python'] + sys.argv)
                pablo = random.randint(cooldown, cooldown_max)
                if display_sleep == "True":
                    print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                else:
                    pass
                await asyncio.sleep(pablo)
            except discord.Forbidden as e:
                if e.code == 40003:
                    print(f"{Fore.LIGHTYELLOW_EX}You have been Rate Limited\nThe Code will be restarted in 90 seconds - {Fore.RED}{e}")
                    await asyncio.sleep(90)
                    os.execv(sys.executable, ['python'] + sys.argv)
                    continue
                else:
                    print(f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t send a DM to {Fore.YELLOW}{chupapi}{Fore.RED} - {e} {indx} / {len(data)}")
                    pablo = random.randint(cooldown, cooldown_max)
                    if always_sleep == "True":
                        if display_sleep == "True":
                            print(f"{Fore.YELLOW}Sleeping {pablo} seconds")
                        await asyncio.sleep(pablo)
            except discord.HTTPException as e:
                print(f"{Fore.BLUE}{current_time} {Fore.RED}[-] Couldn\'t fetch {Fore.YELLOW}{i}{Fore.RED} - {e} {indx} / {len(data)}")
            if chupapi.id not in penis:
                penis.append(chupapi.id)
                with open("alreadyusedids.json", "w") as file:
                    json.dump(penis, file)
    input(f"{Fore.LIGHTGREEN_EX}Press Enter 5 times to close the program.")
    [input(i) for i in range(4, 0, -1)]
    print("Goodbye!\nhttps://github.com/hoemotion/mass-dm-discord Don\'t forget to leave a star!!")
    await sys.exit()
print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_cyan, '''███╗   ███╗ █████╗  ██████╗ ██████╗        ██████╗ ███╗   ███╗
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
    if send_embed == "False":
        await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="github.com/hoemotion"))
        print(f'{Fore.LIGHTGREEN_EX}Logged in as: {Fore.YELLOW}"{bot.user}" {Fore.LIGHTGREEN_EX}| ID: {Fore.YELLOW}"{bot.user}"{Fore.LIGHTGREEN_EX}\nConnected with {Fore.YELLOW}{len(bot.guilds)}{Fore.LIGHTGREEN_EX} Guilds and {Fore.YELLOW}{len(bot.user.friends)} {Fore.LIGHTGREEN_EX}Friends')
        print(f'{Fore.LIGHTYELLOW_EX}[⚡] Started sending DMs to the IDs\n')
        await mass_dm()
    elif send_embed == "True":
        await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="github.com/hoemotion"))
        print(f'{Fore.LIGHTGREEN_EX}Logged in as: {Fore.YELLOW}"{bot.user}" {Fore.LIGHTGREEN_EX}| ID: {Fore.YELLOW}"{bot.user}"{Fore.LIGHTGREEN_EX}\nConnected with {Fore.YELLOW}{len(bot.guilds)}{Fore.LIGHTGREEN_EX} Guilds and {Fore.YELLOW}{len(bot.user.friends)} {Fore.LIGHTGREEN_EX}Friends')
        print(f'{Fore.LIGHTYELLOW_EX}[⚡] Started sending Embed Messages to the IDs\n')
        await mass_dm_embed()
    else:
        print(f"{Fore.RED} EMBED ERROR")
        error_msg()
try:
    bot.run(token, bot=False)
except Exception as e:
    print(f"{Fore.RED}TOKEN ERROR - {e}")
    print(token)
    time.sleep(10)
    os.execv(sys.executable, ['python'] + sys.argv)
