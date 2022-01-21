
from random import randint
cadastro = {'nome':[], 'email':[], 'telefone':[], 'curso':[],}
voucher = randint(100, 400)

def valida_int(pergunta , min, max):
    x = int(input(pergunta))
    while ((x < min) or ( x > max)):
        x =int(input(pergunta))
    return x


def criaCadastro(nomearquivo):
    try:
        a= open(nomearquivo, 'wt+')
        a.close
    except FileNotFoundError:
        print('Erro na criaço de arquivo...')
    else:
        print('arquivo{} foi criado sucesso!\n'. format(nomearquivo))


def existeCadastro(nomearquivo):
    try:
     a = open(nomearquivo, 'rt')
     a.close
    except FileNotFoundError:
        return False
    else:
        return True



def listaCadastro(nomearquivo):
    try:
        a = open (nomearquivo, 'rt')
    except:
        print('Erro ao ler o Arquivo...')
    else:
        print(a.read())
    finally:
        a.close()



def cadastra (nomearquivo, nome, email, telefone, curso, voucher):
    try:
        a = open (nomearquivo,'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
         a.write('\nvoucher: {}\n'.format(voucher))
         a.write('nome: {}\n'.format(nome))
         a.write('email: {}\n'.format(email))
         a.write('telefone: {}\n'.format(telefone))
         a.write('curso: {}\n'.format(curso))
         a.write(48 * '-')
    finally:
        a.close()
       



arquivo = 'lista.txt'
if existeCadastro(arquivo):
    print('Arquivo localizado!')
else:
    print('Aquivo inexistente!')
    criaCadastro
    
while True:
    print(21 * '-', 'MENU', 21* '-')
    print('\n1 - Nova inscrição')
    print('2 - Vizualizar Incrição')
    print('3 - Encerrar')

    op = valida_int('Escolha opção desejada:', 1, 3)
    print('\n')

   
    if (op == 1):
        
        print('voucher: {}'. format(voucher))
        nome = input('Digite seu nome:')
        email = input('Digite teu seu email:')
        telefone = int(input('Digite seu telefone:'))
        curso = input('Digite o curso desejado:')
        cadastra (arquivo, nome, email, telefone, curso, voucher)
        continue
    elif (op ==2):
        print( 15 * '-', 'LISTA DE INSCRITO', 15* '-')
        listaCadastro(arquivo)
        continue
    elif(op==3):
        print('Encerrando!')
        continue
    elif op:
        print('opção invalida ')
        break
       
                

    
   
            
   

    


    
    

    

   