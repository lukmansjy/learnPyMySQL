import pymysql

db = pymysql.connect("localhost", "root", "", "learnPyMySQL")

cursor = db.cursor()

sql = "UPDATE mahasiswa SET alamat = '%s' WHERE id = %d" % ("Selogiri", 1)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()