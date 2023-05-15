import time
import requests
from prettytable import PrettyTable
from colorama import init, Fore, Back, Style

api_url = "http://qt.gtimg.cn/q="
codes = ["sz000665","sz000702","sz000756","sz002031","sz002194","sz002415","sz002454","sz002547","sz002579","sz002909","sh510050","sz159601","sz159625","sz159857","sh510300","sh516160","sh513330","sh513180","sh513060","sh513050","sh512480","sh512200","sh512170","sh510900"]

#0: 未知 1: 名字 2: 代码 3: 当前价格 4: 昨收 5: 今开 6: 成交量（手）7: 外盘 8: 内盘 9: 买一 10: 买一量（手）11-18: 买二 买五 19: 卖一 20: 卖一量 21-28: 卖二 卖五 29: 最近逐笔成交 30: 时间 31: 涨跌 32: 涨跌%
#33: 最高 34: 最低 35: 价格/成交量（手）/成交额 36: 成交量（手）37: 成交额（万）38: 换手率 39: 市盈率 40: 41: 最高 42: 最低 43: 振幅 44: 流通市值 45: 总市值 46: 市净率 47: 涨停价 48: 跌停价

table = PrettyTable(['名称','实价','昨收','今开','涨跌(元)','涨跌幅%','最高','最低','成交额(万)','换手率','时间','涨停价','跌停价'])
init(autoreset=False)

for code in codes:
    result = requests.get(api_url+code)
    result_array = result.text.split('~')
    if float(result_array[32]) >= 3:
        result_array[32] = Style.BRIGHT + Fore.LIGHTRED_EX + result_array[32] + Fore.RESET
        #result_array[32] = "\033[0;31;40m" + result_array[32] + "\033[0m"
    elif float(result_array[32]) <= -3:
        result_array[32] = Style.BRIGHT + Fore.GREEN + result_array[32] + Fore.RESET
        #result_array[32] = "\033[0;32m" + result_array[32] + "\033[0m"

    table.add_row([result_array[1],result_array[3],result_array[4],result_array[5],result_array[31],result_array[32]+'%',result_array[33],result_array[34],result_array[37],result_array[38],result_array[30][4:8]+'-'+result_array[30][8:],result_array[47],result_array[48]])
    time.sleep(1)

print(table)