

#  Biney
![Linguagem](https://img.shields.io/badge/python-3-blue?style=flat-square)
![POO](https://img.shields.io/badge/paradigma-POO-4f7d9c?style=flat-square)
![Status](https://img.shields.io/badge/status-concluído-brightgreen?style=flat-square)

**Biney** é um conversor de números entre as bases **binária**, **octal**, **decimal** e **hexadecimal**, desenvolvido em Python. Nasceu como projeto acadêmico para praticar Programação Orientada a Objetos e Sistemas de Numeração ao mesmo tempo — sem depender de funções prontas da linguagem para fazer as conversões.

O nome vem da junção de **bin**ário com o meu nome, Neylor

<img width="573" height="563" alt="Captura de Tela 2026-08-30 às 18 28 21" src="https://github.com/user-attachments/assets/9b437dc7-d1bc-4586-9d75-70c671f7a78c" />


## 📂 Estrutura do repositório
Este repositório reúne três versões do mesmo projeto, cada uma com uma proposta diferente — por isso, cada pasta tem seu próprio README com detalhes específicos:

| Pasta | O que é | Leia mais |
|---|---|---|
|  [`windows/`](./windows) | Versão com interface gráfica, empacotada em `.exe` com ícone próprio. A mais polida visualmente. | [README](./windows/README.md) |
|  [`mac/`](./mac) | Código-fonte completo da interface gráfica original, sem executável. Congelada no ponto em que o foco de desenvolvimento migrou para o Windows. | [README](./mac/README.md) |
|  [`backend/`](./backend) | O coração do projeto: lógica de conversão pura, em terminal, sem interface e sem dependências. Roda em qualquer sistema com Python. | [README](./backend/README.md) |

## A ideia por trás do projeto
Independente da pasta, todas as versões compartilham o mesmo design:

- **Composição em vez de herança**: uma classe `Numero` guarda o valor sempre em decimal — a referência única — e cada base numérica tem seu próprio `Conversor` (`ConversorBinario`, `ConversorOctal`, `ConversorHexadecimal`), responsável por `para_decimal()` e `de_decimal()`.
- **Divisões sucessivas**: o algoritmo de conversão de decimal para outras bases foi implementado manualmente, dividindo o número repetidamente pela base desejada e coletando os restos, em vez de usar `bin()`, `oct()` ou `hex()` prontos do Python.

As versões com interface gráfica (Windows e macOS) são só uma camada visual construída em cima dessa lógica de terminal.

##  O diferencial: o programa ensina, não só converte

Esse é o ponto que separa as versões com interface das demais: Biney não entrega apenas o resultado, ele explica **como chegou nele**.

Nas versões Windows e macOS, o botão **"Entender o Cálculo (Passo a Passo)"** abre uma explicação do algoritmo em ação — a mesma lógica que roda por trás dos panos em `de_decimal()`, só que exposta na tela em vez de ficar escondida:

- o número é dividido sucessivamente pela base escolhida;
- cada divisão mostra o **quociente** e o **resto**;
- os restos vão sendo empilhados, de baixo para cima, até formar o resultado final na nova base.

A ideia não é só resolver a conversão, mas mostrar o raciocínio por trás do Sistema de Numeração — o mesmo processo que qualquer pessoa faria no papel, só que automatizado e visualizado passo a passo. É o projeto tentando ensinar, e não só calcular.

##  Por onde começar
- Quer só usar o programa? Baixe o `.exe` em [`windows/`](./windows).
- Está no Mac e quer rodar a partir do código? Veja [`mac/`](./mac).
- Quer entender a lógica das conversões sem interface nenhuma no meio? Vá direto ao [`backend/`](./backend) — é a parte mais fiel ao que o projeto realmente ensina.

##  Autor
Neylor Cruz — [@N3ylim](https://github.com/N3ylim)
