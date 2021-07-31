import time

temp = 9999
print(temp)
while True :
    if temp < 2 :
       print("참")
       print(temp) 
       time.sleep(5)
    else : 
        print("그짓")
        temp = 1
        time.sleep(5)