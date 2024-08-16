import tkinter as tk

nome = "João Vitor Melo"  # Substitua pelo seu nome real

# Cria a janela principal
root = tk.Tk()
root.title("Animação de Nome")

# Cria um canvas para desenhar a animação
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

# Define a fonte para o texto
fonte = ("Arial", 24)

# Função para desenhar a animação
def desenhar_animacao():
    # Limpa o canvas
    canvas.delete("all")

    # Desenha o texto caractere por caractere
    for i, char in enumerate(nome):
        x = 50 + i * 20
        y = 100
        canvas.create_text(x, y, text=char, font=fonte)

    # Atualiza a animação
    root.after(100, desenhar_animacao)

# Inicia a animação
desenhar_animacao()

# Inicia o loop de eventos
root.mainloop()