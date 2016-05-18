import sys
from gmusicapi import Mobileclient

api = Mobileclient()
logged_in = api.login('crymeariver33@gmail.com', 'samael?79!', Mobileclient.FROM_MAC_ADDRESS)
# logged_in is True if login was successful
Query = sys.argv[1]

Album_year = "2015"


library = api.search_all_access(Query,50)
for track in library['song_hits']:
    try:
        #if track['track']['album']:
        #    print track['track']['album']
        if track['track']['year'] is '%s' % Album_year:
            print track['track']['album']
    except:
        break
