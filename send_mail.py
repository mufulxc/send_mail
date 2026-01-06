
from dotenv import load_dotenv
import yagmail,os

load_dotenv()
EMAIL= os.getenv("EMAIL")
QQ_AUTH_CODE = os.getenv("QQ_AUTH_CODE")
QQ_RECEIVER_EMAIL = os.getenv("QQ_RECEIVER_EMAIL")



def send_email(subject, contents):
    yag = yagmail.SMTP(user=EMAIL, password=QQ_AUTH_CODE, host='smtp.qq.com')
    yag.send(to=QQ_RECEIVER_EMAIL, subject=subject, contents=contents)
    print("邮件发送成功")

if __name__ == '__main__':
    send_email("测试", "测试邮件")
    
    
    
    
'''  
    
git add .                                   # 添加所有改动
git commit -m "添加定时邮件功能"            # 提交，消息随便写
git push                                    # 推送（因为你之前设置过跟踪，直接 push 就行）
git push origin main                        # 推送(如果你之前没有设置过跟踪, 需要指定分支名)


git remote remove origin                    # 先删除旧的远程(如果有)
git remote add origin https://github.com/mufulxc/send_mail.git # 添加新的远程

然后正常添加、提交、推送: bash

git add .
git commit -m "初次上传: 定时发送邮件项目"
git branch -M main                          # 确保分支叫 main
git push -u origin main

推送时如果弹出浏览器让你授权, 就按提示同意; 或者输入用户名和 Token(和之前一样).

完成! 刷新 https://github.com/mufulxc/send_mail 就能看到你的代码了.


git remote -v  #正在推送到哪个地址      
git remote set-url origin https://github.com/mufulxc/send_mail.git  #修改远程地址
git remote set-url origin 新的仓库地址
git remote -v  #确认是否修改成功


git push -u origin main  #推送


git add .            # 添加所有改动
git commit -m "init"  # 提交, 消息随便写
git branch -M main    # 确保分支叫 main
git push -u origin main  # 推送(因为你之前设置过跟踪, 直接 push 就行)






'''