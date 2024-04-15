##---------------pirveli davaleba--------------
num1 = int(input("shemoiyvanet pirveli ricxvi:"))
num2 = int(input("shemoiyvanet meore ricxvi:"))

if num1 > num2:
    print("pirveli ricxvi metia meoreze")
elif num1 < num2:
    print("meore ricxvi metia pirvelze")
else:
    print("ricxvebi tolia")

##---------------meore davaleba-------------
score = 10
answer = int(input("25 % 5 == ? - ra unda eweros kitxvisnishnis adgilas rom iyos true"))
while answer != 0:
    answer = int(input("pasuxi arasworia scadet xelaxla"))
    score -= 1

answer = int(input("meramdene davalebaa es pythonshi?"))
while answer != 3:
    answer = int(input("pasuxi arasworia scadet xelaxla"))
    score -= 1

answer = input("ra aris germaniis dedaqalaqi?").lower() ## BERLINI
while answer != "berlini":
    answer = input("pasuxi arasworia scadet xelaxla").lower()
    score -= 1

answer = input("romeli zgva mdebareobs saqartvelos dasavletit").lower()
while answer != "shavi zgva":
    answer = input("pasuxi arasworia scadet xelaxla").lower()
    score -= 1
answer = int(input("2 + 2(2+2)=?"))
while answer != 10:
    answer = int(input("pasuxi arasworia scadet xelaxla"))
    score -= 1

print("your score is {score}/10")