from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey,
    Float
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_credentials = {
    "username": "postgres",
    "password": "Terminator-965",
    "host": "localhost",
    "port": "5432",
    "database": "chinook"
}

db_url = f"postgresql://{db_credentials['username']}:{db_credentials['password']}@{db_credentials['host']}:{db_credentials['port']}/{db_credentials['database']}"

db = create_engine(db_url)

base = declarative_base()


class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


Session = sessionmaker(db)
session = Session()


base.metadata.create_all(db)


# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )
