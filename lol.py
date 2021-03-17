import os
import cassiopeia as cass
from riotwatcher import LolWatcher, ApiError

cass.set_riot_api_key(os.getenv('RiotAPIkey'))
cass.set_default_region("EUW")
watcher = LolWatcher(os.getenv('RiotAPIkey'))
my_region = 'euw1'

def get_most_played(name):
  summoner = cass.get_summoner(name=name)
  good_with = summoner.champion_masteries.filter(lambda cm: cm.level >= 6)
  return [cm.champion.name for cm in good_with]


def test1(name):
  summoner = cass.get_summoner(name=name)
  current_match = cass.get_current_match(summoner)
  output = ""
  for sum in current_match:
    output = output + str(sum.name) + str(get_most_played(sum))
  return output

def stats(name):
  me = watcher.summoner.by_name(my_region, name)
  output = me['name'] + ", Level " + str(me['summonerLevel']) + "\n"
  my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
  for q in my_ranked_stats:
    qtype = q['queueType']
    if qtype == "RANKED_SOLO_5x5":
        qtype = "SoloQ"
    elif qtype == "RANKED_FLEX_SR":
        qtype = "FlexQ"
    output = output + qtype + ": " + q['tier'] + " " + q['rank'] + "\n"
