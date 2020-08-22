import sqlite3
class myconnect:
      
      def __init__(self):
            #4
            self.con = sqlite3.connect("emp.db")
            #5
            self.con.execute(''' create table if not exists emp(
                                        id integer primary  key AUTOINCREMENT,
                                        name text,
                                        email text,
                                        mobile_no text,
                                        type text,
                                        experience integer,
                                        salary text
                                  ) ''')
                  
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            #6
            with self.con:
                  self.con.execute(
                        "insert into emp(name,email,mobile_no,type,experience,salary) values(:name,:email,:mobile_no,:type,:experience,:salary)",
                        {'name': ename, 'email': eemail, 'mobile_no': emob, 'type': etype, 'experience': eexp,
                         'salary': esalary})
            self.con.commit()

      def display(self):
            #7
      
