medicos = [{
    "nome": "Kayon",
    "endereço": "São Caetano",
    "telefone": "88 998103374",
    "sexo": "masculino",
    "crm": "sp/123456",
    "senha": "1320",
    "rg": "123456789",
    "cpf": "109.900.899-03",
}]

pacientes = [{
    "nome": "matheus",
    "endereço": "Jaguaribe",
    "telefone": "88981403557",
    "sexo": "masculino",
    "rg": "0101019",
    "cpf": "545.000.122-09",
    "idade": "19",
}]

convenios = [{
    "nome": "unimed",
    "endereço": "Varzea alegre",
    "telefone": "88981433231",
    "CNPJ": "111.111.111-00",
}]

agenda = []



buscarMedicos = (medicos)

import re
import getpass
import random
import string



def validarCPF(cpf):
    cpf_regex = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
    return bool(cpf_regex.match(cpf))

def validarCNPJ(cnpj):
    cnpj_regex = re.compile(r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$')
    return bool(cnpj_regex.match(cnpj))

def validarEndereco(endereco):
    return len(endereco.strip()) > 0

def validarRG(rg):
    rg_regex = re.compile(r'^\d{9}$')
    return bool(rg_regex.match(rg))

def validarTelefone(telefone):
    telefone_regex = re.compile(r'^\d{2}.\d{9}$')
    return bool(telefone_regex.match(telefone))

def validarCRM(crm):
    crm_regex = re.compile(r'^[A-Za-z]{2}/\d{6}$')
    return bool(crm.strip())>0

def validarSex(sex):
    sex_regex = re.compile(r'^(1|2)$')
    if sex_regex.match(str(sex)):
        return True
    else:
        return False

def cadastrarMedicos():


    while True:
        print("Deseja cadastrar um médico?\n 1- sim\n 2 - não")
        resposta = int(input(""))

        if resposta == 1:
            print("Para realizar o cadastro do médico, insira as seguintes informações:")
        else: 
            print("programa cancelado!")
            break
         
        while True:
         mNome = (input("insira o nome do médico: "))
         if mNome.isnumeric() :
                print("nome invalido. tente novamente")
                continue
         break
     
        while True:
         mCPF = (input("insira o CPF do médico (com dígitos): "))
         if not validarCPF(mCPF):
            print("CPF inválido. tente novamente")
            continue
         break
        
        while True:
            mRG = (input("insira o RG do médico (sem dígito): "))
            if not validarRG(mRG):
                print("RG inválido. tente novamente")
                continue
            break
        
        while True:
            mCRM = (input("insira o CRM do médico: "))
            if not validarCRM(mCRM):
                print("CRM inválido. tente novamente")
                continue
            break


        while True:
            mTel = input("Insira o telefone do médico: ")
            if not validarTelefone(mTel):
                print("Telefone inválido! Por favor, insira um telefone válido.")
                continue
            break

        while True:
            mEnd = input("Insira o endereço do médico: ")
            if not validarEndereco(mEnd):
                print("Endereço inválido! Por favor, insira um endereço válido.")
                continue
            break
        
        while True:
            mSex = input("Insira o sexo do médico\n 1- feminino\n2- masculino\n")
            if not validarSex(mSex):
                print("Sexo inválido. Tente novamente")
                continue
            break

        mSen = input("crie a senha de acesso do médico: ")

        print(f'senha criada. sua senha é {mSen}')


        medicos.append({
            "nome": mNome,
            "cpf": mCPF,
            "rg": mRG,
            "crm": mCRM,
            "telefone": mTel,
            "endereço": mEnd,
            "sexo": mSex,
            "senha": mSen
        }
        )
  
        print(medicos)
        print("médico cadastrado com sucesso")

def cadastrarPacientes():
    while True:
        print("Deseja cadastrar um paciente?\n 1- sim\n 2 - não")
        resposta = int(input(""))

        if resposta == 1:
            print("Para realizar o cadastro do paciente, insira as seguintes informações:")
        else: 
            print("programa cancelado!")
            break
         
        while True:
         pNome = (input("insira o nome do paciente: "))
         if pNome.isnumeric() :
                print("nome invalido. tente novamente")
                continue
         break

        while True:
            pIdade = (input("insira a idade do paciente: "))
            if not pIdade.isnumeric():
                print("idade inválida. tente novamente")
                continue
            break
     
        while True:
         pCPF = (input("insira o CPF do paciente (com dígitos): "))
         if not validarCPF(pCPF):
            print("CPF inválido. tente novamente")
            continue
         break
        
        while True:
            pRG = (input("insira o RG do paciente (sem dígito): "))
            if not validarRG(pRG):
                print("RG inválido. tente novamente")
                continue
            break
        
        while True:
            pTel = input("Insira o telefone do paciente: ")
            if not validarTelefone(pTel):
                print("Telefone inválido! Por favor, insira um telefone válido.")
                continue
            break

        while True:
            pEnd = input("Insira o endereço do paciente: ")
            if not validarEndereco(pEnd):
                print("Endereço inválido! Por favor, insira um endereço válido.")
                continue
            break
        
        while True:
            pSex = input("Insira o sexo do paciente\n 1- feminino\n2- masculino\n")
            if not validarSex(pSex):
                print("Sexo inválido. Tente novamente")
                continue
            break

        pSen = input("crie a senha de acesso do paciente: ")

        print(f'senha criada. sua senha é {pSen}')

        
        pacientes.append({
            "nome": pNome,
            "idade": pIdade,
            "endereço": pEnd,
            "telefone": pTel,
            "cpf": pCPF,
            "rg": pRG,
            "sexo": pSex,
        })
        print(pacientes)
        print("paciente cadastrado com sucesso")

    else:
        print("Programa cancelado!")


def cadastrarConvenios():
    
    while True:
        print("Deseja cadastrar um convênio?\n 1 - sim 2- não")

        resposta1 = int(input(""))

        if resposta1 == 1:
            print("para realizar o cadastro do convênio, insira as seguintes informações.")
            break
        else:
            print("Programa cancelado!")

    while True:
         cNome = (input("insira o nome o convênio: "))
         if cNome.isnumeric() :
                print("nome invalido. tente novamente")
                continue
         break
     
    while True:
         cCNPJ = (input("insira o CNPJ do convênio com dígitos: "))
         if not validarCPF(cCNPJ):
            print("CNPJ inválido. tente novamente")
            continue
         break
    
    while True:
        cEnd = (input("insira o endereço do convênio: "))
        if not validarEndereco(cEnd):
            print("Endereço inválido. tente novamente")
            continue
        break

    while True:
            cTel = input("Insira o telefone do convênio: ")
            if not validarTelefone(cTel):
                print("Telefone inválido! Por favor, insira um telefone válido.")
                continue
            break
    
    while True:
        cPlan = int(input("escolha um dos planos disponíveis: 1-Amil Saúde, 2-Unimed, 3-SulAmérica Saúde, 4-Bradesco Saúde, 5-Golden Cross"))

        if cPlan == 1 :
            print(f"o plano escolhido foi o Amil Saúde")
            
        
        elif cPlan ==2:
             print(f"o plano escolhido foi o Unimed")
       
             
        elif cPlan ==3:
             print(f"o plano escolhido foi o SulAmérica Saúde")
           
        
        elif cPlan ==4:
             print(f"o plano escolhido foi o Bradesco Saúde")
           
        
        elif cPlan ==5:
             print(f"o plano escolhido foi o Golden Cross")
             
            
        else: 
            print("Plano Indisponível. tente novamente")
            continue
        break

        convenios.append({
                "nome": cNome,
                "endereco": cEnd,
                "telefone": cTel,
                "CNPJ": cCNPJ,
                "Planos": cPlan,
            })
        
        print(convenios)
        print("convenio cadastrado com sucesso")

    else:
        print("programa cancelado")

def BuscarMedicos():
    print("Informe o nome ou CRM do médico")
    busm = input("").lower()
    resultados = [medico for medico in medicos if busm in medico['nome'] or busm in medico['crm']]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CRM: {resultado['crm']}")
    else:
        print("Nenhum médico encontrado.")

def buscarPacientes():
    print("Informe o nome ou CPF do paciente: ")
    busp = input("").lower()
    resuls = [paciente for paciente in pacientes if busp in paciente['nome'] or busp in paciente['cpf']]
    if resuls:
        for resultado in resuls:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CPF: {resultado['cpf']}")
    else:
        print("Nenhum paciente encontrado.")

def buscarConvenios():
    print("Informe o nome ou CNPJ do convênio")
    busc = input("").lower()
    resultados = [convenio for convenio in convenios if busc in convenio['nome'] or busc in convenio['CNPJ']]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CNPJ: {resultado['CNPJ']}")
    else:
        print("Nenhum convênio encontrado.")


def alterarMedicos():
    print("Forneça o CRM do médico a ser alterado")
    crm = input("")
    medico = next((medico for medico in medicos if medico['crm'] == crm), None)
    if medico:
        print(f"Dados atuais: {medico}")
        print("Forneça os novos dados (deixe em branco para manter o valor atual):")
        Mnome = input(f"Nome ({medico['nome']}): ") or medico['nome']
        Mtelefone = input(f"Telefone ({medico['telefone']}): ") or medico['telefone']
        Mendereco = input(f"Endereço ({medico['endereço']}): ") or medico['endereço']
        Msexo = input(f"Sexo ({medico['sexo']}): ") or medico['sexo']
        Mcrm = input(f"CRM ({medico['crm']}): ") or medico["crm"]
        Msenha = input(f"Senha ({medico['senha']}): ") or medico['senha']
        medico.update({
            "nome": Mnome,
            "telefone": Mtelefone,
            "endereço": Mendereco,
            "sexo": Msexo,
            "senha": Msenha,
            "crm": Mcrm,
        })
        print("Dados do médico atualizados.")
    else:
        print("Médico não encontrado.")

def alterarPacientes():
    print("Forneça o CPF do paciente a ser alterado")
    cpf = input("")
    paciente = next((paciente for paciente in pacientes if paciente['cpf'] == cpf), None)
    if paciente:
        print(f"Dados atuais: {paciente}")
        print("Forneça os novos dados (deixe em branco para manter o valor atual):")
        pnome = input(f"Nome ({paciente['nome']}): ") or paciente['nome']
        Lidade = input(f"Idade ({paciente['idade']}): ") or paciente['idade']
        ptelefone = input(f"Telefone ({paciente['telefone']}): ") or paciente['telefone']
        pendereco = input(f"Endereço ({paciente['endereço']}): ") or paciente['endereço']
        psexo = input(f"Sexo ({paciente['sexo']}): ") or paciente['sexo']
        paciente.update({
            "nome": pnome,
            "idade": Lidade,
            "telefone": ptelefone,
            "endereço": pendereco,
            "sexo": psexo
        })
        print("Dados do paciente atualizados.")
    else:
        print("Paciente não encontrado.")

def marcarCompromisso():
    print("Você deseja marcar um compromisso?")
    compromisso = input("")
    if compromisso.lower() == "sim":
        print("Informe a data que você deseja (formato: DD/MM/AAAA):")
        data = input("")
        print("Informe a hora que você deseja iniciar sua consulta (formato: HH:MM - HH:MM):")
        horario = input("")
        print("Descreva o seu compromisso:")
        descreva = input("")
        print("Você deseja salvar essas informações? SIM/NÃO")
        rc = input("")
        if rc.lower() == "sim":
            agenda.append({
                "data": data,
                "hora": horario,
                "descrição": descreva
            })
            print("Compromisso agendado com sucesso!")
        else:
            print("Programa cancelado.")
    else:
        print("Programa encerrado")

      


def marcarConsulta():
    print("Você deseja marcar uma consulta? sim/não")
    marcac = input("")
    
    if marcac == "sim":
        print("Informe o nome do médico:")
        nm = input("")
        mencontrado = next((medico for medico in  medicos ['nome'] == str), None)
    
        if mencontrado:
            print("Informe o nome do paciente:")
            pnome = input("")
            pencontrado = next((paciente for paciente in pacientes if paciente['nome'] == pnome), None)
            
            if pencontrado:
                print("Informe a data da consulta (formato: DD/MM/AAAA):")
                data = input("")
                print("Informe o horário da consulta (formato: HH:MM - HH:MM):")
                horario = input("")
                print("Consulta marcada com sucesso!")
                agenda.append({
                    "data": data,
                    "horario": horario,
                    "medico": nm,
                    "paciente": pnome
                })
            else:
                print("Paciente não encontrado.")
        else:
            print("Que pena, médico não encontrado.")
    else:
        print("Programa Cancelado.")

def emitirRelatorio():
    print("Qual relatório você deseja emitir?")
    print("1 - Médicos cadastrados")
    print("2 - Pacientes cadastrados")
    print("3 - Convênios")
    print("4 - Consultas realizadas em um intervalo de data")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        print("Médicos cadastrados:")
        for medico in medicos:
            print(f"Nome: {medico['nome']}, CPF: {medico['cpf']}, CRM: {medico['crm']}, Telefone: {medico['telefone']}")
    elif escolha == "2":
        print("Pacientes cadastrados:")
        for paciente in pacientes:
            print(f"Nome: {paciente['nome']}, CPF: {paciente['cpf']}, Telefone: {paciente['telefone']}")
    elif escolha == "3":
        print("Convênios:")
        for convenio in convenios:
            print(f"Nome: {convenio['nome']}, CNPJ: {convenio['CNPJ']}, Telefone: {convenio['telefone']}")
    elif escolha == "4":
        print("Informe a data de início (formato DD/MM/AAAA):")
        data_inicio = input("")
        print("Informe a data de fim (formato DD/MM/AAAA):")
        data_fim = input("")
        print(f"Consultas de {data_inicio} a {data_fim}:")
        for consulta in agenda:
            data_consulta = consulta.get("data", "")
            if data_inicio <= data_consulta <= data_fim:
                print(f"Data: {consulta['data']}, Horário: {consulta.get('horario', '')}, Médico: {consulta.get('medico', '')}, Paciente: {consulta.get('paciente', '')}")
    else:
        print("Opção inválida.")

lang = input("1 - Cadastrar Médicos\n"
             "2 - Cadastrar Pacientes\n"
             "3 - Cadastrar Convênios\n"
             "4 - Buscar Médicos\n"
             "5 - Buscar Pacientes\n"
             "6 - Buscar Convênios\n"
             "7 - Alterar Médicos\n"
             "8 - Alterar Pacientes\n"
             "9 - Marcar Compromisso\n"
             "10 - Marcar Consulta\n"
             "11 - Emitir Relatório\n"
             "12 - Encerrar Programa\n"
             "O que você deseja fazer? ")

while lang != "12":
    match lang:
        case "1":
            cadastrarMedicos()
        case "2":
            cadastrarPacientes()
        case "3":
            cadastrarConvenios()
        case "4":
            BuscarMedicos()
        case "5":
            buscarPacientes()
        case "6":
            buscarConvenios()
        case "7":
            alterarMedicos()
        case "8":
            alterarPacientes()
        case "9":
            marcarCompromisso()
        case "10":
            marcarConsulta()
        case "11":
            emitirRelatorio()
        case "12":
            print("Encerrando programa...")
            break
        case _:
            print("Escolha uma opção válida.")

    lang = input("1 - Cadastrar Médicos\n"
                 "2 - Cadastrar Pacientes\n"
                 "3 - Cadastrar Convênios\n"
                 "4 - Buscar Médicos\n"
                 "5 - Buscar Pacientes\n"
                 "6 - Buscar Convênios\n"
                 "7 - Alterar Médicos\n"
                 "8 - Alterar Pacientes\n"
                 "9 - Marcar Compromisso\n"
                 "10 - Marcar Consulta\n"
                 "11 - Emitir Relatório\n"
                 "12 - Encerrar Programa\n"
                 "O que você deseja fazer? ")