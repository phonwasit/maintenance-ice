from tkinter import * #ดึงไลบรารี่
from tkinter import messagebox
import csv
from datetime import datetime

def writecsv(record_list):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(record_list)
GUI = Tk()

GUI.title('โปรแกรมซ่อมบำรุง by Phonwasit & Chatmongkol')
GUI.geometry('500x500+500+250')
# 500+250เป็นการระบุตำแหน่งจอแสดงผลให้โผล่ตรงจุดไหนตอนRUN
# x ที่ใช้สำหรับการคูณต้องเป็นตัวเล็ก

####FONT####
FONT1 = ('Angsana new',20)
FONT2 = ('Angsana new',15)
############

#Header#
L = Label(GUI, text='ใบแจ้งซ่อม',font=FONT1)
# ทำป้ายแสดง แต่ยังไม่ได้เอาไปวางในหน้าจอแสดงผล
L.pack()#คำสั่งจัดวางลงในหน้าจอแสดงผล


#E1 คือการสร้างกรอบคำสั่งสำหรับกรอกข้อมูลลงในหน้าจอแสดงผล
L = Label(GUI, text='ชื่อผู้แจ้ง :',font=FONT2)
L.place(x=30,y=50)
v_name = StringVar()
#สร้างตัวแปลพิเศษใช้กับGUI เพื่อให้มันรู้ว่าต้องเอาไปเก็บที่ไหน + ใส่คลาสให้มันว่าเป็นข้อมูลแบบไหน 
E1 = Entry(GUI, textvariable=v_name,font=FONT2)
#ยัดตัวแปรที่สร้างเข้าในช่องสำหรับกรอก
E1.place(x=150,y=50)
#-----------------------

L = Label(GUI, text='แผนก :',font=FONT2)
L.place(x=30,y=100)
v_department =StringVar()
E2 = Entry(GUI,textvariable=v_department,font=FONT2)
E2.place(x=150,y=100)
#-----------------------

L = Label(GUI, text='อุปกรณ์/เครื่องจักร :',font=FONT2)
L.place(x=30,y=150)
v_machine = StringVar()
E3 = Entry(GUI,textvariable=v_machine,font=FONT2)
E3.place(x=150,y=150)
#-----------------------

L = Label(GUI, text='อาการเสีย :',font=FONT2)
L.place(x=30,y=200)
v_problem = StringVar()
E4 = Entry(GUI,textvariable=v_problem,font=FONT2)
E4.place(x=150,y=200)
#-----------------------

L = Label(GUI, text='หมายเลข :',font=FONT2)
L.place(x=30,y=250)
v_number = StringVar()
E5 = Entry(GUI,textvariable=v_number,font=FONT2)
E5.place(x=150,y=250)
#-----------------------

L = Label(GUI, text='เบอร์โทร :',font=FONT2)
L.place(x=30,y=300)
v_tel= StringVar()
E6 = Entry(GUI,textvariable=v_tel,font=FONT2)
E6.place(x=150,y=300)
#-----------------------

def save():
    name = v_name.get() # .get() คือการดึงค่าออกมาจาก StringVar
    department = v_department.get()
    machine = v_machine.get()
    problem = v_problem.get()
    number = v_number.get()
    tel = v_tel.get()

    text = 'ชื่อผู้แจ้ง: ' + name + '\n'
    text = text + 'แผนก' + department + '\n'
    text = text + 'อุปกรณ์/เครื่องจักร' + machine + '\n'
    text = text + 'อาการเสีย' + problem + '\n'
    text = text + 'หมายเลข' + number + '\n'
    text = text + 'โทร' + tel + '\n'
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
    datalist = [dt,name,department,machine,problem,number,tel]
    writecsv(datalist)
    messagebox.showinfo('กำลังบันทึกข้อมูล...',text)
    


B = Button(GUI, text='บันทึกใบแจ้งซ่อม',command=save)
B.place(x=200,y=350)
#ปุ่ม


# L.pack()
# L.grid(row=0,column=0)
# L.place(x=20,y=100)
GUI.mainloop()
 
