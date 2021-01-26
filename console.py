import pdb
from models.artist import Artist
from models.album import Album

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete(all)
artist_repository.delete(all)

artist_1 = Artist("Bob Dylan")
artist_repository.save(artist_1)

artist_2 = Artist("Old Crow Medicine Club")
artist_repository.save(artist_2)

album_1 = Album("Another Side of Bob Dylan", artist_1, "folk")
album_repository.save(album_1)

album_2 = Album("OCMS", artist_2, "folk")
album_repository.save(album_2)

album = Album("Desire", artist_1, "folk")
album_repository.save(album)

pdb.set_trace()
