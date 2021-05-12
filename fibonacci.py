from telegram.ext.conversationhandler import ConversationHandler


INPUT_FIB = 0
lista = []
posiblesListas = []

def input_command_fibonacci(update, context):
    update.message.reply_text(f"Digite la serie de números:")
    return INPUT_FIB


def input_callback_fibonacci(update, context):
    update.callback_query.message.edit_text("Digite la serie de números:")
    return INPUT_FIB


def input_serie(update, context):
    try:
        global lista
        serie = update.message.text
        lista = list(map(int, serie.strip().split()))[:len(serie.strip().split())]
        resultado = encontrar_fib(lista)
        update.message.reply_text('Lista: '+str(resultado))
        return ConversationHandler.END
    except (IndexError, ValueError):
        update.message.reply_text('Por favor utiliza dos numeros')

def encontrar_fib(lista):
    for index in range(0, len(lista)-2):
        global posiblesListas
        temp = secuencia(index)
        posiblesListas = posiblesListas + temp
    return posiblesListas


def ya_esta_en_la_lista(temp):
    s2 = len(temp)
    for i in posiblesListas:
        s1 = len(i)
        if(i[s1-1] == temp[s2-1] and i[s1-2] == temp[s2-2] and i[s1-3] == temp[s2-3]):
            return True
    return False


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


def completar_secuencia(temp, k):
    if(k == len(lista)):
        return
    next_num = temp[len(temp)-2] + temp[len(temp)-1]
    aux = []
    for index in range(k+1, len(lista)):
        if lista[index] == next_num:
            aux = aux + completar_secuencia(temp + [next_num], index)
            return aux
    return temp

# Ej: /fibonacci 2,3,4,5,7,11,13,18,22,29
# lista = [2,3,4,5,7,11,13,18,22,29]
# encontrarFib(lista)
