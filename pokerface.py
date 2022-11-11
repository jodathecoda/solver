#copyright (c) 2019
#jodathecoda@yahoo.com

import random
import settings

face1='\U0001F600'
face2='\U0001F602'
face3='\U0001F603'
face4='\U0001F604'
face5='\U0001F605'
face6='\U0001F606'
face7='\U0001F609'
face8='\U0001F60A'
face9='\U0001F60B'
face10='\U0001F60E'
face11='\U0001F60D'
face12='\U0001F618'
face13='\U0001F61A'
face14= face4
face15= face5
face16= face6
#face14='\U0001F642'
#face15='\U0001F917'
#face16='\U0001F914'
face17='\U0001F610'
face18='\U0001F611'
face19='\U0001F636'
#face20='\U0001F623'
face20= face10
face21='\U0001F625'
face22='\U0001F62E'
#face23='\U0001F910'
face23= face13

face24='\U0001F62F'
face25='\U0001F62A'
face26='\U0001F62B'
face27='\U0001F634'
face28='\U0001F60C'
face29='\U0001F61B'

face30='\U0001F61C'
face31='\U0001F61D'
face32='\U0001F615'
face33='\U0001F612'
face34='\U0001F613'
face35='\U0001F614'

#face36='\U0001F643'
#face37='\U0001F911'
face37= face27
face38='\U0001F632'

#negative
#face39='\U0001F641'
face39= face13
face40='\U0001F616'
face41='\U0001F61E'
face42='\U0001F61F'
#face43='\U0001F624'
face43= face33
face44='\U0001F622'

face45='\U0001F62D'
face46='\U0001F626'
face47='\U0001F627'
face48='\U0001F628'
face49='\U0001F629'
face50='\U0001F62F'
#face51='\U0001F62C'
face51= face41

face52='\U0001F630'
face53='\U0001F631'
face54='\U0001F633'
face55='\U0001F635'

face56='\U0001F621'
face57='\U0001F620'

face58='\U0001F637'
face59='\U0001F607'

#fantasy
face60='\U0001F608'
face61='\U0001F47F'
face62='\U0001F479'
face63='\U0001F47A'
face64='\U0001F480'

face65='\U0001F47B'
face66='\U0001F47D'
face67='\U0001F47E'
face68='\U0001F63A'

face69='\U0001F648'
face70='\U0001F649'
face71='\U0001F64A'
face72='\U0001F476'

face100 = ':)'
face200 = ':}'
face300 = ':]'
face400 = ':|'
face500 = ':['
face600 = ':{'
face700 = ':('

faces = []
faces1 = [face100, face200, face300, face400, face500, face600, face700]
faces2 = [face1, face2, face3, face4, face5, face6, face7, face8, face9, face10, face11, face12, face13, face14, face15, face16, face17, face18, face19, face20, face21, face22, face23, face24, face25, face26\
, face27, face28, face29, face30, face31, face32, face33, face34, face35, face37, face38, face39, face40, face41, face42, face43, face44, face45, face46, face47, face48, face49, face50, face51, face52\
, face53, face54] #, face55, face56, face57, face58, face59, face60, face61, face62, face63, face64, face65, face66, face67, face68, face69, face70, face71, face72, face36]
#print(faces2)

class Pokerface:
    def __init__(self):
        if settings.fancy:
            self.faces = [face1, face2, face3, face4, face5, face6, face7, face8, face9, face10, face11, face12, face13, face14, face15, face16, face17, face18, face19, face20, face21, face22, face23, face24, face25, face26\
, face27, face28, face29, face30, face31, face32, face33, face34, face35, face37, face38, face39, face40, face41, face42, face43, face44, face45, face46, face47, face48, face49, face50, face51, face52\
, face53, face54] #, face55, face56, face57, face58, face59, face60, face61, face62, face63, face64, face65, face66, face67, face68, face69, face70, face71, face72, face36]
        else:
            self.faces = [face100, face200, face300, face400, face500, face600, face700]
        random.shuffle(self.faces)