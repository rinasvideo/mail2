import hashlib
import getpass
import configparser
import pickle
import smtplib, ssl
print('')
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
