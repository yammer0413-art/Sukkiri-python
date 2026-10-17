scores={'sugaku':50,'rika':60,'kokugo':90}

key=input('追加する科目名を入力してください >>')
if key in scores:
    print('既に登録済みです。')
else:
    data=int(input('得点を入力してください >>'))
    scores[key]=data
print(scores)
