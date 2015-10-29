import serial
import time
import mysql.connector
import sys
conexao = serial.Serial('COM5', '9600')
#ler porta
if conexao.isOpen():
        cnx = mysql.connector.connect(user='root',password='root',host='localhost',database='rede')
        cur=cnx.cursor()                                
        while True:
                valor=conexao.readline()
                valor=valor.decode("utf-8")
                id_sensor,val_coleta,tipo_sensor,data = valor.split('.')
                print(x)
                print(e)
                #inserir dados na tabela
                sql="INSERT INTO dados(valor) VALUES('"'+id_sensor+'"+"'val_coleta'"+"'tipo_sensor+'"+"'data'"')
                cur.execute(sql)
                cnx.commit()
                #time.sleep(1)

