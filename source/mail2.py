
# 必要なライブラリのインポート

import smtplib, ssl
from email.mime.text import MIMEText
import pickle
import os
import sys
import copy
import configparser
import getpass

args = sys.argv
os.chdir(os.path.dirname(args[0]))
def hostadd():
    host2=input(' smtpサーバのホスト名 >> ')
    port=input(' smtpサーバのポート番号 >> ')
    account = input(' ユーザー名 >> ')
    from_email=account
    print('')
    password = getpass.getpass()
    k=input(' セッション情報を記憶しますか？　(Y or N) >> ')
    if k=="Y" or k=="y":
        filename=input(' セッションファイル名 >> ')
        filename=filename+".bin"
        config = configparser.ConfigParser()
        config.read('.\\host.ini')
        section2 = 'profile'
        config.add_section(section2)
        config.set(section2, 'file', filename)
        cc=config.get(section2, 'hostc')
        cc=cc+1
        config.set(section2, 'hostc', cc)
        with open('.\\host.ini', 'w') as file:
            config.write(file)
        print(' ')
        print(' 記憶したセッション情報をクリアするには\n アプリケーションディレクトリ内の「profile.bin」を削除してください')
        print('')
        cgn=input(' 次回からユーザー情報の入力を省略します (Enter) >>')
        usear=[account,password,cgn,host2,port]
        f=open(filename,'wb')
        pickle.dump(usear,f)
        f.close()

cds=0
j=len(args)
if j==2 and args[1]=='-a':
    hostadd()
    j=0
if j==2:
    with open(args[1]) as f:
        message = f.read()
        cds=1

os.chdir(os.path.dirname(args[0]))
filecheck=os.path.exists('./host.ini')
if filecheck!=0:
    ccvg=1
    try:
        config = configparser.ConfigParser()
        config.read('./host.ini')
        section1 = 'profile'
        file=config.get(section1, 'file') # localhost
        cc=config.get(section1, 'hostc')
        g=os.path.isfile(file)
    except configparser.NoSectionError:
        g=0
else:
    ccvg=0
os.system('cls')
if cc>=1:
    file=input(' ロードするセッションファイル名 >> ')
    file=file+'.bin'
    g=os.path.isfile(file)
# 表示位置調整
print('')

# デバッグ情報の表示
debag=0

# SMTPサーバへのログイン
cdf=1
while cdf==1:
    if g==True and ccvg==1:
        # SMTP認証情報の読み込み
        f=open(file,'rb')
        usear=pickle.load(f)
        account=copy.copy(usear[0])
        password=copy.copy(usear[1])
        host2=copy.copy(usear[3])
        port=copy.copy(usear[4])
        from_email=account
        server = smtplib.SMTP_SSL(host2, int(port), context=ssl.create_default_context())
        server.login(account, password)
        server.set_debuglevel(debag)
        break
    print('')
    host2=input(' smtpサーバのホスト名 >> ')
    port=input(' smtpサーバのポート番号 >> ')
    account = input(' ユーザー名 >> ')
    from_email=account
    print('')
    password = getpass.getpass()
    try:
        server = smtplib.SMTP_SSL(host2, int(port), context=ssl.create_default_context())
        server.login(account, password)
        server.set_debuglevel(debag)
    except:
        print('')
        print(' エラー:認証に失敗しました')
        print('')
        print(' アカウントの権限を確認してください')
        print('')
        input(' リトライするにはエンターキーを押してください')
        if g==true:
            g=0
        continue
    else:
        cdf=0
        k=input(' セッション情報を記憶しますか？　(Y or N) >> ')
        if k=="Y" or k=="y":
            filename=input(' セッションファイル名 >> ')
            filename=filename+".bin"
            config = configparser.ConfigParser()
            config.read('.\\host.ini')
            section2 = 'profile'
            config.add_section(section2)
            config.set(section2, 'file', filename)
            cc=config.get(section2, 'hostc')
            cc=cc+1
            config.set(section2, 'hostc', cc)
            with open('.\\host.ini', 'w') as file:
                config.write(file)
            print(' ')
            print(' 記憶したセッション情報をクリアするには\n アプリケーションディレクトリ内の「profile.bin」を削除してください')
            print('')
            cgn=input(' 次回からユーザー情報の入力を省略します (Enter) >>')
            usear=[account,password,cgn,host2,port]
            f=open(filename,'wb')
            pickle.dump(usear,f)
            f.close()

os.system('cls')
print('')

# 送信先
to_email = input(' 送信先 >> ')
print('')
 
# MIMEの作成
subject = input(' 件名 >> ')
print('')
print(' 改行するには改行タグ/nを入力してください')
print('')
print(' このメールはhtmlタグを使用できます。')
print('')

# 本文の入力（ファイルからの読み込みの場合は入力しない)
if cds==0:
    message = input(' 本文 >> ')
message1=copy.copy(message)
message=message.replace('/n','<br>')

# メールの作成
msg = MIMEText(message, "html")
msg["Subject"] = subject
msg["To"] = to_email
msg["From"] = from_email
backups="件名:"+subject+"\n送信先: "+to_email+"\n送信元:"+from_email+"\n\n本文:"+message1
print('')
print(backups)
print('')

# メールの送信
server.send_message(msg)
server.quit()
input(' 送信しました>>')
sys.exit()
