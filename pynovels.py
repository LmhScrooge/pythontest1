from bs4 import BeautifulSoup
from  urllib import request

if __name__ =="__main__":
    novel_url = 'http://www.biqukan.com/1_1094/5403177.html'
    head = {}
    head['User-Agent'] =  'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    novel_req = request.Request(url = novel_url,headers = head)
    novel_response = request.urlopen(novel_req)
    novel_html = novel_response.read().decode('gbk','ignore')
    soup_novel = BeautifulSoup(novel_html,'lxml')
    novel_text = soup_novel.find_all(id = 'content',class_ = 'showtxt')
    delete_text = BeautifulSoup(str(novel_text),'lxml')
    print(delete_text.div.text.replace('\xa0',''))