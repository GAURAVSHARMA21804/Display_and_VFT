import mysql.connector
import json
from flask import make_response,jsonify
# class user_model():
#     def _init_(self):
#         try:
#             self.con=mysql.connector.connect(host="localhost",user="root",password="Ga2001pillu14##",database="dunit")
#             self.cur=self.con.cursor(dictionary=True)
#             self.con.autocommit=True
#             print("connected successfully")
#         except:
#             print("some error")
            
#     def user_getall_model(self):
#         self.cur.execute("SELECT * FROM stations")
#         result=self.cur.fetchall()
#         if len(result)>0:
#             res = make_response({'payload':result},200)
#             res.headers['Access-Control-Allow-Origin']="*"
#             return res
#         else:
#             return make_response({"message":"No Data found"},204)
        
        
#     def user_addone_model(self,data):
#         self.cur.execute(f"INSERT INTO users(id,name,email,phone,password,role) VALUES({data['id']},'{data['name']}','{data['email']}','{data['phone']}','{data['password']}','{data['role']}')")
        
        
#         return make_response({"message":"user created successfully"},201)
            

class display_unit_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="Ga2001pillu14##",database="dunit")
            self.cur=self.con.cursor(dictionary=True)
            self.con.autocommit=True
            print("connected successfully")
        except:
            print("some error")
            
    def Station_model(self, data):
        try:
            qry = "INSERT INTO stations(station_id, e_one, e_one_name, e_one_skill, e_two, e_two_name, e_two_skill) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = [(stationdata.get('station_id'),
                stationdata.get('e_one'),
                stationdata.get('e_one_name'),
                stationdata.get('e_one_skill'),
                stationdata.get('e_two'),
                stationdata.get('e_two_name'),
                stationdata.get('e_two_skill')) for stationdata in data]
            self.cur.executemany(qry, values)
            return make_response({"message": "Stations(s) added successfully"}, 201)
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            return make_response({"error": "Internal Server Error"}, 500)
            
        
        # print(data)
        # qry="INSERT INTO stations(station_id, e_one, e_two, process_id) VALUES "
        # for stationdata in data:
        #     qry +=f"('{stationdata['station_id']}','{stationdata['e_one']}','{stationdata['e_two']}','{stationdata['process_id']}')"
        # finalqry = qry.rstrip(",")
        # self.cur.execute(finalqry)
        
        # # res.headers['Access-Control-Allow-Origin']="*"
        # # res.headers['Content-Type']="application/json"
        # return make_response({"message":"Station added successfully"},201)
    def get_process(self,data):
        try:
            qry = "SELECT process_id,process_name,prrocess_skill FROM processes WHERE part_id = %s"  
            values = [data.get('part_id')]
            self.cur.execute(qry,values)
            result = self.cur.fetchall()
            if len(result)>0:
                res = make_response({'payload':result},200)
                res.headers['Access-Control-Allow-Origin']="*"
                return res
            else:
             return make_response({"message":"No Data found"},204)
        
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            return make_response({"error": "Internal Server Error"}, 500)
        

    def get_process_and_login_data(self,data):
        try:
            qry = "SELECT process_id,process_name,prrocess_skill FROM processes WHERE part_id = %s"  
            values = [data.get('part_id')]
            self.cur.execute(qry,values)
            process_result = self.cur.fetchall()

            qry_login_operators= "SELECT CONCAT(first_name, ' ', last_name) AS full_name, employee_code, skill FROM login_operator"
            self.cur.execute(qry_login_operators)
            employees_result=self.cur.fetchall()

            response_data={
                'process_data':process_result,
                'employess_data':employees_result
            }

            if len(process_result) > 0 or len(employees_result) > 0:
                res = make_response({'payload':response_data},200)
                res.headers['Access-Control-Allow-Origin']="*"
                return res
            else:
             return make_response({"message":"No Data found"},204)
        
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            return make_response({"error": "Internal Server Error"}, 500)