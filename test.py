import random
import time

chat1 = ["selam"]
chat2 = ['selam']

chat3 = ["nasılsın"]
chat4 = ["iyiyim"]

chat5 = ["adın ne"]
chat6 = ["uras"]

chat7 = ["bende uras'ım"]
chat8 = ["ozaman adaşız"]

def chat(input_text):
    input_text = input_text.lower()

    for a in chat1:
        if a in input_text:
            return random.choice(chat2)
        
    for s in chat3:
        if s in input_text:
            return random.choice(chat4)
        
    for d in chat5:
        if d in input_text:
            return random.choice(chat6)
        
    for f in chat7:
        if f in input_text:
            return random.choice(chat8)
        
    return "Anlayamadım..."

print("selam!!!")
while True:
    user = input("Sen: ")
    if user.lower() == "q":
        for x in range(10,0,-1):
            print(x)
            time.sleep(1)
        break
    cevap = chat(user)
    print("Bot:",cevap)