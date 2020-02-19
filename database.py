
import mysql.connector

class database:
    
    def __init__(self,database):
        self.database = database
        self.mydatabase = mysql.connector.connect(host = "localhost",
                                       user="root",
                                       passwd="ZKMoguz1958+",
                                       database= database)
        #mycursor= self.mydatabase.cursor()
    def show_table(self,table_name):  
        mycursor= self.mydatabase.cursor()
        mycursor.execute("DESCRIBE {}".format(table_name))
        
        for table in mycursor:
            print(table)
        
           
    def create_table(self,table_name,fields):
        query = "CREATE TABLE IF NOT EXISTS {} (".format(table_name)
        for i in range(len(fields)-1):
            query = query+ "{},".format(fields[i])
        query += "{})".format(fields[-1])
        
        mycursor= self.mydatabase.cursor()
        mycursor.execute(query)
        
    def insert_data(self,table_name,fields,data):
        
        
        query = "INSERT INTO {} (".format(table_name)
        
        if len(fields) ==1:
            
            query += "{})".format(fields[0])
        else:
            for field in range(len(fields)-1):
                
                query += "{},".format(fields[field])
                
            query += "{})".format(fields[-1]) 
            
        query += " VALUES ("
       
        if len(data) == 1:
            query += "%s)"
        else:
            for i in range(len(data)-1):
                query += "%s,"
            query += "%s)"
        query = "" + query + ""      
        
        
        
        #param = tuple(i for i in data)
        mycursor= self.mydatabase.cursor()
        mycursor.execute(query,data)
        self.mydatabase.commit()
       
            
    def delete_data(self,table_name,field,data):
        query = "DELETE FROM {}".format(table_name) 
        query += " WHERE {}=".format(field)
        if len(data)==1:
            query += "'{}'".format(data)
        #else:
        #    for i in range(len(data)-1):
        #        query += "'{}',".format(data[i])
       # query += "'{}'".format(data[-1])
        print(query)
        mycursor= self.mydatabase.cursor()
        mycursor.execute(query)
        self.mydatabase.commit()
        print("{} is deleted".format(data))
        
    def update_data(self,table_name,field ,data ,new_data):
        query = " UPDATE {}".format(table_name) 
        query += " SET {}".format(field)
        query +=" = {}".format(new_data) 
        query += " WHERE {}".format(field)
        query += " = {}".format(data)
        
        print(query)
        mycursor= self.mydatabase.cursor()
        mycursor.execute(query)
        self.mydatabase.commit()
        
    def data_searching(self,table_name,fields,data):
        mycursor= self.mydatabase.cursor()
        query = "SELECT * FROM {}".format(table_name)
        query += " WHERE {} = ".format(fields)
       
        query += "\"{}\"".format(data) 
        print(query)
        mycursor= self.mydatabase.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchone()
        return myresult
    
    def select_data(self,table_name,fields):
        mycursor= self.mydatabase.cursor()
        query = "SELECT"
        
        if len(fields)==1:
            query += "{} FROM {}".format(fields,table_name)
        
        else:
            for i in range(len(fields)-1):
                query += " {},".format(fields[i])
            
            query += "{} ".format(fields[-1])            
            query += "FROM {}".format(table_name)
        
        print(query)    
        mycursor= self.mydatabase.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        print(myresult)
        return myresult
        
        mycursor.execute(query)
        myresult = mycursor.fetchone()
        return myresult
        
