
# 🔢 Biney

![Linguagem](https://img.shields.io/badge/python-3-blue?style=flat-square)
![POO](https://img.shields.io/badge/paradigma-POO-4f7d9c?style=flat-square)
![Status](https://img.shields.io/badge/status-concluído-brightgreen?style=flat-square)

**Biney** é um conversor de números entre as bases **binária**, **octal**, **decimal** e **hexadecimal**, desenvolvido em Python. Nasceu como projeto acadêmico para praticar Programação Orientada a Objetos e Sistemas de Numeração ao mesmo tempo — sem depender de funções prontas da linguagem para fazer as conversões.

O nome vem da junção de **bin**ário com o meu nome, Neylor

## 📂 Estrutura do repositório

Este repositório reúne três versões do mesmo projeto, cada uma com uma proposta diferente — por isso, cada pasta tem seu próprio README com detalhes específicos:

| Pasta | O que é | Leia mais |
|---|---|---|
| 🪟 [`windows/`](./windows) | Versão com interface gráfica, empacotada em `.exe` com ícone próprio. A mais polida visualmente. | [README](./windows/README.md) |
| 🍎 [`mac/`](./mac) | Código-fonte completo da interface gráfica original, sem executável. Congelada no ponto em que o foco de desenvolvimento migrou para o Windows. | [README](./mac/README.md) |
| ⚙️ [`backend/`](./backend) | O coração do projeto: lógica de conversão pura, em terminal, sem interface e sem dependências. Roda em qualquer sistema com Python. | [README](./backend/README.md) |

## 🧠 A ideia por trás do projeto

Independente da pasta, todas as versões compartilham o mesmo design:

- **Composição em vez de herança**: uma classe `Numero` guarda o valor sempre em decimal — a referência única — e cada base numérica tem seu próprio `Conversor` (`ConversorBinario`, `ConversorOctal`, `ConversorHexadecimal`), responsável por `para_decimal()` e `de_decimal()`.
- **Divisões sucessivas**: o algoritmo de conversão de decimal para outras bases foi implementado manualmente, dividindo o número repetidamente pela base desejada e coletando os restos, em vez de usar `bin()`, `oct()` ou `hex()` prontos do Python.

As versões com interface gráfica (Windows e macOS) são só uma camada visual construída em cima dessa lógica de terminal.

## 🚀 Por onde começar

- Quer só usar o programa? Baixe o `.exe` em [`windows/`](./windows).
- Está no Mac e quer rodar a partir do código? Veja [`mac/`](./mac).
- Quer entender a lógica das conversões sem interface nenhuma no meio? Vá direto ao [`backend/`](./backend) — é a parte mais fiel ao que o projeto realmente ensina.

## 👤 Autor

Neylor Cruz — [@N3ylim](https://github.com/N3ylim)
