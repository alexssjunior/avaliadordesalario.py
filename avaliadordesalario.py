#o codigo a seguir analisa o salario descrito e retorna que tipo de dev a pessoa é.

salario = float(input("informe o salario:"))

if salario <=3000:
    print("programador junior")
elif salario > 3000 and salario <= 6000:
    print("programador pleno")
elif salario >6000 and salario <=15000:
    print("programador senior")
else:
    print("gerente de projetos")
    