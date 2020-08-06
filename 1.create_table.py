import pymysql

db = pymysql.connect("localhost", "root", "", "learnPyMySQL")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS MAHASISWA")

sql = """CREATE TABLE mahasiswa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(30) NOT NULL,
    alamat VARCHAR(30) NOT NULL)"""

cursor.execute(sql)

db.close()