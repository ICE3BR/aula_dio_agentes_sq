import mysql.connector

try:
    conn = mysql.connector.connect(
        host="ec2-18-231-98-152.sa-east-1.compute.amazonaws.com",
        user="diobank",
        password="quinup20",
        database="dioBank",
        port=3306,
    )
    print("Conexão bem-sucedida!")

    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    print("Tabelas disponíveis:", cursor.fetchall())
    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"Erro: {err}")
