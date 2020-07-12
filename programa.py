# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 15:27:28 2020

@author: joao_
"""
from interpy import *
import resource
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np
import csv
from PyQt5.QtWidgets import QDialog, QPushButton, QLabel,QFileDialog,QVBoxLayout
def main(ui):  
    def browseFile(self):
        path = QtWidgets.QFileDialog.getOpenFileName(None,filter='*.csv')
        planilha = pd.read_csv(path[0])
        def limpar():
            if ui.checkBox_email.isChecked():
                name_cols = [col for col in planilha.columns if 'gp:Nome' in col]
                email_cols=[col for col in planilha.columns if 'gp:Email' in col]
                nome=name_cols[0]
                email=email_cols[0]
                selecionados = planilha [[nome,email]]
                selecionados=selecionados.rename(columns={nome: "Name", email: "Email"})
                selecionados['dividir']=selecionados.Name.str.split(' ')
                selecionados['FirstName']=selecionados.dividir.str.get(0)
                selecionados2=selecionados[['Email','FirstName']]
                selecionados3=selecionados2.FirstName.str.replace('\t','')
                selecionados4=selecionados2.Email.str.replace('\t','')
                finalframe= pd.DataFrame()
                finalframe['Email']=selecionados4
                finalframe['First Name']=selecionados3
                finalframe.set_index('Email', inplace=True)
                if ui.horizontalSlider_Dividir.value()==2:
                    finalfi=np.array_split(finalframe, 2)
                    finalfi[0].to_csv(ui.lineEdit_Nome.text()+'1.csv',encoding='utf-8-sig')
                    finalfi[1].to_csv(ui.lineEdit_Nome.text()+'2.csv',encoding='utf-8-sig')
                elif ui.horizontalSlider_Dividir.value()==3:
                    finalfi=np.array_split(finalframe, 3)
                    finalfi[0].to_csv(ui.lineEdit_Nome.text()+'1.csv',encoding='utf-8-sig')
                    finalfi[1].to_csv(ui.lineEdit_Nome.text()+'2.csv',encoding='utf-8-sig')
                    finalfi[2].to_csv(ui.lineEdit_Nome.text()+'3.csv',encoding='utf-8-sig')
                elif ui.horizontalSlider_Dividir.value()==4:   
                    finalfi=np.array_split(finalframe, 4)
                    finalfi[0].to_csv(ui.lineEdit_Nome.text()+'1.csv',encoding='utf-8-sig')
                    finalfi[1].to_csv(ui.lineEdit_Nome.text()+'2.csv',encoding='utf-8-sig')
                    finalfi[2].to_csv(ui.lineEdit_Nome.text()+'3.csv',encoding='utf-8-sig')
                    finalfi[3].to_csv(ui.lineEdit_Nome.text()+'4.csv',encoding='utf-8-sig')    
                elif ui.horizontalSlider_Dividir.value()==5:   
                    finalfi=np.array_split(finalframe, 5)
                    finalfi[0].to_csv(ui.lineEdit_Nome.text()+'1.csv',encoding='utf-8-sig')
                    finalfi[1].to_csv(ui.lineEdit_Nome.text()+'2.csv',encoding='utf-8-sig')
                    finalfi[2].to_csv(ui.lineEdit_Nome.text()+'3.csv',encoding='utf-8-sig')
                    finalfi[3].to_csv(ui.lineEdit_Nome.text()+'4.csv',encoding='utf-8-sig')
                    finalfi[4].to_csv(ui.lineEdit_Nome.text()+'5.csv',encoding='utf-8-sig')
                else:
                    finalfi=finalframe
                    finalfi.to_csv(ui.lineEdit_Nome.text()+'.csv',encoding='utf-8-sig')
            if ui.checkBox_SMS.isChecked():
                name_cols = [col for col in planilha.columns if 'gp:Nome' in col]
                phone_cols=[col for col in planilha.columns if 'gp:Celular' in col]
                nome=name_cols[0]
                phone=phone_cols[0]
                selecionadosk = planilha [[nome,phone]]
                selecionadosk=selecionadosk.rename(columns={nome: "Name", phone: "Phone"})
                selecionadosk['dividir']=selecionadosk.Name.str.split(' ')
                selecionadosk['FirstName']=selecionadosk.dividir.str.get(0)
                selecionadosk2=selecionadosk[['Phone','FirstName']]
                selecionadosk3=selecionadosk2.FirstName.str.replace('\t','')
                selecionadosk4=selecionadosk2.Phone.str.replace(r'\W','')#tirar caracteres especiais
                finalframek= pd.DataFrame()
                finalframek['Phone']=selecionadosk4
                finalframek['First Name']=selecionadosk3
                finalfik=finalframek.replace(r'^\s*$', np.nan, regex=True) 
                finalzaok=finalfik.dropna() #tirar os nulos
                def setarstring(tabela): #colocar 9 se so tem 10 digitos
                    if len(tabela)==10:
                        return (tabela[:2] + '9' + tabela[2:])
                    return tabela
                finalk=finalzaok.apply(lambda row: setarstring(row['Phone']), axis=1) #aplicar função
                final2k= pd.DataFrame()
                final2k['Phone']=finalk
                final2k['First Name']=finalzaok['First Name']
                final2k.set_index('Phone', inplace=True) 
                final2k.to_csv(ui.lineEdit_Nome.text()+'SMS.csv',encoding='utf-8-sig')    
            else:
                pass
        ui.pushButton_Submit.clicked.connect(limpar)
    ui.pushButton_arquivo.clicked.connect(browseFile)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    main(ui)
    sys.exit(app.exec_())