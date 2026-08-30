#  Biney — Windows Edition.  <img width="256" height="256" alt="icone" src="https://github.com/user-attachments/assets/234eea9d-aae8-4ba9-affe-b1a55a8d066b" />



![Plataforma](https://img.shields.io/badge/plataforma-Windows-4f7d9c?style=flat-square)
![Linguagem](https://img.shields.io/badge/python-3.14-blue?style=flat-square)
![Status](https://img.shields.io/badge/status-concluído-brightgreen?style=flat-square)

**Biney** é um conversor de bases numéricas (binário, octal, decimal e hexadecimal) com interface gráfica própria, feito do zero em Python. Esta pasta contém a versão empacotada para **Windows**, pronta para instalar e usar sem precisar de Python instalado.

## 📥  Instalação

1. Baixe o executável `Biney.exe` disponível nesta pasta.
2. Dê dois cliques para abrir — não é necessário instalar nada.
3. Pronto. O ícone próprio do Biney já vem embutido no executável.

> Se o Windows Defender / SmartScreen alertar por ser um app de um desenvolvedor não verificado, clique em **"Mais informações" → "Executar assim mesmo"**. Isso acontece porque o executável não possui certificado de assinatura digital (comum em projetos acadêmicos/independentes), não por conter qualquer conteúdo malicioso.

##  Funcionalidades

- Conversão entre **binário, octal, decimal e hexadecimal**, em qualquer direção
- Campos de resultado com botão de **copiar** individual por linha
- **Modo Estudante**: uma janela separada que mostra o passo a passo do cálculo por trás de cada conversão, para quem quer entender a lógica e não só o resultado
- Interface com paleta de cores neutra (cinza-azulado) e seleção de base por abas segmentadas, desenhada especificamente para esta versão

##  Sobre a interface

A versão Windows recebeu um cuidado visual extra em relação às demais: as abas de seleção de base usam um controle segmentado customizado (em vez dos botões de rádio padrão do Tk), com cor de destaque quando selecionadas, tipografia Segoe UI/Consolas e um tema escuro dedicado para a janela do Modo Estudante. Essas escolhas resolveram problemas visuais específicos do Windows, como o tema claro do sistema sobrescrevendo as cores customizadas.

##  Rodando a partir do código-fonte (opcional)

Se preferir rodar via Python em vez do `.exe`:

```bash
python main.py
```

Requer Python 3.14+ com Tkinter.

##  Sobre o projeto

Biney nasceu como um projeto acadêmico para reforçar dois conceitos ao mesmo tempo:

- **Programação Orientada a Objetos**: composição em vez de herança — uma classe `Numero` guarda o valor em decimal como referência única, e cada base tem seu próprio `Conversor` (`ConversorBinario`, `ConversorOctal`, `ConversorHexadecimal`) com métodos `para_decimal()` e `de_decimal()`.
- **Teoria de Sistemas de Numeração**: os algoritmos de conversão foram implementados manualmente pelo método das **divisões sucessivas**, em vez de depender de funções prontas da linguagem.

Para a lógica pura por trás das conversões, veja a pasta [`backend/`](../backend).

##  Autor

Neylor Cruz — [@N3ylim](https://github.com/N3ylim)
