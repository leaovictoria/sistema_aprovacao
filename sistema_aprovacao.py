nome = input("Qual é o nome do aluno?")
nota = int(input("Qual é a nota do aluno?"))
frequencia = float(input("Qual é a frequência do aluno nas aulas?"))

if nota >= 7 and frequencia >= 75:
    print("Aluno,", nome, "Aprovado")
elif nota >= 5 and frequencia >= 75:
   print("Aluno,", nome, "Recuperação")
else:
    print("Aluno,", nome, "Reprovado")
