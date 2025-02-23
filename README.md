# Idéia Geral do Projeto
Projeto desenvolvido a partir de um desafio de código onde o objetivo era desenvolver um sistema simples de banco onde o usuário poderia adicionar dinheiro e retirar dinheiro, como o intuito desse projeto foi para desenvolver raciocínio lógico fui um pouco além no projeto e gostei bastante do resultado

# Sistema Bancário XPTO

Uma implementação robusta e simples de um sistema bancário em Python que fornece operações bancárias básicas e recursos de gerenciamento de contas.

## Funcionalidades

- Criação e Gerenciamento de Contas
- Sistema de Login Seguro
- Operações Bancárias (Depósitos e Saques)
- Histórico de Transações
- Consulta de Saldo
- Interface via Terminal
- Persistência de Dados usando arquivos JSON

## Requisitos do Sistema

- Python 3.x
- Sem dependências externas (usa apenas bibliotecas nativas do Python)
- Compatível com Windows e sistemas Unix

## Instalação

1. Clone este repositório:
```bash
git clone https://github.com/seuusuario/banco-xpto.git
cd banco-xpto
```

2. Execute o script principal:
```bash
python main.py
```

## Estrutura do Projeto

O sistema utiliza dois arquivos JSON para persistência de dados:
- `clientes.json`: Armazena informações das contas dos clientes
- `movimentacoes.json`: Armazena histórico de transações

## Funções Principais

### Gerenciamento de Contas

#### `cadastrar_cliente()`
Cria uma nova conta de cliente com as seguintes informações:
- Nome completo
- Número de telefone
- Número de conta com 5 dígitos gerado automaticamente
- Saldo inicial de 0

#### `login()`
Gerencia o processo de login:
- Valida o número de conta de 5 dígitos
- Exibe uma animação de carregamento
- Recupera os dados do cliente

### Operações Bancárias

#### `fazer_deposito(cliente)`
Gerencia operações de depósito:
- Valida o valor do depósito
- Atualiza o saldo da conta
- Registra a transação no histórico
- Fornece feedback imediato

#### `fazer_saque(cliente)`
Gerencia operações de saque:
- Valida o valor do saque
- Verifica se há saldo suficiente
- Atualiza o saldo da conta
- Registra a transação no histórico
- Fornece feedback imediato

### Histórico de Transações
```
======================================================================
                      HISTÓRICO DE MOVIMENTAÇÕES
Cliente: Jose da Silva - Conta: 71089
======================================================================
Data/Hora           | Tipo     |        Valor | Saldo Anterior |  Saldo Atual
----------------------------------------------------------------------
22/02/2025 23:19:23 | Depósito |      4000.00 |           0.00 |      4000.00
22/02/2025 23:20:32 | Saque    |       115.75 |        4000.00 |      3884.25
23/02/2025 00:21:07 | Depósito |      1000.00 |        3884.25 |      4884.25
23/02/2025 00:21:22 | Depósito |      1000.00 |        4884.25 |      5884.25
======================================================================

Pressione Enter para voltar ao menu principal...
```

#### `registrar_movimentacao()`
Registra todas as transações financeiras com:
- Data e hora
- Número da conta
- Tipo de transação
- Valor da transação
- Saldo anterior
- Novo saldo

#### `ver_historico()`
Exibe um histórico formatado de transações incluindo:
- Todas as transações da conta específica
- Listagem cronológica
- Informações detalhadas da transação

### Persistência de Dados

#### `salvar_cliente()`
Gerencia a persistência dos dados do cliente:
- Cria/atualiza registros de clientes em formato JSON
- Gerencia operações de arquivo
- Garante integridade dos dados

#### `salvar_saldo()`
Gerencia atualizações de saldo:
- Atualiza o saldo do cliente no banco de dados
- Garante operações atômicas
- Mantém consistência dos dados

## Interface do Usuário

### Menu Principal
```
=== BEM-VINDO AO BANCO XPTO ===
    
      [1] Entrar na Conta
      [2] Abrir Conta
      [0] Sair
```

### Menu de Operações
```
==================================================
                    BANCO XPTO
==================================================
Data/Hora: 23/02/2025 00:27:14
Cliente: Jose da Silva
Conta: 71089
Telefone: 11999887766
--------------------------------------------------
Saldo Atual: R$ 5884.25
Última Operação: Nenhuma
--------------------------------------------------

    MENU DE OPERAÇÕES:
    [1] Depósito
    [2] Saque
    [3] Histórico de Movimentações
    [0] Sair

==================================================

Escolha uma operação:
```

## Recursos de Segurança

- Números de conta gerados aleatoriamente
- Limpeza do terminal para informações sensíveis
- Validação básica de entrada
- Tratamento de operações inválidas

## Tratamento de Erros

O sistema inclui tratamento abrangente de erros para:
- Entradas inválidas
- Saldo insuficiente
- Operações de arquivo
- Interrupções do sistema (Ctrl+C)
- Exceções gerais

## Formato de Armazenamento de Dados

### Estrutura de Dados do Cliente (clientes.json)
```json
{
    "nome": "Nome do Cliente",
    "telefone": "Número de Telefone",
    "numero_conta": "número de 5 dígitos",
    "saldo": 0.0
}
```

### Estrutura de Dados de Transação (movimentacoes.json)
```json
{
    "data_hora": "DD/MM/AAAA HH:MM:SS",
    "numero_conta": "número de 5 dígitos",
    "tipo": "Tipo de Transação",
    "valor": 0.0,
    "saldo_anterior": 0.0,
    "saldo_atual": 0.0
}
```

## Boas Práticas

O código segue várias boas práticas do Python:
- Documentação clara das funções
- Tratamento consistente de erros
- Design modular
- Estrutura limpa de código
- Nomes descritivos de variáveis
- Suporte a codificação UTF-8

## Como Contribuir

Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.
