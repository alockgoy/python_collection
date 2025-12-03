def vigenere_encrypt(plaintext, keyword):
    ciphertext = []
    keyword_repeated = (keyword * (len(plaintext) // len(keyword))) + keyword[:len(plaintext) % len(keyword)]

    for p, k in zip(plaintext, keyword_repeated):
        if p.isalpha():
            shift = ord(k.lower()) - ord('a')  # Obtiene el desplazamiento de la letra clave
            if p.islower():
                encrypted_char = chr(((ord(p) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(p) - ord('A') + shift) % 26) + ord('A'))
            ciphertext.append(encrypted_char)
        else:
            # Si el carácter no es una letra, se mantiene tal cual (como espacios, signos de puntuación, etc.)
            ciphertext.append(p)

    return ''.join(ciphertext)

# Solicitar inputs al usuario
message = input("Ingresa el mensaje a cifrar: ")
keyword = input("Ingresa la palabra clave: ")

# Cifrar el mensaje con Vigenère
encrypted_message = vigenere_encrypt(message, keyword)

print(f"Mensaje cifrado: {encrypted_message}")
