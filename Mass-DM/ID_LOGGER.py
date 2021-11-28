import sys, subprocess, json, time, asyncio
try:
    import discord, colorama, pyfade
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'discord.py'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'colorama'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyfade'])
from discord.ext import commands
from colorama import Fore
from datetime import datetime
def error_msg():
    print(pyfade.Fade.Horizontal(pyfade.Colors.purple_to_red, """Bruhhhh
Seems like you\'re new to Python and/or JSON..
Join the Support-Server and lemme help you :)
https://discord.gg/verQuxaBqy"""))
    time.sleep(10)
    input(f"{Fore.YELLOW}Press Enter to exit the script")
    raise SystemExit
sys.tracebacklimit = 0
with open('config.json') as f:
    yamete_kudasai = json.load(f)
token = yamete_kudasai['token']
whitelist = "False"
print(pyfade.Fade.Horizontal(pyfade.Colors.cyan_to_blue, '''
██╗██████╗         ██╗      █████╗  ██████╗  ██████╗ ███████╗██████╗ 
██║██╔══██╗        ██║     ██╔══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
██║██║  ██║        ██║     ██║  ██║██║  ██╗ ██║  ██╗ █████╗  ██████╔╝
██║██║  ██║        ██║     ██║  ██║██║  ╚██╗██║  ╚██╗██╔══╝  ██╔══██╗
██║██████╔╝        ███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
╚═╝╚═════╝         ╚══════╝ ╚════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝'''))
print(f'''{Fore.LIGHTWHITE_EX}                                                    Made by {Fore.YELLOW}hoemotion 
{Fore.LIGHTWHITE_EX}Check out the github page for updates: {Fore.LIGHTBLUE_EX}https://github.com/hoemotion/mass-dm-discord/  
''')


def log_id(reason, id, name, discriminator, guild):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    try:
        with open("blacklistedids.json", "r") as file:
            data = json.load(file)
            if id not in data:
                pass
            elif id in data:
                return

        with open("ids.json", "r") as file:
            data = json.load(file)
            time.sleep(0.01)

        if id not in data:
            time.sleep(0.01)
            data.append(id)

            with open("ids.json", "w") as file:
                time.sleep(0.01)
                json.dump(data, file)

            try:
                print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[{Fore.YELLOW}{guild}{Fore.LIGHTGREEN_EX} | {Fore.YELLOW}{reason}{Fore.LIGHTGREEN_EX}] {Fore.YELLOW}{name}#{discriminator} {Fore.LIGHTGREEN_EX}- {Fore.YELLOW}{id}{Fore.LIGHTGREEN_EX} Total:{Fore.YELLOW} {len(data)}")
            except AttributeError:
                print(f"{Fore.BLUE}{current_time} {Fore.LIGHTGREEN_EX}[{Fore.YELLOW}{reason}{Fore.LIGHTGREEN_EX}]{Fore.YELLOW} {name}#{discriminator} {Fore.LIGHTGREEN_EX}- {Fore.YELLOW}{id} {Fore.LIGHTGREEN_EX}Total: {Fore.YELLOW}{len(data)}")
            except:
                pass

    except:
        pass

bot = discord.Client()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="github.com/hoemotion️"))
    await bot.change_presence(status=discord.Status.idle)
    print(f'{Fore.LIGHTGREEN_EX}Logged in as: {Fore.YELLOW}"{bot.user}" {Fore.LIGHTGREEN_EX}| ID: {Fore.YELLOW}"{bot.user.id}"{Fore.LIGHTGREEN_EX}\nConnected with {Fore.YELLOW}{len(bot.guilds)}{Fore.LIGHTGREEN_EX} Guilds and {Fore.YELLOW}{len(bot.user.friends)} {Fore.LIGHTGREEN_EX}Friends')
    print(f'{Fore.LIGHTYELLOW_EX}[⚡] Started logging IDs\n')
    if len(bot.guilds) < 20:
        print("Logging IDs will become faster if you join more Servers!")

@bot.event
async def on_message(message):
    if whitelist == "True":
        with open('whitelistedservers.json') as f:
            whitlisted_servers = json.load(f)
        if message.guild.id in whitlisted_servers:
            await asyncio.sleep(0.1)
            try:
                with open('blacklistedservers.json') as f:
                    banned_servers = json.load(f)
                if message.guild.id in banned_servers:
                    return
                else:
                    pass
                try:
                    if not message.author.bot:
                        try:
                            reason = "MESSAGE"
                            log_id(message.author.id, message.author.name, message.author.discriminator,
                                   message.author.guild, reason)
                        except AttributeError:
                            pass

                    if message.author.bot:
                        pass
                except AttributeError:
                    pass
            except:
                pass
        else:
            return
    else:
        await asyncio.sleep(0.1)
        try:
            with open('blacklistedservers.json') as f:
                banned_servers = json.load(f)
            if message.guild.id in banned_servers:
                return
            else:
                pass
            try:
                if not message.author.bot:
                    try:
                        reason = "MESSAGE"
                        log_id(reason, message.author.id, message.author.name, message.author.discriminator,
                               message.author.guild)
                    except AttributeError:
                        pass

                if message.author.bot:
                    pass
            except AttributeError:
                pass
        except:
            pass

@bot.event
async def on_delete(message):
    if whitelist == "True":
        with open('whitelistedservers.json', "r") as f:
            whitlisted_servers = json.load(f)
        if message.guild.id in whitlisted_servers:
            await asyncio.sleep(0.1)
            try:
                with open('blacklistedservers.json', "r") as f:
                    banned_servers = json.load(f)
                if message.guild.id in banned_servers:
                    return
                else:
                    pass
                    try:
                        if not message.author.bot:
                            reason = "MESSAGE DELETED"
                            log_id(reason, message.author.id, message.author.name, message.author.discriminator,
                                   message.author.guild)
                        if message.author.bot:
                            pass
                    except AttributeError:
                        pass
            except:
                pass
        else:
            pass
    else:
        await asyncio.sleep(0.1)
        try:
            with open('blacklistedservers.json', "r") as f:
                banned_servers = json.load(f)
            if message.guild.id in banned_servers:
                return
            else:
                pass
                try:
                    if not message.author.bot:
                        reason = "MESSAGE DELETED"
                        log_id(reason, message.author.id, message.author.name, message.author.discriminator,
                               message.author.guild)
                    if message.author.bot:
                        pass
                except AttributeError:
                    pass
        except:
            pass

@bot.event
async def on_raw_reaction_add(payload):
    if whitelist == "True":
        with open('whitelistedservers.json', "r") as f:
            whitlisted_servers = json.load(f)
        if payload.member.guild.id in whitlisted_servers:
            await asyncio.sleep(0.1)
            try:
                with open('blacklistedservers.json', "r") as f:
                    banned_servers = json.load(f)
                if payload.member.guild.id in banned_servers:
                    return
                else:
                    pass
                try:
                    if not payload.member.bot:
                        reason = "EMOJI REACTION (RAW)"
                        log_id(reason, payload.member.id, payload.member.name, payload.member.discriminator,
                               payload.member.guild)
                except:
                    pass
            except:
                pass
        else:
            return
    else:
        await asyncio.sleep(0.1)
        try:
            with open('blacklistedservers.json', "r") as f:
                banned_servers = json.load(f)
            if payload.member.guild.id in banned_servers:
                return
            else:
                pass
            try:
                if not payload.member.bot:
                    reason = "EMOJI REACTION (RAW)"
                    log_id(reason, payload.member.id, payload.member.name, payload.member.discriminator,
                           payload.member.guild)
            except:
                pass
        except:
            pass


@bot.event
async def on_edit(message):
    if whitelist == "True":
        with open('whitelistedservers.json', "r") as f:
            whitlisted_servers = json.load(f)
        if message.guild.id in whitlisted_servers:
            await asyncio.sleep(0.1)
            try:
                with open('blacklistedservers.json', "r") as f:
                    banned_servers = json.load(f)
                if message.guild.id in banned_servers:
                    return
                else:
                    pass
                    try:
                        if not message.author.bot:
                            reason = "MESSAGE EDIT"
                            log_id(reason, message.author.id, message.author.name, message.author.discriminator,
                                   message.author.guild)
                        if message.author.bot:
                            pass
                    except AttributeError:
                        pass
            except:
                pass
        else:
            return
    else:
        await asyncio.sleep(0.1)
        try:
            with open('blacklistedservers.json', "r") as f:
                banned_servers = json.load(f)
            if message.guild.id in banned_servers:
                return
            else:
                pass
                try:
                    if not message.author.bot:
                        reason = "MESSAGE EDIT"
                        log_id(reason, message.author.id, message.author.name, message.author.discriminator,
                               message.author.guild)
                    if message.author.bot:
                        pass
                except AttributeError:
                    pass
        except:
            pass

@bot.event
async def on_member_join(member):
    if whitelist == "True":
        with open('whitelistedservers.json', "r") as f:
            whitlisted_servers = json.load(f)
        if member.guild.id in whitlisted_servers:
            await asyncio.sleep(0.1)
            try:
                with open('blacklistedservers.json', "r") as f:
                    banned_servers = json.load(f)
                if member.guild.id in banned_servers:
                    return
                else:
                    pass
                    try:
                        if not member.bot:
                            reason = "GUILD JOIN"
                            log_id(reason, member.id, member.name, member.discriminator, member.guild)
                        if member.bot:
                            pass
                    except AttributeError:
                        pass
            except:
                pass
        else:
            return
    else:
        await asyncio.sleep(0.1)
        try:
            with open('blacklistedservers.json', "r") as f:
                banned_servers = json.load(f)
            if member.guild.id in banned_servers:
                return
            else:
                pass
                try:
                    if not member.bot:
                        reason = "GUILD JOIN"
                        log_id(reason, member.id, member.name, member.discriminator, member.guild)
                    if member.bot:
                        pass
                except AttributeError:
                    pass
        except:
            pass

@bot.event
async def on_member_remove(user):
    if whitelist == "True":
        with open('whitelistedservers.json', "r") as f:
            whitlisted_servers = json.load(f)
        if user.guild.id in whitlisted_servers:
            await asyncio.sleep(0.1)
            try:
                with open('blacklistedservers.json', "r") as f:
                    banned_servers = json.load(f)
                if user.guild.id in banned_servers:
                    return
                else:
                    pass
                    try:
                        if not user.bot:
                            reason = "GUILD LEAVE"
                            log_id(reason, user.id, user.name, user.discriminator, user.guild)
                        if user.bot:
                            pass
                    except AttributeError:
                        pass
            except:
                pass
        else:
            return
    else:
        await asyncio.sleep(0.1)
        try:
            with open('blacklistedservers.json', "r") as f:
                banned_servers = json.load(f)
            if user.guild.id in banned_servers:
                return
            else:
                pass
                try:
                    if not user.bot:
                        reason = "GUILD LEAVE"
                        log_id(reason, user.id, user.name, user.discriminator, user.guild)
                    if user.bot:
                        pass
                except AttributeError:
                    pass
        except:
            pass

@bot.event
async def on_member_update(before, after):
    if whitelist == "True":
        with open('whitelistedservers.json', "r") as f:
            whitlisted_servers = json.load(f)
        if before.member.guild.id in whitlisted_servers:
            await asyncio.sleep(0.1)
            try:
                with open('blacklistedservers.json', "r") as f:
                    banned_servers = json.load(f)
                if after.member.guild.id in banned_servers:
                    return
                else:
                    pass
                    try:
                        if not after.member.bot:
                            reason = "MEMBER UPDATE"
                            log_id(reason, after.member.id, after.member.name, after.member.discriminator,
                                   after.member.guild)
                        if after.member.bot:
                            pass
                    except AttributeError:
                        pass
            except:
                pass
        else:
            return
    else:
        await asyncio.sleep(0.1)
        try:
            with open('blacklistedservers.json', "r") as f:
                banned_servers = json.load(f)
            if after.member.guild.id in banned_servers:
                return
            else:
                pass
                try:
                    if not after.member.bot:
                        reason = "MEMBER UPDATE"
                        log_id(reason, after.member.id, after.member.name, after.member.discriminator, after.member.guild)
                    if after.member.bot:
                        pass
                except AttributeError:
                    pass
        except:
            pass

@bot.event
async def on_voice_state_update(member, before, after):
    if whitelist == "True":
        with open('whitelistedservers.json', "r") as f:
            whitlisted_servers = json.load(f)
        if before.member.guild.id in whitlisted_servers:
            await asyncio.sleep(0.1)
            try:
                with open('blacklistedservers.json', "r") as f:
                    banned_servers = json.load(f)
                if after.member.guild.id in banned_servers:
                    return
                else:
                    pass
                    try:
                        if not member.bot:
                            reason = "VOICE STATE UPDATE"
                            log_id(reason, member.id, member.name, member.discriminator, member.guild)
                        if member.bot:
                            pass
                    except AttributeError:
                        pass
            except:
                pass
        else:
            return
    else:
        await asyncio.sleep(0.1)
        try:
            with open('blacklistedservers.json', "r") as f:
                banned_servers = json.load(f)
            if after.member.guild.id in banned_servers:
                return
            else:
                pass
                try:
                    if not member.bot:
                        reason = "VOICE STATE UPDATE"
                        log_id(reason, member.id, member.name, member.discriminator, member.guild)
                    if member.bot:
                        pass
                except AttributeError:
                    pass
        except:
            pass

@bot.event
async def on_reaction_add(reaction, member):
    if whitelist == "True":
        with open('whitelistedservers.json', "r") as f:
            whitlisted_servers = json.load(f)
        if member.guild.id in whitlisted_servers:
            await asyncio.sleep(0.1)
            try:
                with open('blacklistedservers.json', "r") as f:
                    banned_servers = json.load(f)
                if member.guild.id in banned_servers:
                    return
                else:
                    pass
                    try:
                        if not member.bot:
                            reason = "EMOJI REACTION"
                            log_id(reason, member.id, member.name, member.discriminator, member.guild)
                        if member.bot:
                            pass
                    except AttributeError:
                        pass
            except:
                pass
        else:
            return
    await asyncio.sleep(0.1)
    try:
        with open('blacklistedservers.json', "r") as f:
            banned_servers = json.load(f)
        if member.guild.id in banned_servers:
            return
        else:
            pass
            try:
                if not member.bot:
                    reason = "EMOJI REACTION"
                    log_id(reason, member.id, member.name, member.discriminator, member.guild)
                if member.bot:
                    pass
            except AttributeError:
                pass
    except:
        pass
try:
    bot.run(token, bot=False)
except Exception as e:
    print(f"{Fore.RED}TOKEN ERROR - {e}")
    error_msg()
