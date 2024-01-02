#coding:utf-8

import time,sys,banner,getpass
from Guardian_module import data,Pass,user

# 🔑 Github: https://github.com/dddinmx/

red =  "\033[1;31m"
reset = "\033[0;0m"
blue = "\033[1;34m"

def main():
    table1 = ("["+blue+"+"+reset+"] "+"密码管理(a)"+"  "+"数据处理(w)"+"  "+"用户管理(x)")
    table2 =("["+blue+"-"+reset+"] "+"退出"+"("+red+"q"+reset+")")
    print(table1)
    print(table2)
    tablename = input("["+blue+">"+reset+"] "+"选择: ")
    if tablename not in ["a", "w", "x", "q"]:
        print ("["+blue+"-"+reset+"] "+"重新选择")
        time.sleep(0.8)
        for i in range(4):
            print("\033[F\033[J", end="")
    else:
        for i in range(3):      #去除选择框
            print("\033[F\033[J", end="")
    if tablename == "a":
        while(True):
            table1 = ("["+blue+"-"+reset+"] "+'生成密码(a)'+'  '+'删除密码(d)'+'  '+'查询密码(s)')
            table2 =("["+blue+"-"+reset+"] "+"退出"+"("+red+"q"+reset+")")
            print(table1)
            print(table2)
            choice = input("["+blue+">"+reset+"] "+"选择: ")
            if  tablename not in ["a", "d", "s", "q"]:
                print ("["+blue+"-"+reset+"] "+"重新选择")
                time.sleep(1)
                for i in range(4):
                    print("\033[F\033[J", end="")
            elif choice == "q":
                for i in range(3):
                    print("\033[F\033[J", end="")
                break   
            elif choice == "a":
                app_name = input("["+blue+"App"+reset+"] "+"输入需生成密码应用名: ")
                app_user = input("["+blue+"User"+reset+"] "+"应用用户(如:root): ")
                password_length = int(input("["+blue+"-"+reset+"] "+"设置密码长度: "))
                # 生成密码
                generated_password = Pass.generate_password(password_length)
                Pass.wpasstodb(app_name,app_user,generated_password)
                print("["+blue+"-"+reset+"] "+f"生成的密码为：{generated_password}")
                for i in range(10, 0, -1):
                    print ("["+blue+"-"+reset+"] "+"密码"  + f"  {i} 秒后消失", end='\r')
                    time.sleep(1)
                for i in range(7):
                    print("\033[F\033[J", end="")
            elif choice == "d":
                app_name = input("["+blue+"App"+reset+"] "+"删除应用名: ")
                app_user = input("["+blue+"User"+reset+"] "+"删除用户名: ")
                Pass.delpass(app_name,app_user)
            elif choice == "s":
                server = str(input("["+blue+"App"+reset+"] "+"查询应用(空为搜索全部): "))
                try:
                    name,spass,var = Pass.searchpass(str(server))
                    if spass == False:
                        print ("["+blue+"-"+reset+"] "+"未找到结果。")
                        time.sleep(1)
                        for i in range(5):
                            print("\033[F\033[J", end="")               
                        pass
                    else:
                        for i in range(10, 0, -1):
                            print ("["+blue+"-"+reset+"] "+f"  {i} 秒后消失", end='\r')
                            time.sleep(1)
                        for i in range(5+var):
                            print("\033[F\033[J", end="")
                except Exception as e:
                    print ("["+blue+"-"+reset+"] "+"未找到结果。")
                    time.sleep(1)
                    for i in range(5):
                        print("\033[F\033[J", end="") 
                    pass
    elif tablename=="w":
        while(True):
            table1 = ("["+blue+"-"+reset+"] "+'导出密码(r)'+'  '+'导入密码(w)')
            table2 =("["+blue+"-"+reset+"] "+"退出"+"("+red+"q"+reset+")")
            print(table1)
            print(table2)
            choice = input("["+blue+">"+reset+"] "+"选择: ")
            if  choice != "q" and choice != "r" and choice != "w":
                print ("["+blue+"-"+reset+"] "+"重新选择")
                time.sleep(1)
                for i in range(4):
                    print("\033[F\033[J", end="")
            elif choice == "q":
                for i in range(3):
                    print("\033[F\033[J", end="")
                break
            elif choice == "r":
                data.rcsv()
                print("["+blue+"-"+reset+"] "+"pass.csv导出成功")
                time.sleep(1.5)
                for i in range(3):
                    print("\033[F\033[J", end="")
                print("\033[F\033[J", end="") 
            elif choice == "w":
                data.wcsv()
                print("["+blue+"-"+reset+"] "+"pass.csv导入成功")
                time.sleep(1.5)
                for i in range(5):
                    print("\033[F\033[J", end="")
    elif tablename=="x":
        while(True):
            table1 = ("["+blue+"-"+reset+"] "+'用户登陆密码修改(x)'+'  '+'新增用户(a)'+'  '+'删除用户(d)'+'  '+'查询用户(s)')
            table2 =("["+blue+"-"+reset+"] "+"退出"+"("+red+"q"+reset+")")
            print(table1)
            print(table2)
            choice = input("["+blue+">"+reset+"] "+"选择: ")
            if choice not in ["x", "a", "d", "s","q"]:
                print ("["+blue+"-"+reset+"] "+"重新选择")
                time.sleep(1)
                for i in range(4):
                    print("\033[F\033[J", end="")
            elif choice == "q":
                for i in range(3):
                    print("\033[F\033[J", end="")
                break  
            elif choice == "x":
                flags = user.passwd()
                if flags == False:
                    for i in range(6):
                        print("\033[F\033[J", end="") 
                elif flags == "0":
                    for i in range(5):
                        print("\033[F\033[J", end="")
                else:
                    for i in range(7):
                        print("\033[F\033[J", end="")
            elif choice == "a":
                user.adduser()
                for i in range(6):
                    print("\033[F\033[J", end="") 
            elif choice == "d":
                user.showuser()
                username = input("["+blue+"Del User"+reset+"] "+'删除用户名: ')
                if username == "admin":
                    print("["+red+"!"+reset+"] "+"不能删除admin账号!")
                    time.sleep(1.5)
                    for i in range(6):
                        print("\033[F\033[J", end="")
                    break
                password = getpass.getpass("["+blue+"-"+reset+"] "+'admin密码: ')
                user.deluser(username,password)
            elif choice == "s":
                user.showalluser()
    elif tablename== "q":
        for i in range(4):
            print("\033[F\033[J", end="")
        sys.exit()


if __name__ == "__main__":
    banner.key_banner()
    user.auth()  
    while(True):
        main()  #主程序