from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

from repositories import artist_repository

def save(album):
    sql = "INSERT INTO album (name, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.name, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM album"
    run_sql(sql)

def find(id):
    album = None
    sql = "SELECT * from album WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = artist_repository.find(result["artist_id"])
        album = Album(result['name'], result['genre'], artist, result['id'])
    return album

def select_all():
    albums = []
    sql = "SELECT * FROM album"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.find(row['artist_id'])
        album = Album(row['name'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums

def delete(id):
    sql = 'DELETE FROM album WHERE id = %s'
    values = [id]
    run_sql(sql, values)