import customtkinter as ctk
from src.conversor.numero_base import Numero
from src.conversor.conversor_binario import ConversorBinario
from src.conversor.conversor_octal import ConversorOctal
from src.conversor.conversor_hexadecimal import ConversorHexadecimal
from src.conversor.sistema_ensino import SistemaEnsino
from src.conversor.ui_estilo import *

class InterfaceConversor:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Números")
        self.root.resizable(False, False)
        self.root.configure(fg_color=COR_FUNDO)
        
        configurar_tema()
        self.base_atual = "Binário"
        self.criar_widgets()
        self.centralizar_janela() # Chama a centralização no final

    def centralizar_janela(self):
        self.root.update_idletasks()
        largura = 460
        altura = 600
        x = (self.root.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.root.winfo_screenheight() // 2) - (altura // 2)
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")

    def criar_widgets(self):
        container = ctk.CTkFrame(self.root, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=30, pady=30)

        ctk.CTkLabel(container, text="Conversor de Números", font=(FONTE_BASE, 22, "bold"), text_color=COR_TEXTO).pack()
        ctk.CTkLabel(container, text="Escolha a base e digite o número", font=(FONTE_BASE, 12), text_color=COR_TEXTO_SECUNDARIO).pack(pady=(4, 20))

        self.seletor = ctk.CTkSegmentedButton(
            container, 
            values=["Binário", "Octal", "Decimal", "Hexadecimal"],
            command=self.selecionar_base,
            font=(FONTE_BASE, 12, "bold"),
            fg_color=COR_FUNDO_CARTAO,
            selected_color=COR_ACENTO,
            selected_hover_color=COR_ACENTO_HOVER,
            unselected_color=COR_FUNDO_CARTAO,
            text_color=COR_TEXTO,
            corner_radius=20
        )
        self.seletor.pack(fill="x", pady=(0, 20))
        self.seletor.set("Binário")

        self.entrada = ctk.CTkEntry(
            container, font=(FONTE_MONO, 20), justify="center", height=50,
            corner_radius=15, fg_color=COR_FUNDO_CAMPO, border_width=0
        )
        self.entrada.pack(fill="x", pady=(0, 20))
        self.entrada.bind("<KeyRelease>", lambda e: self.converter())
        
        cartao_resultado = ctk.CTkFrame(container, fg_color=COR_FUNDO_CARTAO, corner_radius=15)
        cartao_resultado.pack(fill="x", pady=(0, 15), ipadx=10, ipady=10)

        self.linhas_resultado = {}
        for rotulo in ["Decimal", "Binário", "Octal", "Hexadecimal"]:
            linha = ctk.CTkFrame(cartao_resultado, fg_color="transparent")
            linha.pack(fill="x", padx=15, pady=8)
            
            ctk.CTkLabel(linha, text=rotulo, font=(FONTE_BASE, 12, "bold"), text_color=COR_TEXTO_SECUNDARIO, width=90, anchor="w").pack(side="left")
            
            valor = ctk.CTkEntry(linha, font=(FONTE_MONO, 12), fg_color="transparent", border_width=0, state="readonly", text_color=COR_TEXTO)
            valor.pack(side="left", fill="x", expand=True)
            
            btn_copiar = ctk.CTkButton(
                linha, text="Copiar", width=60, height=28, corner_radius=10,
                fg_color="#3a3a3a", hover_color="#4a4a4a", font=(FONTE_BASE, 11),
                command=lambda r=rotulo: self.copiar_texto(r)
            )
            btn_copiar.pack(side="right")
            self.linhas_resultado[rotulo] = valor

        self.label_erro = ctk.CTkLabel(container, text="", text_color="#ff4d4d", font=(FONTE_BASE, 12))
        self.label_erro.pack(pady=(0, 10))

        btn_ensino = ctk.CTkButton(
            container, text="Entender o Cálculo (Passo a Passo)", height=45, corner_radius=15,
            fg_color=COR_ACENTO, hover_color=COR_ACENTO_HOVER, font=(FONTE_BASE, 14, "bold"),
            command=self.abrir_tutorial
        )
        btn_ensino.pack(fill="x", side="bottom")
        self.limpar_resultado()

    def selecionar_base(self, opcao):
        self.base_atual = opcao
        self.converter()

    def copiar_texto(self, rotulo):
        texto = self.linhas_resultado[rotulo].get()
        if texto and texto != "—":
            self.root.clipboard_clear()
            self.root.clipboard_append(texto)
            self.root.update()

    def atualizar_valor(self, rotulo, texto):
        widget = self.linhas_resultado[rotulo]
        widget.configure(state="normal")
        widget.delete(0, ctk.END)
        widget.insert(0, texto)
        widget.configure(state="readonly")

    def limpar_resultado(self):
        for rotulo in self.linhas_resultado:
            self.atualizar_valor(rotulo, "—")
        self.label_erro.configure(text="")

    def converter(self):
        texto = self.entrada.get().strip()
        if texto == "":
            self.limpar_resultado()
            self.valor_decimal_atual = None
            return

        try:
            if self.base_atual == "Binário": valor_decimal = ConversorBinario.para_decimal(texto)
            elif self.base_atual == "Octal": valor_decimal = ConversorOctal.para_decimal(texto)
            elif self.base_atual == "Decimal": valor_decimal = int(texto)
            elif self.base_atual == "Hexadecimal": valor_decimal = ConversorHexadecimal.para_decimal(texto)

            if valor_decimal < 0: raise ValueError("números negativos não são suportados")
            
            numero = Numero(valor_decimal)
            self.label_erro.configure(text="")
            self.valor_decimal_atual = numero.valor_decimal

            self.atualizar_valor("Decimal", str(numero.valor_decimal))
            self.atualizar_valor("Binário", ConversorBinario.de_decimal(numero.valor_decimal))
            self.atualizar_valor("Octal", ConversorOctal.de_decimal(numero.valor_decimal))
            self.atualizar_valor("Hexadecimal", ConversorHexadecimal.de_decimal(numero.valor_decimal))
            
        except ValueError:
            self.limpar_resultado()
            self.valor_decimal_atual = None
            self.label_erro.configure(text=f'"{texto}" não é válido em {self.base_atual.lower()}.')
        except Exception as erro:
            self.limpar_resultado()
            self.valor_decimal_atual = None
            self.label_erro.configure(text=f"Erro inesperado: {erro}")

    def abrir_tutorial(self):
        if getattr(self, "valor_decimal_atual", None) is None:
            self.label_erro.configure(text="Digite um número válido primeiro.")
            return
        if hasattr(self, "janela_ensino") and self.janela_ensino.janela.winfo_exists():
            self.janela_ensino.janela.destroy()
        self.janela_ensino = SistemaEnsino(self.root, self.valor_decimal_atual)

def iniciar_interface():
    root = ctk.CTk()
    app = InterfaceConversor(root)
    root.mainloop()