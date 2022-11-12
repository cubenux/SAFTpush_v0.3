#!/usr/bin/env python
# -*-coding:utf-8 -*-
#-----------------------------------------------------------------------------------------
'''
@File    :   envio_saftPT.py
@Time    :   2022/07/09
@Author  :   Carlos Martins 
@Version :   n.d.
@Email   :   n.d.
@License :   Public License
@Desc    :   
--------------------------------------------------------------------
Aplicação para envio de ficheiros SAFT-PT via linha de comandos
--------------------------------------------------------------------

COMANDO PARA pyinstaller:

pyinstaller aplicacao.py --clean --onefile --add-data "envio_2.5.16-9655.jar;../" --runtime-tmpdir "."


'''
#-----------------------------------------------------------------------------------------


#=========================================================================================
#>>>> IMPORTS / MÓDULOS
#=========================================================================================

import os
from time import sleep

# modulo para criar campo de input de passwords (pip install getpass)
import getpass

# modulo para colocar o asterisco com campo das passwords (pip install stdiomask)
import stdiomask


#=========================================================================================
#>>>> VARIÁVEIS GLOBAIS
#=========================================================================================

# flag que permite aceder ao envio do ficheiro se valor for '1'
flag_envio_GLOBAL = 0


#=========================================================================================
#>>>> FUNÇÕES 
#=========================================================================================

# limpa ecrã
#-----------------------------------------------------------------------------------------
def cls():
    
    os.system('cls' if os.name=='nt' else 'clear')


# titulo da aplicacao
#-----------------------------------------------------------------------------------------
def titulo_app():
  
    print("\033[1;36;40m")
    print("===============================================================================")
    print("")
    print("      _____ _____ _____ _____     _____         _   ") 
    print("     |   __|  _  |   __|_   _|___|  _  |_ _ ___| |_ ")
    print("     |__   |     |   __| | | |___|   __| | |_ -|   |")
    print("     |_____|__|__|__|    |_|     |__|  |___|___|_|_|")                                     
    print("")
    print("       VALIDAÇÃO E ENVIO DE FICHEIROS SAFT-PT v.0.1")
    print("")
    print("===============================================================================")
    print("\033[0m")
    

# detalhes da aplicação
#-----------------------------------------------------------------------------------------
def detalhes_app():
    
    print("     \033[1;37;46m[ SOBRE O 'SAFT-Push' ]\033[0m\n")
    print("     Esta aplicação foi desenvolvida para suprimir problemas no envio de ")
    print("     ficheiros SAFT-PT (xml) no Portal E-Fatura através de browsers via ")
    print("     applet Java.")
    print("\n")
    print("     \033[1;37;46m[ DESENVOLVIMENTO ]\033[0m \n\n     Carlos Martins ( cmartins@cubenux.com )")

    print("\n________________________________")
    print("\033[93m» Prima ENTER para continuar...\033[0m")
    input()
    
    
# ajuda da aplicação
#-----------------------------------------------------------------------------------------
def ajuda():
    
    print("     \033[1;37;46m[ AJUDA ]\033[0m\n")
    print("     - A aplicação deve ser executada dentro da pasta onde está o ")
    print("       ficheiro que pretende Validar e Enviar. ")
    print("     - O campo 'Mês' relativo ao ficheiro deve ter o formato 'MM' ")
    print("       Exemplo: 06 ")
    print("     - No campo 'Nome do ficheiro XML' o nome é case sensitive  ")
    print("       e não deve incluir a extensão. ")


    print("\n________________________________")
    print("\033[93m» Prima ENTER para continuar...\033[0m")
    input()


# sub-titulo1
#-----------------------------------------------------------------------------------------
def sub_titulo1(texto):
    
    print(f"\n\033[1;37;44m:: {texto} \033[0m\n")
    


# aviso verde
#-----------------------------------------------------------------------------------------
def aviso_verde(aviso):
            
    print(f"\n \033[1;37;42m[ {aviso} ]\033[0m\n")
    

# aviso vermelho
#-----------------------------------------------------------------------------------------    
def aviso_vermelho(aviso):
    
    print(f"\n \033[1;37;41m[ {aviso} ]\033[0m\n")            


# VALIDA ficheiro XML
#-----------------------------------------------------------------------------------------    
def valida_ficheiro():
    
    print("A validar...")
    
    comando_validacao = 'java -jar envio_2.5.16-9655.jar -n ' + nif + ' -p ' + senha + ' -a ' + ano + ' -m ' + mes + ' -op validar -i "' + ficheiro + '" > output_validacao.txt'        
    # executa o comando
    os.system(comando_validacao)
    
    #++++++++++++++++++++++++++++
    #pesquisa output do comando
    termo_a_pesquisar = 'SAFT file is valid'
    
    # abre o ficheiro
    fich_output = open("output_validacao.txt","r")
    
    # define uma flag e index a 0
    flag = 0
    index = 0
    
    # loop linha a linha do ficheiro
    for linha in fich_output:
        index += 1
        
        # se a string está presente altera a flag para '1'
        if termo_a_pesquisar in linha:
            flag = 1
            
            break
    if flag == 0:
        aviso_vermelho("FICHEIRO XML INVÁLIDO !")
        
        # fecha o ficheiro
        fich_output.close()
        
        # elimina o ficheiro gerado na validacao
        os.system("del output_validacao.txt")
        
        input()
    elif flag == 1:
        aviso_verde("FICHEIRO XML VÁLIDO!")
               
        # define o valor da variável global 
        global flag_envio_GLOBAL
        flag_envio_GLOBAL = 1
    
        # fecha o ficheiro
        fich_output.close()
            
        # elimina o ficheiro gerado na validacao
        os.system("del output_validacao.txt")
        

# ENVIA ficheiro XML
#----------------------------------------------------------------------------------------- 
def envia_ficheiro():

    print ("A enviar...")
    
    comando_envio = 'java -jar envio_2.5.16-9655.jar -n ' + nif + ' -p ' + senha + ' -a ' + ano + ' -m ' + mes + ' -op validar -i "' + ficheiro + '" -o "' + ficheiro_resumido + '"'
    
    # executa o comando
    os.system(comando_envio)
    


#=========================================================================================
#>>>> OUTROS PARÂMETROS
#=========================================================================================

# define tamanho da janela da consola
os.system("mode con cols=80 lines=30")

# esconde o ficheiro que é expandido
os.system("attrib +h envio_2.5.16-9655.jar")


#=========================================================================================
#>>>> PROGRAMA PRINCIPAL
#=========================================================================================

cls()
titulo_app()

#nif = str(input("Indique o NIF :  "))

# NIF/NIPC da empresa
nif = "515627216"

# nome da empresa
nome_empresa = "(GERMINAGRO, LDA)"


# MENU
while True:
    
    cls()
    print(f"[ NIF/NIPC autorizado: {nif} ]")
    titulo_app()  
    print()
    print("   \033[1;37;46m 1 \033[0m VALIDAR / ENVIAR SAFT-PT")
    print()
    print("   \033[1;37;46m 2 \033[0m Sobre o SAFT-Push")
    print()
    print("   \033[1;37;46m 3 \033[0m Ajuda")
    print()
    print("   \033[1;37;46m 0 \033[0m Sair")
    print()
    print("\n________________________________")
    opcao = int(input("\033[93m» OPÇÃO:  \033[0m"))
    
    if opcao == 1:
        
        sub_titulo1("CREDENCIAIS PORTAL E-FATURA")
        
        print(f"   \033[1;37;46m NIPC  \033[0m : \033[93m515627216 \033[0m {nome_empresa}\n")
        
        # senha para o portal e-fatura
        senha = stdiomask.getpass(prompt="   \033[1;37;46m Senha \033[0m : ")

        sub_titulo1("DADOS DO FICHEIRO SAFT-PT (xml)")

        # ano a que se refere o ficheiro
        ano =str(input("   \033[1;37;46m Ano \033[0m : "))

        # mês a que se refere o ficheiro
        mes = str(input("   \033[1;37;46m Mês \033[0m : "))

        print()
        # nome do ficheiro XML (sem a extensão)
        ficheiro = str(input("   \033[1;37;46m Nome do ficheiro XML \033[0m : "))
        ficheiro = ficheiro + ".xml"

        print()
        ficheiro_resumido = ficheiro + ".resumido.xml"
        
        
        sub_titulo1("CONFIRMAÇÃO DE DADOS")
        print("   \033[1;37;46m NIF.......\033[0m " + nif)
        #print("   \033[1;37;46m SENHA.....\033[0m " + senha)
        print("   \033[1;37;46m ANO.......\033[0m " + ano)
        print("   \033[1;37;46m MÊS.......\033[0m " + mes)
        print("   \033[1;37;46m FICHEIRO..\033[0m " + ficheiro)

        print()

        confirmacao1_operacao = input("-» \033[93mA informação está correcta? \033[0m [ (s) sim / (n) não ] :  ")

        if confirmacao1_operacao == "s":   
                
            valida_ficheiro()
            
            if (flag_envio_GLOBAL == 1):  # se o ficheiro for válido o valor da variavel é 1
        
                confirmacao_envio = input("-» \033[93mDeseja enviar o ficheiro SAFT-PT? \033[0m [ (s) sim / (n) não ] :  ")
                
                if confirmacao_envio == "s":
                    print("A enviar... (opcao de envio inactiva - versao demonstrativa)")
                    
                    # chama função para enviar ficheiro XML (alterar -op 'validar 'para 'enviar')
                    #envia_ficheiro()
                    
                    
                    input()
                
                else:
                    print("")
                    
            
        else:
            print()
                
    elif opcao == 2:
        
        cls()
        titulo_app()       
        detalhes_app()
        
    elif opcao == 3:
        
        cls()
        titulo_app()       
        ajuda()
    
    elif opcao == 0:
        print("A encerrar aplicação...")
        
        # elimina o ficheiro 'jar' (escondido)
        os.system("del /A:H envio_2.5.16-9655.jar")
        
        sleep(1)
        exit()
    
    else:
        print("Opção inválida!")



    
    
                    