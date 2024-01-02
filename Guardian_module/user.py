#coding:utf-8

import getpass,os,sqlite3,time,sys

red =  "\033[1;31m"
reset = "\033[0;0m"
blue = "\033[1;34m"

def auth():     #用户认证
    global loginname
    loginname = input("🎓 用户名: ")
    password = getpass.getpass("🔒 密码: ")
    user_auth(loginname,password)

def user_auth(name,password):   #用户认证
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/DB/pass.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE name=?",(name,))
    result = cursor.fetchall()
    if result:
        user,p1 = result[0]
        if p1 == password:
            print(red+'[+]'+reset+" 认证通过!")
            time.sleep(0.8)
            for i in range(3):
                print("\033[F\033[J", end="")
            pass
        else:
            print("认证失败!")
            sys.exit()
    else:
        print ("证失失败！")
        sys.exit()


def adduser():   #新增用户
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/DB/pass.db')
    c = conn.cursor()
    username = input("["+blue+"User"+reset+"] "+'新增用户名: ')
    password = input("["+blue+"Pass"+reset+"] "+'新增密码: ')
    data = (username,password)
    c.execute("INSERT OR REPLACE INTO user (name, password) VALUES (?, ?)", data)
    conn.commit()
    conn.close()
    print ("["+blue+"-"+reset+"] "+"新增用户成功!")
    time.sleep(1.5)


def deluser(username,password):   #删除用户
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/DB/pass.db')
    c = conn.cursor()
    c.execute("SELECT name FROM user")
    result_user = c.fetchall()
    try:
        if result_user:
            var=0
            for row in result_user:
                name = row[0]
                var=var+1
        c.execute("SELECT password FROM user WHERE name='admin'")
        result = c.fetchone()
        if result and result[0] == password and str(username) in str(result_user):
            c.execute("DELETE FROM user WHERE name = ?", (username,))
            conn.commit()
            conn.close()
            print("["+blue+"-"+reset+"] "+"删除成功!")
            time.sleep(1.5)
            for i in range(6+var):
                print("\033[F\033[J", end="") 
        else:
            print("["+red+"!"+reset+"] "+'admin密码不正确或用户不存在。')
            time.sleep(1.5)
            for i in range(6+var):
                print("\033[F\033[J", end="") 
    except Exception as e:
        print("["+red+"!"+reset+"] "+'admin密码不正确或用户不存在。')
        time.sleep(1.5)
        for i in range(6+var):
                print("\033[F\033[J", end="") 

def showuser():   #显示用户
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/DB/pass.db')
    c = conn.cursor()
    c.execute("SELECT name FROM user")
    result = c.fetchall()
    var = 0 
    try:
        if result:
            print("\033[F\033[J", end="")
            print("["+blue+"List"+reset+"] "+"用户列表")
            for row in result:
                name = row[0]
                print (red+"[User] "+reset+name)
    except Exception as e:
        pass

def showalluser():   #显示所有用户
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/DB/pass.db')
    c = conn.cursor()
    c.execute("SELECT name FROM user")
    result = c.fetchall()
    var = 0 
    try:
        if result:
            print("\033[F\033[J", end="")
            print("["+blue+"List"+reset+"] "+"用户列表")
            for row in result:
                name = row[0]
                print (red+"[User] "+reset+name)
                var=var+1
            time.sleep(5)
            for i in range(3+var):
                print("\033[F\033[J", end="")
    except Exception as e:
        pass


def passwd():   #用户登录密码修改
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/DB/pass.db')
    c = conn.cursor()
    username = input("["+blue+"User"+reset+"] "+'输入用户名: ')
    if username == loginname:
        old_password = input("["+blue+"Pass"+reset+"] "+'输入旧密码: ')
        c.execute("SELECT password FROM user WHERE name = ?", (username,))
        result = c.fetchone()
        if result and result[0] == old_password:
            new_password = input("["+blue+"New Pass"+reset+"] "+'输入新密码: ')
            # 更新密码
            c.execute("UPDATE user SET password = ? WHERE name = ?", (new_password, username))
            conn.commit()
            for i in range(5, 0, -1):
                print ("["+blue+"-"+reset+"] "+"修改成功！密码: " +new_password+ f"  {i} 秒后消失", end='\r')
                time.sleep(1)
            return True
        else:
            print("["+red+"!"+reset+"] "+'旧密码不正确或用户不存在。')
            time.sleep(1.5)      
            return False
    else:
        print("["+red+"!"+reset+"] "+'只能修改当前登录用户密码!')
        time.sleep(1.5)      
        return "0"
    
