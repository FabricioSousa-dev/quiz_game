questions = [
    "Quantos elementos tem na tabela periódica?",
    "Há quantos anos o Brasil foi descoberto?",
    "Qual é a capital do Brasil?",
    "Qual é a capital da França?",
    "Qual é a capital da Alemanha?",
]

options = (
    ("a. 116", "b. 523", "c. 118", "d. 120"),
    ("a. 523", "b. 524", "c. 500", "d. 526"),
    ("a. Brasília", "b. Rio de Janeiro", "c. São Paulo", "d. Minas Gerais"),
    ("a. Paris", "b. Londres", "c. Berlim", "d. Madrid"),
    ("a. Berlim", "b. Londres", "c. Paris", "d. Madrid"),
)

answers = ("c", "a", "a", "a", "a")
guesses = []
score = 0

for question_num, question in enumerate(questions):
    print("=====" * 20)
    print(f"{question}")
    for option in options[question_num]:
        print(option)

    guess = input("Escolha a sua resposta (A, B, C ou D): ").upper().strip()
    guesses.append(guess)

    if guess == answers[question_num].upper():
        score += 1
        print("Você acertou na mosca!")
    else:
        print(f"Ops! A resposta correta é {answers[question_num].upper()}")

print("========" * 10)
print("Resultado!")
print("========" * 10)

print("Gabarito:  ", end="")
for answer in answers:
    print(answer.upper(), end=" ")

print()
print("Seus palpites: ", end="")
for guess in guesses:
    print(guess, end=" ")

print()
score_pct = int((score / len(answers)) * 100)
print(f"\nSua pontuação: {score_pct}%")