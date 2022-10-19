#primeiro passo é instalar o flask:  pip instal flask
#após importar ele - 




from flask import Flask, render_template, request

#iremos importar o arquivo que está o codigo pro banco de dados dao.py

import dao


app = Flask(__name__)

@app.route('/')
def abre():
    return render_template("index.html")

@app.route('/index')
def abre_index():
    return abre()

@app.route('/home')
def abre_home():
    return render_template("home.html", dados_aluno = dao.consulta_alunos(), dados_livro = dao.consulta_livros())

@app.route('/cadastro_aluno')
def abre_cadastro_aluno():
    return render_template("cadastro_aluno.html")

@app.route('/cadastro_livro')
def abre_cadastro_livro():
    return render_template("cadastro_livro.html")

@app.route('/cadastro_usuario')
def abre_cadastro_usuario():
    return render_template("cadastro_usuario.html")

@app.route('/excluir_aluno')
def abre_excluir_aluno():
    return render_template('excluir_aluno.html',dados = dao.consulta_alunos())

@app.route('/excluir_livro')
def abre_excluir_livro():
    return render_template('excluir_livro.html',dados = dao.consulta_livros())

@app.route('/atualizar_aluno')
def abre_atualizar_aluno():
    return render_template('atualizar_aluno.html',dados = dao.consulta_alunos())

@app.route('/atualizar_livro')
def abre_atualizar_livro():
    return render_template('atualizar_livro.html', dados = dao.consulta_livros())

@app.route('/consulta_aluno')
def abre_consulta_aluno():
    return render_template('consulta_aluno.html', dados = dao.consulta_alunos())

@app.route('/consulta_livro')
def abre_consulta_livro():
    return render_template('consulta_livro.html', dados = dao.consulta_livros())

@app.route('/emprestimo')
def abre_emprestimo():
    return render_template('emprestimo.html', dados_livro = dao.emprestimo_livro(), dados_aluno = dao.emprestimo_aluno(),dados_emprestimo =  dao.consulta_emprestimo() )

@app.route('/emprestimo', methods=['POST'] )
def insert_emprestimo():
    id_livro      = request.form['livro']
    id_aluno      = request.form['aluno']
    dt_emprestimo = request.form['data_emprestimo']
    dt_devolucao  = request.form['data_devolucao']
   #situacao      = request.form ['situacao']
    
    dao.insert_emprestimo(id_aluno,id_livro,dt_emprestimo,dt_devolucao)

    return abre_emprestimo()


#cada rota acima define pra onde ir quando é solicitado esssas rotas na url

@app.route('/cadastro_aluno', methods=['POST']) # esse cadastro aluno dele estavar no action do form do HTML e o method post.
def gravar_dados_aluno():
    nome      = request.form['nome']    # o request.form serve para pegar os inputs do html e trazer pra essa variavel no python
    cpf       = request.form['cpf']
    matricula = request.form['matricula']
    telefone  = request.form['telefone']


    consulta_matricula     = dao.consultaMatricula(matricula)
    consulta_cpf           = dao.consultaCpf_aluno(cpf)
   
    if consulta_matricula is not None:
        return render_template("cadastro_aluno.html",erro ='Aluno já está cadastrado!')

    if consulta_cpf is not None:
        return render_template("cadastro_aluno.html",erro ='CPF já está cadastrado!')
    
    else:

        #iremos chamar o arquivo dao.py e a função que queremos executar e passar os parametros que colocamos para inserir no banco de dados
        dao.insert_tb_aluno(nome,cpf,matricula,telefone) # Aqui pegamos a variavel que está com os valores dos inputs do html e passamos 
        #como parametros que vai ser inserido no banco de dados

        return abre_cadastro_aluno()


@app.route('/cadastro_livro', methods=['POST'])
def gravar_dados_livro():
    nome      = request.form['nome']    
    isbn      = request.form['isbn']
    editora   = request.form['editora']
    tipo      = request.form['tipo']

      
    consulta_isbn           = dao.consultaisbn(isbn)
   
    if consulta_isbn is not None:
        return render_template("cadastro_livro.html",erro ='Livro já está cadastrado!')

    else:
        dao.insert_tb_livro(nome,isbn,editora,tipo)
        return abre_cadastro_livro()


@app.route('/consulta_aluno',  methods=['POST'])
def consulta_aluno():
    matricula            = request.form['matricula']
    return render_template('consulta_aluno.html', dado = dao.consulta_aluno1(matricula), dados = dao.consulta_alunos())

@app.route('/consulta_livro',  methods=['POST'])
def consulta_livro():
    nome            = request.form['nome']
    return render_template('consulta_livro.html', dado = dao.consulta_livro1(nome), dados = dao.consulta_livros())


@app.route('/cadastro_usuario', methods=['POST'])
def gravar_dados_usuario():
    nome     = request.form['nome']    
    cpf      = request.form['cpf']
    telefone = request.form['telefone']
    email    = request.form['email']
    usuario  = request.form['usuario']
    senha    = request.form['senha']

    consulta_cpf     = dao.consultaCpf(cpf)
    consulta_email   = dao.consultaEmail(email)
    consulta_usuario = dao.consultaUsuario(usuario)
 
   
    if consulta_cpf   is not None and consulta_email is not None and consulta_usuario is not None:
        return render_template("cadastro_usuario.html",erro ='Existe cadastro com esses dados!')
    elif consulta_cpf   is not None:
        return render_template("cadastro_usuario.html",erro ='CPF já está cadastrado!')
    elif consulta_email is not None:
        return render_template("cadastro_usuario.html",erro ='Email já está cadastrado!')
    elif consulta_usuario is not None:
        return render_template("cadastro_usuario.html",erro ='Nome de usuario não disponivel!')
 
    else:
 
        dao.insert_tb_usuario(nome,cpf,telefone,email,usuario,senha)
    
        return abre()
        

@app.route('/index',  methods=['POST'])
def login():
    usuario       = request.form['usuario']
    senha         = request.form['senha']

    dados_login = dao.login_usuario(usuario, senha)


    if dados_login is not None:
        return abre_home()
    else:
       
        return render_template("index.html",erro ='Usuario ou senha incorretos!')

#rotas de delete

@app.route('/delete_aluno',  methods=['POST'])
def delete_aluno():
    matricula  = request.form['matricula']

    dao.delete_alunos(matricula)
    return abre_excluir_aluno()

@app.route('/delete_livro',  methods=['POST'])
def delete_livro():
    isbn  = request.form['isbn']

    dao.delete_livros(isbn)
    return abre_excluir_livro()

@app.route('/atualizar_aluno',  methods=['POST'])
def atualizar_aluno():
    nome           = request.form['novo_nome']    
    cpf            = request.form['novo_cpf']
    nova_matricula = request.form['nova_matricula']
    telefone       = request.form['novo_telefone']
    matricula      = request.form['matricula']

    consulta_matricula      = dao.consultaMatricula(nova_matricula)
    consulta_matricula2     = dao.consultaMatricula(matricula)
    consulta_cpf            = dao.consultaCpf_aluno(cpf)

    if consulta_matricula2 is None:
        return render_template("atualizar_aluno.html",erro ='Matricula não encontrada', dados = dao.consulta_alunos())

    else:

        if consulta_matricula is not None:
            return render_template("atualizar_aluno.html",erro ='Matricula já está cadastrada!!!', dados = dao.consulta_alunos())

        if consulta_cpf is not None:
            return render_template("atualizar_aluno.html",erro ='CPF já está cadastrado!!!', dados = dao.consulta_alunos())
        
        else:

            dao.update_aluno(nome,cpf,nova_matricula,telefone,matricula)
            return render_template('atualizar_aluno.html',dados = dao.consulta_alunos())

@app.route('/atualizar_livro',  methods=['POST'])
def atualizar_livro():
    nome           = request.form['nome']    
    novo_isbn      = request.form['isbn']
    editora        = request.form['editora']
    tipo           = request.form['tipo']
    isbn           = request.form['isbn_antigo']

      
    consulta_isbn           = dao.consultaisbn(novo_isbn)
    consulta_isbn2           = dao.consultaisbn(isbn)

    print (isbn)

    if consulta_isbn2  is None:
        return render_template("atualizar_livro.html",erro ='ISBN não encontrado!!!',dados = dao.consulta_livros())
    else:

        if consulta_isbn is not None:
            return render_template("atualizar_livro.html",erro ='ISBN já está cadastrado!!!',dados = dao.consulta_livros())

        else:
            dao.update_livro(nome,novo_isbn,editora,tipo,isbn)
            return render_template('atualizar_livro.html',dados = dao.consulta_livros())

app.run(debug=True)






