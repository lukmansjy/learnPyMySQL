import pymysql

db = pymysql.connect("localhost", "root", "", "learnPyMySQL")

cursor = db.cursor()

sql = "SELECT * FROM mahasiswa"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        name = row[1]
        address = row[2]
        print("id: %d, Nama mahasiswa: %s, alamat: %s" % \
            (id, name, address ))
except:
    db.rollback()

db.close()