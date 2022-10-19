#esse arquivo é para conexão com o banco de dados, iremos istalar o conector e depois importa lo. pip install mysql-connector-python


#create table usuario(
#id int auto_increment primary key,
#nome varchar(150) not null,
#cpf varchar(50) unique not null,
#telefone varchar(50) not null,
#email varchar(50) unique not null,
#usuario varchar(50) unique not null,
#senha varchar(50) not null);

import mysql.connector  as banco 

meubanco = banco.connect(host = "192.168.1.254", user = "estagiario", password = "estagio123", database = "treinamento_daila")
#meubanco = banco.connect(host = "localhost", user = "root", password = "admin", database = "biblioteca")

#aqui abaixo ficam as querys, pode ficar dentro das funções tbm... essas querys serão executadas no banco de dados pode ser insert, update, 
# delete...

sql_insert_aluno         = "insert into aluno(nome,cpf,matricula,telefone) values (%s,%s,%s,%s)"  # A tabela e as colunas devem estar exatamente 

#como banco de dados / '%s' permite que você passe os valores na função
sql_insert_livro         = "insert into livro(nome,isbn,editora,tipo) values (%s,%s,%s,%s)"
sql_insert_usuario       = "insert into usuario(nome,cpf,telefone,email,usuario,senha) values(%s,%s,%s,%s,%s,%s)"
sql_select_usuario       = "select usuario,senha from usuario where usuario like %s and senha like %s "
sql_insert_emprestimo    = "insert into emprestimo(fk_id_aluno,fk_id_livro,data_emprestimo,data_devolucao) values(%s,%s,%s,%s)"


# consultas para ver se já tem cpf, email ou usuario já cadastrado tela de cadastro de usuario
sql_select_usu_cpf       = "select cpf from usuario where cpf like %s "
sql_select_usu_email     = "select email from usuario where email like %s "
sql_select_usu_usuario   = "select usuario from usuario where usuario like %s "

# consultas para ver se já tem cpf e matricula já cadastrado tela de cadastro de aluno
sql_select_alu_matricula = "select matricula from aluno where matricula like %s"
sql_select_alu_cpf       = "select cpf from aluno where cpf like %s"

# consultas para ver se já tem isbn já cadastrado tela de cadastro de livro
sql_select_li_isbn       = "select isbn from livro where isbn like %s"

# consultas para filtrar os dados das tabelas da tela aluno e livros
sql_select_aluno         = "select * from aluno where matricula = %s"
sql_select_livro         = "select * from livro where nome like %s"

# consultas para retornar todos os dados para as tabelas da tela aluno e livros e emprestimo
sql_consuta_alunos         = "select * from aluno"
sql_consuta_livros         = "select * from livro"
sql_consuta_emprestimo     = "select aluno.nome, matricula,livro.nome,data_emprestimo,data_devolucao from aluno,livro,emprestimo where aluno.id = emprestimo.fk_id_aluno and livro.id = emprestimo.fk_id_livro order by data_emprestimo"


# delete
sql_delete_aluno        = "delete from aluno where matricula like %s"
sql_delete_livro        = "delete from livro where isbn like %s"

# Update
sql_update_aluno        = "update aluno set nome = %s, cpf = %s, matricula = %s, telefone = %s where matricula = %s"
sql_update_livro        = "update livro set nome = %s, isbn = %s, editora = %s, tipo = %s where isbn = %s"

#abaixo temos as funções 

# Funçoes para inserir dados no banco de dados:

def insert_tb_aluno(nome,cpf,matricula,telefone): # Dentro dos parenteses ficam os valores que iremos pegar no input e que serão enviados 
    #pro banco de dados, temos que chamar essa função na rota do main para ser executada.

  #faz conexão com o banco de dados, criamos uma variavel e passamos os parametros para conectar com o banco
    

  #recebe o cursor para poder manipular o sql, o python não entende sql mas já existe esse cursor(), então atribuimos ele para poder executar 
  # um comando em sql 
    cursor = meubanco.cursor()

  #executa o comando sql, aqui atribuimos os valores que iremos passar pro banco de dados a uma variavel
    valores = (nome, cpf, matricula,telefone) 

  #chama o cursor pra interpletar o sql e executar a query que definimos no inicio e tbm passamos a variavel de valores
    cursor.execute(sql_insert_aluno,valores)

   #confima a inserção dos bancos
    meubanco.commit()


def insert_tb_livro(nome,isbn,editora,tipo):
    
    cursor = meubanco.cursor()
    valores = (nome, isbn, editora,tipo)
    cursor.execute(sql_insert_livro,valores)
    meubanco.commit()

def insert_tb_usuario(nome,cpf,telefone,email,usuario,senha):
    
    cursor = meubanco.cursor()
    valores = (nome,cpf,telefone,email,usuario,senha)
    cursor.execute(sql_insert_usuario,valores)
    meubanco.commit()
#fim inserir dados no banco de dados

#tela login:
def login_usuario(usuario,senha):

    
    cursor = meubanco.cursor()
    valores = (usuario,senha)
    cursor.execute(sql_select_usuario, valores)
    
    return cursor.fetchone()

# Funções para consultar se já existe cadastro:
# Usuario:
def consultaCpf(cpf):

    
    cursor = meubanco.cursor()
    valores = (cpf,)
    cursor.execute(sql_select_usu_cpf, valores)
    
    return cursor.fetchone()

def consultaEmail(email):

    
    cursor = meubanco.cursor()
    valores = (email,)
    cursor.execute(sql_select_usu_email, valores)
    
    return cursor.fetchone()


def consultaUsuario(usuario):

    
    cursor = meubanco.cursor()
    valores = (usuario,)
    cursor.execute(sql_select_usu_usuario, valores)
    
    return cursor.fetchone()

#Alunos:
def consultaMatricula(matricula):

    
    cursor = meubanco.cursor()
    valores = (matricula,)
    cursor.execute(sql_select_alu_matricula, valores)
    
    return cursor.fetchone()

def consultaCpf_aluno(cpf):

    
    cursor = meubanco.cursor()
    valores = (cpf,)
    cursor.execute(sql_select_alu_cpf, valores)
    
    return cursor.fetchone()


#livros:
def consultaisbn(isbn):

    
    cursor = meubanco.cursor()
    valores = (isbn,)
    cursor.execute(sql_select_li_isbn, valores)
    
    return cursor.fetchone()


#  Funções para filtro para a tela Alunos e livros: 
def consulta_aluno1(matricula):

    
    cursor = meubanco.cursor()
    valores = (matricula,)
    cursor.execute(sql_select_aluno, valores)
    
    return cursor.fetchall()

def consulta_alunos():

    
    cursor = meubanco.cursor()
    
    cursor.execute(sql_consuta_alunos)
    
    return cursor.fetchall()


def consulta_livro1(nome):

    
    cursor = meubanco.cursor()
    valores = (nome,)
    cursor.execute(sql_select_livro, valores)
    
    return cursor.fetchall()

def consulta_livros():

    
    cursor = meubanco.cursor()
    cursor.execute(sql_consuta_livros)
    
    return cursor.fetchall()        
#fim filtro das tabelas


#delete aluno

def delete_alunos(matricula):

    
    cursor = meubanco.cursor()
    valores = (matricula,)
    cursor.execute(sql_delete_aluno, valores)
    meubanco.commit() #sempre que fazer uma alteração tem que utilizar para validar
     

#delete livro

def delete_livros(isbn):

   
    cursor = meubanco.cursor()
    valores = (isbn,)
    cursor.execute(sql_delete_livro, valores)
    meubanco.commit()

def update_aluno(nome,cpf,nova_matricula,telefone,matricula):
    cursor = meubanco.cursor()
    valores = (nome,cpf,nova_matricula,telefone,matricula)
    cursor.execute(sql_update_aluno, valores)
    meubanco.commit()

def update_livro(nome,novo_isbn,editora,tipo,isbn):
    cursor = meubanco.cursor()
    valores = (nome,novo_isbn,editora,tipo,isbn)
    cursor.execute(sql_update_livro, valores)
    meubanco.commit()


#retorna o nome para lista de emprestimo de livros


def emprestimo_livro():

    cursor = meubanco.cursor()
    
    cursor.execute(sql_consuta_livros)
    
    return cursor.fetchall()


def emprestimo_aluno():

    cursor = meubanco.cursor()
    
    cursor.execute(sql_consuta_alunos)
    
    return cursor.fetchall()


def consulta_emprestimo():
    cursor = meubanco.cursor()
    cursor.execute(sql_consuta_emprestimo)
    
    return cursor.fetchall()  


def insert_emprestimo(id_aluno,id_livro,dt_emprestimo,dt_devolucao):
    cursor = meubanco.cursor()
    valores = (id_aluno,id_livro,dt_emprestimo,dt_devolucao)
    cursor.execute(sql_insert_emprestimo, valores)
    meubanco.commit()