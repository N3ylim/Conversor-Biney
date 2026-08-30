import tkinter as tk
from tkinter import ttk
from src.conversor.numero_base import Numero
from src.conversor.conversor_binario import ConversorBinario
from src.conversor.conversor_octal import ConversorOctal
from src.conversor.conversor_hexadecimal import ConversorHexadecimal
from src.conversor.sistema_ensino import SistemaEnsino


##COR_ROTULO = "#7a92a8"
COR_TEXTO_SECUNDARIO = "#9a9a9a"
COR_ERRO = "#e05c5c"


class InterfaceConversor:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Números")
        self.root.resizable(False, False)

        self.base_selecionada = tk.StringVar(value="Decimal")
        self.base_selecionada.trace_add("write", lambda *args: self.converter())

        self.criar_widgets()
        self.centralizar_janela()

    def centralizar_janela(self):
        self.root.update_idletasks()
        largura = max(self.root.winfo_reqwidth(), 420)
        altura = self.root.winfo_reqheight()
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")

    def criar_widgets(self):
        estilo = ttk.Style()
        estilo.configure("Titulo.TLabel", font=("Helvetica Neue", 22, "bold"))
        estilo.configure("Subtitulo.TLabel", font=("Helvetica Neue", 12), foreground=COR_TEXTO_SECUNDARIO)
        estilo.configure("Rotulo.TLabel", font=("Menlo", 13, "bold")) ##, foreground=COR_ROTULO cor azul nas letras
        estilo.configure("Erro.TLabel", font=("Helvetica Neue", 13), foreground=COR_ERRO)

        container = ttk.Frame(self.root, padding=(35, 30))
        container.pack(fill="both", expand=True)

        titulo = ttk.Label(container, text="Conversor de Números", style="Titulo.TLabel")
        titulo.pack()

        subtitulo = ttk.Label(
            container, text="Escolha a base e digite o número", style="Subtitulo.TLabel"
        )
        subtitulo.pack(pady=(2, 20))

        frame_opcoes = ttk.Frame(container)
        frame_opcoes.pack(fill="x", pady=(0, 15))

        opcoes = ["Binário", "Octal", "Decimal", "Hexadecimal"]
        for opcao in opcoes:
            radio = ttk.Radiobutton(
                frame_opcoes, text=opcao, value=opcao, variable=self.base_selecionada
            )
            radio.pack(side="left", expand=True)

        self.entrada = ttk.Entry(container, font=("Menlo", 18), justify="center")
        self.entrada.pack(pady=15, ipady=8, fill="x")
        self.entrada.bind("<KeyRelease>", lambda evento: self.converter())
        self.entrada.focus()

        separador = ttk.Separator(container, orient="horizontal")
        separador.pack(fill="x", pady=10)

        self.frame_resultado = ttk.Frame(container)
        self.frame_resultado.pack(fill="x")

        self.linhas_resultado = {}
        for rotulo in ["Decimal", "Binário", "Octal", "Hexadecimal"]:
            linha = ttk.Frame(self.frame_resultado)
            linha.pack(fill="x", pady=3)

            ttk.Label(linha, text=rotulo, style="Rotulo.TLabel", width=12).pack(side="left")

            valor = ttk.Entry(linha, font=("Menlo", 13), state="readonly")
            valor.pack(side="left", fill="x", expand=True, padx=(0, 5))

            btn_copiar = ttk.Button(
                linha, text="Copiar", width=8,
                command=lambda r=rotulo: self.copiar_texto(r)
            )
            btn_copiar.pack(side="right", padx=(5, 0))

            self.linhas_resultado[rotulo] = valor

        self.label_erro = ttk.Label(container, text="", style="Erro.TLabel")
        self.label_erro.pack(pady=(10, 0), fill="x")

        btn_ensino = ttk.Button(
            container, text="Entender o Cálculo (Passo a Passo)", command=self.abrir_tutorial
        )
        btn_ensino.pack(pady=(15, 0), ipady=4, fill="x")

        self.limpar_resultado()

    def copiar_texto(self, rotulo):
        texto = self.linhas_resultado[rotulo].get()
        if texto and texto != "—":
            self.root.clipboard_clear()
            self.root.clipboard_append(texto)
            self.root.update()

    def atualizar_valor(self, rotulo, texto):
        widget = self.linhas_resultado[rotulo]
        widget.config(state="normal")
        widget.delete(0, tk.END)
        widget.insert(0, texto)
        widget.config(state="readonly")

    def limpar_resultado(self):
        for rotulo in self.linhas_resultado:
            self.atualizar_valor(rotulo, "—")
        self.label_erro.config(text="")

    def converter(self):
        texto = self.entrada.get().strip()
        base = self.base_selecionada.get()

        if texto == "":
            self.limpar_resultado()
            self.valor_decimal_atual = None
            return

        try:
            if base == "Binário":
                valor_decimal = ConversorBinario.para_decimal(texto)
            elif base == "Octal":
                valor_decimal = ConversorOctal.para_decimal(texto)
            elif base == "Decimal":
                valor_decimal = int(texto)
            elif base == "Hexadecimal":
                valor_decimal = ConversorHexadecimal.para_decimal(texto)
            else:
                return

            if valor_decimal < 0:
                raise ValueError("números negativos não são suportados")

            numero = Numero(valor_decimal)
            self.label_erro.config(text="")
            self.valor_decimal_atual = numero.valor_decimal

            try:
                self.atualizar_valor("Decimal", str(numero.valor_decimal))
                self.atualizar_valor("Binário", ConversorBinario.de_decimal(numero.valor_decimal))
                self.atualizar_valor("Octal", ConversorOctal.de_decimal(numero.valor_decimal))
                self.atualizar_valor("Hexadecimal", ConversorHexadecimal.de_decimal(numero.valor_decimal))
            except Exception as erro:
                self.limpar_resultado()
                self.label_erro.config(text=f"Erro ao gerar resultado: {erro}")

        except ValueError:
            self.limpar_resultado()
            self.valor_decimal_atual = None
            self.label_erro.config(text=f'"{texto}" não é válido em {base.lower()}.')
        except Exception as erro:
            self.limpar_resultado()
            self.valor_decimal_atual = None
            self.label_erro.config(text=f"Erro inesperado: {erro}")

    def abrir_tutorial(self):
        if not hasattr(self, "valor_decimal_atual") or self.valor_decimal_atual is None:
            self.label_erro.config(text="Digite um número válido primeiro para ver o passo a passo.")
            return

        if hasattr(self, "janela_ensino") and self.janela_ensino.janela.winfo_exists():
            self.janela_ensino.janela.destroy()

        self.janela_ensino = SistemaEnsino(self.root, self.valor_decimal_atual)


def iniciar_interface():
    root = tk.Tk()
    app = InterfaceConversor(root)
    root.mainloop()