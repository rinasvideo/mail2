import hashlib
import getpass
import configparser
import pickle
import smtplib, ssl
import os
import sys
import copy
print('')
print(' 確認ではなく新規作成するには「-a」と入力してください')
files=input(' 確認するセッションファイル名 >> ')
def edit(files):
    print('')
    print(' セッションファイルの確認')
    print('')
    files=files+".bin"
    g=os.path.isfile(files)
    if g==1:
        f=open(files,'rb')
        usear=pickle.load(f)
        cg=copy.copy(usear[2])
        if cg=="n" or cg=="N":
            ccf="なし"
        else:
            ccf="あり"
        account=" メールアカウント: "+copy.copy(usear[0])
        pas=" セッションパスワード: "+ccf
        host2=" ホスト名: "+copy.copy(usear[3])
        port=" ポート番号: "+copy.copy(usear[4])
        usear=[host2,port,account,pas]
        print(' 一部の重要な情報は非表示になっています...')
        print('')
        [print(i) for i in usear]
        print('')
        input(' <'+files+'> ')
if files!="-a":
   edit(files)
   sys.exit()
def hostadd():
    cdf=1
    host2=input(' smtpサーバのホスト名 >> ')
    port=input(' smtpサーバのポート番号 >> ')
    account = input(' ユーザー名 >> ')
    from_email=account
    print('')
    password = getpass.getpass()
    k=input(' セッション情報を記憶しますか？　(Y or N) >> ')
    if k=="Y" or k=="y":
        cc=2
        filename=input(' セッションファイル名 >> ')
        filename=filename+".bin"
        config = configparser.ConfigParser()
        section2 = 'profile'
        config.add_section(section2)
        config.set(section2, 'file', filename)
        config.set(section2, 'hostc', str(cc))
        with open('.\\host.ini', 'w') as file:
            config.write(file)
        print(' ')
        print(' 記憶したセッション情報をクリアするには\n アプリケーションディレクトリ内の「profile.bin」を削除してください')
        print('')
        cgn=input(' 次回からユーザー情報の入力を省略します (Enter) >>')
        pas=input(' パスワードロックをかけますか? (推奨)  (y or n) >> ')
        if pas=="y":
           pas2= getpass.getpass()
           hs = hashlib.sha256(pas2.encode()).hexdigest()
        else:
           hs=""
           pas="n"
        usear=[account,password,pas,host2,port,hs]
        f=open(filename,'wb')
        pickle.dump(usear,f)
        f.close()
hostadd()
