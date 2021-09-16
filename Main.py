# -*- coding: utf-8 -*-
# =============================================================================
# 歡迎大家一起加入肥宅的行列
# 有人像折木奉太郎嗎 ?
# =============================================================================

from random import randint as r, choices as c
from os import system as cmd, name as sys_name
import re

# 更改後面數字，可以使該則訊息更常出現
greasy_end = {
    ' wwwwwwww':  2,
    ' (笑':       1,
    ' (燦笑':     1,
    ' (推眼鏡':   2,
    ' (摸摸頭':   1,
    ' (茶':       1,
    ' (歪頭':     1,
    ' (汗顏':     1,
    ' (噗哧':     1,
    ' (嘿嘿':     1,
    ' (喂！':     1,
    ' (遠望':     2,
    ' (乖乖':     1
    }

greasy_front = {
    '嘛 ':        1,
    '阿咧阿咧 ':  1,
    '欸都 ':      2,
    '摁姆.. ':    1
    }

greasy_chaos = {
    ' (黑化': 1,
    ' (射精': 1,
    ' (勃起': 2,
    ' (捶牆壁': 1,
    ' (撕心裂肺地笑著': 1,
    ' (憤怒': 1,
    ' (憤怒槌牆': 2,
    ' (深深恨著自己': 1
    }

def _cls():
    cmd('cls' if sys_name == 'nt' else 'clear')

def main():
    # input nerd msg
    shit = int(input("噁心指數(請輸入1~9): "))
    if shit >= 8:
        print("\n爻 已x黑x化 爻")
        global greasy_end
        greasy_end = {**greasy_end, **greasy_chaos}
    msg = ""
    _str = input("\n\n  輸入要轉換的文章\n  有分行的文章請直接貼上\n  (輸入'q'結束輸入))\n> ")
    while _str != 'q':
        msg = msg + _str + "\n"
        _str = input()
    # split to list
    msg = re.split('，|。|！|\n|!|;|\?|；|？', str(msg))
    # merge
    output = []
    for i in msg:
        if i == '':
            continue
        if r(0, 9-shit) == 0:
            i = c(list(greasy_front.keys()), weights = tuple(greasy_front.values()), k = 1)[0] + i
        if r(0, 9) <= shit:
            i = i + c(list(greasy_end.keys()), weights = tuple(greasy_end.values()), k = 1)[0]
        output.append(i + "\n")
    # clean screen
    _cls()
    # print result
    [print(i, end = "") for i in output]

if __name__ == '__main__':
    while True:
        main()
        if input("\n\n輸入\'cls\'清除螢幕! : ") == "cls":
            _cls()
else:
    exit
