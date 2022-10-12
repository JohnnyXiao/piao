import requests
import json

url = "http://chartssq.caiminbang.com/port/client_json.php?lotteryName=FC_SSQ&transactionType=10008&daytime=600&type=H_LHFB&timeId=-1&t=0.23087346175407886"

header = {
}

result = requests.get(url)
issue_data = json.loads(result.text)["list"]
print("期和：" + str(len(issue_data)))

appear_sum = json.loads(result.text)["footList"][0]
appear_sum_lian = appear_sum["footStr"][-10:-4]
#print(appear_sum)
#print(appear_sum_lian)
print("0L概率：" + str(100 * appear_sum_lian[0] / len(issue_data)) + "%")
print("2L概率：" + str(100 * appear_sum_lian[1] / len(issue_data)) + "%")
print("3L概率：" + str(100 * appear_sum_lian[2] / len(issue_data)) + "%")
print("4L概率：" + str(100 * appear_sum_lian[3] / len(issue_data)) + "%")

dir_22L = []
dir_23L = []
dir_24L = []
for item in issue_data:
    sumAttrib = item["sumAttrib"].split(",")
    if sumAttrib[1] == '-' and sumAttrib[3] == '-':
        #print("2L+4L:  " + item["issue"] + " : " + item["winNum"])
        #print("-----------------------------------")
        dir_24L.append(item["issue"] + " : " + item["winNum"])
    elif sumAttrib[1] == '-' and sumAttrib[2] == '-':
        #print("2L+3L:  " + item["issue"] + " : " + item["winNum"])
        #print("-----------------------------------")
        dir_23L.append(item["issue"] + " : " + item["winNum"])
    elif sumAttrib[1] == '-' and (sumAttrib[8] == '-' or sumAttrib[9] == '-'):
        #print("2L+2L:  " + item["issue"] + " : " + item["winNum"])
        #print("-----------------------------------")
        dir_22L.append(item["issue"] + " : " + item["winNum"])
#print("2L: " + str(dir_22L))
#print("23L: " + str(dir_23L))
#print("24L: " + str(dir_24L))