import random

kor = ["불고기", "설렁탕", "삼겹살", "김치찌게", "삼계탕", "순대" ]
foriegn = ["스파게티", "피자", "탕수육", "스테이크"]
random.shuffle(kor)
random.shuffle(foriegn)

f = []

def ideal_type():
    if len(a)%2 == 0: #짝수명이면 부전승 없이
        loop = len(a) // 2
        for i in range(0, loop): #대결 팀 배정
            while True:
                if loop == 1:
                    print("<< 준결승 >>n")
                else:
                    print("<< 제 %d 강 >>n " %(2**loop))
                print("%s vs %s" %(a[i], a[i+1]))         
                print("앞 음식이 맘에 들면 1번을, 뒷 음식이 맘에들면 2번을 입력")
                print("n 입력:", end = ' ')
                temp = int(input())
                print()
                if temp == 1:
                    a.remove(a[i+1]) 
                    break
                elif temp == 2:
                    a.remove(a[i])   
                    break
                else:
                    print("잘못 입력하셨습니다. 다시 입력하세요.")
                    print()

