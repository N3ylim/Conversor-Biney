# 🍎 Biney — macOS Edition

![Plataforma](https://img.shields.io/badge/plataforma-macOS-4f7d9c?style=flat-square)
![Linguagem](https://img.shields.io/badge/python-3.14-blue?style=flat-square)
![Status](https://img.shields.io/badge/status-congelado-lightgrey?style=flat-square)

**Biney** é um conversor de bases numéricas (binário, octal, decimal e hexadecimal) com interface gráfica própria, feito do zero em Python. Esta pasta contém a versão original do projeto, desenvolvida e testada no macOS.

> Esta é a versão em que a interface gráfica nasceu. O desenvolvimento visual mais recente do Biney (abas segmentadas, tema escuro do Modo Estudante) foi feito depois, focado na versão Windows, então esta pasta reflete o projeto congelado no ponto em que o foco mudou de plataforma. Funciona perfeitamente — só não recebeu os últimos ajustes de visual.

## 📦 O que tem aqui

Diferente da versão Windows, esta pasta não inclui um executável pronto (`.app`) — apenas o **código-fonte completo**, para rodar diretamente com Python.

## 🚀 Como rodar

### Pré-requisitos

O Tk que vem por padrão em versões mais antigas do macOS tem um bug conhecido de renderização (tela preta ao abrir janelas Tkinter). Para evitar isso, instale a versão do Tk via Homebrew:

```bash
brew install python-tk@3.14
```

### Executando

Na raiz do projeto:

```bash
python3.14 main.py
```

## ✨ Funcionalidades

- Conversão entre **binário, octal, decimal e hexadecimal**, em qualquer direção
- Campos de resultado com botão de **copiar** individual por linha
- **Modo Estudante**: janela separada que mostra o passo a passo do cálculo por trás de cada conversão
- Paleta de cores neutra (cinza-azulado), definida antes da divisão em versões separadas para Windows e Mac

## 🧠 Sobre o projeto

Biney nasceu como um projeto acadêmico para reforçar dois conceitos ao mesmo tempo:

- **Programação Orientada a Objetos**: composição em vez de herança — uma classe `Numero` guarda o valor em decimal como referência única, e cada base tem seu próprio `Conversor` (`ConversorBinario`, `ConversorOctal`, `ConversorHexadecimal`) com métodos `para_decimal()` e `de_decimal()`.
- **Teoria de Sistemas de Numeração**: os algoritmos de conversão foram implementados manualmente pelo método das **divisões sucessivas**, em vez de depender de funções prontas da linguagem.

Quer ver a versão mais atual e polida da interface? Confira a pasta [`windows/`](../windows). Quer só a lógica pura, sem interface nenhuma? Veja [`backend/`](../backend).

## 👤 Autor

Neylor Cruz — [@N3ylim](https://github.com/N3ylim)
