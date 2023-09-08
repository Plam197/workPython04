#function 2 : Have Parameters/No Return
#parameter คือ ตัวแปรประเภทหนึ่ง ขอบเขตการใช้งานพารามิเตอร์
#จะใช้ได้เฉพาะในฟังก์ชันนั้นๆ เท่านั้น

def funcA(x, y) :
    print(' hi')
    z = x + y
    print(f'{x} + {y} = {z}')
    #ไม่มีคำสั่ง return

def funcB(x) :
    print(f"x is {x} 555....")
funcA(10, 20) #Argument อากิวเมนต์
funcA(5, 5)
funcB('SAU  IOT')
