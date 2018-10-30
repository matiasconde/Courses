def ventadechurros(clase, *argumentos, **claves):
    print("Sr. tiene churros tipo: ",clase)
    print("SI!!, tengo de esa ",clase)
    for arg in argumentos:
        print(arg)
    print("_"*10)
    claves = sorted(claves.keys())
    for c in claves:
        print(c, ":",claves[c])

ventadechurros("rellenos","delicioso","muy esquisito",
               tipo="bañado",adicional="chocolate",
               cliente="pepe",vendedor="juanch")

def f(edaddelgato, estado='cagado', tipo='niño'):
    print("la edad del gato es: ",edaddelgato)
    print("el estado del gato es: ",estado)
    print("el tipo de gato es: ", tipo)

f(25)
f('no cagaado')
#f(edaddelgato=2,'limpio', 'adulto') #error las nombradas no van antes de las posicionales
f(2,'limpio','adulto')
f(edaddelgato=19)
f(edaddelgato=10,estado='limpio')
#f(estado='limpio',10)             #error idem
f(estado='limpio',edaddelgato=10)
f('limpio','caca')
f('miñ',estado='cagado')