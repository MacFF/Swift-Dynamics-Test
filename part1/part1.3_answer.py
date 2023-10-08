"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python 
โดยห้ามใช้ math.factorial เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว
"""
def factorial(num):
    result = 1
    answer = 0
    for i in range(1,num+1):
        result = result*i
    x=str(result)
    for j in range(1,len(x)+1):
        if x[-j] == '0':
            answer+=1
        else :
            return answer

print(factorial(13))