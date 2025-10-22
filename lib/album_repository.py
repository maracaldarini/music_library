from lib.album import *

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums
    
    def find(self, album_id):
        rows = self._connection.execute('SELECT * FROM albums WHERE id = %s', [album_id]) #returns a list containing a dict containing the data for the retrieved album
        row = rows[0] #only one itwm should be return as id should be a unique number, so grab the first (and only) item in the list
        album = Album(row["id"], row["title"], row["release_year"], row["artist_id"]) #create a new Album object with the extracted data
        return album