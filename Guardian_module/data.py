#coding:utf-8

import os,sqlite3,csv,datetime

def rcsv():     #导出密码
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/DB/pass.db')
    cursor = conn.cursor()
    cursor.execute('SELECT Server, User, Password FROM Server')
    data = cursor.fetchall()
    with open('./pass.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['appName', 'User', 'Password'])
        csv_writer.writerows(data)
    conn.close()

'''
def wcsv():     #导入密码 excel
    file_path = str(input(r"文件路径: "))  # 你的文件路径
    data = pd.read_excel(file_path, usecols=['应用', '用户', '密码']) 
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/DB/pass.db')
    cursor = conn.cursor()
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for index,row in data.iterrows():
        app = row['应用']
        user = row['用户']
        password = row['密码']
        cursor.execute('INSERT OR REPLACE INTO Server (Updatetime, Server, User, Password) VALUES (?, ?, ?, ?)', (current_time, app, user, password))
    conn.commit()
    conn.close()'''

def wcsv():     #导入密码
    file_path = str(input(r"文件路径: "))  # 你的文件路径
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + '/DB/pass.db')
    cursor = conn.cursor()
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file_path, 'r', encoding='gbk') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            app = row['应用']
            user = row['用户']
            password = row['密码']
            cursor.execute("INSERT INTO Server (Updatetime, Server, User, Password) VALUES (?, ?, ?, ?)", (current_time, app, user, password))
    conn.commit()
    conn.close()