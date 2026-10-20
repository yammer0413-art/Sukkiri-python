print('すべての質問にyまたはnで答えてください。')
okane_aruka=input('お金に余裕はありますか？ >>')
if okane_aruka == 'y':
    onaka_suiteruka=input('お腹はすいていますか？ >>')
    nomitai_kibunha=('お酒は飲みたいですか？ >>')
    if onaka_suiteruka == 'y' and nomitai_kibunha == 'y':
        print('焼き肉はいかがですか？')
    elif onaka_suiteruka =='y':
        print('カレーはいかがですか？')
    elif nomitai_kibunha == 'y':
        print('焼き鳥はいかがですか？')
    else:
        print('パスタはいかがですか？')
    yasyoku_iruka=input('夜食はいりますか？ >>')
    if yasyoku_iruka == 'y':
        print('コンビニのチキンはいかがですか？')
else:
    print('家で食べましょう。')
