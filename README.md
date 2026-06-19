# 🧠 Quiz de Perguntas

Quiz interativo de perguntas e respostas no terminal, desenvolvido em Python.

## 💡 Como funciona

- As perguntas são carregadas de um arquivo `perguntas.json` externo
- O jogador responde escolhendo A, B, C ou D
- Ao final exibe o gabarito, os palpites e a pontuação em %

## ▶️ Como rodar

```bash
python quiz.py
```

## 🛠️ Tecnologias

- Python 3
- Módulo `json` (nativo)

## ➕ Como adicionar perguntas

Edite o arquivo `perguntas.json` seguindo o padrão:

```json
{
    "pergunta": "Sua pergunta aqui?",
    "opcoes": ["opção a", "opção b", "opção c", "opção d"],
    "resposta": "a"
}
```
