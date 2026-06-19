import json

with open("perguntas.json", "r", encoding="utf-8") as arquivo:
    questions = json.load(arquivo)

letras = ["a", "b", "c", "d"]
guesses = []
score = 0

for question_num, q in enumerate(questions):
    print("=====" * 20)
    print(f"{question_num + 1}. {q['pergunta']}")

    for i, opcao in enumerate(q["opcoes"]):
        print(f"{letras[i]}. {opcao}")

    guess = input("Escolha a sua resposta (A, B, C ou D): ").lower().strip()
    guesses.append(guess)

    if guess == q["resposta"]:
        score += 1
        print("Você acertou na mosca!")
    else:
        resposta_certa = q["opcoes"][letras.index(q["resposta"])]
        print(f"Ops! A resposta correta é {q['resposta'].upper()} - {resposta_certa}")

print("========" * 10)
print("Resultado!")
print("========" * 10)

print("Gabarito:   ", end="")
for q in questions:
    print(q["resposta"].upper(), end=" ")

print()
print("Seus palpites: ", end="")
for guess in guesses:
    print(guess.upper(), end=" ")

print()
score_pct = int((score / len(questions)) * 100)
print(f"\nSua pontuação: {score_pct}%")