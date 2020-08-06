import pymysql

db = pymysql.connect("localhost", "root", "", "learnPyMySQL")

cursor = db.cursor()

sql = "DELETE FROM mahasiswa WHERE id = '%d'" % (4)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()