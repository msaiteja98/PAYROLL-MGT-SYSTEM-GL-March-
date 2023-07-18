import sqlite3

conn = sqlite3.connect('pms.db')

cur  = conn.cursor()

class Employees:
    
    def empinsert(self,**k):
        cur.execute(f'''INSERTED INTO EMPLOYEE_DETAILS
                    VALUES({k['eid']},"{k['ename']}","{k['designation']}",
                    {k['dprid']},"{k['email']}",{k['contact']},"{k['address']}")
            ''')
        conn.commit()