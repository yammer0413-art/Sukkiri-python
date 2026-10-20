score=int(input('試験の点数を入力してください >>'))
if score<0 or score >100:
    print('異常な得点です')
    print('正しい点数を入力してください')
elif score >= 60:
    print('合格です')
    print('よく頑張りましたね！')
else:
    print('不合格です')