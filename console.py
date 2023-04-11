from repositories import album_repository
from repositories import artist_repository

from models.album import Album
from models.artist import Artist

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist('Sleep Token')
artist_repository.save(artist_1)

artist_2 = Artist('MIA')
artist_repository.save(artist_2)

artist_3 = Artist('Wu-Tang Clan')
artist_repository.save(artist_3)

album_1 = Album('This Place Will Be Your Tomb', 'Metal', artist_1)
album_repository.save(album_1)

album_2 = Album('Take Me To Eden', 'Metal', artist_1)
album_repository.save(album_2)

album_3 = Album('Mata', 'World Music', artist_2)
album_repository.save(album_3)

album_4 = Album('Matangi', 'World Music', artist_2)
album_repository.save(album_4)

album_5 = Album('36 Chambers', 'Hip Hop', artist_3)
album_repository.save(album_5)

artist_3.name = 'Lady Gaga'
artist_repository.update(artist_3)

result = artist_repository.get_albums(artist_1)
for album in result:
    print(album.__dict__)

artist_repository.select_all()
album_repository.select_all()

