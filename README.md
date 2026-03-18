# Sistema de Correção de Simulados

## Descrição
Aplicação desktop em Python com Tkinter para automatizar a correção de provas de múltipla escolha, calculando acertos e percentual de desempenho.

## Como Executar o Projeto

### Passo a passo
1. Clone o repositório ou copie o código  
2. Acesse a pasta do projeto  
3. Execute o programa:  
   python correcao.py  

## Como Usar
1. Ao iniciar o sistema:  
   * Informe a **quantidade de questões**  
   * Informe a **quantidade de alternativas**  

2. Clique em **"Continuar"**  

3. Preencha:  
   * O **gabarito**  
   * As **respostas do aluno**  

4. Clique em **"Corrigir Prova"**  

5. O sistema exibirá:  
   * Número de acertos  
   * Percentual de desempenho  
---

# API Back-end

API simples em Node.js que recebe respostas de alunos e retorna média, percentual e ranking. Suporta múltiplos alunos via requisição POST.

## Como executar

Caso ainda não tenha o projeto configurado:

npm init -y  
npm install express  
node app.js  

## Como usar

Com a API rodando, abra outro terminal e faça a requisição:

curl -X POST http://localhost:3000/corrigir \
-H "Content-Type: application/json" \
-d '{
  "gabarito": ["A", "B", "C", "D"],
  "alunos": [
    { "nome": "João", "respostas": ["A", "B", "C", "D"] },
    { "nome": "Maria", "respostas": ["A", "C", "C", "D"] }
  ]
}'