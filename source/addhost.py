
import getpass
import configparser
import pickle
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
        section2 = 'profile'
        config.add_section(section2)
        config.set(section2, 'file', filename)
        cc=config.get(section2, 'hostc')
        cc=int(cc)
        cc=cc+1
        config.set(section2, 'hostc', str(cc))
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
hostadd()