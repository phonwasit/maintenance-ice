def hello():#defคือย่อมาจากdefine เพื่อประกาศสร้างฟังก์ชั่น
    print('hello,My name is ice')

#hello()



def hellofriend(name):
    print(f'hello,My name is {name}')
#hellofriend('ice1')



def checkNameAge(name,age=80):#name กับ Age เป็นParameter 
    print(f'hello,My name is {name}')
    print(f'I am {age} years old.')
    # f เป็นการนำค่าของparameter ไปแทรกในคำสั่ง print
#checkNameAge('ice',30)
#checkNameAge(age=30,name='ize')
#checkNameAge('ice',age=100)



def addNumber(x,y):
    return x + y #ฟังก์ชั่นไหนที่มี return เราต้องสร้างตัวแปรเอาไว้เก็บค่าด้วย
sum = addNumber(10,20)#สร้างตัวแปร sum เอาไว้เก็บค่าของฟังก์ชั่นก่อน แล้วค่อยสั่งprintตัวแปรนั้นออกมา
#หลังจากนั้นจะเอาตัวแปร sum ไปทำอะไรก็ตามใจ
#print(sum)



#คำสั่งif - else เป็นคำสั่งเงื้่อนไขที่มีทางเลือกในการทำงานขึ้นอยู่กับสถานการณ์ที่เราเขียนให้เพื่อเป็นทางเลือกในการทำงานของฟังก์ชั่น
#ตัวอย่างคำสั่ง ในการหาปีที่มี 366 วัน(กุมภาพันธ์มี 29 วัน)
#หลักการ เอาปี คศ หาร 4 ถ้าปีไหนลงตัว หรือ หาร 100 ไม่ลงตัว คือใช่
#ถ้ามีคศ ใด หารด้วย 400 ลงตัวก็คือใช่
#year = int(input('ปี ค.ศ. :'))
#if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
    #print(f'ค.ศ. {year} เป็น leap year')
#else:
    #print(f'ค.ศ. {year} ไม่เป็น leap year')





##ต่อไปเป็นเรื่องของการประกาศตัวแปรที่เก็บค่าได้มากกว่า 1 ค่า
color = ['red','green','blue']#ใช้ก้ามปูในการประกาศแล้วใช้คอมม่าในการแยกเป็นชุดๆโดยเรียงลำดับเป็นชุดๆ 
#เรียกอีกอย่างว่า index โดยเริ่มจากตำแหน่งที่ 0 --> 1 --> 2
#print(color[0]) #ถ้าใช้ตำแหน่งที่ 0 output จะออกเป็น red 
##print(color[1]) #ถ้าใช้ตำแหน่งที่ 1 output จะออกเป็น green
#print(color[2]) #ถ้าใช้ตำแหน่งที่ 2 output จะออกเป็น blue
#ถ้าเมื่อไหร่ใช้ค่า-1 มันจะเริ่มจากตำแหน่งขวาสุด -2 ก็ตัวถัดมา


#วิธีการเพิ่มสมาชิกในตัวแปร
color.append('yellow')
#มันจะไปเพิ่มเป็นตัวสุดท้าย(ทางขวาสุด)

#การทำซ้ำๅ(วนลูป)
for c in color:
    print(c)


#การใส่ # หลายบรรทัด ให้ลากคลุมให้หมด แล้วกด Ctrl + / 

