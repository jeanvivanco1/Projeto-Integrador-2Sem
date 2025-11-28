import random
import string
import re

def check_password_strength(password):
    """Verifica a força de uma senha e retorna um score e feedback."""
    score = 0
    feedback = []

    # 1. Comprimento
    if len(password) >= 12:
        score += 2
        feedback.append("Comprimento: Excelente (>= 12 caracteres)")
    elif len(password) >= 8:
        score += 1
        feedback.append("Comprimento: Bom (>= 8 caracteres)")
    else:
        feedback.append("Comprimento: Fraco (Recomendado: 8+ caracteres)")

    # 2. Letras maiúsculas
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("Maiúsculas: Presente")
    else:
        feedback.append("Maiúsculas: Ausente (Recomendado: Incluir)")

    # 3. Letras minúsculas
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("Minúsculas: Presente")
    else:
        feedback.append("Minúsculas: Ausente (Recomendado: Incluir)")

    # 4. Números
    if re.search(r"\d", password):
        score += 1
        feedback.append("Números: Presente")
    else:
        feedback.append("Números: Ausente (Recomendado: Incluir)")

    # 5. Símbolos
    if re.search(r"[!@#$%^&*()_+=\-[\]{}|\\:;\"'<>,.?/`~]", password):
        score += 1
        feedback.append("Símbolos: Presente")
    else:
        feedback.append("Símbolos: Ausente (Recomendado: Incluir)")

    # Classificação final
    if score >= 5:
        strength = "Muito Forte"
    elif score == 4:
        strength = "Forte"
    elif score == 3:
        strength = "Moderada"
    else:
        strength = "Fraca"

    return strength, feedback

def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """Gera uma senha aleatória e segura."""
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("--- Password Guardian: Ferramenta de Segurança de Senhas ---")
    
    while True:
        print("\nSelecione uma opção:")
        print("1. Verificar Força da Senha")
        print("2. Gerar Senha Segura")
        print("3. Sair")
        
        choice = input("Opção: ")
        
        if choice == '1':
            password = input("Digite a senha para verificar: ")
            strength, feedback = check_password_strength(password)
            print(f"\nResultado da Verificação:")
            print(f"Força: {strength}")
            print("Detalhes:")
            for item in feedback:
                print(f"- {item}")
        
        elif choice == '2':
            try:
                length = int(input("Comprimento da senha (padrão 16): ") or 16)
                use_upper = input("Incluir letras maiúsculas? (s/n, padrão s): ").lower() in ('s', '')
                use_lower = input("Incluir letras minúsculas? (s/n, padrão s): ").lower() in ('s', '')
                use_digits = input("Incluir números? (s/n, padrão s): ").lower() in ('s', '')
                use_symbols = input("Incluir símbolos? (s/n, padrão s): ").lower() in ('s', '')
                
                generated_password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
                print(f"\nSenha Gerada: {generated_password}")
                
                # Verifica a força da senha gerada
                strength, _ = check_password_strength(generated_password)
                print(f"Força Verificada: {strength}")
                
            except ValueError as e:
                print(f"Erro: {e}")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
                
        elif choice == '3':
            print("Obrigado por usar o Password Guardian. Até mais!")
            break
            
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
