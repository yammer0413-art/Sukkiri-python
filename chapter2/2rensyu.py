#2-1
#(1)ディクショナリ
#(2)リスト
#(3)セット
#(4)セット
#(5)リスト

#2-2
scores=[]
scores.append(int(input("国語＞＞＞")))
scores.append(int(input("算数＞＞＞")))
scores.append(int(input("理科＞＞＞")))
scores.append(int(input("社会＞＞＞")))
scores.append(int(input("英語＞＞＞")))

print(f'合計点{sum(scores)}点、平均点{sum(scores)/len(scores)}')

#2-3
print1={'読書','昼寝','映画鑑賞','散歩','料理'}
print2={'テニス','将棋','料理','読書','旅行'}
input('心の準備ができたらEnterキーを押してください')
common=player1&player2
total=player1|player2
compatibility_rate=len(common)/len(total)*100
print(f'相性度は{compatibility_rate}パーセントでした')