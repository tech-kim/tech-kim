import random
import time
import hgtk

word_list = [
    "오랫동안 기다려 왔어","내가 원한 너였기에",
    "슬픔을 감추며 널 보내줬었지",
    "날 속여가면서",
    "잡고 싶었는지 몰라",
    "너의 눈물 속에 내 모습",
    "아직까지 남아있어",
    "추억을 버리긴 너무나 아쉬워",
    "난 너를 기억해 이젠 말할께",
    "나의 오랜 기다림",
    "너 떠나고 너의 미소",
    "볼 수 없지만 항상 기억할께",
    "너의 그 모든걸 사랑보다 깊은",
    "상처만 준 난 이젠 깨달았어",
    "후회하고 있다는걸",
]

random.shuffle(word_list)
list_len = len(word_list)
current_count = 0

while current_count < list_len:
    q = word_list[current_count]
    current_count += 1
    

    start_time = time.time()
    user_input = input(q + '\n')
    end_time = time.time() - start_time
    
    src = hgtk.text.decompose(q).replace("ᴥ","")
    tar = hgtk.text.decompose(user_input).replace("ᴥ","")

    for c in enumerate(src, start-0):
        prince(i,c)
