# 💸 Otimizando o Sistema Bancário em Python

🤝 Este projeto faz parte do bootcamp **Engenharia de Dados com Python**, uma parceria entre a [DIO](https://www.dio.me/) e a [NTT DATA](https://br.nttdata.com/), e tem como objetivo principal desenvolver um sistema bancário simples, que permite realizar operações como depósitos, saques, visualizar extratos, criar contas e usuários, e listar contas ativas. Ele é ideal para entender o funcionamento de funções, estruturas de controle e manipulação de dados básicos. Continuação do Desafio 1 [Criando um sistema bancario em Python](https://github.com/luiseduardot17/projeto_dio_sistema_bancario_python).

## 📋 Funcionalidades

O sistema permite realizar as seguintes operações:
- **Depósito**: Adicione saldo à conta.
- **Saque**: Retire um valor, respeitando o limite e a quantidade máxima de saques.
- **Extrato**: Veja o histórico de transações e o saldo atual.
- **Criação de Usuários**: Cadastre novos usuários informando CPF, nome, data de nascimento e endereço.
- **Criação de Contas**: Crie uma conta vinculada a um usuário existente.
- **Listagem de Contas**: Exiba todas as contas ativas com informações detalhadas.

## ⚙️ Pré-requisitos

Antes de executar o programa, certifique-se de que você tem o seguinte instalado:
- **Python 3.6+**: O código é desenvolvido em Python e exige uma versão recente.
- **Biblioteca `textwrap`**: Usada para manipulação de strings e formatação de texto (já incluída no Python).

## 📦 Instalação

1. **Clone o repositório**:
   ```
   git clone https://github.com/luiseduardot17/otimizando_o_sistema_bancario_python.git
   ```
   
2. **Navegue até o diretório do projeto**:
   ```
   cd otimizando_o_sistema_bancario_python
   ```

3. **Execute o script**:
   Não há dependências externas a instalar. Basta executar o script diretamente com Python.
   ```
   python otimizando_o_sistema_bancario_python.py
   ```

## 🚀 Como Executar

Ao executar o script, você verá um menu com as opções disponíveis. Digite a letra correspondente à operação desejada e siga as instruções na tela. Abaixo está um exemplo do menu:

```
    ================ MENU ================
    [d]    Depositar
    [s]    Sacar
    [e]    Extrato
    [nc]   Nova conta
    [lc]   Listar contas
    [nu]   Novo usuário
    [q]    Sair
```

- Escolha a operação que deseja realizar.
- Para sair, digite `[q]`.

## 🧩 Estrutura do Projeto

- `otimizando_o_sistema_bancario_python.py`: Arquivo principal que contém todas as funções e o loop do menu principal.
- **Funções**: Cada operação possui uma função dedicada para manter o código modular e organizado.

## 📚 Bibliotecas Usadas

- `textwrap`: Biblioteca padrão do Python, utilizada para auxiliar na formatação e exibição do menu.

## 🛠️ Como Personalizar

Você pode ajustar os valores de:
- **Limite de saques diários**
- **Limite de valor por saque**
  
Basta modificar as variáveis `MAX_SAQUES` e `limite_saque` no código principal para personalizar essas configurações.