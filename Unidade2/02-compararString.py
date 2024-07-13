# strings podem ser comparadas com o operador de igualdade (==) ou desigualdade (!=)
# exemplo de login

usuario = "admin"
senha = "abacaxi"

attUsuario = input("Digite o usuário: ")
attSenha = input("Digite a senha: ")

if attUsuario == usuario and attSenha == senha:
    print("Login efetuado com sucesso")
else:
    print("Usuário ou senha incorretos")