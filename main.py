from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from re import findall
from os import getenv

queue = []

arg = input('Insira um URL do Spotify: ')
pattern = r'^(?:https?:\/\/)?(?:open|play)\.spotify\.com\/(?:intl-[a-z]{2}\/)?(album|artist|track|playlist|episode|show)\/(\S+)\/?$'
regex = findall(pattern, arg)

if not regex: print('Vídeo não encontrado.')
elif regex[0][0] in ['episode', 'show']: print('Infelizmente, não há suporte à Podcasts.')
else:
    load_dotenv()
    id = getenv('client_id')
    secret = getenv('client_secret')
    spotify = Spotify(auth_manager = SpotifyClientCredentials(client_id = id, client_secret = secret))

    check_dict = {
        'artist': spotify.artist_top_tracks,
        'playlist': spotify.playlist_tracks,
        'album': spotify.album_tracks,
        'track': spotify.track
    }

    results = check_dict.get(regex[0][0])(regex[0][1])
    if 'track' in regex[0][0]: queue.append(f'{results["artists"][0]["name"]} - {results["name"]}')
    elif 'tracks' in results: results = results["tracks"]
    while results:
        for track in results["items"] if 'items' in results else results:
            if 'playlist' in regex[0][1]: track = track["track"]
            try: queue.append(f'{track["artists"][0]["name"]} - {track["name"]}')
            except TypeError: pass
        results = spotify.next(results) if 'playlist' in regex[0][1] else None
    if not track: print('Infelizmente, não há suporte à Podcasts.')

with open('output.txt', 'w', encoding = 'utf8') as file:
    file.write('\n'.join(queue))

print('Processo concluído com sucesso.')
