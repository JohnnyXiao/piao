import random

import xlrd, xlwt


houxuan = [1,2,5,7,8,9,10,11,19,21,22,24,25]
zshu = [1,2,5,7,11,19]
hshu = [8,9,10,21,22,24,25]
jshu = [1,5,7,9,11,19,21,25]
oshu = [2,8,10,22,24]
tongwei = [[1,11,21],[2,22],[5,25],[9,19]]
lianhao = [[1,2],[7,8,9,10,11],[21,22],[24,25]]

#data = xlrd.open_workbook(r"E:\workspace\code\piao\data\1112.xlsx")

# table = data.sheets()[0]
# print(table.nrows,table.ncols)
# rows = table.get_rows()
# for row in rows:
#     print(row[1])


def rangeball(num):
    for n in range(num):
        allRed = list(range(1,34))
        allBlue = list(range(1,17))
        redDone = []

        # choice redball
        for i in range(1, 7):
            redTemp = random.choice(allRed)
            redDone.append(redTemp)
            allRed.remove(redTemp)

        # choice blueball
        blueDone = random.choice(allBlue)
        # choice result
        print(f"{sorted(redDone)}   {blueDone}")

if __name__ == "__main__":
    rangeball(5)