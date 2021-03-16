import os
import cassiopeia as cass

cass.set_riot_api_key(os.getenv('RiotAPIkey'))
cass.set_default_region("EUW")

def get_most_played(name):
  summoner = cass.get_summoner(name=name)
  good_with = summoner.champion_masteries.filter(lambda cm: cm.level >= 6)
  return [cm.champion.name for cm in good_with]


def test(name):
  summoner = cass.get_summoner(name=name)
  current_match = cass.get_current_match(summoner)
  output = ""
  for sum in current_match:
    output = output + str(sum.name) + str(get_most_played(sum))
  return output