import time
import requests
from prettytable import PrettyTable
from colorama import init, Fore, Back, Style

api_url = "http://qt.gtimg.cn/q="
codes = ["sz000665","sz000702","sz000756","sz002031","sz002194","sz002415","sz002454","sz002547","sz002579","sz002909","sh510050","sz159625","sz159857"]

table = PrettyTable(['名称','实价','昨收','今开','涨跌(元)','涨跌幅','最高','最低','成交额(万)','时间','涨停价','跌停价'])
init(autoreset=False)

for code in codes:
    result = requests.get(api_url+code)
    result_array = result.text.split('~')
    if float(result_array[32]) >= 5:
        result_array[32] = Style.BRIGHT + Fore.LIGHTRED_EX + result_array[32] + Fore.RESET
        #result_array[32] = "\033[0;31;40m" + result_array[32] + "\033[0m"
    elif float(result_array[32]) <= -5:
        result_array[32] = Style.BRIGHT + Fore.GREEN + result_array[32] + Fore.RESET
        #result_array[32] = "\033[0;32m" + result_array[32] + "\033[0m"
    table.add_row([result_array[1],result_array[3],result_array[4],result_array[5],result_array[31],result_array[32],result_array[33],result_array[34],result_array[37],result_array[30][4:8]+'-'+result_array[30][8:],result_array[47],result_array[48]])
    time.sleep(0.5)

print(table)