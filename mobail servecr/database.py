import sqlite3

class DataBase:
    
    def __init__(self, cosmos):
        self.con = sqlite3.connect(cosmos)
        self.cur = self.con.cursor()
        
        sql = """
        CREATE TABLE IF NOT EXISTS cosmos (
                ID Integer Primary Key,
                Customer_Name text,
                Phon_Number text,
                Model text,
                IMEI text,
                SN text,
                Warrenty_state text,
                Fulty text,
                Your_Servece text,
                Item_Code text,
                Descraption text,
                Price_Dolar text,
                Price_IQ text,
                Date text,
                Jub_NUM text
                
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, Customer_Name, Phon_Number, Model, IMEI, SN, Warrenty_state, Fulty, Your_Servece, Item_Code, Descraption, Price_Dolar, Price_IQ, Date, Jub_NUM):
        self.cur.execute("INSERT INTO cosmos (Customer_Name, Phon_Number, Model, IMEI, SN, Warrenty_state, Fulty, Your_Servece, Item_Code, Descraption, Price_Dolar, Price_IQ, Date, Jub_NUM) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", 
                     (Customer_Name, Phon_Number, Model, IMEI, SN, Warrenty_state, Fulty, Your_Servece, Item_Code, Descraption, Price_Dolar, Price_IQ, Date, Jub_NUM))
        self.con.commit()

        
    def fetch(self):
        self.cur.execute("SELECT * FROM cosmos")
        rows = self.cur.fetchall()
        return rows

    def remove(self,id):
        self.cur.execute("delete from cosmos where id=?",(id,))
        self.con.commit()
        
        
        
        
    def update(self, ID, Customer_Name, Phon_Number, Model, IMEI, SN, Warrenty_state, Fulty, Your_Servece, Item_Code, Descraption,Price_Dolar, Price_IQ, Date,Jub_NUM):
        self.cur.execute("UPDATE cosmos SET Customer_Name=?, Phon_Number=?, Model=?, IMEI=?, SN=?, Warrenty_state=?, Fulty=?, Your_Servece=?, Item_Code=?, Descrption=?,Price_Dolar=?, Price_IQ=?, Date=?, job_NUM=? WHERE ID=?",
                         ( ID, Customer_Name, Phon_Number, Model, IMEI, SN, Warrenty_state, Fulty, Your_Servece, Item_Code, Descraption,Price_Dolar, Price_IQ, Date,Jub_NUM))
        self.con.commit()
    
    
    def search(self, Jub_NUM):
        self.cur.execute("SELECT * FROM cosmos WHERE Jub_NUM=?".format (Jub_NUM))
        rows = self.cur.fetchall()
        return rows

        