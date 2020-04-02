import mysql.connector
from sqlfolder.connection import connection
class Student:
    connection = connection
    cursor = connection.cursor()

    def __init__(self,studentNumber,name,surname,birthdate,gender):
        self.StudentNumber= studentNumber
        self.name= name
        self.surname= surname
        self.birthdate= birthdate
        self.gender= gender
    def addStudent(self):
        sql = "INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.StudentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.cursor.execute(sql,value)

        try:
            connection.commit()
            print(f"{Student.cursor.rowcount} tane kayıt eklendi...")
        except mysql.connector.Error as err:
            print("hata= ",err)
        finally:
            connection.close
    @staticmethod
    def addMany(liste):
        sql = "INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        Student.cursor.executemany(sql,liste)
        try:
            connection.commit()
            print(f"{Student.cursor.rowcount} tane kayıt eklendi...")
        except mysql.connector.Error as err:
            print("hata= ", err)
        finally:
            connection.close
    @staticmethod
    def getAllRecords():
        Student.cursor.execute("SELECT * FROM student")
        result = Student.cursor.fetchall()
        for student in result:
            print(student)

    @staticmethod
    def getelementbyid(id):
        sql = f"Select * From student Where id={id}"
        Student.cursor.execute(sql)
        res = Student.cursor.fetchone()
        print(f"Ogrenci no: {res[1]}, Isim: {res[2]}, Soyisim: {res[3]}, Date: {res[4]}")
    @staticmethod
    def howmanyrows():
        sql= "SELECT COUNT(*) From student"
        Student.cursor.execute(sql)
        howmany = Student.cursor.fetchone()

        print(f"{howmany} tane kayıt var.")
    @staticmethod
    def getgirls():
        sql= "SELECT * From student Where gender='F' "
        Student.cursor.execute(sql)
        list = Student.cursor.fetchall()
        for i in list:
            print(f"Ogrenci no: {i[1]}, Isim: {i[2]}, Soyisim: {i[3]}, Date: {i[4]}")
    @staticmethod
    def getinfofromyear(year):
        sql= f"SELECT * From Student Where YEAR(birthdate)= {year} "
        Student.cursor.execute(sql)
        year = Student.cursor.fetchall()
        if year == "none":
            print("Hiç kayıt yok")
        else:
            for i in year:
                print(f"Ogrenci no: {i[1]}, Isim: {i[2]}, Soyisim: {i[3]}, Date: {i[4]}")
    @staticmethod
    def getnamelike(info):
        sql = f"Select * From student Where name like '%{info}%' "
        Student.cursor.execute(sql)
        info = Student.cursor.fetchall()
        for i in info:
            print(f"Ogrenci no: {i[1]}, Isim: {i[2]}, Soyisim: {i[3]}, Date: {i[4]}")
    @staticmethod
    def countgender(gender):
        sql=f"SELECT * From student where gender= '{gender}'"
        Student.cursor.execute(sql)
        count = Student.cursor.fetchall()
        if gender == "M":
            print(f"{len(count)} kadar erkek var")
        else:
            print(f"{len(count)} kadar kadın var")












