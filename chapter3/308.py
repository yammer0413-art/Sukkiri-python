name=input('あなたの名前を教えてください >>')
print(f'{name}さん、こんにちは')
if name=='山村':
    print('山村さんに会えてうれしいです')
food=input(f'{name}さんの、好きな食べ物を教えてください >>')
if 'カレー' in food:
    print('とても美味しいですよね、私も大好きです')
else:
    print(f'私も{food}が好きですよ')