
import email
import ssl
import imaplib
import getpass
import os
from email.header import decode_header, make_header
os.system('cls')
print('')
print(' このツールで表示できるのはメールのほとんどが文字で構成されたhtmlメールのみです。')
print('')
print(' ログイン')
print('')
host = input(' ホスト名 >> ')
nego_combo = ("ssl", 993) # ("通信方式", port番号)

if nego_combo[0] == "no-encrypt":
    imapclient = imaplib.IMAP4(host, nego_combo[1])
elif nego_combo[0] == "starttls":
    context = ssl.create_default_context()
    imapclient = imaplib.IMAP4(host, nego_combo[1])
    imapclient.starttls(ssl_context=context)
elif nego_combo[0] == "ssl":
    context = ssl.create_default_context()
    imapclient = imaplib.IMAP4_SSL(host, nego_combo[1], ssl_context=context)
imapclient.debug = 0  # 各命令をトレースする
print('')
username = input(' ユーザーネーム(メールアドレス) >> ')
print('')
password = getpass.getpass(" パスワード >> ")
imapclient.login(username, password)



imapclient.select() # メールボックスの選択
typ, data = imapclient.search(None, "ALL")  # data = [b"1 2 3 4 ..."]
datas = data[0].split()
fetch_num = input(' 取得したいメッセージ数 >> ')  # 取得したいメッセージの数
fetch_num=int(fetch_num)
if (len(datas)-fetch_num) < 0:
    fetch_num = len(datas)
msg_list = []  # 取得したMIMEメッセージを格納するリスト
for num in datas[len(datas)-fetch_num::]:
    typ, data = imapclient.fetch(num, '(RFC822)')
    msg = email.message_from_bytes(data[0][1])
    msg_list.append(msg)
imapclient.close()
imapclient.logout()


os.system('cls')
for msg in msg_list:
    print(msg)

for msg in msg_list:
    # 各ヘッダ情報はディクショナリのようにアクセスできる
    from_addr = str(make_header(decode_header(msg["From"])))
    subject = str(make_header(decode_header(msg["Subject"])))

    # 本文(payload)を取得する
    if msg.is_multipart() is False:
        # シングルパートのとき
        payload = msg.get_payload(decode=True) # 備考の※1
        charset = msg.get_content_charset()    # 備考の※2
        if charset is not None:
            payload = payload.decode(charset, "ignore")
        print(payload)
        print()
    else:
        # マルチパートのとき
        for part in msg.walk():
            payload = part.get_payload(decode=True)
            if payload is None:
                continue
            charset = part.get_content_charset()
            if charset is not None:
                payload = payload.decode(charset, "ignore")
            print(payload)
            print()
input(' メールの取得終了')