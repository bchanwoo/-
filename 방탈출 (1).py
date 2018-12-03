print("<<<방탈출하기>>>")
print("공지: <<당신의 생존 여부는 오로지 당신의 선택에 달려있습니다.>>")

print("---------------------------------------------------------")

print("당신은 어느 폐쇄된 방에서 눈을 떴습니다. 왜 여기에서 눈을 떴는지는 기억하지 못합니다, 그러나 여기에서 나가야되는 것 한가지는 기억이 납니다.")
input("당신의 이름을 알려주세요:")

print("눈을 뜨니 당신 손목에는 기계가 씌여있습니다. 그 기계 화면에는 다음과 같이 써져있습니다.")
print("한 도로에서 차가 막히고 있다. 이 2차선 도로는 아슬아슬하게 차 2대가 지나갈 정도로 좁다.'''1시간 정체되면 100대, 2시간이면 차량 200대가 막혀 버린다. 오직 자동차로 인해서만 교통체증이 발생할 경우, 3시간의 정체를 발생시키려면 최소 몇대의 차량이 필요할까?'''")
num = int(input("정답을 입력하시오:"))
        
if num==1:
        print("철컥 소리와 함께 족쇄가 풀렸습니다.")
else:
        print("족쇄가 폭발해 당신은 죽었습니다.")
       
if num==1:
    print(" 족쇄가 풀려난 당신은 주변을 둘러봅니다. '''주변은 어느 고풍스러운 저택의 침실처럼 꾸며져 있었으며 온통 빨간색으로 꾸며져있습니다. 방 한쪽에는 창문이 있었다. 당신은 나가기 위해 문은 열려했지만 잠겨있었고 아무리 문릉 부수려해도 흠집도 나지 않았습니다.'''")
    print("절망하던 당신의 눈 앞에 침대 위에 놓여있는 한 쪽지를 발견합니다")
    print(" 무수한 톱니바퀴로 이루어져있으며 어느 특정한 순간마다 째깍거리는 물체에 다음 단계가 존재한다.")
    tmp=str(input())
    if tmp == '괘종시계':
        print("당신은 괘종시계 앞으로 가서 또 다른 쪽지를 발견한다.")
        print("Israel, Egypt, 3rd war, length?")
        num = int(input("정답을 입력하시오:"))


if num==6:
        print("당신의 6을 눌렀고 그와 동시에 괘종시계의 12시 부분에서 열쇠가 튀어나왔다.")
else:
        print("시계에서 전기가 흘러나와 당신은 죽었습니다.")
if num==6:
        print("당신은 열쇠를 문에다가 꽃아보았지만 맞지 않았다. 열받은 당신은 씩씩거리고 있던 와중에 전자 금고를 발견하고 다가간다.")
        print("전자금고에는 다음과 같은 문구가 새겨져있었다. '''3X3짜리 나무판이 존재한다. 중앙을 지나는 가로, 세로, 대각선의 각각의 열의 합이 모두 동일하도록 1~51의 숫자 중에서 9개의 숫자를 써넣으려고 한다. 열의 합계가 가장 크게 되도록 하려면 중앙의 나무판에는 어떤 숫자를 넣어야 할까?'''")
        num = int(input("정답을 입력하세요"))

if num==51:
        print("전자 금고가 철컥하는 소리와 함께 열렸고 그 안에는 작은 전자금고가 하나 더 있었다.")
else:
        print("금고가 폭발해 당신은 죽었습니다.")

if num==51:
        print("작은 전자 금고에는 다음과 같이 쓰여져있었다. '''조커를 뺸 52장 1세트의 트럼프가 있다. 이 52장을 잘 섞어서 26장씩 2개(A,B)로 나누었다. 이때 A에 있는 검은 카드의 매수와 B에 있는 빨간 카드의 매수가 정확히 일치하는 일은 1000번중 몇 번 일어날 수 있을까?'''")
        num = int(input("정답을 입력하시오:"))

if num==1000:
        print(" 철컥 소리와 함께 금고가 열렸고 그 안에는 자물쇠가 걸려있는 작은 상자가 있었다.")
else:
        print("금고가 폭발해 당신은 죽었습니다.")

if num==1000:
    print("아까 받은 열쇠로 상자를 열어보니 또다른 열쇠가하나 더 있었습니다.")
    print("그 열쇠로 당신은 방문을 열었다.")
    print("방문 너머에는...... 또다른 방이 있었고 바닥에는 쓰러진 남자가 있었다. 당신은 절망했지만 이내 쓰러진 남성에게 달려가 맥박을 재보니 이미 죽어있었다.")
    print("깊은 절망감에 빠진 당신은 절규하지만 이내 남자의 손에 쥐어진 피묻은 쪽지를 발견한다. 쪽지에는 두껍고 둔탁한 느낌의 필기체로 글씨가 쓰여있었다.")
    print("당신이 이 쪽지를 읽고 있다면 아마 난 죽었겠지. 여기는 빠져나갈 수 없는 미궁이다. 1년동안 나가려고 노력했지만 도저히 출구를 찾을 수가 없었다. 방문 너머에는 언제나 빨간 침실이 나를 기다리고 있었다. 이 쪽지를 읽고 있는 당신 아마 절망한 상태일지도 모르겠군.")
    print("하지만 방법이 하나 있다. 나는 1년동안 방들을 헤매면서 유일한 탈출구에 관한 증거를 얻을 수가 있었다. ''' ∫∫∫v ÷ FdV = ∫∫sF·ndS, 이곳에 다음 힌트가 있을 것이다.'''")
    if tmp == '가우스':
        print("당신은 책장에서 가우스가 생전에 집필했던 정수론 연구를 펼쳐 들니 또다른 쪽지가 있었다.")
        print("'''4명의 어부와 7명의 사람 그리고 배신자 1명이 있네'''")
    if tmp == '12사도':
        print("당신은 성경을 집어들어서 마태복음 10장을 피니 한 쪽지가 끼어있었다.")
        print("내 계산에 따르면 이곳은 수만개의 방으로 이루어진 미로다. 그리고 그 어느방에도 탈출구가 없다. 수년간의 방황 끝에 나는 한가지 사실을 발견했다. 아무리 많은 시간이 지나도 내가 전혀 배가 고프지 않았다는 사실이다. 죽음, 죽음만이 유일한 탈출구라는 사실, 그 하나만은 변하지 않았다.")
        print("당신은 그 쪽지를 읽고 당황한다. 죽음이라고? 유일한 탈출구가.... 죽음이라고?")
        print("마음을 추스린 당신은 다시 쪽지를 읽어내려가기 시작한다.")
        print("죽음이 유일한 탈출구인 것을 꺠달은 당신들에게 도움이 될 수 있게 한가지 방법을 제시해주겠다. 방 구석에 있는 전자금고 안에는 장전되어있는 권총 하나가 놓여있다. 그걸 사용하라. 내 가설이 맞다면 아마 당신이 눈을 다시 뜰 쯤에 내가 옆에 있을 것이다.")
        print("당신은 오랫동안 망설였지만 결국 현실을 인정하고 전자금고쪽으로 다가간다.")
        print("
