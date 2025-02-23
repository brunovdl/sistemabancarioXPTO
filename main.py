# Sistema Bancário XPTO
# Este script implementa um sistema bancário simples com funcionalidades de:
# - Cadastro de clientes
# - Login
# - Operações bancárias (depósito, saque, consulta de saldo)
# - Histórico de movimentações

import random
import json
import os
import time
from datetime import datetime

def limpar_terminal():
    """
    Limpa o terminal para melhor visualização.
    Usa 'cls' no Windows e 'clear' em sistemas Unix-like
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_numero_conta():
    """
    Gera um número de conta aleatório com 5 dígitos.
    Retorna: string com 5 dígitos numéricos
    """
    return ''.join([str(random.randint(0, 9)) for _ in range(5)])

def salvar_cliente(nome, telefone, numero_conta):
    """
    Salva os dados de um novo cliente no arquivo clientes.json
    
    Args:
        nome (str): Nome completo do cliente 
        telefone (str): Número de telefone
        numero_conta (str): Número da conta gerado automaticamente
    
    Retorna:
        dict: Dicionário com os dados do cliente criado
    """
    # Cria dicionário com dados do cliente
    cliente = {
        "nome": nome,
        "telefone": telefone,
        "numero_conta": numero_conta,
        "saldo": 0  # Saldo inicial zerado
    }

    # Carrega ou cria lista de clientes
    if os.path.exists('clientes.json'):
        with open('clientes.json', 'r', encoding='utf-8') as f:
            clientes = json.load(f)
    else:
        clientes = []

    # Adiciona novo cliente e salva arquivo
    clientes.append(cliente)
    with open('clientes.json', 'w', encoding='utf-8') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

    print("\nConta criada com sucesso!")
    return cliente

def login():
    """
    Realiza o processo de login verificando o número da conta.
    Exibe uma barra de progresso durante o login.
    
    Retorna:
        dict: Dados do cliente se encontrado
        None: Se a conta não existir
    """
    limpar_terminal()
    print("\n=== Login ===")
    conta = input("Digite o número da conta com 5 dígitos: ").strip()
    
    if os.path.exists('clientes.json'):
        with open('clientes.json', 'r', encoding='utf-8') as f:
            clientes = json.load(f)
            
        for cliente in clientes:
            if cliente['numero_conta'] == conta:
                # Animação de carregamento
                limpar_terminal()
                print("==========> 30%")
                time.sleep(1)
                limpar_terminal()
                print("====================> 60%")
                time.sleep(1)
                limpar_terminal()
                print("=============================> 100%")
                time.sleep(1)
                print(f"\nBem-vindo(a) {cliente['nome']}!")
                time.sleep(1)
                return cliente
    
    print("\nERRO: Conta não encontrada!")
    time.sleep(2)
    return None

def cadastrar_cliente():
    """
    Realiza o cadastro de um novo cliente.
    Solicita nome e telefone, gera número da conta.
    
    Retorna:
        dict: Dados do cliente cadastrado
    """
    limpar_terminal()
    print("\n=== Cadastro de Novo Cliente ===")
    
    # Coleta e valida nome
    nome = input("Digite seu nome completo: ").strip()
    while not nome:
        print("O nome não pode estar vazio!")
        nome = input("Digite seu nome completo: ").strip()
    
    # Coleta e valida telefone
    telefone = input("Digite seu telefone: ").strip()
    while not telefone:
        print("O telefone não pode estar vazio!")
        telefone = input("Digite seu telefone: ").strip()
    
    # Gera número da conta
    numero_conta = gerar_numero_conta()

    # Exibe dados do cadastro
    print(f"""
    === Dados do Novo Cliente ===
    Nome: {nome}
    Telefone: {telefone}
    Número da Conta: {numero_conta}
    """)

    return salvar_cliente(nome, telefone, numero_conta)

def salvar_saldo(numero_conta, novo_saldo):
    """
    Atualiza o saldo de um cliente no arquivo.
    
    Args:
        numero_conta (str): Número da conta do cliente
        novo_saldo (float): Novo valor do saldo
    """
    if os.path.exists('clientes.json'):
        with open('clientes.json', 'r', encoding='utf-8') as f:
            clientes = json.load(f)
            
        for cliente in clientes:
            if cliente['numero_conta'] == numero_conta:
                cliente['saldo'] = novo_saldo
                break
                
        with open('clientes.json', 'w', encoding='utf-8') as f:
            json.dump(clientes, f, indent=4, ensure_ascii=False)

def registrar_movimentacao(numero_conta, tipo, valor, saldo_anterior, saldo_atual):
    """
    Registra uma movimentação no histórico (movimentacoes.json)
    
    Args:
        numero_conta (str): Número da conta
        tipo (str): Tipo da operação (depósito/saque)
        valor (float): Valor da operação
        saldo_anterior (float): Saldo antes da operação
        saldo_atual (float): Saldo após a operação
    """
    # Cria registro da movimentação
    movimentacao = {
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "numero_conta": numero_conta,
        "tipo": tipo,
        "valor": valor,
        "saldo_anterior": saldo_anterior,
        "saldo_atual": saldo_atual
    }

    # Carrega ou cria lista de movimentações
    if os.path.exists('movimentacoes.json'):
        with open('movimentacoes.json', 'r', encoding='utf-8') as f:
            movimentacoes = json.load(f)
    else:
        movimentacoes = []

    # Adiciona nova movimentação e salva
    movimentacoes.append(movimentacao)
    with open('movimentacoes.json', 'w', encoding='utf-8') as f:
        json.dump(movimentacoes, f, indent=4, ensure_ascii=False)

def ver_historico(cliente):
    """
    Exibe o histórico de movimentações de uma conta específica
    
    Args:
        cliente (dict): Dados do cliente
    """
    # Verifica se existe arquivo de movimentações
    if not os.path.exists('movimentacoes.json'):
        exibir_painel(cliente, "Não há histórico de movimentações disponível")
        time.sleep(2)
        return

    # Carrega movimentações
    with open('movimentacoes.json', 'r', encoding='utf-8') as f:
        movimentacoes = json.load(f)

    # Filtra movimentações da conta atual
    movimentacoes_conta = [m for m in movimentacoes if m['numero_conta'] == cliente['numero_conta']]

    if not movimentacoes_conta:
        exibir_painel(cliente, "Não há movimentações registradas para esta conta")
        time.sleep(2)
        return

    # Exibe histórico formatado
    limpar_terminal()
    print("="*70)
    print(f"{'HISTÓRICO DE MOVIMENTAÇÕES':^70}")
    print(f"Cliente: {cliente['nome']} - Conta: {cliente['numero_conta']}")
    print("="*70)
    print(f"{'Data/Hora':<19} | {'Tipo':<8} | {'Valor':>12} | {'Saldo Anterior':>14} | {'Saldo Atual':>12}")
    print("-"*70)

    for mov in movimentacoes_conta:
        print(f"{mov['data_hora']:<19} | {mov['tipo']:<8} | {mov['valor']:>12.2f} | {mov['saldo_anterior']:>14.2f} | {mov['saldo_atual']:>12.2f}")

    print("="*70)
    input("\nPressione Enter para voltar ao menu principal...")

def exibir_painel(cliente, ultima_operacao="Nenhuma"):
    """
    Exibe o painel principal do sistema com informações do cliente
    
    Args:
        cliente (dict): Dados do cliente
        ultima_operacao (str): Descrição da última operação realizada
    """
    limpar_terminal()
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Monta interface do painel
    print("="*50)
    print(f"{'BANCO XPTO':^50}")
    print("="*50)
    print(f"Data/Hora: {data_hora}")
    print(f"Cliente: {cliente['nome']}")
    print(f"Conta: {cliente['numero_conta']}")
    print(f"Telefone: {cliente['telefone']}")
    print("-"*50)
    print(f"Saldo Atual: R$ {cliente['saldo']:.2f}")
    print(f"Última Operação: {ultima_operacao}")
    print("-"*50)
    print("""
    MENU DE OPERAÇÕES:
    [1] Depósito
    [2] Saque
    [3] Histórico de Movimentações
    [0] Sair
    """)
    print("="*50)

def fazer_deposito(cliente):
    """
    Realiza operação de depósito na conta
    
    Args:
        cliente (dict): Dados do cliente
    """
    try:
        valor = float(input("\nDigite o valor do depósito: R$ "))
        
        # Validação do valor
        if valor <= 0:
            exibir_painel(cliente, "ERRO: Valor inválido para depósito!")
            time.sleep(2)
            return
        
        # Atualiza saldo
        saldo_anterior = cliente['saldo']    
        cliente['saldo'] += valor
        salvar_saldo(cliente['numero_conta'], cliente['saldo'])
        
        # Registra movimentação
        registrar_movimentacao(
            cliente['numero_conta'],
            "Depósito",
            valor,
            saldo_anterior,
            cliente['saldo']
        )
        
        exibir_painel(cliente, f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        time.sleep(2)
        
    except ValueError:
        exibir_painel(cliente, "ERRO: Digite um valor numérico válido!")
        time.sleep(2)

def fazer_saque(cliente):
    """
    Realiza operação de saque na conta
    
    Args:
        cliente (dict): Dados do cliente
    """
    try:
        valor = float(input("\nDigite o valor do saque: R$ "))
        
        # Validação do valor
        if valor <= 0:
            exibir_painel(cliente, "ERRO: Valor inválido para saque!")
            time.sleep(2)
            return
            
        # Verifica se há saldo suficiente
        if cliente['saldo'] >= valor:
            saldo_anterior = cliente['saldo']
            cliente['saldo'] -= valor
            salvar_saldo(cliente['numero_conta'], cliente['saldo'])
            
            # Registra movimentação
            registrar_movimentacao(
                cliente['numero_conta'],
                "Saque",
                valor,
                saldo_anterior,
                cliente['saldo']
            )
            
            exibir_painel(cliente, f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            exibir_painel(cliente, "ERRO: Saldo insuficiente para realizar esse saque!")
        
        time.sleep(2)
            
    except ValueError:
        exibir_painel(cliente, "ERRO: Digite um valor numérico válido!")
        time.sleep(2)

def ver_saldo(cliente):
    """
    Exibe o saldo atual da conta
    
    Args:
        cliente (dict): Dados do cliente
    """
    exibir_painel(cliente, "Consulta de saldo realizada")
    time.sleep(2)

def menu_bancario(cliente):
    """
    Gerencia o menu principal de operações bancárias
    
    Args:
        cliente (dict): Dados do cliente
    """
    while True:
        exibir_painel(cliente)
        try:
            opcao = input("\nEscolha uma operação: ").strip()
            
            # Processa opção escolhida
            if opcao == '1':
                fazer_deposito(cliente)
            elif opcao == '2':
                fazer_saque(cliente)
            #elif opcao == '3':
                #ver_saldo(cliente)
            elif opcao == '3':
                ver_historico(cliente)
            elif opcao == '0':
                exibir_painel(cliente, "Saindo do sistema...")
                time.sleep(2)
                break
            else:
                exibir_painel(cliente, "ERRO: Opção inválida!")
                time.sleep(2)
                
        except Exception as e:
            exibir_painel(cliente, f"ERRO: {str(e)}")
            time.sleep(2)

def main():
    """
    Função principal que controla o fluxo do programa
    """
    while True:
        limpar_terminal()
        print("""
        === BEM-VINDO AO BANCO XPTO ===
            
              [1] Entrar na Conta
              [2] Abrir Conta
              [0] Sair
        """)
        
        try:
            opcao = input("             Escolha uma opção: ").strip()

            # Processa opção do menu inicial
            if opcao == '1':
                cliente = login()
                if cliente:
                    menu_bancario(cliente)
            elif opcao == '2':
                cliente = cadastrar_cliente()
                if input("\nDeseja acessar sua conta agora? (S/N): ").strip().upper() == 'S':
                    menu_bancario(cliente)
            elif opcao == '0':
                limpar_terminal()
                print("\nObrigado por usar nosso banco!")
                break
            else:
                print("\nOpção inválida!")
                time.sleep(2)

        except KeyboardInterrupt:
            # Tratamento para interrupção do programa (Ctrl+C)
            print("\nOperação cancelada pelo usuário.")
            break
        except Exception as e:
            # Tratamento de outros erros inesperados
            print(f"\nOcorreu um erro: {e}")
            time.sleep(2)

# Ponto de entrada do programa
if __name__ == "__main__":
    main()