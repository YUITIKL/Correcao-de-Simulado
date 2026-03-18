import tkinter as tk
from tkinter import messagebox
import string


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Correção")
        self.root.geometry("500x500")
        self.root.configure(bg="#f5f5f5")

        self.qtd_questoes = 0
        self.qtd_alternativas = 0
        self.opcoes = []

        self.gabarito_vars = []
        self.respostas_vars = []

        self.tela_inicial()

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def tela_inicial(self):
        self.limpar_tela()

        frame = tk.Frame(self.root, bg="#f5f5f5")
        frame.pack(expand=True)

        tk.Label(frame, text="Correção de Simulado",
                 font=("Arial", 18, "bold"), bg="#f5f5f5").pack(pady=20)

        tk.Label(frame, text="Quantidade de questões:",
                 font=("Arial", 12), bg="#f5f5f5").pack()

        self.input_qtd = tk.Entry(frame, justify="center", font=("Arial", 12))
        self.input_qtd.pack(pady=5)

        tk.Label(frame, text="Quantidade de alternativas:",
                 font=("Arial", 12), bg="#f5f5f5").pack(pady=(10, 0))

        self.input_alt = tk.Entry(frame, justify="center", font=("Arial", 12))
        self.input_alt.pack(pady=5)

        tk.Button(frame, text="Continuar",
                  bg="#4CAF50", fg="white",
                  font=("Arial", 12, "bold"),
                  command=self.criar_prova).pack(pady=15)

    def criar_prova(self):
        try:
            self.qtd_questoes = int(self.input_qtd.get())
            self.qtd_alternativas = int(self.input_alt.get())

            if self.qtd_questoes <= 0 or self.qtd_alternativas <= 1:
                raise ValueError

        except:
            messagebox.showerror("Erro", "Valores inválidos!")
            return

        self.opcoes = list(string.ascii_uppercase[:self.qtd_alternativas])

        self.limpar_tela()

        canvas = tk.Canvas(self.root, bg="#f5f5f5")
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        frame = tk.Frame(canvas, bg="#f5f5f5")

        frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        tk.Label(frame, text="Gabarito", font=("Arial", 14, "bold"),
                 bg="#f5f5f5").pack(pady=10)

        self.gabarito_vars = []
        for i in range(self.qtd_questoes):
            var = tk.StringVar()
            self.gabarito_vars.append(var)

            linha = tk.Frame(frame, bg="#f5f5f5")
            linha.pack(pady=2)

            tk.Label(linha, text=f"Q{i+1}", width=4,
                     bg="#f5f5f5").pack(side="left")

            for op in self.opcoes:
                tk.Radiobutton(
                    linha, text=op, value=op, variable=var,
                    bg="#f5f5f5"
                ).pack(side="left")

        tk.Label(frame, text="Respostas do Aluno",
                 font=("Arial", 14, "bold"),
                 bg="#f5f5f5").pack(pady=10)

        self.respostas_vars = []
        for i in range(self.qtd_questoes):
            var = tk.StringVar()
            self.respostas_vars.append(var)

            linha = tk.Frame(frame, bg="#f5f5f5")
            linha.pack(pady=2)

            tk.Label(linha, text=f"Q{i+1}", width=4,
                     bg="#f5f5f5").pack(side="left")

            for op in self.opcoes:
                tk.Radiobutton(
                    linha, text=op, value=op, variable=var,
                    bg="#f5f5f5"
                ).pack(side="left")

        tk.Button(frame, text="Corrigir Prova",
                  bg="#2196F3", fg="white",
                  font=("Arial", 12, "bold"),
                  command=self.corrigir).pack(pady=15)

        self.resultado = tk.Label(frame, text="", font=("Arial", 12, "bold"),
                                 bg="#f5f5f5")
        self.resultado.pack(pady=10)

    def corrigir(self):
        gabarito = [v.get() for v in self.gabarito_vars]
        respostas = [v.get() for v in self.respostas_vars]

        if "" in gabarito or "" in respostas:
            messagebox.showerror("Erro", "Preencha todas as questões!")
            return  

        acertos = sum(1 for i in range(self.qtd_questoes) if gabarito[i] == respostas[i])
        percentual = (acertos / self.qtd_questoes) * 100

        self.resultado.config(
            text=f"Acertos: {acertos}/{self.qtd_questoes} | {percentual:.2f}%"
        )


root = tk.Tk()
app = App(root)
root.mainloop()