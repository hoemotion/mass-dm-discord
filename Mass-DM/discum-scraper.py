import time
start = time.time()
import sys
import subprocess
# python -m pip install --user --upgrade git+https://github.com/Merubokkusu/Discord-S.C.U.M#egg=discum
try:
  import discum
except ImportError:
  try:
      subprocess.check_call([sys.executable, "-m", "pip", "install", '--user', "--upgrade",
                             "git+https://github.com/Merubokkusu/Discord-S.C.U.M#egg=discum"])
  except:
      subprocess.check_call([sys.executable, "-m", "pip", "install", 'discum'])

import os
import json
with open('config.json') as f:
    yamete_kudasai = json.load(f)
token = yamete_kudasai['token']
bot = discum.Client(token=token)

def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members) #this line is optional
        print(str(lenmembersfetched)+' members fetched') #this line is optional
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()

def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1) #get all user attributes, wait 1 second between requests
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession() #saves 10 seconds when gateway is run again
    return bot.gateway.session.guild(guild_id).members

members = get_members('guild id here', 'channel id here')
memberslist = []
with open("ids.json", "r") as file:
  data = json.load(file)
total_scraped = 0
for memberID in members:
  if memberID not in data:
    total_scraped += 1
    data.append(int(memberID))
    print(f"{total_scraped}/{len(members)} - {memberID}")
with open("ids.json", "w") as file:
  json.dump(data, file)
end = time.time()
print(f"Scraped {total_scraped} User IDs successfully\nTime Taken: {end - start}s")
