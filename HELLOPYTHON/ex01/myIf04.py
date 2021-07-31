'''
Created on 2021. 2. 1. 가위바위보.

@author: ����..����
'''

import random
mine = input("가위바위보를 입력하세요")

rnd = random.random()

com = ""
if rnd<0.33 :
    com = "가위"
elif 0.33<rnd<0.66 :
    com = "바위"
elif 0.66 < rnd :
    com= "보"       




result = ""

if com == "바위" and mine == "가위" or com == "보" and mine == "바위" or com == "가위" and mine == "보" :
    result = "짐"
elif com == mine :
    result = "비김"
else : 
    result = "이김" 
    
print("com:" + com)
print("mine:" + mine)
print("result:" + result)