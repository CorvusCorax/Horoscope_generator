import pandas as pd
import datetime

terminator=' That is all.'
#length=200
data = pd.read_csv('horoscopes.csv', header = None, delimiter = '|').dropna()
dates = []
for f in data[2]:
    f2=f.split('-')
    d=datetime.date(int(f2[2]),int(f2[0]),int(f2[1]))
    dates.append(d.strftime('%B %d'))
zodiac = [ f.capitalize() for f in data[3] ]
otexts = data[1]
texts=[]
for n in range(len(otexts)):
    try:
        if len(otexts[n])>5:
            t=otexts[n].strip()
            #words=len(t.split(' '))
            #remainder=int((100-words)/len(terminator.split(' ')))
            #filler=terminator*remainder
            texts.append(zodiac[n]+'. '+dates[n]+'. '+t+terminator)
    except:
        print("failed on key %i"%(n))

with open('all.txt', 'w') as f:
  f.write('\n'.join(texts))

#with open('train.txt', 'w') as f:
#  f.write('\n'.join(texts[:12500]))

#with open('valid.txt', 'w') as f:
#  f.write('\n'.join(texts[12500:]))
