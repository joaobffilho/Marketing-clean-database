# Marketing-clean-database
#I did a script to clean data to send emails and SMS faster.
#Tratamento Responde Aí - Emails
import pandas as pd
import numpy as np
n=2
nome='mlkd'
planilha=pd.read_csv('C:/Users/joao_/Documents/My/Data Science/amplitude_users.csv')
selecionados = planilha [['\tgp:Nome','\tgp:Email']]
selecionados=selecionados.rename(columns={"\tgp:Nome": "Name", "\tgp:Email": "Email"})
selecionados['dividir']=selecionados.Name.str.split(' ')
selecionados['FirstName']=selecionados.dividir.str.get(0)
selecionados2=selecionados[['Email','FirstName']]
selecionados3=selecionados2.FirstName.str.replace('\t','')
selecionados4=selecionados2.Email.str.replace('\t','')
finalframe= pd.DataFrame()
finalframe['Email']=selecionados4
finalframe['First Name']=selecionados3
finalframe.set_index('Email', inplace=True)
if n==2:
    finalfi=np.array_split(finalframe, n)
    finalfi[0].to_csv(nome+'1.csv')
    finalfi[1].to_csv(nome+'2.csv')
elif n==3:
    finalfi=np.array_split(finalframe, n)
    finalfi[0].to_csv(nome+'1.csv')
    finalfi[1].to_csv(nome+'2.csv')
    finalfi[2].to_csv(nome+'3.csv')
elif n==4:   
    finalfi=np.array_split(finalframe, n)
    finalfi[0].to_csv(nome+'1.csv')
    finalfi[1].to_csv(nome+'2.csv')
    finalfi[2].to_csv(nome+'3.csv')
    finalfi[3].to_csv(nome+'4.csv')    
else:
    finalfi=finalframe
    finalfi.to_csv(nome+'.csv')
