import requests
from lxml import etree
import json 
import time


#url
baseUrl ="http://www.gzhfpc.gov.cn/ztzl_500663/xxgzbdgrdfyyqfk/yqdt"
html = requests.get("http://www.gzhfpc.gov.cn/ztzl_500663/xxgzbdgrdfyyqfk/yqdt/")
api = "https://sc.ftqq.com/SCU78158T2d9bda1bdb1f64ff7df37c7d2da869cb5e23adf537f6a.send"
filename = "chechRepeat.json"
coding = html.apparent_encoding
html.coding = "utf-8"
path_title ='//div[@class="right_list f_r f14"]//script[@type="text/javascript"]//text()'
tree = etree.HTML(html.content) 
node_title = tree.xpath(path_title)
# print(node_title[0])
node_title = str(node_title[0])
start_num  =node_title.find("str_1")+10
end_num = node_title.find("html\";")+4
detailUrl =baseUrl+node_title[start_num:end_num]
print(detailUrl)


start_num2  =node_title.find("str_2")+9


public_date = node_title[start_num2:start_num2+10]

print(public_date)

start_num3  =node_title.find("str_3")+9
end_num3 = node_title.find('if (str=="")')

gzTitle = node_title[start_num3:end_num3-2]
gzTitle =gzTitle[0:gzTitle.find('";')]
print(gzTitle)



content =  " 💊 [点击查看详细:]"+"(" + detailUrl+")";
             

#send Message
data = {
   "text":gzTitle,
   "desp":content
}
nowDate  = time.strftime("%Y-%m-%d",time.localtime())

readFile = open("./chechRepeat.json")
readFile = json.load(readFile)
sentMessage = readFile['gzTitle']
print(sentMessage)



outJson = {
	'detailUrl':detailUrl,
	'public_date':public_date,
	'gzTitle':gzTitle,
}

if(sentMessage==gzTitle):
	print("sent this Message")
else:
	req = requests.post(api,data = data)
	with open(filename,'w') as file_obj:
		json.dump(outJson,file_obj)






