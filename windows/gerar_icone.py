from PIL import Image, ImageDraw, ImageFont

# Cria uma base transparente de 256x256 pixels
imagem = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
desenho = ImageDraw.Draw(imagem)

# Desenha o fundo: um quadrado arredondado cinza chumbo (cor do seu app)
desenho.rounded_rectangle(
    [(10, 10), (246, 246)], 
    radius=50, 
    fill="#2b2b2b", 
    outline="#525252", 
    width=8
)

# Adiciona a letra "B" (de Biney) no centro
try:
    fonte = ImageFont.truetype("arialbd.ttf", 140) # Arial Bold do Windows
except:
    fonte = ImageFont.load_default()

texto = "B"
_, _, w, h = desenho.textbbox((0, 0), texto, font=fonte)
desenho.text(((256-w)/2, (256-h)/2 - 25), texto, fill="#ffffff", font=fonte)

# Salva no formato oficial do Windows
imagem.save("icone.ico", format="ICO", sizes=[(256, 256)])
print("Ícone 'icone.ico' criado com sucesso na pasta!")