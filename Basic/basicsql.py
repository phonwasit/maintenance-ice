##basicsql.py

#สร้างตารางฐานข้อมูล
#หลักๆให้ไปดูในโปรแกรมหลักว่าจะใช้ค่าอะไรบ้างจำนวนเท่าไหร่กี่ค่า?
import sqlite3
'''
name = v_name.get() # .get() คือการดึงค่าออกมาจาก StringVar
    department = v_department.get()
    machine = v_machine.get()
    problem = v_problem.get()
    number = v_number.get()
    tel = v_tel.get()
'''
#จากbasicgui เอาไว้ดู

#สร้างconnection เพื่อเชื่อมต่อกับฐานข้อมูล
conn = sqlite3.connect('maintenance.sqlite3')

#สร้าง cursor # ตัวที่เอาไว้สั่งคำสั่ง sql
c = conn.cursor()
#ตัวพิมพ์ใหญ่คือคำสั่งของโปรแกรมSQL
c.execute(""" CREATE TABLE IF NOT EXISTS mt_workorder (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    tsid TEXT, 
                    name TEXT,
                    department TEXT,
                    machine TEXT,
                    problem TEXT,
                    number TEXT,
                    tel TEXT) """)


def insert_mtworkorder(tsid,name,department,machine,problem,number,tel):
    #CREATE
    with conn:
        command = 'INSERT INTO mt_workorder VALUES (?,?,?,?,?,?,?,?)'#ใส่ตามจำนวนตัวแปร
        c.execute(command,(None,tsid,name,department,machine,problem,number,tel))
#None ในบรรทัดที่37เอามาเพื่อสร้าง ID อัตโนมัติ
    conn.commit() #save database
    print('saved')    



def view_mtworkorder():
    #READ
    with conn:
        command = 'SELECT * FROM mt_workorder'
        c.execute(command)
        result = c.fetchall() #เอาตั้งหมด ดูตรง fetch มันมีหลายตัว
    print(result)
    return result#ส่งค่าเอาออกมาใช้


def update_mtworkorder(tsid,field,newvalue):
    #UPDATE
    with conn:
        command = 'UPDATE mt_workorder SET {} = (?)WHERE tsid=(?)'.format(field) #ตัว ? จะใช้กับพวกcommand
        c.execute(command,(newvalue,tsid))
    conn.commit()
    print('updated')




def delete_mtworkorder(tsid):
    #DELETE
    with conn:
        command = 'DELETE FROM mt_workorder WHERE tsid=(?)'
        c.execute(command,([tsid])) #ถ้าใส่ค่าแค่อันเดียวให้ใส่วงเล็บ2ชั้น ถ้ามากกว่า1 ใส่วงเล็บชั้นเดียว
    conn.commit()
    print('deleted')   




#insert_mtworkorder('TS1002','ไอซ์','ซ่อมบำรุง','เครื่องปริ้น','เปิดไม่ติด','P01','0629899614')
#update_mtworkorder('TS1002','problem','หมุนผิดทาง')
#delete_mtworkorder('TS1002')
#result = view_mtworkorder()
#print(result[1][1]) #เลือกดึงข้อมูลจากdatabase ออกมาใช้

  