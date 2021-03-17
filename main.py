import discord
import os
from keep_alive import keep_alive
from reddit_func import get_meme, get_meme_sub
import chat_func
from lol import stats, get_most_played

client = discord.Client()


def get_help():
  return "hola espanol?\n!csgo: Waffen/Strats für maximalen Int\n!int: Inten oder nicht?\n!champ: Random Champ\n!runes: Random Runen\n!items: Random Items\n!team: Perfekt gedraftetes Team für LoL\n!team_wild: Die etwas würzigere Alternative\n!jocho: random champ+runen+items\n!strategy: Geniale Wege, das Spiel zu drehen\n!meme: Random aktuelles Meme von Reddit, besondere subs: !cursed !oger !ich_iel !ok !history !prog !crypto\n!sub x y z ...: Random Top-Post aus einem der angegebenen Subreddits\n!ban x: Zeigt Champions mit Mastery > 6 des angegebenen Summoners, kann unter Umständen ordentlich dauern"


@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='ESNhelp'))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!team_wild'):
    await message.channel.send(chat_func.get_team_wild())
  elif message.content.startswith('hola'):
    await message.channel.send('Espanol???')
  elif message.content.startswith('!team'):
    await message.channel.send(chat_func.get_team())
  elif message.content.startswith('!runes'):
    await message.channel.send(chat_func.get_runes())
  elif message.content.startswith('!champ'):
    await message.channel.send(chat_func.get_champ())
  elif message.content.startswith('!int'):
    await message.channel.send(chat_func.get_int())
  elif message.content.startswith('!items'):
    await message.channel.send(chat_func.get_items(6))
  elif message.content.startswith('!csgo'):
    await message.channel.send(chat_func.get_csgo())
  elif message.content.startswith('ESNhelp'):
    await message.channel.send(get_help())
  elif message.content.startswith('!items'):
    await message.channel.send(chat_func.get_items(6))
  elif message.content.startswith('!strategy'):
    await message.channel.send(chat_func.get_strategy())
  elif message.content.startswith('!meme'):
    await message.channel.send(get_meme())
  elif message.content.startswith('!cursed'):
    await message.channel.send(get_meme_sub(["cursedimages", "blursedimages"]))
  elif message.content.startswith('!oger'):
    await message.channel.send(get_meme_sub(["altschauerberg"]))
  elif message.content.startswith('!ich_iel'):
    await message.channel.send(get_meme_sub(["ich_iel"]))
  elif message.content.startswith('!jocho'):
    await message.channel.send(chat_func.get_jocho())
  elif message.content.startswith('!ok'):
    await message.channel.send(get_meme_sub(["okbrudimongo","okbuddyretard"]))
  elif message.content.startswith('!sub'):
    subs = []
    for sub in message.content.split():
      if not sub.startswith('!'):
        subs.append(sub)
    try:
      await message.channel.send(get_meme_sub(subs))
    except:
      await message.channel.send("Der sub " + str(subs) + " existiert nicht lmao")
  elif message.content.startswith('!history'):
    await message.channel.send(get_meme_sub(["historymemes"]))
  elif message.content.startswith('!prog'):
    await message.channel.send(get_meme_sub(["programmerhumor"]))
  elif message.content.startswith('!crypto'):
    await message.channel.send(get_meme_sub(["wallstreetbets", "mauerstrassenwetten", "dogecoin"]))
  elif message.content.startswith('!ban'):
    summoner = ""
    for arg in message.content.split():
      if not arg.startswith('!ban'):
        summoner = summoner + arg
    try:
      await message.channel.send(get_most_played(summoner))
    except Exception as e:
      await message.channel.send("Da ist wohl was schief gelaufen wie ein betrunkener Fußgänger!\n" + "[ERROR] " + str(e))
  elif message.content.startswith('!stats'):
    summoner = ""
    for arg in message.content.split():
      if not arg.startswith('!stats'):
        summoner = summoner + arg
    
    try:
      await message.channel.send(stats(summoner))
    except Exception as e:
      await message.channel.send("Da ist wohl was schief gelaufen wie ein betrunkener Fußgänger!\n" + "[ERROR] " + str(e))

keep_alive()
client.run(os.getenv('TOKEN'))
