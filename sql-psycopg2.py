import psycopg2

connection = psycopg2.connect(host="localhost", port="5432", database="chinook", user="postgres", password="Terminator-965")

cursor = connection.cursor()

cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

results = cursor.fetchall()

connection.close()

for result in results:
    print(result)