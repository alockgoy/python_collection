def vigenere_decrypt(ciphertext, keyword):
    plaintext = []
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword))) + keyword[:len(ciphertext) % len(keyword)]

    for c, k in zip(ciphertext, keyword_repeated):
        if c.isalpha():
            shift = ord(k.lower()) - ord('a')  # Obtiene el desplazamiento de la letra clave
            if c.islower():
                decrypted_char = chr(((ord(c) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(c) - ord('A') - shift) % 26) + ord('A'))
            plaintext.append(decrypted_char)
        else:
            # Si el carácter no es una letra, se mantiene tal cual (como espacios, signos de puntuación, etc.)
            plaintext.append(c)

    return ''.join(plaintext)

# Solicitar inputs al usuario
ciphertext = input("Ingresa el mensaje cifrado: ")
keyword = input("Ingresa la palabra clave: ")

# Descifrar el mensaje con Vigenère
decrypted_message = vigenere_decrypt(ciphertext, keyword)

print(f"Mensaje descifrado: {decrypted_message}")
