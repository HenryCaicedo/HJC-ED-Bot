
def fibonacci(update, context):
    try:
        lista = context.args[0].split(",")
        lista = [int(i) for i in lista]
        resultado = encontrarFib(lista)
        update.message.reply_text('Lista: '+str(resultado)) 
    except (IndexError, ValueError):
        update.message.reply_text('Por favor utiliza dos numeros') 

# FIBONACCI

#Ej: /fibonacci 2,3,4,5,7,11,13,18,22,29

def encontrarFib(lista):
  for index in range(0, len(lista)-2):
    global posiblesListas
    temp = secuencia(index)
    posiblesListas = posiblesListas + temp
  return posiblesListas

def yaEstaEnLaLista(temp):
  s2 = len(temp)
  for i in posiblesListas:
    s1 = len(i)
    if(i[s1-1]==temp[s2-1] and i[s1-2]==temp[s2-2] and i[s1-3]==temp[s2-3]):
      return True
  return False

def secuencia(i):
  listasPosibles = []
  for index in range(i+1, len(lista)-1):
    nextNum = lista[i] + lista[index]
    for k in range(index+1, len(lista)):
      if lista[k]==nextNum:
        aux = [lista[i], lista[index], lista[k]]
        temp = completarSecuencia(aux,k)
        if(yaEstaEnLaLista(temp)==False):
          listasPosibles.append(temp)
  return listasPosibles

def completarSecuencia(temp,k):
  if(k==len(lista)):
    return    
  nextNum = temp[len(temp)-2] + temp[len(temp)-1]
  aux = []
  for index in range(k+1, len(lista)):
    if lista[index]==nextNum:
      aux = aux + completarSecuencia(temp + [nextNum],index)
      return aux
  return temp

lista = [2,3,4,5,7,11,13,18,22,29]

posiblesListas = []

encontrarFib(lista)
# END FIBONACCI