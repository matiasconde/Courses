import string

def remover_puntuacion(texto):
    texto_sin_puntuacion = ""
    for _ in texto:
        if _ not in string.punctuation:
            texto_sin_puntuacion += _
    return texto_sin_puntuacion

words = str(input("ingrese texto: ",))

resultado = remover_puntuacion(words).split()

print(resultado)

