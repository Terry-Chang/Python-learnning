#while()迴圈
import random
com=random.randint(1,100)
print("電腦骰出的數字為:",com)
input("請輸入Roll來骰出你的數字:")
player=random.randint(1,100)
print("你骰出的數字為:",player)
while com>(player-1):
    input("真可惜, 要再玩一次請輸入Roll:")
    player=random.randint(1,100)
    print("你骰出的數字為:",player)
else:
    print("恭喜你!!")