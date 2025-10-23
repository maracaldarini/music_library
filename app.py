from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

# file: app.py

from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")
        self._album_repository = AlbumRepository(self._connection)
        self._artist_repository = ArtistRepository(self._connection)

    def run(self):

        print("Welcome to the music library manager!\n")
        print("What would you like to do?\n")
        print(" 1 - List all albums?")
        print(" 2 - List all artists?\n")
        x = input("Enter your choice: ")

        if int(x) in [1, 2]:
            print("")
            if int(x) == 1:
                albums = self._album_repository.all()
                for album in albums:
                    print(f" * {album.id} - {album.title}")
            elif int(x) == 2:
                artists = self._artist_repository.all()
                for artist in artists:
                    print(f" * {artist.id} - {artist.name}")
        else:
            print("\nInvalid choice. Please enter 1 or 2\n")
            self.run()

        

if __name__ == '__main__':
    app = Application()
    app.run()

""" 
# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
for artist in artists:
    print(artist)

# Retrieve all albums
album_repository = AlbumRepository(connection)
albums = album_repository.all()

# List them out
for album in albums:
    print(album)

# Find album with id = 3
album_repository = AlbumRepository(connection)
album_id_1 = album_repository.find(1)

# Print it out
print(album_id_1) """