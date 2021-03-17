import os
import cassiopeia as cass
from riotwatcher import LolWatcher, ApiError
import pandas as pd

cass.set_riot_api_key(os.getenv('RiotAPIkey'))
cass.set_default_region("EUW")
watcher = LolWatcher(os.getenv('RiotAPIkey'))
my_region = 'euw1'

def get_most_played(name):
  summoner = cass.get_summoner(name=name)
  good_with = summoner.champion_masteries.filter(lambda cm: cm.level >= 6)
  return [cm.champion.name for cm in good_with]


def recently_played(name):
  me = watcher.summoner.by_name(my_region, name)
  # check league's latest version
  latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
  # Lets get some champions static information
  static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')

  my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])

  # fetch last match detail
  count = 100
  last_matches = my_matches['matches'][0:count]

  champs = []
  for row in last_matches:
      champs_row = {'champID': row['champion'], 'q': row['queue']}
      champs.append(champs_row)

  champ_dict = {}
  for key in static_champ_list['data']:
      row = static_champ_list['data'][key]
      champ_dict[row['key']] = row['id']
  for row in champs:
      row['champID'] = champ_dict[str(row['champID'])]
      if row['q'] == 440:
          row['q'] = 'flex'
      elif row['q'] == 450:
          row['q'] = 'aram'
      elif row['q'] == 420:
          row['q'] = 'solo'
      elif row['q'] == 400:
          row['q'] = 'solo'

  df = pd.DataFrame(champs)
  df = df[(df.q != "aram")]
  games = len(df)
  df['frequency'] = df['champID'].map(df['champID'].value_counts())
  df.drop_duplicates(subset=["champID"], keep="first", inplace=True)
  df = df.sort_values('frequency', ascending=False)
  df = df[(df.frequency > games/20)]
  
  output = ""
  for i in range(0,len(df)):
      output = output + df.iloc[i, 0] + ", " + str(int((int(df.iloc[i, 2])/games) * 100)) + "% gespielt\n"
  return output

def stats(name):
  #level und name
  me = watcher.summoner.by_name(my_region, name)
  output = me['name'] + ", Level " + str(me['summonerLevel']) + "\n"
  
  #ranked stats
  my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
  for q in my_ranked_stats:
    qtype = q['queueType']
    if qtype == "RANKED_SOLO_5x5":
        qtype = "SoloQ"
    elif qtype == "RANKED_FLEX_SR":
        qtype = "FlexQ"
    output = output + qtype + ": " + q['tier'] + " " + q['rank'] + "\n"
  
  #masteries
  masteries = watcher.champion_mastery.by_summoner(my_region, me['id'])
  stats = []
  for row in masteries:
      stats_row = {'champID': row['championId'], 'points': row['championPoints']}
      stats.append(stats_row)
  df = pd.DataFrame(stats)

  # check league's latest version
  latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
  static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')

  champ_dict = {}
  for key in static_champ_list['data']:
      row = static_champ_list['data'][key]
      champ_dict[row['key']] = row['id']
  for row in stats:
      row['championName'] = champ_dict[str(row['champID'])]

  df = pd.DataFrame(stats)
  df.drop('champID', axis=1, inplace=True)
  lines = []
  for i in range(0,10):
      points = '{:,}'.format(int(df.iloc[i, 0])).replace(',', '.')
      lines.append('{:<25s} {:<20s}'.format(df.iloc[i, 1], points + " Punkte"))

  for line in lines:
      output = output + line + "\n"
    
  output = output + "\n" + recently_played(name)

  return output
