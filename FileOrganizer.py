import os
import shutil
import customtkinter as ctk
from tkinter import filedialog

# Organizador de arquivos
# Objetivo desse projeto é criar uma aplicação simples para organizar os arquivos de um diretório
# Os arquivos são movidos conforme suas extensões e são criadas pastas com essas extensões e os arquivos são movidos
# Ficando de forma objetiva e clara a pasta organizada por extensões de arquivos e seus respectivos arquivos dentro dessas pastas
# Foi criado uma janela utilizando customtkinter para melhor experiência do usuário afim de não utilizar a aplicação por rodar via terminal
# Adicionado um botão para o usuário procurar a pasta que ele quer organizar

def organizar_arquivos():
    path = entrada_pasta.get()
    if not os.path.exists(path):
        label_resultado.configure(text="Pasta inválida.", text_color="red")
        return

    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        
        # Verifica se é um arquivo e não uma pasta
        if os.path.isfile(file_path):
            filename, extension = os.path.splitext(file)
            extension = extension[1:]  # Remove o ponto da extensão

            # Cria a pasta da extensão se não existir
            if not os.path.exists(os.path.join(path, extension)):
                os.makedirs(os.path.join(path, extension))

            # Move o arquivo para a pasta correspondente
            try:
                shutil.move(file_path, os.path.join(path, extension, file))
            except shutil.Error:
                label_resultado.configure(text=f"Arquivo {file} já existe na pasta {extension}", text_color="yellow")

    label_resultado.configure(text="Arquivos organizados com sucesso!", text_color="green")

def selecionar_pasta():
    # Abre a janela de seleção de pasta
    pasta_selecionada = filedialog.askdirectory()
    if pasta_selecionada:  # Se uma pasta foi selecionada
        entrada_pasta.delete(0, ctk.END)  # Limpa o campo de entrada
        entrada_pasta.insert(0, pasta_selecionada)  # Insere o caminho da pasta selecionada

# Configuração da janela principal
janela = ctk.CTk()  # Correção aqui: Usar CTk para criar a janela principal
janela.title("Organizador de Arquivos")
janela.geometry("400x200")

# Componentes da interface
label_pasta = ctk.CTkLabel(janela, text="Selecione a pasta para organizar:")
label_pasta.pack(pady=10)

entrada_pasta = ctk.CTkEntry(janela, width=300)
entrada_pasta.pack(pady=5)

# Botão para selecionar a pasta
botao_selecionar = ctk.CTkButton(janela, text="Selecionar Pasta", command=selecionar_pasta)
botao_selecionar.pack(pady=5)

botao_organizar = ctk.CTkButton(janela, text="Organizar", command=organizar_arquivos)
botao_organizar.pack(pady=10)

label_resultado = ctk.CTkLabel(janela, text="")
label_resultado.pack()

# Execução da janela
janela.mainloop()