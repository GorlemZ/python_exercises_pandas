import pandas as pd
import numpy
import csv as csv

hospdata=pd.read_csv("dati-ospedali.csv")

absfreq = hospdata['Regione'].value_counts()

relfreq = pd.Series(data= absfreq.values/absfreq.values.sum() , index= absfreq.axes, name= 'frequenze_relative')

colmedici = hospdata[['Denominazione Str. Pubblica New', 'Medici SSN']] 
less200 = colmedici[colmedici['Medici SSN']<200]


ospedalinomi = hospdata[['Regione','Denominazione Str. Pubblica New']]
osplombar = ospedalinomi [ospedalinomi ['Regione']=='Lombardia']['Denominazione Str. Pubblica New']

ospingegn = hospdata[['Regione','Ingegneri SSN']]
ingegncamp= ospingegn[ospingegn['Regione']=='Campania']['Ingegneri SSN']
mediaingcamp = ingegncamp.values.sum()/ingegncamp.count()

associal= hospdata[['Assistenti sociali SSN','Medici SSN']]
lessmedi = associal[associal['Medici SSN']>400]['Assistenti sociali SSN']
associalvar = lessmedi[lessmedi>-1].var() 

maxhospregion = absfreq.idxmax()
minmedici = less200.at[less200['Medici SSN'].idxmin(), 'Denominazione Str. Pubblica New']

maxmedici = hospdata[['Medici SSN','Denominazione Str. Pubblica New']].sort_values(by=['Medici SSN']).head(10)
ordmaxmed = maxmedici['Denominazione Str. Pubblica New'].sort_index()


maxingeg = hospdata.iloc[hospdata['Ingegneri SSN'].idxmax()]

ospodont = hospdata[hospdata['Odontoiatri SSN']>0]['Odontoiatri SSN'].count()

odonabsfreq = hospdata[hospdata['Odontoiatri SSN']>0]['Odontoiatri SSN'].value_counts()
odonrelfreq = odonabsfreq/ospodont

print(odonrelfreq) 

	
