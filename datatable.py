from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import mysql.connector


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="11121314",
            database="second_db")
        c = mydb.cursor()
        c.execute("select * from etudiant ")
        etu = c.fetchall()
        table = MDDataTable(
            column_data=[
                ("NUM", dp(30)),
                ("Nom", dp(30)),
                ("Prenom", dp(30)),
                ("CNE", dp(30)),
                ("Ecole", dp(30))],
            row_data= etu,)
        mydb.commit()
        mydb.close()
        screen.add_widget(table)
        return screen

if __name__=="__main__" :
    MainApp().run()
