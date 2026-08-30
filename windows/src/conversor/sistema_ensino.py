import customtkinter as ctk
from src.conversor.conversor_hexadecimal import ConversorHexadecimal
from src.conversor.ui_estilo import *

SIMBOLOS_HEX = ConversorHexadecimal.SIMBOLOS
SOBRESCRITOS = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

ALTURA_MAXIMA_JANELA = 850
LARGURA_JANELA = 760

class SistemaEnsino:
    def __init__(self, parent, valor_decimal):
        self.parent = parent
        self.valor_decimal = valor_decimal
        
        self.mapa_bases = {"Binário": 2, "Octal": 8, "Hexadecimal": 16}
        self.mapa_direcao = {"Decimal → Base": "forward", "Base → Decimal": "backward"}
        
        self.base_atual = 2
        self.direcao_atual = "forward"
        self.caixa_texto_visivel = None

        self.janela = ctk.CTkToplevel(parent)
        self.janela.title("Modo Estudante - Passo a Passo")
        self.janela.resizable(False, False)
        self.janela.configure(fg_color=COR_FUNDO)
        self.janela.grab_set() 

        self.criar_widgets()
        self.centralizar_janela()

    def centralizar_janela(self):
        self.janela.update_idletasks()
        altura_tela = self.janela.winfo_screenheight()
        largura_tela = self.janela.winfo_screenwidth()

        altura = min(ALTURA_MAXIMA_JANELA, altura_tela - 100)
        x = (largura_tela - LARGURA_JANELA) // 2
        y = (altura_tela - altura) // 2  # Calculo exato do centro
        self.janela.geometry(f"{LARGURA_JANELA}x{altura}+{x}+{y}")
    def criar_widgets(self):
        container = ctk.CTkFrame(self.janela, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=30, pady=25)

        ctk.CTkLabel(
            container, text="Passo a Passo da Conversão", 
            font=(FONTE_BASE, 18, "bold"), text_color=COR_TEXTO
        ).pack(anchor="w")

        ctk.CTkLabel(
            container, text="Veja como o resultado é calculado em cada base", 
            font=(FONTE_BASE, 12), text_color=COR_TEXTO_SECUNDARIO
        ).pack(anchor="w", pady=(2, 18))

        self.seletor_base = ctk.CTkSegmentedButton(
            container, 
            values=["Binário", "Octal", "Hexadecimal"],
            command=self.selecionar_aba,
            font=(FONTE_BASE, 13, "bold"),
            fg_color=COR_FUNDO_CARTAO,
            selected_color=COR_ACENTO,
            selected_hover_color=COR_ACENTO_HOVER,
            unselected_color=COR_FUNDO_CARTAO,
            text_color=COR_TEXTO,
            corner_radius=20
        )
        self.seletor_base.pack(fill="x", pady=(0, 20))
        self.seletor_base.set("Binário")

        divisor_grupos = ctk.CTkFrame(container, height=1, fg_color=COR_FUNDO_CARTAO)
        divisor_grupos.pack(fill="x", pady=(5, 15))

        self.seletor_direcao = ctk.CTkSegmentedButton(
            container, 
            values=["Decimal → Base", "Base → Decimal"],
            command=self.alternar_direcao,
            font=(FONTE_BASE, 11, "bold"),
            fg_color=COR_FUNDO_CARTAO,
            selected_color=COR_ACENTO_SECUNDARIO,         # Nova cor neutra
            selected_hover_color=COR_ACENTO_SECUNDARIO_HOVER, # Nova cor neutra
            unselected_color=COR_FUNDO_CARTAO,
            text_color=COR_TEXTO,
            corner_radius=15
        )
        self.seletor_direcao.pack(fill="x", pady=(0, 20))
        self.seletor_direcao.set("Decimal → Base")

        self.caixas_conteudo = {}
        configs = [(2, "Binário"), (8, "Octal"), (16, "Hexadecimal")]

        for base, nome in configs:
            texto_forward, resultado_final = self.calcular_forward(base)
            caixa_forward = self.montar_area_texto(container, texto_forward)

            texto_backward = self.calcular_backward(resultado_final, base, nome)
            caixa_backward = self.montar_area_texto(container, texto_backward)

            self.caixas_conteudo[base] = {"forward": caixa_forward, "backward": caixa_backward}

        self.atualizar_conteudo_visivel()

    def selecionar_aba(self, nome_base):
        self.base_atual = self.mapa_bases[nome_base]
        self.atualizar_conteudo_visivel()

    def alternar_direcao(self, nome_direcao):
        self.direcao_atual = self.mapa_direcao[nome_direcao]
        self.atualizar_conteudo_visivel()

    def atualizar_conteudo_visivel(self):
        if self.caixa_texto_visivel is not None:
            self.caixa_texto_visivel.pack_forget()
        alvo = self.caixas_conteudo[self.base_atual][self.direcao_atual]
        alvo.pack(fill="both", expand=True)
        self.caixa_texto_visivel = alvo

    def calcular_forward(self, base):
        linhas = []
        if self.valor_decimal == 0:
            linhas.append(("passo", "O valor é 0. Em qualquer base, 0 é 0.\n"))
            resultado_final = "0"
        else:
            n = self.valor_decimal
            restos = []
            while n > 0:
                quociente = n // base
                resto = n % base
                simbolo_resto = SIMBOLOS_HEX[resto] if base == 16 else str(resto)
                restos.append(simbolo_resto)
                linha = f"{n:>7}  ÷ {base:<2} =  {quociente:<7}   resto {simbolo_resto}\n"
                linhas.append(("passo", linha))
                n = quociente
            resultado_final = "".join(reversed(restos))

        cabecalho = [
            ("regra", f"Divida o número decimal sucessivamente por {base}, até o quociente chegar a 0. O resultado é formado pelos restos, lidos de baixo para cima.\n\n"),
            ("subtitulo_calc", f"Convertendo o decimal {self.valor_decimal}\n\n"),
        ]
        rodape = [
            ("quebra", "\n"),
            ("resultado_rotulo", "Resultado  "),
            ("resultado_valor", f"{resultado_final}\n"),
        ]
        return cabecalho + linhas + rodape, resultado_final

    def calcular_backward(self, valor_base_str, base, nome_base):
        linhas = []
        total_digitos = len(valor_base_str)
        soma = 0
        termos_soma = []

        for indice, caractere in enumerate(valor_base_str):
            posicao = total_digitos - 1 - indice
            valor_digito = SIMBOLOS_HEX.index(caractere) if base == 16 else int(caractere)
            parcial = valor_digito * (base ** posicao)
            soma += parcial
            termos_soma.append(str(parcial))
            
            expoente = str(posicao).translate(SOBRESCRITOS)
            linha = f"{caractere}  ×  {base}{expoente}   =  {parcial}\n"
            linhas.append(("passo", linha))

        cabecalho = [
            ("regra", f"Multiplique cada dígito pela base elevada à sua posição (da direita para a esquerda, começando em 0). Depois, some todos os resultados.\n\n"),
            ("subtitulo_calc", f"Convertendo o {nome_base.lower()} {valor_base_str}\n\n"),
        ]

        limite_por_linha = 5
        linhas_formatadas = []
        for i in range(0, len(termos_soma), limite_por_linha):
            pedaco = termos_soma[i : i + limite_por_linha]
            linhas_formatadas.append("  +  ".join(pedaco))

        texto_soma_final = "\n  +  ".join(linhas_formatadas) + f"\n  =  {soma}\n\n"

        rodape = [
            ("quebra", "\n"),
            ("resultado_rotulo", "Soma\n\n"),
            ("passo", texto_soma_final),
            ("resultado_rotulo", "Resultado  "),
            ("resultado_valor", f"{soma}\n"),
        ]
        return cabecalho + linhas + rodape

    def montar_area_texto(self, parent, partes_texto):
        area_texto = ctk.CTkTextbox(
            parent,
            font=(FONTE_MONO, 14),
            wrap="word",
            fg_color=COR_FUNDO_CAMPO,
            text_color=COR_TEXTO,
            border_width=0,
            corner_radius=15,
            padx=20,
            pady=20
        )

        # O "segredo" está no ._textbox antes do tag_configure. 
        # Isso acessa a camada profunda do widget e burla o bloqueio do CustomTkinter.
        area_texto._textbox.tag_configure("regra", font=(FONTE_BASE, 13), foreground=COR_TEXTO_SECUNDARIO)
        area_texto._textbox.tag_configure("subtitulo_calc", font=(FONTE_BASE, 13, "bold"), foreground=COR_TEXTO)
        area_texto._textbox.tag_configure("passo", font=(FONTE_MONO, 14), foreground=COR_TEXTO)
        area_texto._textbox.tag_configure("resultado_rotulo", font=(FONTE_BASE, 13, "bold"), foreground=COR_TEXTO_SECUNDARIO)
        area_texto._textbox.tag_configure("resultado_valor", font=(FONTE_MONO, 16, "bold"), foreground=COR_ACENTO)
        area_texto._textbox.tag_configure("quebra", font=(FONTE_MONO, 4))

        for tag, texto in partes_texto:
            area_texto.insert("end", texto, tag)

        area_texto.configure(state="disabled")
        return area_texto