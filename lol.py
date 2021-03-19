import os
from riotwatcher import LolWatcher, ApiError
import pandas as pd

watcher = LolWatcher(os.getenv('RiotAPIkey'))
my_region = 'euw1'


def get_masteries(name):
    me = watcher.summoner.by_name(my_region, name)
    masteries = watcher.champion_mastery.by_summoner(my_region, me['id'])

    stats = []
    for row in masteries:
        stats_row = {'champID': row['championId'], 'points': row['championPoints']}
        stats.append(stats_row)
    return pd.DataFrame(stats)


def get_recently_played(name, count=100):

    me = watcher.summoner.by_name(my_region, name)

    my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])

    last_matches = my_matches['matches'][0:count]

    stats = []
    for i in range(0, len(last_matches)):
        if last_matches[i]['queue'] != 450 and last_matches[i]['queue'] != 700:
            match_detail = watcher.match.by_id(my_region, last_matches[i]['gameId'])
            champ = last_matches[i]['champion']
            for row in match_detail['participants']:
                if row['championId'] == champ:
                    deaths = row['stats']['deaths']
                    if deaths == 0:
                        deaths = 1
                    if row['stats']['win']:
                        stats_row = {'champID': champ, 'win': 1, 'KDA': (row['stats']['kills'] + row['stats']['assists']) / deaths}
                    else:
                        stats_row = {'champID': champ, 'win': 0, 'KDA': (row['stats']['kills'] + row['stats']['assists']) / deaths}
                    stats.append(stats_row)
                    break
    df = pd.DataFrame(stats)
    games = len(df)

    df['frequency'] = df['champID'].map(df['champID'].value_counts() / games)
    df = df.groupby('champID', as_index=False).mean()
    col_list = list(df)
    col_list.remove('champID')
    df['win'] = df['win'].apply(lambda x: x + 0.1) # um *0 auszuschließen
    df['score'] = df[col_list].prod(axis=1)
    df['score'] = df['score'].apply(lambda x: x * 100)

    latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
    static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')

    # champ static list data to dict for looking up
    champ_dict = {}
    for key in static_champ_list['data']:
        row = static_champ_list['data'][key]
        champ_dict[row['key']] = row['id']

    for i in range(0, len(df)):
        df.at[i, "champ"] = champ_dict[str(df.iloc[i, 0])]

    df = df.sort_values('score', ascending=False)
    return df


def stats(name):
    me = watcher.summoner.by_name(my_region, name)
    output = me['name'] + ", Level " + str(me['summonerLevel']) + "\n"

    # ranked stats
    my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
    for q in my_ranked_stats:
        qtype = q['queueType']
        if qtype == "RANKED_SOLO_5x5":
            qtype = "SoloQ"
        elif qtype == "RANKED_FLEX_SR":
            qtype = "FlexQ"
        output = output + qtype + ": " + q['tier'] + " " + q['rank'] + "\n"

    scores = get_recently_played(name, 20)
    scores = scores.head(5)

    for i in range(0, len(scores)):
        output = output + '{:<20s} {:<20s}'.format(scores.iloc[i, 5], str(round(scores.iloc[i, 4], 2))) + "\n"

    return output
