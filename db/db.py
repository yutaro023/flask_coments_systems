import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='usuarios'
    )
    return conn

def sign_up(nome, e_mail, senha, date):
    conn = get_connection()
    pointer = conn.cursor()
    pointer.execute('INSERT INTO login (nome, email, senha, data_nascimento) values(%s, %s, %s, %s)', (nome, e_mail, senha, date))
    conn.commit()
    pointer.close()
    conn.close()

def insert_coment(comentarios):
   conn = get_connection()
   cursor = conn.cursor() 
   cursor.execute("INSERT INTO comentarios (texto) VALUES (%s)", (comentarios,))
   conn.commit()
   cursor.close()
   conn.close()

def get_comment():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT texto FROM comentarios")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def credentials_is_existy(e_mail, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('select email, senha from login where email= %s and senha=%s', (e_mail, password))
    result = cursor.fetchone() 
    cursor.close()
    conn.close()
    if(not(result is None)):
        return True
    else:
        return False
    


