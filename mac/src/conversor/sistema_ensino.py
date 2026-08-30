
import tkinter as tk
from tkinter import ttk
from src.conversor.conversor_hexadecimal import ConversorHexadecimal


COR_FUNDO_JANELA = "#242424"
COR_TEXTO_TITULO = "#f2f2f2"
COR_TEXTO_SECUNDARIO = "#9a9a9a"

COR_FUNDO_CODIGO = "#2d2d2d"
COR_TEXTO_CODIGO = "#d4d4d4"
COR_TEXTO_REGRA = "#a8a8a8"
COR_TEXTO_RESULTADO = "#ffffff"
COR_BORDA_CODIGO = "#3a3a3a"

COR_ABA_ATIVA_BG = "#3a3a3a"
COR_ABA_ATIVA_FG = "#ffffff"
COR_ABA_INATIVA_FG = "#8a8a8a"

COR_SUBABA_ATIVA_BG = "#333333"
COR_SUBABA_ATIVA_FG = "#e6e6e6"
COR_SUBABA_INATIVA_FG = "#787878"

SIMBOLOS_HEX = ConversorHexadecimal.SIMBOLOS
SOBRESCRITOS = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

ALTURA_MAXIMA_JANELA = 780
LARGURA_JANELA = 700


class SistemaEnsino:

    def __init__(self, parent, valor_decimal):
        self.parent = parent
        self.valor_decimal = valor_decimal
        self.base_atual = 2
        self.direcao_atual = "forward"
        self.frame_visivel = None

        self.janela = tk.Toplevel(parent)
        self.janela.title("Modo Estudante - Passo a Passo")
        self.janela.resizable(False, False)
        self.janela.configure(bg=COR_FUNDO_JANELA)

        self.criar_widgets()
        self.centralizar_janela()

    def centralizar_janela(self):
        self.janela.update_idletasks()

        altura_tela = self.janela.winfo_screenheight()
        largura_tela = self.janela.winfo_screenwidth()

        altura = min(ALTURA_MAXIMA_JANELA, altura_tela - 100)

        x = (largura_tela - LARGURA_JANELA) // 2
        y = max(20, (altura_tela - altura) // 2 - 60)

        self.janela.geometry(
            f"{LARGURA_JANELA}x{altura}+{x}+{y}"
        )

    def criar_widgets(self):
        container = tk.Frame(
            self.janela,
            bg=COR_FUNDO_JANELA
        )
        container.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )

        titulo = tk.Label(
            container,
            text="Passo a Passo da Conversão",
            font=("Helvetica Neue", 18, "bold"),
            bg=COR_FUNDO_JANELA,
            fg=COR_TEXTO_TITULO
        )
        titulo.pack(anchor="w")

        subtitulo = tk.Label(
            container,
            text="Veja como o resultado é calculado em cada base",
            font=("Helvetica Neue", 12),
            bg=COR_FUNDO_JANELA,
            fg=COR_TEXTO_SECUNDARIO
        )
        subtitulo.pack(anchor="w", pady=(2, 18))

        barra_abas = tk.Frame(
            container,
            bg=COR_FUNDO_JANELA
        )
        barra_abas.pack(pady=(0, 12))

        self.botoes = {}
        self.frames_conteudo = {}

        configs = [
            (2, "Binário"),
            (8, "Octal"),
            (16, "Hexadecimal")
        ]

        for base, nome in configs:
            lbl = tk.Label(
                barra_abas,
                text=nome,
                font=("Helvetica Neue", 13, "bold"),
                bg=COR_FUNDO_JANELA,
                fg=COR_ABA_INATIVA_FG,
                padx=16,
                pady=7,
                cursor="pointinghand"
            )
            lbl.pack(side="left", padx=4)

            lbl.bind(
                "<Button-1>",
                lambda evento, b=base: self.selecionar_aba(b)
            )

            self.botoes[base] = lbl

            texto_forward, resultado_final = self.calcular_forward(base)
            frame_forward = self.montar_area_texto(
                container,
                texto_forward
            )

            texto_backward = self.calcular_backward(
                resultado_final,
                base,
                nome
            )
            frame_backward = self.montar_area_texto(
                container,
                texto_backward
            )

            self.frames_conteudo[base] = {
                "forward": frame_forward,
                "backward": frame_backward
            }

        separador_direcao = tk.Frame(
            container,
            height=1,
            bg=COR_BORDA_CODIGO
        )
        separador_direcao.pack(
            fill="x",
            pady=(5, 12)
        )

        titulo_direcao = tk.Label(
            container,
            text="Sentido da conversão",
            font=("Helvetica Neue", 11, "bold"),
            bg=COR_FUNDO_JANELA,
            fg=COR_TEXTO_TITULO
        )
        titulo_direcao.pack(anchor="w")

        subtitulo_direcao = tk.Label(
            container,
            text="Escolha em qual direção deseja realizar a conversão",
            font=("Helvetica Neue", 10),
            bg=COR_FUNDO_JANELA,
            fg=COR_TEXTO_SECUNDARIO
        )
        subtitulo_direcao.pack(
            anchor="w",
            pady=(2, 8)
        )

        barra_direcao = tk.Frame(
            container,
            bg=COR_FUNDO_JANELA
        )
        barra_direcao.pack(
            anchor="w",
            pady=(0, 15)
        )

        self.sub_botoes = {}

        opcoes_direcao = [
            ("forward", "Decimal  →  Base"),
            ("backward", "Base  →  Decimal")
        ]

        for direcao, texto in opcoes_direcao:
            lbl = tk.Label(
                barra_direcao,
                text=texto,
                font=("Helvetica Neue", 11, "bold"),
                bg=COR_FUNDO_JANELA,
                fg=COR_SUBABA_INATIVA_FG,
                padx=14,
                pady=7,
                cursor="pointinghand"
            )

            lbl.pack(
                side="left",
                padx=(0, 8)
            )

            lbl.bind(
                "<Button-1>",
                lambda evento, d=direcao: self.alternar_direcao(d)
            )

            self.sub_botoes[direcao] = lbl

        divisor = tk.Frame(
            container,
            height=1,
            bg=COR_BORDA_CODIGO
        )
        divisor.pack(
            fill="x",
            pady=(0, 18)
        )

        self.area_conteudo_pai = container

        self.atualizar_estilo_abas()
        self.atualizar_estilo_direcao()
        self.atualizar_conteudo_visivel()

    def selecionar_aba(self, base_selecionada):
        self.base_atual = base_selecionada
        self.atualizar_estilo_abas()
        self.atualizar_conteudo_visivel()

    def alternar_direcao(self, direcao_selecionada):
        self.direcao_atual = direcao_selecionada
        self.atualizar_estilo_direcao()
        self.atualizar_conteudo_visivel()

    def atualizar_estilo_abas(self):
        for base, lbl in self.botoes.items():
            ativo = base == self.base_atual

            lbl.config(
                bg=COR_ABA_ATIVA_BG if ativo else COR_FUNDO_JANELA,
                fg=COR_ABA_ATIVA_FG if ativo else COR_ABA_INATIVA_FG
            )

    def atualizar_estilo_direcao(self):
        for direcao, lbl in self.sub_botoes.items():
            ativo = direcao == self.direcao_atual

            lbl.config(
                bg=COR_SUBABA_ATIVA_BG if ativo else COR_FUNDO_JANELA,
                fg=COR_SUBABA_ATIVA_FG if ativo else COR_SUBABA_INATIVA_FG
            )

    def atualizar_conteudo_visivel(self):
        if self.frame_visivel is not None:
            self.frame_visivel.pack_forget()

        alvo = self.frames_conteudo[
            self.base_atual
        ][
            self.direcao_atual
        ]

        alvo.pack(
            fill="both",
            expand=True
        )

        self.frame_visivel = alvo

    def calcular_forward(self, base):
        linhas = []

        if self.valor_decimal == 0:
            linhas.append(
                (
                    "passo",
                    "O valor é 0. Em qualquer base, 0 é 0.\n"
                )
            )
            resultado_final = "0"

        else:
            n = self.valor_decimal
            restos = []

            while n > 0:
                quociente = n // base
                resto = n % base

                simbolo_resto = (
                    SIMBOLOS_HEX[resto]
                    if base == 16
                    else str(resto)
                )

                restos.append(simbolo_resto)

                linha = (
                    f"{n:>7}  ÷ {base:<2} =  "
                    f"{quociente:<7}   resto {simbolo_resto}\n"
                )

                linhas.append(
                    ("passo", linha)
                )

                n = quociente

            resultado_final = "".join(
                reversed(restos)
            )

        cabecalho = [
            (
                "regra",
                f"Divida o número decimal sucessivamente por {base}, "
                f"até o quociente chegar a 0. O resultado é formado "
                f"pelos restos, lidos de baixo para cima.\n\n"
            ),
            (
                "subtitulo_calc",
                f"Convertendo o decimal {self.valor_decimal}\n\n"
            )
        ]

        rodape = [
            ("quebra", "\n"),
            ("resultado_rotulo", "Resultado  "),
            ("resultado_valor", f"{resultado_final}\n")
        ]

        return cabecalho + linhas + rodape, resultado_final

    def calcular_backward(
        self,
        valor_base_str,
        base,
        nome_base
    ):
        linhas = []

        total_digitos = len(valor_base_str)
        soma = 0

        for indice, caractere in enumerate(valor_base_str):
            posicao = total_digitos - 1 - indice

            valor_digito = (
                SIMBOLOS_HEX.index(caractere)
                if base == 16
                else int(caractere)
            )

            parcial = valor_digito * (base ** posicao)
            soma += parcial

            expoente = str(posicao).translate(SOBRESCRITOS)

            linha = (
                f"{caractere}  ×  {base}{expoente}   =  {parcial}\n"
            )

            linhas.append(
                ("passo", linha)
            )

        cabecalho = [
            (
                "regra",
                f"Multiplique cada dígito pela base elevada à sua posição "
                f"(da direita para a esquerda, começando em 0). "
                f"Depois, some todos os resultados.\n\n"
            ),
            (
                "subtitulo_calc",
                f"Convertendo o {nome_base.lower()} "
                f"{valor_base_str}\n\n"
            )
        ]

        rodape = [
            ("quebra", "\n"),
            ("resultado_rotulo", "Soma  "),
            (
                "passo",
                "  +  ".join(
                    str(
                        (
                            SIMBOLOS_HEX.index(c)
                            if base == 16
                            else int(c)
                        )
                        * (
                            base
                            ** (
                                total_digitos
                                - 1
                                - i
                            )
                        )
                    )
                    for i, c in enumerate(valor_base_str)
                )
                + f"  =  {soma}\n\n"
            ),
            ("resultado_rotulo", "Resultado  "),
            ("resultado_valor", f"{soma}\n")
        ]

        return cabecalho + linhas + rodape

    def montar_area_texto(self, parent, partes_texto):
        frame = tk.Frame(
            parent,
            bg=COR_FUNDO_JANELA
        )

        area_texto = tk.Text(
            frame,
            font=("Menlo", 12),
            wrap="word",
            bg=COR_FUNDO_CODIGO,
            fg=COR_TEXTO_CODIGO,
            insertbackground=COR_TEXTO_CODIGO,
            borderwidth=0,
            highlightthickness=1,
            highlightbackground=COR_BORDA_CODIGO,
            highlightcolor=COR_BORDA_CODIGO,
            padx=20,
            pady=18,
            spacing3=4
        )

        area_texto.tag_configure(
            "regra",
            font=("Helvetica Neue", 12),
            foreground=COR_TEXTO_REGRA
        )

        area_texto.tag_configure(
            "subtitulo_calc",
            font=("Helvetica Neue", 12, "bold"),
            foreground=COR_TEXTO_TITULO
        )

        area_texto.tag_configure(
            "passo",
            font=("Menlo", 12),
            foreground=COR_TEXTO_CODIGO
        )

        area_texto.tag_configure(
            "resultado_rotulo",
            font=("Helvetica Neue", 12, "bold"),
            foreground=COR_TEXTO_REGRA
        )

        area_texto.tag_configure(
            "resultado_valor",
            font=("Menlo", 15, "bold"),
            foreground=COR_TEXTO_RESULTADO
        )

        area_texto.tag_configure(
            "quebra",
            font=("Menlo", 4)
        )

        for tag, texto in partes_texto:
            area_texto.insert(
                "end",
                texto,
                tag
            )

        area_texto.config(
            state="disabled"
        )

        scrollbar = ttk.Scrollbar(
            frame,
            orient="vertical",
            command=area_texto.yview
        )

        area_texto.config(
            yscrollcommand=scrollbar.set
        )

        area_texto.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        return frame
