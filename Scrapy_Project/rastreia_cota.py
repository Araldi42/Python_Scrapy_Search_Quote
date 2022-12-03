import os
import pandas as pd
import time
import subprocess
from datetime import datetime
from PyQt6.QtWidgets import QMessageBox


while True:
    try:
        cota_val = float(input("Insira o valor de sua Cota: "))
    except ValueError:
        print("Valor inválido, insira novamente")
        continue
    else:
        break

cota_val01 = cota_val
cota_val = str(cota_val)
cota_val = cota_val.replace(".",",",1)




print(f"O valor de sua cota é {cota_val}")

command ='scrapy crawl busca_cota -O cota_val.json'







now = datetime.now()

current_time = now.strftime("%H:%M:%S")



pl = subprocess.Popen(command, shell=True,stdout= subprocess.DEVNULL, stderr= subprocess.DEVNULL)
pl.wait()

df = pd.read_json('cota_val.json')

df['cotacao'] = df['cotacao'][0][:-2]


#print(pl.wait())
print('estou aqui')

time.sleep(3)
if int(current_time[:-6]) <= 18:

    print('agora aqui')

    command ='scrapy crawl busca_cota -O cota_val.json'
    pl = subprocess.Popen(command, shell=True,stdout= subprocess.DEVNULL, stderr= subprocess.DEVNULL)
    pl.wait()

    print('.')
    
    time.sleep(1.5)
    try:

        print('.')

        while True:
            print('.')

            if int(current_time[:-6]) <= 18:

                print('.')
                command ='scrapy crawl busca_cota -O cota_val.json'

                pl = subprocess.Popen(command, shell=True,stdout= subprocess.DEVNULL, stderr= subprocess.DEVNULL)
                

                

                current_time = now.strftime("%H:%M:%S")


               
                pl.wait()

                print('.')

                time.sleep(2)

                df = pd.read_json('cota_val.json')
                
                dfy = df.copy()
                dfy['cotacao'] = dfy['cotacao'][0][:-2]

                print( dfy['cotacao'])

                dfy['cotacao'] = dfy['cotacao'][0].replace(",",".",1)

                

                dfy['cotacao'] = dfy['cotacao'].astype(float)

                print('.')

                
                

                if cota_val01 != dfy['cotacao'].item():

                    print('.')

                    time.sleep(1.5)

                    continue
                    

                else:
                    
                    import sys
                    # from PyQt6.QtWidgets import QMessageBox, QApplication
                    import pyautogui

                    print('COTAÇÃO ENCONTRADA \nCOTAÇÃO ENCONTRADA \n COTAÇÃO ENCONTRADA \n COTAÇÃO ENCONTRADA \n COTAÇÃO ENCONTRADA \n COTAÇÃO ENCONTRADA')


                    pyautogui.hotkey('win','m')
                   

                    pyautogui.confirm("COTAÇÃO ENCONTRADA")
                    
                    

                    # App = QApplication(sys.argv)

                    # msg = QMessageBox()

                    # msg.setIcon(QMessageBox.critical)

                    # msg.setWindowTitle("COTAÇÃO ENCONTRADA!!")
                    # msg.setText("COTAÇÃO "+{cota_val}+ " ENCONTRADA!!")
                   
                    # msg.show() 

                    # sys.exit(App.exec())

                    

                    break

            else:

                break


    except:

        print('Busca cota finalizada!')






# if pl.returncode == 0:

#     print('path executado')

#     pass

# else:

#     print('comando falhou')


#print(cmd)








#float(input("Insira o valor de sua Cota: ").split()

