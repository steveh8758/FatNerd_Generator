# -*- coding: utf-8 -*-
# =============================================================================
# 歡迎大家一起加入肥宅的行列
# 有人像折木奉太郎嗎 ?
# =============================================================================

from random import randint as r, choices as c
from os import system as cmd

# 更改後面數字，可以使該則訊息更常出現
greasy_end = {
    ' wwwwwwww':  3,
    ' (笑':       1,
    ' (燦笑':     1,
    ' (推眼鏡':   1,
    ' (摸摸頭':   5,
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
    ' (撕心裂肺地笑著': 3,
    ' (憤怒': 1,
    ' (憤怒槌牆': 1,
    ' (深深恨著自己': 1
    }


def main():
    # input nerd msg
    shit = int(input("噁心指數(請輸入1~9): "))
    if shit >= 7:
        print("已黑化")
        global greasy_end
        greasy_end = {**greasy_end, **greasy_chaos}
    msg = ""
    _str = input("\n\n> 輸入要轉換的文章\n  有分行的文章請直接貼上\n  (輸入'q'結束輸入))\n: ")
    while _str != 'q':
        msg = msg + _str + "\n"
        _str = input()
    # split to list
    msg = msg.split("\n")[0:-1]
    # merge
    output = []
    for i in msg:
        if i == '':
            continue
        if r(0, 11-shit) == 0:
            i = c(list(greasy_front.keys()), weights = tuple(greasy_front.values()), k = 1)[0] + i
        if r(0, 9) <= shit:
            i = i + c(list(greasy_end.keys()), weights = tuple(greasy_end.values()), k = 1)[0]
        output.append(i + "\n")
    # clean screen
    try:
        cmd("clear")
    except:
        cmd("cls")
    # print result
    [print(i, end = "") for i in output]

if __name__ == '__main__':
    main()
else:
    exit
