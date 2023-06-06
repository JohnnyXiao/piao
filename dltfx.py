import random
import numpy as np
import xlrd, xlwt


houxuan = [1,2,5,7,8,9,10,11,19,21,22,24,25]
zshu = [1,2,5,7,11,19]
hshu = [8,9,10,21,22,24,25]
jshu = [1,5,7,9,11,19,21,25]
oshu = [2,8,10,22,24]
tongwei = [[1,11,21],[2,22],[5,25],[9,19]]
lianhao = [[1,2],[7,8,9,10,11],[21,22],[24,25]]

redAll = set(range(1, 34))
zhishu = {1,2,3,5,7,11,13,17,19,23,29,31}
heshu = redAll - zhishu

xiaoshu = set(range(1, 17))
dashu = set(range(18, 34))

data = xlrd.open_workbook(r".\data\ssq_origin_data.xlsx")

table = data.sheets()[0]
#print(table.nrows, table.ncols)
rows = table.get_rows()
def getLatestN(n):
    set_latest5 = {1} & {2}
    for m in range(n):
        cellValue_str = table.row(m+1)[2].value
        #print(fr'cellValue_str: {cellValue_str}')
        cellValue_set = set(int(item) for item in cellValue_str.split(' '))    #将列表中str元素转成int再将整个列表转成set

        set_latest5 = set_latest5 | cellValue_set     #近5合集
        # print(set_latest5)
        # print(len(set_latest5))
    # print(set_latest5)
    # print(len(set_latest5))
    return list(set_latest5)

def getLatestSeq():
    latestSeq = table.row(1)[1].value
    return latestSeq

def getHeshuNum(s):
    n = 0
    for i in s:
        if i in list(heshu):
            n += 1
    return n

def getXiaoshuNum(s):
    n = 0
    for i in s:
        if i in xiaoshu:
            n += 1
    return n

def getOushuNum(s):
    n = 0
    for i in s:
        if i % 2 == 0:
            n += 1
    return n

def get2LianNum(s):
    n = 0
    s.sort()
    for i in range(len(s) - 1):
        if abs(s[i] - s[i + 1]) == 1:
            n += 1
    return n

def get3LianNum(s):
    n = 0
    s.sort()
    for i in range(len(s) - 2):
        if abs(s[i] - s[i + 1]) == 1 and abs(s[i + 1] - s[i + 2]) == 1:
            n += 1
    return n

def getUnitSameNum(s):
    n = 0
    dic = {}
    for i in s:
        unit = i % 10
        if unit in dic.keys():
            dic[unit] += 1
        else:
            dic[unit] = 1
    # print(dic)
    for value in dic.values():
        if value == 2 or value == 3:
            n += 1
    return n

def getRegionNum(s):
    # 参考:[1,2,3]
    dic = {
        'R1': 0,
        'R2': 0,
        'R3': 0
    }
    for i in s:
        if i in range(1, 12):
            dic['R1'] += 1
        elif i in range(12, 23):
            dic['R2'] += 1
        else:
            dic['R3'] += 1
    return dic

def getChongNum(s):
    prev = getLatestN(1)
    n = 0
    for i in s:
        if i in prev:
            n += 1
    # print(f'前一期：{prev}')
    return n

def getGeNum(s):
    pPrev = set(getLatestN(2)) - set(getLatestN(1))
    n = 0
    for i in s:
        if i in pPrev:
            n += 1
    # print(f'前前一期：{pPrev}')
    return n

def getLingNum(s):
    prev = getLatestN(1)
    n = 0
    for i in s:
        if i == 1:
            if 33 in prev:
                n += 1

            if 2 in prev:
                n += 1
        elif i == 33:
            if 32 in prev:
                n += 1

            if 1 in prev:
                n += 1
        else:
            if (i - 1) in prev:
                n += 1

            if (i + 1) in prev:
                n += 1
    return n

def getXieLian3Num(s):
    pPrev = set(getLatestN(2)) - set(getLatestN(1))  # 倒数第二
    n = 0
    for i in s:
        if i == 1:
            if 33 in getLatestN(1) and 32 in pPrev:
                n += 1

            if 2 in getLatestN(1) and 3 in pPrev:
                n += 1
        elif i == 2:
            if 1 in getLatestN(1) and 33 in pPrev:
                n += 1

            if 3 in getLatestN(1) and 4 in pPrev:
                n += 1
        elif i == 32:
            if 31 in getLatestN(1) and 30 in pPrev:
                n += 1

            if 33 in getLatestN(1) and 1 in pPrev:
                n += 1
        elif i == 33:
            if 32 in getLatestN(1) and 31 in pPrev:
                n += 1

            if 1 in getLatestN(1) and 2 in pPrev:
                n += 1
        else:
            if (i - 1) in getLatestN(1) and (i - 2) in pPrev:
                n += 1

            if (i + 1) in getLatestN(1) and (i + 2) in pPrev:
                n += 1
    return n

def rangeball(num, houxuan):
    n = 0
    selectNum = 0
    allBlue = list(range(1, 17))
    # choice blueball
    blueDone = random.choice(allBlue)
    latestSeq = getLatestSeq()
    print(f'{int(latestSeq) + 1}：')
    while 1:
        if houxuan:
            red_houxuan = houxuan
        else:
            #red_houxuan = [1,2,5,7,8,9,10,11,19,21,22,24,25]
            red_houxuan = redAll

        if n < num:
            selectNum += 1
            # choice redball
            # 1.先从近N里选x，再剩余选y
            # redDone1 = random.sample(red_houxuan, 4)
            # redDone2 = random.sample(list(redAll - set(red_houxuan)), 2)
            # #redDone = set(redDone1) | set(float(i) for i in redDone2)
            # redDone = set(redDone1) | set(redDone2)

            # 2.直接全部里选x+y
            redDone = np.random.choice(list(redAll), 6, replace=False)

            ou = getOushuNum(redDone)
            xiao = getXiaoshuNum(redDone)
            he = getHeshuNum(redDone)
            lian_2 = get2LianNum(list(redDone))
            lian_3 = get3LianNum(list(redDone))
            tong = getUnitSameNum(redDone)
            region = getRegionNum(redDone)
            chong = getChongNum(redDone)
            ge = getGeNum(redDone)
            ling = getLingNum(redDone)
            xielian3 = getXieLian3Num(redDone)

            if len(set(redDone) & set(red_houxuan)) == 4 and ou in range(2, 5) and xiao in range(2, 5) and he in range(3, 6)\
                    and lian_2 in range(0, 3) and lian_3 <= 1 and tong in [1, 2] and not (set(region.values()) & {0, 4, 5, 6}) \
                    and chong in [0, 1, 2] and ge in [1, 2, 3] and ling in [2, 3, 4] and xielian3 in [0, 1, 2]:
                # choice result
                print(fr"偶:{ou}  小:{xiao}  合:{he}  2连:{lian_2}  3连:{lian_3}  同尾:{tong}组  3区:{'_'.join(str(i) for i in region.values())}  重:{chong}  隔:{ge}  邻:{ling}  斜3:{xielian3},  {' '.join(str(i) for i in sorted(redDone))} + {blueDone}")
                n += 1
            else:
                continue
        else:
            print(f'CHOICE OVER! total: {selectNum}')
            break

if __name__ == "__main__":
    Latest5 = getLatestN(5)
    print(f'latest n is: {Latest5}, {len(Latest5)}')
    rangeball(5, Latest5)
    # getRegionNum([1,5,12,15,19,29,30])
    # getChongNum([6,5,12,15,19,29,26])
