def pedir_confirmacion(prompt, reintentos=4, recordatorio='por favor intente nuevamente'):
    while True:
        ok = input(prompt)
        if ok in ("s", "S", "si", "Si"):
            return True
        if ok in ("n","N","No","no"):
            return False
        reintentos=reintentos-1
        if reintentos < 0:
            raise ValueError('respuesta de usuario inválida')
        print(recordatorio)

