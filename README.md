
# DESAFIO DE CÓDIGO SISTEMA BANCÁRIO
## 💻 Tecnologias utilizadas no projeto

- [ChatGPT](https://chat.openai.com/) 

## ✨ Entendendo o projeto:

# Projeto Bancário em Python

Este é um projeto bancário simples desenvolvido em Python, projetado para gerenciar ações cotidianas como depósitos, saques, visualização de extratos e verificações básicas de transação. Ele é ideal para iniciantes que desejam aprender sobre programação procedural e manipulação de dados.

## Funcionalidades

O sistema oferece as seguintes opções:

1. **Depósito**: Permite ao usuário adicionar valores à sua conta.
2. **Saque**: Permite retirar valores da conta respeitando limites diários e saldo disponível.
3. **Extrato**: Exibe todas as transações realizadas e o saldo atual.
4. **Sair**: Encerra o programa.

## Tecnologias Utilizadas

- Linguagem de Programação: Python (versão mais recente disponível).

## Especificações do Sistema

### Variáveis Principais
- `saldo`: Armazena o saldo disponível na conta.
- `limite`: Define o valor máximo que pode ser sacado em uma única operação.
- `extrato`: Armazena o histórico de transações realizadas.
- `numero_saques`: Conta o número de saques realizados no dia.
- `LIMITE_SAQUES`: Define o número máximo de saques permitidos por dia.

### Funções

#### 1. `depositar(valor, saldo, extrato)`
- **Descrição**: Realiza a operação de depósito, atualizando o saldo e o extrato.

- **Parâmetros**:
  - `valor`: Valor a ser depositado.
  - `saldo`: Saldo atual da conta.
  - `extrato`: Histórico das transações.

- **Retorno**: Novo saldo e extrato atualizado.

- **Validação**: O depósito só é realizado se o valor for maior que zero.

#### 2. `sacar(valor, saldo, extrato, numero_saques, limite, LIMITE_SAQUES)`
- **Descrição**: Realiza a operação de saque, considerando o saldo disponível, o limite de saque por operação e o número máximo de saques diários.

- **Parâmetros**:
  - `valor`: Valor a ser sacado.
  - `saldo`: Saldo atual da conta.
  - `extrato`: Histórico das transações.
  - `numero_saques`: Número de saques já realizados no dia.
  - `limite`: Limite máximo de saque por operação.
  - `LIMITE_SAQUES`: Limite de saques diários permitidos.

- **Retorno**: Novo saldo, extrato atualizado e o número atualizado de saques realizados.

- **Validações**:
  - Verifica se o saldo é suficiente.
  - Garante que o valor do saque não ultrapasse o limite.
  - Limita o número de saques diários.
  - Aceita apenas valores positivos.

#### 3. `exibir_extrato(saldo, extrato)`
- **Descrição**: Exibe o extrato das transações realizadas e o saldo atual.

- **Parâmetros**:
  - `saldo`: Saldo atual da conta.
  - `extrato`: Histórico das transações.

- **Validação**: Exibe uma mensagem indicando que não há movimentações se o extrato estiver vazio.

### Interface do Usuário
O menu principal do sistema é apresentado da seguinte forma:

```plaintext
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>
```

O usuário pode selecionar a operação desejada digitando a letra correspondente.

### Exemplo de Execução

1. **Depósito**:
   - Entrada: `d` (Depositar) seguido do valor do depósito.
   - Saída: Confirmação do depósito e saldo atualizado.

2. **Saque**:
   - Entrada: `s` (Sacar) seguido do valor do saque.
   - Saída: Confirmação do saque ou mensagem de erro caso as condições não sejam atendidas.

3. **Extrato**:
   - Entrada: `e` (Extrato).
   - Saída: Histórico de transações e saldo atual.

4. **Sair**:
   - Entrada: `q` (Sair).
   - Saída: Mensagem de despedida e encerramento do programa.

## Como Executar
1. Certifique-se de ter o Python instalado em sua máquina.
2. Copie o código do projeto para um arquivo com extensão `.py`.
3. Execute o arquivo no terminal ou em um ambiente de desenvolvimento Python.

## Melhorias Futuras
- Implementar autenticação de usuário com senha.
- Permitir transferência entre contas.
- Adicionar categorias às transações para melhor organização.
- Implementar interface gráfica para maior usabilidade.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e novas funcionalidades.

## 📚 Materiais

- [ChatGPT](https://chat.openai.com/)

## 🛠️ Instruções de execução

- Utilize os prompts dentro do link do `ChaGPT`.

- 🤖 1. Use os prompts de roteiro no `ChaGPT`.

## 👨‍💻 Expert

<p>
    <img 
      align=left 
      margin=10 
      width=80 
      src="https://avatars.githubusercontent.com/u/151440851?v=4"
    />
    <p>&nbsp&nbsp&nbspRoberto Costa<br>
    &nbsp&nbsp&nbsp
    <a 
        href="https://github.com/RobertoAHOW">
        GitHub
    </a>
    &nbsp;|&nbsp;
    <a 
        href="www.linkedin.com/in/robertoascosta/">
        LinkedIn
    </a>
   
<br/><br/>
<p>

---

⌨️ com 💜 por [Roberto Costa](https://github.com/RobertoAHOW)