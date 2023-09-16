
># bjtk-expand

>A program to get materials  which is limited to not be download on the question bank.

# 北京题库拓展 应用程序
## 引言
_（这段是作者的絮絮叨叨，不感兴趣可以跳过）_

本项目可以用于下载来自“[北京题库](http://www.jingshibang.com/home/)”的资料。这些试题、汇编等内容通常是限制下载或收费的。

作为一名中学生，我个人认为，不管是为了中考高考还是自我提升，练习是很有效的一个方式。

很庆幸，我找到了一个好用且相对不那么黑心的平台，也就是刚才所说的，“北京题库”。

![“北京题库”网页端页面截图](https://cdn-community.codemao.cn/47/community/d2ViXzMwMDFfNzkyODc1NV81NjQyODdfMTY5NDgyOTY0ODM4MV8wMmJmYWEwYg.png)

这一平台，当时是我的数学老师向我推荐的，不得不说这是十分适合（尤其是北京地区的）学生所使用的。

该平台的使用限制是，非会员（微信登录）每日限制下载两篇免费文档，会员不受限制且可以下载付费文档。

虽然这个平台主要是老师在使用，但不知道是不是我的极少数老师没那么负责，还是需要我们自己去搜集试卷。

那么这样一来，个人使用的弊端就展现出来了。

随着年级的增长、课业的增加和个人需求，我发现这些资料越来越不够用。

于是就尝试着去用各种手段扒出了这个平台的API，当时正好我在了解JavaScript，就顺手编写了一段油猴脚本，这个后面会再提到。随后又制作了PC端和Andriod的版本。

总之，这就是，我设计这个项目的初衷。

## 程序使用
### PC端程序
PC段程序是使用Pyside2设计的图形交互程序。由于众所周知的，这个库的加载时间，打包成应用程序后将会慢到极致。

所以，在此推荐在电脑上配置python环境。我（开发时）的环境配置是这样的：
1. windows 10
2. python 3.10.6
3. pyperclip 1.8.2
4. pyside2 5.15.2.1
5. qrcode 7.4.2
6. requests  2.28.2
7. matplotlib 3.7.1

以及我在程序中使用了两种字体，存放在/ttf文件夹中，需进行下载

虽然还没有测试该程序在其他操作系统上的运行情况，但我想应该是问题不大的。

**程序的使用：**
程序分为四部分：标题、热门文档、搜索、底部状态栏。它们相对互相独立。
![如图](https://cdn-community.codemao.cn/47/community/d2ViXzMwMDFfNzkyODc1NV81NjQyODdfMTY5NDgzMDkyNTg2M18zY2Q5NTYwZA.png)
在点击同意后，将解锁功能使用
![](https://cdn-community.codemao.cn/47/community/d2ViXzMwMDFfNzkyODc1NV81NjQyODdfMTY5NDgzMTA5MDQ3N180OWU1Y2I3Mg.png)
（当然，你也可以改代码，我也管不着）

“获取”与“搜索”之间完全独立。可以分开使用。

获取的内容由可选项，但暂未开发完成
![](https://cdn-community.codemao.cn/47/community/d2ViXzMwMDFfNzkyODc1NV81NjQyODdfMTY5NDgzMTIyOTAwNl84NGZkYmExZg.png)

搜索的候选词为热搜词，点击按钮将添加到文本输入框中
![](https://cdn-community.codemao.cn/47/community/d2ViXzMwMDFfNzkyODc1NV81NjQyODdfMTY5NDgzMTM3MjA1NF84YWU4MDhiOQ.png)

点击“获取”或“搜索”后，需要一点时间进行网络请求

请求结束后，将会把结果展示在列表框中。期间会禁用下方下载按钮
![](https://cdn-community.codemao.cn/47/community/d2ViXzMwMDFfNzkyODc1NV81NjQyODdfMTY5NDgzMTU2NTY2OF84NjY1YWMwMw.png)

单击选择一个文档后，将会解锁相应的下载按钮：
![](https://cdn-community.codemao.cn/47/community/d2ViXzMwMDFfNzkyODc1NV81NjQyODdfMTY5NDgzMTY3OTkzMF80ZmZkYmExMw.png)

点击后将打开浏览器。