#create database programm
import mysql.connector  
# pthon mysql library importing command pip install mysql-connector-python
mysqldb=mysql.connector.connect(host="localhost",user="",password="")
#established connection  type your username and password as mysql
mycursor=mysqldb.cursor()
#cursor() method create a cursor object  
mycursor.execute("create database python")
#Execute SQL Query to create a database first we create database pythondata  
mysqldb.close()#Connection Close 

#---------------------------------------------------------------------------------------
#                                 create table
#---------------------------------------------------------------------------------------
import mysql.connector  
# pthon mysql library importing command pip install mysql-connector-python
mysqldb=mysql.connector.connect(host="localhost",user="",password="",database="python")
#established connection  type your username and password as mysql
mycursor=mysqldb.cursor()
#cursor() method create a cursor object  
mycursor.execute("create table supporttechnology(No INT(2),Name VARCHAR(255))")
#Execute SQL Query to create a database first we create database pythondata  
mysqldb.close()#Connection Close 

#---------------------------------------------------------------------------------------
#                                 insert data
#---------------------------------------------------------------------------------------
import mysql.connector  
mysqldb=mysql.connector.connect(host="localhost",user="",password="",database="python")#established connection between your database  
mycursor=mysqldb.cursor()#cursor() method create a cursor object    
try:  
   #Execute SQL Query to insert record  
   mycursor.execute("insert into supporttechnology values(1,'DataAnalytic'),(2,'Webdevlopment'),(3,'Machinelearning'),(4,'Artificialintelligence'),(4,'Webdevlop')")  
   mysqldb.commit() # Commit is used for your changes in the database  
   print('Record inserted successfully...')   
except:  
   # rollback used for if any error   
   mysqldb.rollback()  
mysqldb.close()#Connection Close 

#---------------------------------------------------------------------------------------
#                                 select data
#---------------------------------------------------------------------------------------
import mysql.connector  
# pthon mysql library importing command pip install mysql-connector-python
mysqldb=mysql.connector.connect(host="localhost",user="",password="",database="python")
#established connection  type your username and password as mysql
mycursor=mysqldb.cursor()
#cursor() method create a cursor object  
try:  
   mycursor.execute("select * from supporttechnology")#Execute SQL Query to select all record   
   result=mycursor.fetchall() #fetches all the rows in a result set   
   for i in result:    
      No=i[0]  
      Name=i[1]  
      
      print(No,Name)  
except:   
   print('Error:Unable to fetch data.')  
mysqldb.close()#Connection Close

#------------------------------------------------------------------------------------------------
#                                          update data
#-------------------------------------------------------------------------------------------------

import mysql.connector  
mysqldb=mysql.connector.connect(host="localhost",user="",password="",database="python")#established connection between your database  
mycursor=mysqldb.cursor()#cursor() method create a cursor object    
try:  
   #Execute SQL Query to insert record  
   mycursor.execute("UPDATE supporttechnology SET Name='WebDevlopment', WHERE No=4")  
   mysqldb.commit() # Commit is used for your changes in the database  
   print('Record inserted successfully...')   
except:  
   # rollback used for if any error   
   mysqldb.rollback()  
mysqldb.close()#Connection Close 

#------------------------------------------------------------------------------------------------
#                                          delete data
#-------------------------------------------------------------------------------------------------

import mysql.connector  
mysqldb=mysql.connector.connect(host="localhost",user="",password="",database="python")#established connection between your database  
mycursor=mysqldb.cursor()#cursor() method create a cursor object    
try:  
   #Execute SQL Query to insert record  
   mycursor.execute("DELETE FROM supporttechnology WHERE No=4")  
   mysqldb.commit() # Commit is used for your changes in the database  
   print('Record delete successfully...')   
except:  
   # rollback used for if any error   
   mysqldb.rollback()  
mysqldb.close()#Connection Close 
