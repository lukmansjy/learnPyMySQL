import pymysql

db = pymysql.connect("localhost", "root", "", "learnPyMySQL")

cursor = db.cursor()

# sql = """INSERT INTO mahasiswa (nama, alamat) VALUES ('Lukman Sanjaya', 'Wonogiri')"""

sql = "INSERT INTO mahasiswa(nama, alamat) VALUES ('%s', '%s' )" % \
    ('Lukman S', 'Selogiri')

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()