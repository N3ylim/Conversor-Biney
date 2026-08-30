# ⚙️ Biney — Core / Backend

![Plataforma](https://img.shields.io/badge/plataforma-universal-4f7d9c?style=flat-square)
![Linguagem](https://img.shields.io/badge/python-3-blue?style=flat-square)
![Dependências](https://img.shields.io/badge/dependências-nenhuma-brightgreen?style=flat-square)

Esta é a **base de tudo**: a versão em terminal do Biney, sem interface gráfica, sem dependências externas — só Python puro. É o coração do projeto, de onde nasceram as versões com interface para [Windows](../windows) e [macOS](../mac).

## 🚀 Como rodar

Na raiz do projeto:

```bash
python3 main.py
```

O programa abre um menu interativo no terminal: você escolhe a base do número que quer converter e vê o resultado nas outras três bases. Continua rodando em loop até você escolher sair.

Funciona em qualquer sistema com Python 3 instalado — Windows, macOS ou Linux — sem precisar instalar nada além disso.

## ✨ Funcionalidades

- Conversão entre **binário, octal, decimal e hexadecimal**, em qualquer direção
- Menu interativo em loop, com opção de sair a qualquer momento
- Tratamento de opção inválida, permitindo nova tentativa sem travar o programa

## 🧠 Design do projeto

O projeto segue o princípio de **composição**, em vez de herança:

- A classe `Numero` representa um número guardado sempre em sua forma **decimal** — a referência única a partir da qual todas as outras bases são derivadas.
- Cada base numérica tem seu próprio **Conversor** (`ConversorBinario`, `ConversorOctal`, `ConversorHexadecimal`), responsável por dois métodos:
  - `para_decimal(texto)`: converte uma string em determinada base para o valor decimal correspondente.
  - `de_decimal(valor)`: converte um valor decimal para a representação em string daquela base.

Essa separação segue o princípio de responsabilidade única: `Numero` só sabe armazenar um valor, e cada `Conversor` só sabe converter entre sua base específica e o decimal.

## 🔢 Algoritmo de conversão

As conversões de decimal para outras bases foram implementadas manualmente pelo método das **divisões sucessivas**: divide-se o número repetidamente pela base desejada, coletando os restos — que formam os dígitos, do menos para o mais significativo — até que o quociente chegue a zero. Nada de `bin()`, `oct()` ou `hex()` prontos da linguagem: a lógica foi construída do zero, que é justamente o ponto do exercício.

## 📁 Estrutura

```
backend/
├── src/
│   └── conversor/
│       ├── __init__.py
│       ├── numero_base.py            # Classe Numero: guarda o valor em decimal
│       ├── conversor_binario.py      # Conversão decimal ↔ binário
│       ├── conversor_octal.py        # Conversão decimal ↔ octal
│       └── conversor_hexadecimal.py  # Conversão decimal ↔ hexadecimal
├── main.py                           # Ponto de entrada: menu interativo
├── tests/                            # Testes do projeto
└── README.md
```

## 💡 Por que essa pasta importa

As versões com interface (Windows e macOS) são construídas em cima dessa lógica — a diferença é só a camada visual por cima. Se você quer entender **como as conversões realmente funcionam por dentro**, sem se preocupar com botões, janelas ou temas, é aqui que a resposta está.

## 👤 Autor

Neylor Cruz — [@N3ylim](https://github.com/N3ylim)
