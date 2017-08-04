#!/usr/bin/env python3

def song_decoder(song):
    result = str.replace(song, 'WUB', ' ').strip()
    result = ' '.join(result.split())
    return result


print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))