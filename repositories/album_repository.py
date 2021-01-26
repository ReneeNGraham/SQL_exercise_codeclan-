from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository


def save(album):
   sql = f"INSERT INTO albums (title, artist_id, genre) VALUES (%s, %s, %s) RETURNING*"
   values = [album.title, album.artist.id, album.genre]
   results = run_sql(sql, values)
   id = results[0]['id']
   album.id = id
   return album


def delete_all():
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select(id):
    album = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]


def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], artist ,row['genre'], row['id'])
        albums.append(album)
    return albums
        
# Extensions

def delete(id):
    sql = "DELETE FROM albums WHERE ID = %s"
    values = [id]
    run_sql(sql, values) 

def update(album):
    sql = "UPDATE albums SET (title, artist_id, genre) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.artist.id, album.genre, album.id]
    run_sql(sql, values)
