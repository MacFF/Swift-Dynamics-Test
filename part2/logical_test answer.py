
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
#อิๆ ฮิๆ
x = input("Enter number 0-10,000,000: ")
if int(x) <= 0 or int(x) > 10000000:
    print("Invalid value Please enter again")

z=len(x)
thai_text=''
number = {0:'',1:'หนึ่ง',2:'สอง',3:'สาม',4:'สี่',5:'ห้า',6:'หก',7:'เจ็ด',8:'แปด',9:'เก้า',10:'สิบ'} 
special = {0:'',1:'เอ็ด',2:'ยี่',3:'สาม',4:'สี่',5:'ห้า',6:'หก',7:'เจ็ด',8:'แปด',9:'เก้า',10:'สิบ'}
unit = ['','สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน']

j=1
for i in x:
    i=int(i)
    if i == 0 :
        y = number[i]
    elif z<=2 and x[-1]=='1' and x[-2] != '0':
        y = special[i] + "สิบ" + special[1]
        thai_text+=y
        break
    elif i != 0:
        y = number[i] + unit[len(x)-j]
    z-=1
    thai_text+=y
    j+=1
print(thai_text)
