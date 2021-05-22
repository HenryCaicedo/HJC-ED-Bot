from telegram.ext.conversationhandler import ConversationHandler

INPUT_FIB = 0
lista = []
posiblesListas = []

def input_command_fibonacci(update, context):
    update.message.reply_text(f"Digite la serie de números, separados por espacios:")
    return INPUT_FIB

def input_callback_fibonacci(update, context):
    update.callback_query.message.edit_text("Digite la serie de números, separados por espacios:")
    return INPUT_FIB

def input_serie(update, context):
    try:
        global lista
        serie = update.message.text
        lista = list(map(int, serie.strip().split()))[:len(serie.strip().split())]

        if(listaOrdenada(lista)==False):
            raise ValueError('La lista no está ordenada')

        resultado = encontrar_fib(lista)
        if len(resultado)<3:
            update.message.reply_text('No se encontraron subsecuencias de Fibonacci en la secuencia ingresada.')
        else:
            update.message.reply_text('Lista: '+str(resultado))
        return ConversationHandler.END
    except (IndexError, ValueError):
        update.message.reply_text('Se produjo un error al leer los datos. Recuerda ingresar números enteros ordenados de menor a mayor y separados por espacios.\n\nEj: 2 3 4 5 7 11 13 18 22 29')
        update.message.reply_text('Intententemos de nuevo.\nDigite la serie de números, separados por espacios:')


# Valida si la lista ingresada está ordenada de menor a mayor
def listaOrdenada(lista):
    aux = lista[:]
    aux.sort()
    if(lista == aux):
        return True
    return False

# Escoge la secuencia de mayor longitud
def escogerSecuencia(lista):
    largestLista = []
    for i in lista:
        if len(i)>len(largestLista):
            largestLista=i
    return largestLista

# Encuentra todas las subsecuencias de Fibonacci
def encontrar_fib(lista):
    global posiblesListas
    posiblesListas=[]
    for index in range(0, len(lista)-2):
        temp = secuencia(index)
        posiblesListas = posiblesListas + temp
    resultado = escogerSecuencia(posiblesListas)
    return resultado

# Verifica que no haya sub-secuencias repetidas
# en la lista de subsecuencias
def ya_esta_en_la_lista(temp):
    s2 = len(temp)
    for i in posiblesListas:
        s1 = len(i)
        if(i[s1-1] == temp[s2-1] and i[s1-2] == temp[s2-2] and i[s1-3] == temp[s2-3]):
            return True
    return False

# Encuentra todas las subsecuencias a partir de cierto elemento de la secuencia
def secuencia(i):
    listas_posibles = []
    for index in range(i+1, len(lista)-1):
        next_num = lista[i] + lista[index]
        for k in range(index+1, len(lista)):
            if lista[k] == next_num:
                aux = [lista[i], lista[index], lista[k]]
                temp = completar_secuencia(aux, k)
                if(ya_esta_en_la_lista(temp) == False):
                    listas_posibles.append(temp)
    return listas_posibles

# Completa un subsecuencia de 3 elementos en caso de que pueda extenderse más
def completar_secuencia(temp, k):
    if(k == len(lista)):
        return
    next_num = temp[len(temp)-2] + temp[len(temp)-1]
    aux = []
    for index in range(k+1, len(lista)):
        if lista[index] <= next_num:
            if lista[index] == next_num:
                aux = aux + completar_secuencia(temp + [next_num], index)
                return aux
        else:
            break
    return temp

# Ej: /fibonacci 2,3,4,5,7,11,13,18,22,29
# lista = [2,3,4,5,7,11,13,18,22,29]
# encontrarFib(lista)
