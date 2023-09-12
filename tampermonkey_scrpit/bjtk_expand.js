// ==UserScript==
// @name         北京题库使用优化
// @namespace    none
// @version      2.0
// @description  下载来自“北京题库”的试题
// @author       Mornwind
// @match        *://www.jingshibang.com/*
// @icon         http://www.jingshibang.com/home/_nuxt/img/jsblogo.c73ccde.png
// @grant        GM_xmlhttpRequest
// ==/UserScript==

(function() {
    var name,text,tp,pdf,word,tt;
    'use strict';
    function downloadTxt(fileName, content) {
        let a = document.createElement('a');
        a.href = 'data:text/plain;charset=utf-8,' + content
        a.download = fileName
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    }
    function directDownload(url, filename) {
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", filename);
        document.body.appendChild(link);
        link.click();
        link.remove();
    }
    function downloadPdf(url,name) {
        let list = {
            url,
            name: name,
            type: 'pdf'
        }
        downloadFile(list)
    }


    function downloadFile(data) {
        fetchDownloadFile(data)
    }

    function fetchDownloadFile(data) {
        fetch(data.url, {
            method: "get",
            mode: "cors",
        })
            .then((response) => response.blob())
            .then((res) => {
            const downloadUrl = window.URL.createObjectURL(
                //new Blob() 对后端返回文件流类型处理
                new Blob([res], {
                    type: data.type == "pdf" ? "application/pdf" : data.type == "word" ?
                    "application/msword" : data.type == "xlsx" ? "application/vnd.ms-excel" : ""
                })
            );
            //word文档为msword,pdf文档为pdf
            const link = document.createElement("a");
            link.href = downloadUrl;
            link.setAttribute("download", data.name);
            document.body.appendChild(link);
            link.click();
            link.remove();
        }).catch((error) => {
            window.open(data.url);
        });
    };
    //获取Base64
    function pathToBase64(url) {
        return new Promise((resolve, reject) => {
            let image = new Image();
            image.onload = function() {
                let canvas = document.createElement('canvas');
                canvas.width = this.naturalWidth;
                canvas.height = this.naturalHeight;
                canvas.getContext('2d').drawImage(image, 0, 0);
                let result = canvas.toDataURL('image/png')
                resolve(result);
            };
            image.setAttribute("crossOrigin", 'Anonymous');
            image.src = url
            image.onerror = () => {
                reject(new Error('urlToBase64 error'));
            };
        })
    }
    function get(id){
        console.log(id)
        GM_xmlhttpRequest({
            method:"get",
            url:"http://www.jingshibang.com/api/product/detailpc/"+id,
            //headers:header,
            async onload({ response }) {
                name=JSON.parse(response).data.storeInfo.store_name
                if(JSON.parse(response).data.storeInfo.store_type=="专辑"){
                    tp="txt"
                    text="第三方文档：\n"+JSON.parse(response).data.storeInfo.store_name+"\n百度网盘链接："+JSON.parse(response).data.storeInfo.baidu_url+"\n提取码："+JSON.parse(response).data.storeInfo.baidu_pw
                    name=JSON.parse(response).data.storeInfo.store_name
                }
                else{
                    tp="normal"
                    word="http://www.jingshibang.com"+JSON.parse(response).data.storeInfo.word_answer
                    pdf="https://jsb2022-1253627302.cos.ap-beijing.myqcloud.com"+JSON.parse(response).data.storeInfo.pdf_answer
                }
                if(name.indexOf("：")!=-1){
                    tt=name.split("：").slice(-1)[0]
                }
                else{
                    tt=name
                }
            }
        })
    }
    function getPDF(url){
        var flag=confirm("是否下载word?")
        if(flag){
            window.location.href=word
        }
        downloadPdf(pdf,name)
    }
    function downloadPageT(){
        for(var i=1; i<10**10;i++){
            try{
                getPDF(document.querySelector("#__layout > div > div.index.wrapper_1200_no > div.acea-row > div.rightdiv > div.list.tablelist > a:nth-child("+i+")").href)
            }
            catch (e) {break }
        }
    }
    function downloadPageE(){
        for(var i=1; i<10**10;i++){
            try{
                getPDF(document.querySelector("#__layout > div > div.index.wrapper_1200_no > div > div:nth-child(2) > div.list.tablelist > a:nth-child("+i+")").href)
            }
            catch (e) {break }
        }
    }
    function titleChange(content) {
        if (document.querySelector("title") && document.querySelector("title").innerHTML != content) {
            document.querySelector("title").innerHTML = content
        }
    }
    function open(e){
        console.log(e)
        try{
            name=e.target.innerText
            console.log(name)
            var url="http://www.jingshibang.com/api/products?page=1&limit=99&keyword="+name
            GM_xmlhttpRequest({
                method:"get",
                url:url,
                //headers:header,
                async onload({ response }) {
                    const data=JSON.parse(response).data
                    var pro
                    for(var i=0;i<=data.length;i++){
                        pro=data.slice(i)[0]
                        console.log(pro)
                        if(pro.store_name==name){
                            window.open("http://www.jingshibang.com"+pro.pdf_answer)
                            download(pro.id)
                        }
                    }
                }
            })
        }
        catch(ep){
            console.log(ep)
        }
    }
    function download(id){
        console.log(id)
        GM_xmlhttpRequest({
            method:"get",
            url:"http://www.jingshibang.com/api/product/detailpc/"+id,
            //headers:header,
            async onload({ response }) {
                console.log(response)
                name=JSON.parse(response).data.storeInfo.store_name
                if(JSON.parse(response).data.storeInfo.store_type=="专辑"){
                    tp="txt"
                    text="第三方文档：\n"+JSON.parse(response).data.storeInfo.store_name+"\n百度网盘链接："+JSON.parse(response).data.storeInfo.baidu_url+"\n提取码："+JSON.parse(response).data.storeInfo.baidu_pw
                    name=JSON.parse(response).data.storeInfo.store_name
                }
                else{
                    tp="normal"
                    word="http://www.jingshibang.com"+JSON.parse(response).data.storeInfo.word_answer
                    pdf="https://jsb2022-1253627302.cos.ap-beijing.myqcloud.com"+JSON.parse(response).data.storeInfo.pdf_answer
                }
                if(name.indexOf("：")!=-1){
                    tt=name.split("：").slice(-1)[0]
                }
                else{
                    tt=name
                }

                console.log(tp)
                if(tp=="normal"){
                    window.location.href=word
                    downloadPdf(pdf,name)
                }
                else{
                    downloadTxt(name,text)
                }
            }
        })
    }

    try{
        var url=window.location.href
        var id=url.split("id=").slice(-1)[0]
        try{
            id=id.split("&").slice(0)[0]
        }
        catch (e) { }
        get(id)
    }
    catch(e){}
    document.onclick = function (e) {
        console.log(e)
        if (e.ctrlKey && e.shiftKey){
            if(window.location.href.indexOf("id")!=-1){
                getPDF(window.location.href);
            }
            else{
                open(e)
            }
            /*if(window.location.href=="http://www.jingshibang.com/home/"){
                downloadPageT()
            }
            if(window.location.href=="http://www.jingshibang.com/home/paper"){
                downloadPageE()
            }*/
        }
    }
})();