
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

number = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X'
          ,20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LLX',80:'LXXX',90:'XC',100:'C'
          ,200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM',1000:'M'}

x = int(input())
result = ''


if x <= 0 or x>1000:
    print('Invalid value Please enter again')
else:
    for i in sorted(number.keys(), reverse=True):
        while x >= i:
            result += number[i]
            x -= i
    print(result)

