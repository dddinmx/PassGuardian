#coding:utf-8

import string,datetime,sqlite3,os,random,time

red =  "\033[1;31m"
reset = "\033[0;0m"
blue = "\033[1;34m"

def generate_password(length):  #随机密码生成
    characters = string.ascii_letters+string.digits+string.punctuation
    pass1 = ""
    for _ in range(length):
        pass1 += random.choice(characters)
    password = pass1
    return password

def wpasstodb(server,user,password):     #随机密码写入数据库
    update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/DB/pass.db')
    cursor = conn.cursor()
    data = (update_time,server,user,password)
    cursor.execute("INSERT OR REPLACE INTO Server (Updatetime, Server, User, Password) VALUES (?, ?, ?,?)", data)
    conn.commit()
    conn.close()

def searchpass(Server):     #查找密码
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/DB/pass.db')
    cursor = conn.cursor()
    #cursor.execute('SELECT * FROM Server WHERE Server=?',(Server,))
    cursor.execute("SELECT * FROM Server WHERE Server LIKE ?", ('%' + Server + '%',))
    result = cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
    var = 0 
    if result:
        print ("    应用 | "+"用户名 | "+"密码")
        for row in result:
            uptime,name,user,password = row
            print ("["+red+"-"+reset+"] "+name+"  "+user+"  "+password)
            var=var+1
        return name,password,var
    else:
        return False
    

def delpass(Server,User):
    try:
        path = os.path.dirname(os.path.abspath(__file__))
        conn = sqlite3.connect(path + '/DB/pass.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Server WHERE Server=? AND User = ?', (Server,User))
        result = cursor.fetchall()
        conn.commit()
        if result:
            cursor.execute("DELETE FROM Server WHERE Server = ? AND User = ?", (Server,User))
            conn.commit()
            print ("["+blue+"-"+reset+"] "+"删除成功！")
            time.sleep(1.5)
            for i in range(6):
                print("\033[F\033[J", end="")
        else:
            print ("["+red+"!"+reset+"] "+"未找到对应账号。")
            time.sleep(1.5)
            for i in range(6):
                print("\033[F\033[J", end="")
        conn.close()
    except Exception as e:
        print ("["+red+"!"+reset+"] "+"未找到对应账号。")
        time.sleep(1.5)
        for i in range(6):
            print("\033[F\033[J", end="")