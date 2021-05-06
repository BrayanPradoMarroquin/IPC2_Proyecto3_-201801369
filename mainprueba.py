lista = ["15", "15", "52", "86", "17", "85", "86"]

repetido=[]
archivo=[]
pila=[]
class fechas:
  def __init__(self, fecha, cantidad):
      self.fecha = fecha
      self.cantidad = cantidad

for n in lista:
    if n not in archivo:
        archivo.append(n)
    else:
        repetido.append(n)

for ar in archivo:
    cont=0
    for l in lista:
        if ar == l :
            cont+=1
    pila.append(fechas(ar, cont))

for pi in pila:
    print(str(pi.fecha)+" -> "+str(pi.cantidad))
