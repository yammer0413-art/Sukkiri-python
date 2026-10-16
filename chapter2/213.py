scores={'suugaku':95,'eigo':84, 'rika':57}
print(scores)
print(scores['suugaku'])
scores['syakai']=78
scores['kokugo']=36
print(scores)
scores['suugaku']=99
print(scores)
del scores['suugaku']
print(scores)
total=sum(scores.values())
print(total)