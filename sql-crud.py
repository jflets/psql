from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String
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

# create new class-based models


class Programer(base):
    __tablename__ = "Programers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


Session = sessionmaker(db)
session = Session()


base.metadata.create_all(db)


# create new records
ada_lovelace = Programer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programer"
)

alan_turing = Programer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Compting"
)

grace_hopper = Programer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margret_hamilton = Programer(
    first_name="Margret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_burners_lee = Programer(
    first_name="Tim",
    last_name="Burners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

jordan_fletson = Programer(
    first_name="Jordan",
    last_name="Fletson",
    gender="M",
    nationality="British",
    famous_for="Software Engineer"
)

# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margret_hamilton)
# session.add(bill_gates)
# session.add(tim_burners_lee)
# session.add(jordan_fletson)
# session.commit()

# programmer = session.query(Programer).filter_by(id=7).first()
# programmer.famous_for = "World President"

# session.commit()

# people = session.query(Programer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# deleting a record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programer = session.query(Programer).filter_by(
#     first_name=fname, last_name=lname).first()
# # defensive programming
# if programer is not None:
#     print("Programer Found: ", programer.first_name + " " + programer.last_name)
#     confirmation = input(
#         "Are you sure you want to delete this record? (y/n): ")
#     if confirmation == "y":
#         session.delete(programer)
#         session.commit()
#         print("Record deleted")
#     else:
#         print("Record not deleted")
# else:
#     print("Programer not found")


programers = session.query(Programer)
for programer in programers:
    print(
        programer.id,
        programer.first_name + " " + programer.last_name,
        programer.gender,
        programer.nationality,
        programer.famous_for,
        sep=" | "
    )
