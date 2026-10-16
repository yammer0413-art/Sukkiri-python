#練習1-1
#(1)2+10*5=2+50=52
#(2)'7'*(3+4)=7777777
#(3)f'version{3+2*0.1+9*0.01}'=f'version{3+0.2+0.09}=f'version{3.29}
#(4)4*'num'+'回目のTypeError'=numnumnumnum回目のTypeError

#練習1-2
#(1)int型
#(2)error　intのnumにstrの5を代入しようとしたため。
#(3)str型
#(4)float型

#練習1-3
height=int(input('身長(cm)は＞＞＞'))
weight=int(input('体重(kg)は＞＞＞'))
bmi=str(weight/(height/100)/(height/100))
print(f'あなたの身長は{height}cm、体重{weight}kgなのでBMIは{bmi}です。')