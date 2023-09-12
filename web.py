import requests
import json
import time
class Search:
    def __init__(self):
        self.headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "Host":"www.jingshibang.com",
            "cookie":"auth.strategy=local3; auth._refresh_token.local3=false; auth._token.local3=Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ3d3cuamluZ3NoaWJhbmcuY29tIiwiYXVkIjoid3d3LmppbmdzaGliYW5nLmNvbSIsImlhdCI6MTY5NDIzNzM5MCwibmJmIjoxNjk0MjM3MzkwLCJleHAiOjE2OTQ4NDIxOTAsImp0aSI6eyJpZCI6NTEyODU4LCJ0eXBlIjoid2VjaGF0In19.QCd8cePpq1DFxMZWo58QdXXTbGA2QMnjE4xBE0x6Abc; PHPSESSID=aa0539e167f75cbcf3bad25f6dd78659".encode("UTF-8"),
            "Accept":"application / json, text / plain, * / *",
            "Accept-Encoding":"gzip, deflate",

        }


    def get_hotlist(self):
        w=requests.get("http://www.jingshibang.com/api/liulan/hotKeyword",headers=self.headers)
        lst=[i["keyword"] for i in json.loads(w.text)["data"]]
        return lst

    def search(self,keyword,num):
        url=f"http://www.jingshibang.com/api/products?page=1&limit={num}&keyword={keyword}&selectOrder="
        w=requests.get(url)
        data=json.loads(w.text)["data"]
        #print(data)
        lst=[]
        for i in data:
            try:
                id=i["id"]
                name=i["store_name"]
                t=i["add_time"]
                is_pdf=bool(i["pdf_answer"])
                url=self.is_pan(id,is_pdf,i)
                lst.append({"id":id,"name":name,"time":t,"is_pdf":is_pdf,"url":url})
            except:
                pass
        return lst

    def is_pan(self,id,is_pdf,data):
        if is_pdf:
            return "http://www.jingshibang.com"+data["pdf_answer"]
        w=requests.get(f'http://www.jingshibang.com/api/product/detailpc/{id}',headers=self.headers)
        url=json.loads(w.text)["data"]["storeInfo"]["baidu_url"]+"?pwd="+json.loads(w.text)["data"]["storeInfo"]["baidu_pw"]
        return url

class Get:
    def __init__(self):
        self.headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "Host":"www.jingshibang.com",
            "cookie":"auth.strategy=local3; auth._refresh_token.local3=false; auth._token.local3=Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ3d3cuamluZ3NoaWJhbmcuY29tIiwiYXVkIjoid3d3LmppbmdzaGliYW5nLmNvbSIsImlhdCI6MTY5NDIzNzM5MCwibmJmIjoxNjk0MjM3MzkwLCJleHAiOjE2OTQ4NDIxOTAsImp0aSI6eyJpZCI6NTEyODU4LCJ0eXBlIjoid2VjaGF0In19.QCd8cePpq1DFxMZWo58QdXXTbGA2QMnjE4xBE0x6Abc; PHPSESSID=aa0539e167f75cbcf3bad25f6dd78659".encode("UTF-8"),
            "Accept":"application / json, text / plain, * / *",
            "Accept-Encoding":"gzip, deflate",

        }
    def get_hotlist(self):
        url="http://www.jingshibang.com/api/liulan/hotlist"
        data=json.loads(requests.get(url,headers=self.headers).text)
        lst=[]
        for d in data["data"]:
            id=d["id"]
            w=requests.get(f'http://www.jingshibang.com/api/product/detailpc/{id}',headers=self.headers)
            i=json.loads(w.text)["data"]["storeInfo"]
            id = i["id"]
            name = i["store_name"]
            t = i["add_time"]
            is_pdf = bool(i["pdf_answer"])
            url = self.is_pan(id, is_pdf, i)
            lst.append({"id": id, "name": name, "time": time.ctime(t)[20:]+"-"+str(["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].index(time.ctime(t)[4:7]))+"-"+time.ctime(t)[9:11], "is_pdf": is_pdf, "url": url})
        return lst
    def is_pan(self,id,is_pdf,data):
        if is_pdf:
            return "http://www.jingshibang.com"+data["pdf_answer"]
        url=data["baidu_url"]+"?pwd="+data["baidu_pw"]
        return url

if __name__=="__main__":
    search=Search()
    get=Get()
    print(get.get_hotlist())