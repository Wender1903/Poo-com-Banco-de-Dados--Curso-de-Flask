import tkinter as tk
import orm
from tkinter import messagebox

def adicionar_serie():
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.adicionar_series(nome, ano, nota)
    messagebox.showinfo("Sucesso", "Série Cadastrada com Sucesso!!")

def atualizar_serie():
    id = entry_id.get()
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.atualizar_series(id, nome, ano, nota)
    messagebox.showinfo("Sucesso", "Série Atualizada com Sucesso")

def deletar_serie():
    id = entry_id.get()
    orm.deletar_serie(id)
    messagebox.showinfo("Sucesso", "Série Deletada com Sucesso")
# Interface Gráfica
root = tk.Tk()
root.title("Gerenciador de Séries")

# Rótulos e Campos de Entrada
label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=1, column=0)
entry_nome = tk.Entry(root, width=50)
entry_nome.grid(row=1, column=1, padx=10, pady=5)


label_ano = tk.Label(root, text="Ano:")
label_ano.grid(row=2, column=0)
entry_ano = tk.Entry(root, width=50)
entry_ano.grid(row=2, column=1, padx=10, pady=5)


label_nota = tk.Label(root, text="Nota:")
label_nota.grid(row=3, column=0)
entry_nota = tk.Entry(root, width=50)
entry_nota.grid(row=3, column=1, padx=10, pady=5)

button_adicionar = tk.Button(root, text="Adicionar Série", command=adicionar_serie)
button_adicionar.grid(row=4, column=0, columnspan=2, pady=5)

button_atualizar = tk.Button(root, text="Atualizar Série", command=atualizar_serie)
button_atualizar.grid(row=5, column=0, columnspan=2, pady=5)

button_deletar = tk.Button(root, text="Deletar Série", command=deletar_serie)
button_deletar.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()