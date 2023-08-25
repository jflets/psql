from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Float,
    Integer,
    String,
    ForeignKey,
    MetaData
)

db_credentials = {
    "username": "postgres",
    "password": "Terminator-965",
    "host": "localhost",
    "port": "5432",
    "database": "chinook"
}

db_url = f"postgresql://{db_credentials['username']}:{db_credentials['password']}@{db_credentials['host']}:{db_credentials['port']}/{db_credentials['database']}"

db = create_engine(db_url)

meta = MetaData(db)

artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String),
)

album_table: Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Miliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

with db.connect() as connection:

    # select_query = artist_table.select()
    # select_query = artist_table.select().with_only_columns([
    #     artist_table.c.Name])
    select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)
