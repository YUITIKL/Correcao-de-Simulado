// app.js

const express = require("express");
const app = express();

app.use(express.json());

// Função para corrigir provas
function corrigirProva(gabarito, alunos) {
    const resultados = alunos.map(aluno => {
        const acertos = aluno.respostas.reduce((total, resp, i) => {
            return resp === gabarito[i] ? total + 1 : total;
        }, 0);

        const percentual = (acertos / gabarito.length) * 100;

        return {
            nome: aluno.nome,
            acertos,
            percentual: Number(percentual.toFixed(2))
        };
    });

    const media = resultados.reduce((soma, r) => soma + r.acertos, 0) / resultados.length;

    const ranking = [...resultados].sort((a, b) => b.acertos - a.acertos);

    return {
        media: Number(media.toFixed(2)),
        ranking,
        resultados
    };
}

// Rota principal
app.post("/corrigir", (req, res) => {
    const { gabarito, alunos } = req.body;

    if (!gabarito || !alunos) {
        return res.status(400).json({ erro: "Dados inválidos" });
    }

    const resultado = corrigirProva(gabarito, alunos);

    res.json(resultado);
});

// Servidor
app.listen(3000, () => {
    console.log("API rodando em http://localhost:3000");
});