from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artist (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE FROM artist"
    run_sql(sql)

def find(id):
    artist = None
    sql = "SELECT * from artist WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = Artist(result['name'], result['id'])
    return artist

def select_all():
    artists = []
    sql = "SELECT * FROM artist"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists

def delete(id):
    sql = 'DELETE FROM artist WHERE id = %s'
    values = [id]
    run_sql(sql, values)

def get_albums(artist):
    albums = []
    sql = 'SELECT * FROM album WHERE artist_id = %s'
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row['name'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums

def update(artist):
    sql = "UPDATE artist SET name = %s WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)
    