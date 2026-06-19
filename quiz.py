questions = {
  "Quantos elementos tem na tabela periodica?",
   "Quantos anos o brasil foi descoberto?",
    "Qual é a capital do brasil?", 
    "Qual é a capital da frança?",
    "Qual é a capital da alemanha?",
    
}  

options = (
    ("a.116","b.523","c.118","d.118"),
    ("a.523","b.524","c.500","d.526"),
    ("a.brasilia","b.rio de janeiro","c.são paulo","d.minas gerais"),
    ("a.paris","b.londres","c.berlim","d.madrid"),
    ("a.berlim","b.londres","c.paris","d.madrid")
    
)
guesses = []

answers = ("c","a","a","c","a")
score = 0
question_num = 0

for question in questions:
    print("====="*20)
    print(f"{question}")

for option in options[question_num]:
    print(option)

guess = input("Escolha a sua resposta (A, B, C ou D): ").upper().strip()
guesses.append(guess)

if guess == answers[question_num]:
    score += 1
    print("Você acertou na mosca!")
else:
    print("Ops! A resposta correta é {answers[question_num]}")

question_num += 1

print("========"*50)
print("Resultado!")
print("========"*50)

print("Respostas:")

for answer in answers:
    print(answers, end=" ")
print()

print("Seus palpites:",end=" ")

for guess in guesses:
    print(guess, end=" ")
print()

score = int((score/len(answers))*100)

print(f"Sua pontuação: {score}%")

