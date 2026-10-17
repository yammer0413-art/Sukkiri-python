name=input('あなたの名前を入力してください >>')
print(f'{name}さん、こんにちは')
food=input(f'{name}さんの好きな食べ物を教えてください >>')
if 'カレー' in food:
    print('素敵です。カレー最高ですね!!')
else:
    print(f'私も{food}が好きですよ。')