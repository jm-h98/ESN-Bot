import discord
import os
from keep_alive import keep_alive
import random
import praw

client = discord.Client()
reddit = praw.Reddit(
    client_id=os.getenv('ClientID'),
    client_secret=os.getenv('ClientSecret'),
    password=os.getenv('PW'),
    user_agent="ESNbot",
    username=os.getenv('User'),
    check_for_async=False
)

champs = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol", "Azir", "Bard", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho Gath", "Corki", "Darius", "Diana", "Dr Mundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "Kai Sa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha Zix", "Kindred", "Kled", "Kog Maw", "LeBlanc", "Lee Sin", "Leona", "Lissandra", "Lucian", "Lulu", "Lux", "Lillia", "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nocturne", "Nunu und Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "Rek Sai", "Renekton","Rell", "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Seraphine", "Senna", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh","Tristana","Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr", "Urgot", "Varus", "Viego", "Vayne", "Veigar","Vel Koz", "Vi", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong","Xayah" ,"Xerath", "Xin Zhao", "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"]


mythics = ["Divine Sunderer", "Duskblade", "Eclipse", "Everfrost", "Frostfire Gauntlet", "Galeforce", "Goredrinker", "Rocketbelt", "Immortal Shieldbow", "Imperial Mandate", "Kraken Slayer", "Liandrys", "Locket", "Ludens", "Moonstone Renewer", "Night Harvester", "Prowlers Claw", "Riftmaker", "Shurelyas", "Stridebreaker", "Sunfire", "Trinity", "Turbo Chemtank"]


legendaries = ["Abyssal Mask", "Archangel's Staff", "Ardent Censer","Banshee's Veil","Black Cleaver" ,"Blade of the Ruined King" ,"Bloodthirster" ,"Chempunk Chainsword" ,"Chemtech Putrifier" ,"Cosmic Drive" ,"Dead Man's Plate" ,"Death's Dance" ,"Demonic Embrace" ,"Edge of Night" ,"Essence Reaver" ,"Force of Nature","Frozen Heart" ,"Gargoyle Stoneplate","Guardian Angel" ,"Guinsoo's Rageblade","Horizon Focus" ,"Infinity Edge","Knight's Vow","Lich Bane","Lord Dominik's Regards" ,"Manamune","Maw of Malmortius" ,"Mejai's Soulstealer" ,"Mercurial Scimitar" ,"Mikael's Blessing","Morellonomicon","Mortal Reminder" ,"Muramana" ,"Nashor's Tooth" ,"Navori Quickblades" ,"Phantom Dancer" ,"Rabadon's Deathcap" ,"Randuin's Omen","Rapid Firecannon" ,"Ravenous Hydra","Redemption" ,"Runaan's Hurricane" ,"Rylai's Crystal" ,"Sanguine Blade" ,"Seraph's Embrace" ,"Serpent's Fang" ,"Serylda's Grudge","Silvermere Dawn","Spirit Visage","Staff of Flowing Water","Sterak's Gage" ,"Stormrazor","The Collector","Thornmail","Titanic Hydra","Umbral Glaive","Void Staff","Warmog's Armor","Wit's End","Youmuu's Ghostblade","Zeke's Convergence","Zhonya's Hourglass"]


shoes = ["Berserkers Greaves", "Swifties", "Ionian Boots of Lucidity", "Mercs", "Mobility Boots", "Plated Steelcaps", "Sorcerers shoes"]


runes = ["Press the attack", "Lethal Tempo", "Fleet Footwork", "Conqueror", "Electrocute", "Predator", "Dark Harvest", "Hail of Blades", "Aery", "Comet", "Phase Rush","Grasp", "Aftershock", "Guardian", "Glacial Augment", "Spellbook", "Omnistone"]


rune_trees = ["Precision", "Domination", "Sorcery", "Resolve", "Inspiration"]


playstyles = ["Full-Tank", "Attackspeed", "Full-AD", "Full-AP", "Crit", "Assassin", "Movement Speed", "CDR", "Brawler", "Full-Mana", "On-Hit"]


strategies = ["Bis der nächste Tower fällt: ARAM", "Baron machen", "Drake machen", "Bis der nächste Tower fällt: Alle Top", "Bis der nächste Tower fällt: Alle Bot", "Bis der nächste Tower fällt: 1-3-1", "Alle trappen", "Bis der nächste Tower fällt: 0 Damage machen", "2 Minuten keinen Kill!", "2 Minuten keinen Farm nehmen!", "Harri in der Gegner-Base zünden", "Entenmarsch hinter Jungler, bis er stirbt!", "2 Waves Proxyfarmen",  "2 Minuten lang die Rollen nach unten hin rotieren (Top -> Jgl, Jgl -> Mid etc.)", "2 Minuten lang die Rollen nach oben hin rotieren (Top -> Sup, Jgl -> Top etc.)"]

int_lines = ["REIN DA!", "Der Fahrstuhl kennt nur eine Richtung (Zwinkersmiley)", "Gib dem armen Jungen ein bisschen Gold", "Rein da, aber nur die rechte Hand benutzen!", "Rein da, aber nur die linke Hand benutzen!"]


def get_team_wild():
  rand = random.sample(range(1, len(champs)), 5)
  top = "TOPLANE\nChamp: {0}\n{1}Items: {2}\n\n".format(champs[rand[0]], get_runes(), get_items(6))
  jungle = "JUNGLE\nChamp: {0}\n{1}Items: Jungle-Item, {2}\n\n".format(champs[rand[1]], get_runes(), get_items(5))
  mid = "MIDLANE\nChamp: {0}\n{1}Items: {2}\n\n".format(champs[rand[2]], get_runes(), get_items(6))
  bot = "BOTLANE\nChamp: {0}\n{1}Items: {2}\n\n".format(champs[rand[3]], get_runes(), get_items(6))
  sup = "SUPPORT\nChamp: {0}\n{1}Items: Support-Item, {2}\n\n".format(champs[rand[4]], get_runes(), get_items(5))
  return top + jungle + mid + bot + sup + "GLHF!"


def get_team():
  rand = random.sample(range(1, len(champs)), 5)
  top = "TOPLANE\n{0} {1}\n\n".format(random.choice(playstyles), champs[rand[0]])
  jungle = "JUNGLE\n{0} {1}\n\n".format(random.choice(playstyles), champs[rand[1]])
  mid = "MIDLANE\n{0} {1}\n\n".format(random.choice(playstyles), champs[rand[2]])
  bot = "BOTLANE\n{0} {1}\n\n".format(random.choice(playstyles), champs[rand[3]])
  sup = "SUPPORT\n{0} {1}\n\n".format(random.choice(playstyles), champs[rand[4]])
  return top + jungle + mid + bot + sup + "GLHF!"


def get_items(i):
  items = random.choice(mythics)
  legend = random.sample(range(1, len(legendaries)), i-2)
  for item in legend:
    items = items + ", " + legendaries[item]
  shoe = random.choice(shoes)
  return items + " + " + shoe


def get_champ():
  return random.choice(champs)


def get_strategy():
  return random.choice(strategies)


def get_int():
  rand = random.randint(0, 100)
  if rand > 75:
    return "Nicht inten"
  else:
    return random.choice(int_lines)


def get_meme():
  subs = ["ich_iel", "HistoryMemes", "me_irl", "altschauerberg", "TIHI", "redneckengineering", "okbrudimongo", "cursedimages", "BikiniBottomTwitter", "blursedimages"]
  subreddit = reddit.subreddit(random.choice(subs))
  submissions = []
  submission_buffer = subreddit.hot(limit=25)
  for submission in submission_buffer:
    submissions.append(submission)
  post = random.choice(submissions)
  return post.title + "\n" + post.url


def get_meme_sub(sub):
  subreddit = reddit.subreddit(sub)
  submissions = []
  submission_buffer = subreddit.hot(limit=25)
  for submission in submission_buffer:
    submissions.append(submission)
  post = random.choice(submissions)
  return post.title + "\n" + post.url


def get_csgo():
  strats = ["RUSH B СУКА", "ESN-Spezial auf A Lang", "Mitte runter", "A Short", "Lower Tunnel zu B", "Lower Tunnel zu Short", "Bombe opfern", "Erst aus dem Spawn, wenn ein Kill gefallen ist", "Nur schleichen", "Anfangen zu schießen -> Magazin muss leer", "Entenmarsch zu B"]
  waffen = ["Dual Berettas", "Negev", "Negev", "Negev", "AWP", "MP7", "Deagle", "AR", "Autosniper", "Zeus", "Messer", "Pistol only", "Ohne Granaten"]
  return "Waffe: " + random.choice(waffen) + "\nStrategie: " + random.choice(strats)


def get_help():
  return "hola espanol?\n!csgo: Waffen/Strats für maximalen Int\n!int: Inten oder nicht?\n!champ: Random Champ\n!runes: Random Runen\n!items: Random Items\n!team: Perfekt gedraftetes Team für LoL\n!team_wild: Die etwas würzigere Alternative\n!strategy: Geniale Wege, das Spiel zu drehen\n!meme: Random aktuelles Meme von Reddit, besondere subs: !cursed !oger !ich_iel"


def get_runes():
  rune = runes[random.randint(0, len(runes)-1)]

  b = False
  while not b:
    rand = random.randint(0, len(rune_trees)-1)
    if rune in {"Press the attack", "Lethal Tempo", "Fleet Footwork", "Conqueror"} and rand != 0:
      b = True
    elif rune in {"Electrocute", "Predator", "Dark Harvest", "Hail of Blades"} and rand != 1:
      b = True
    elif rune in {"Aery", "Comet", "Phase Rush"} and rand != 2:
      b = True
    elif rune in {"Grasp", "Aftershock", "Guardian"} and rand != 3:
      b = True
    elif rune in {"Glacial Augment", "Spellbook", "Omnistone"} and rand != 4:
      b = True

  return "Runen: " + rune + " mit " + rune_trees[rand] + "\n"

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='ESNhelp'))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!team_wild'):
    await message.channel.send(get_team_wild())
  elif message.content.startswith('hola'):
    await message.channel.send('Espanol???')
  elif message.content.startswith('!team'):
    await message.channel.send(get_team())
  elif message.content.startswith('!runes'):
    await message.channel.send(get_runes())
  elif message.content.startswith('!champ'):
    await message.channel.send(get_champ())
  elif message.content.startswith('!int'):
    await message.channel.send(get_int())
  elif message.content.startswith('!items'):
    await message.channel.send(get_items(6))
  elif message.content.startswith('!csgo'):
    await message.channel.send(get_csgo())
  elif message.content.startswith('ESNhelp'):
    await message.channel.send(get_help())
  elif message.content.startswith('!items'):
    await message.channel.send(get_items(6))
  elif message.content.startswith('!strategy'):
    await message.channel.send(get_strategy())
  elif message.content.startswith('!meme'):
    await message.channel.send(get_meme())
  elif message.content.startswith('!cursed'):
    await message.channel.send(get_meme_sub("cursedimages"))
  elif message.content.startswith('!oger'):
    await message.channel.send(get_meme_sub("altschauerberg"))
  elif message.content.startswith('!ich_iel'):
    await message.channel.send(get_meme_sub("ich_iel"))

keep_alive()
client.run(os.getenv('TOKEN'))
