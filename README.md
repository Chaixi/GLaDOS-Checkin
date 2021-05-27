# GLaDOS-Checkin
【可添加server酱推送】GLaDOS每日自动签到，凭运气获得使用天数+1。  
最近老是Get 0 day！给个1很难吗>_<  

## 一、Glados注册使用
注册链接：_[https://github.com/glados-network/GLaDOS](https://github.com/glados-network/GLaDOS)_  
输入邀请码 __8PIBH-8ITVA-RE79R-XO1S9__ 激活账号并额外获得3天使用天数。  

注册成功后通过配置Clashx客户端使用，支持Windows、MacOS、Android、Linux.  
Clashx使用说明 _[http://www.xmstudent.ml/post-24.html](http://www.xmstudent.ml/post-24.html)_  
Glados网站上也有使用说明，简单清晰。

## 二、自动签到配置步骤
### 1、fork本仓库到自己的GitHub
![image](https://user-images.githubusercontent.com/26132150/119796161-b52b6e80-bf0b-11eb-86e9-706bbc4d01c7.png)


### 2、设置账号信息
Settings→Secrets→New repository secret；

变量说明：
| Name | Value | 说明 |
| ---- | ---- | ---- |
| COOKIE | \_ga=... | [cookie获取方式](#jump)，多个账号的cookie之间用'-\*-'连接即可，如'cookie1-\*-cookie2-\*-cookie3' |
| SERVER | on/off | 是否打开server酱的微信推送 |
| SCKEY | server酱的sckey | 如果SERVER=off，则SCKEY的value可不填 |

![image](https://user-images.githubusercontent.com/26132150/119796269-cffde300-bf0b-11eb-80d3-eb50fd160921.png)
![image](https://user-images.githubusercontent.com/26132150/119796291-d5f3c400-bf0b-11eb-891f-0d5339f49ff4.png)

### 3、启用GitHub action
启用GitHub action，并修改任意文件commit一次即可运行；  
![image](https://user-images.githubusercontent.com/26132150/119796388-eb68ee00-bf0b-11eb-84db-2cb6f23aa4f2.png)

### 4、查看运行结果
Actions→workflow runs→build→checkin.  
微信收到推送通知。
![image](https://user-images.githubusercontent.com/26132150/119796508-02a7db80-bf0c-11eb-9e5d-b410fb9632a0.png)


## 三、GLaDOS介绍
一款稳定好用的国际网络加速器，免费版本的速度还行，能满足某G开头搜索引擎的日常使用，也有收费版本可选，不算贵。  
如果你有教育邮箱（.edu邮箱）的话，恭喜你，可以使用他们提供的Education Plan，正常情况下可使用360天，每月50G流量。    
![image](https://user-images.githubusercontent.com/26132150/119796984-6b8f5380-bf0c-11eb-8e39-c8beede092b9.png)

每日签到可获取免费使用天数。  
![image](https://user-images.githubusercontent.com/26132150/119797036-76e27f00-bf0c-11eb-9048-86c95245ea8c.png)

## <span id="jump">四、获取账号cookie </span>
1. 进入官网登录界面；  
2. 按下键盘F12打开开发者界面，并选择Network；  
3. 输入账号和登录码登录；  
4. 登录完成后在开发者界面中选择第一条请求（clash？），在右侧找到Request Headers，其中的cookie值就是我们所需要的value，复制下来直接粘贴到Secrets中COOKIE的Value就行。  
![image](https://user-images.githubusercontent.com/26132150/119799784-ff621f00-bf0e-11eb-886f-b463b7df7d5b.png)

