import sqlite3
import csv
import sys

def criar_conexao():
    try:
        conn = sqlite3.connect('banco_dados.db')
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def criar_tabela():
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS contacts(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telefone TEXT NOT NULL,
                    endereco TEXT NOT NULL
                )
            ''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")
        finally:
            conn.close()

def adicionar_contato(nome, email, telefone, endereco):
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO contacts (nome, email, telefone, endereco)
                VALUES (?, ?, ?, ?)
            ''', (nome, email, telefone, endereco))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao adicionar contato: {e}")
        finally:
            conn.close()

def visualizar_contatos():
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM contacts')
            contatos = cursor.fetchall()
            return contatos
        except sqlite3.Error as e:
            print(f"Erro ao visualizar contatos: {e}")
            return []
        finally:
            conn.close()

def atualizar_contato(id, nome, email, telefone, endereco):
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE contacts
                SET nome = ?, email = ?, telefone = ?, endereco = ?
                WHERE id = ?
            ''', (nome, email, telefone, endereco, id))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao atualizar contato: {e}")
        finally:
            conn.close()

def deletar_contato(id):
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM contacts WHERE id = ?', (id,))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao deletar contato: {e}")
        finally:
            conn.close()

def validar_dados(nome, email, telefone, endereco):
    if " " not in nome.strip():
        print("Nome inválido: deve conter nome e sobrenome.")
        return False
    if "@" not in email or "." not in email.split('@')[-1]:
        print("Email inválido.")
        return False
    if not telefone.strip():
        print("Telefone não pode estar vazio.")
        return False
    if not all(char.isdigit() or char in "+- ()" for char in telefone):
        print("Telefone inválido.")
        return False
    if not endereco.strip():
        print("Endereço não pode estar vazio.")
        return False
    return True

def contato_existe(nome, email, telefone, endereco):
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM contacts
                WHERE nome = ? AND email = ? AND telefone = ? AND endereco = ?
            ''', (nome, email, telefone, endereco))
            contato = cursor.fetchone()
            return contato is not None
        except sqlite3.Error as e:
            print(f"Erro ao verificar se o contato existe: {e}")
            return False
        finally:
            conn.close()

def importar_e_filtrar_csv():
    try:
        with open('contacts_with_errors.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                nome = row['Name'].strip()
                email = row['Email'].strip()
                telefone = row['Phone'].strip()
                endereco = row['Address'].strip()

                if not validar_dados(nome, email, telefone, endereco):
                    print(f"Erro nos dados: {row}")
                    continue

                if not contato_existe(nome, email, telefone, endereco):
                    adicionar_contato(nome, email, telefone, endereco)
    except FileNotFoundError:
        print("Arquivo CSV não encontrado.")
    except KeyError as e:
        print(f"Erro no formato do CSV: coluna {e} não encontrada.")

def menu():
    print("1) Adicionar Contatos")
    print("2) Visualizar Contatos")
    print("3) Atualizar Contatos")
    print("4) Deletar Contatos")
    print("5) Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def main():
    criar_tabela()
    importar_e_filtrar_csv()

    while True:
        escolha = menu()
        if escolha == '1':
            nome = input('Nome Completo: ')
            email = input('Email: ')
            telefone = input('Telefone: ')
            endereco = input('Seu endereço: ')
            if validar_dados(nome, email, telefone, endereco):
                adicionar_contato(nome, email, telefone, endereco)
            else:
                print("Dados Inválidos! Por Favor, Tente Novamente")
        elif escolha == '2':
            contatos = visualizar_contatos()
            for contato in contatos:
                print(f"ID: {contato[0]}, Nome: {contato[1]}, Email: {contato[2]}, Telefone: {contato[3]}, Endereço: {contato[4]}")
        elif escolha == '3':
            id = int(input('ID do Contato a Ser Atualizado: '))
            nome = input('Novo Nome: ')
            email = input('Novo Email: ')
            telefone = input('Novo Telefone: ')
            endereco = input('Novo Endereço: ')
            if validar_dados(nome, email, telefone, endereco):
                atualizar_contato(id, nome, email, telefone, endereco)
            else:
                print("Dados Inválidos! Por Favor, Tente Novamente!")
        elif escolha == '4':
            id = int(input('ID do Contato: '))
            deletar_contato(id)
        elif escolha == '5':
            print("Saindo...")
            sys.exit()
        else:
            print('Opção Inválida!')

if __name__ == "__main__":
    main()
