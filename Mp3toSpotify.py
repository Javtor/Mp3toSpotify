import ctypes, sys
import subprocess
import os
import json

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    print('instalando dependencias')
    install('pyacoustid')
    install('spotipy')
    print('dependencias instaladas')

    import spotipy
    from spotipy.oauth2 import SpotifyOAuth
    import os
    cid = "766b98550bef4a44b8d111658e985c52"
    secret = "0e2c82a346254d93bc29e6cfec0ef402"

    os.environ["SPOTIPY_CLIENT_ID"] = cid
    os.environ["SPOTIPY_CLIENT_SECRET"] = secret
    os.environ["SPOTIPY_REDIRECT_URI"] = 'http://localhost:8080'

    scope = 'playlist-modify-public playlist-modify-private user-library-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    playlist_name = 'Mp3toSpotify'
    playlist_description = 'Playlist creada a partir de archivos mp3'
    
    sp.current_user
    playlist = sp.user_playlist_create(sp.current_user()['id'], playlist_name)
    # print(playlist)

    sys.path += [os.getcwd()] 

    path = "./music"

    import acoustid
    spids = []
    for _,_,files in os.walk(path):
        for f in files:
            file = os.path.join(path, f)
            print(f)
            duration, fp = acoustid.fingerprint_file(file)
            print()
            json = acoustid.lookup('lFPruUAJVk', fp, duration, meta='recordings')
            if not json['results']:
                print('no se xd')
            else:
                results = json['results']
                for result in results:      
                    if 'recordings' in result:
                        recordings = result['recordings']
                        for recording in recordings:
                            if 'title' in recording:
                                title = recording['title']
                                artist = ''
                                for a in recording['artists']:
                                    artist += str(a['name'])+' '
                                artist.strip()
                                q = title+' '+artist
                                print('Identificada como '+q)
                                s = sp.search(q=q, type='track', limit=1)
                                if s['tracks']['items']:
                                    spid = "spotify:track:"+s['tracks']['items'][0]['id']
                                    print('Spotify id: '+spid)
                                    if spid not in spids:
                                        sp.playlist_add_items(playlist['id'],[spid])
                                        print('cancion agregada correctamente')
                                break
                        break
            # for score, recording_id, title, artist in acoustid.match('lFPruUAJVk', file):
            #     print(str(score)+' - '+str(title))
            print('--------------------------------------------')
        
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


