import logging
import networkx as nx
import random
import matplotlib.pyplot as plt
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def start(update, context):
    logger.info("Se ha iniciado el bot.")
    name = update.message.chat["first_name"]
    update.message.reply_text(f"¡Hola, {name} \U0001F44B!, un gusto tenerte por acá.")


def ayuda(update, context):
    opciones = [[InlineKeyboardButton("Punto 1", callback_data="op1")],
                [InlineKeyboardButton("secuencia", callback_data="op2")],
                [InlineKeyboardButton("Fibonacci", callback_data="op3")],
                [InlineKeyboardButton("Grafos", callback_data="op4")]]
    reply_markup = InlineKeyboardMarkup(opciones)
    name = update.message.chat["first_name"]
    logger.info(f"El usuario {name} ha solicitado ayuda.")
    text = f"Hola {name}, estos los comandos que puedo ejecutar:"
    update.message.reply_text(text, reply_markup=reply_markup)


def saludar(name, query):
    logger.info(f"El usuario {name} ha solicitado su nombre.")
    query.message.reply_text(f"Bienvenido {name}.")


def apellido(name, last_name, query):
    logger.info(f"El usuario {name} ha solicitado su apellido.")
    query.message.reply_text(f"Su apellido es: {last_name}.")



def document(chat_id, query):
    logger.info("El usuario ha solicitado un documento.")
    documento = open("src/docs/documento.pdf", "rb")
    query.message.reply_text("Se está subiendo el documento, por favor espere...")
    query.bot.send_document(chat_id=chat_id, document=documento, timeout=200)


def documento(update, context):
    logger.info("El usuario ha solicitado un documento.")
    documento = open("src/docs/documento.pdf", "rb")
    update.message.reply_text("Se está subiendo el documento, por favor espere...")
    chat_id = update.message.chat_id
    update.message.bot.sendDocument(chat_id=chat_id, document=documento, timeout=200)


def image(update, context):
    logger.info("El usuario ha solicitado una imagen.")
    img = open("src/images/imagen.jpg", "rb")
    chat_id = update.message.chat_id
    update.message.bot.sendPhoto(chat_id=chat_id, photo=img)


def grafo(update, context):
    logger.info(f"El usuario {update.message.chat['first_name']} ha solicitado un grafo.")
    text = update.message.text
    text = text.replace("/grafo ", "").strip()
    update.message.reply_text(f"Usted ha escrito: \n{text}")
    try:
        graph = eval(text)
        vertices = int(graph[0])
        aristas = int(graph[1])
        k = int(graph[2])
        update.message.reply_text(f"La cantidad de vértices son: {vertices}")
        update.message.reply_text(f"La cantidad de aristas son: {aristas}")
        update.message.reply_text(f"k es: {k}")
        dibujar_grafo(vertices, aristas, k)
        chat_id = update.message.chat_id
        context.bot.send_photo(chat_id=chat_id, photo=open('foo.png', 'rb'))
    except Exception as e:
        logger.exception("Ha ocurrido un error en los parámetros.")
        update.message.reply_text("Por favor, digite los parámetros nuevamente.")


def secuencia_prime(update, context):
    text = update.message.text
    text = text.replace("/sec ", "").strip()
    update.message.reply_text(f"Usted ha escrito: \n{text}")
    try:       
        RR = eval(text)
        update.message.reply_text(f"Digite las condiciones inciales")
        text = update.message.text
        ci = eval(text)
        update.message.reply_text(f"Digita i0:")
        text = update.message.text
        i0 = eval(text)
        update.message.reply_text(f"f(n) ={solucionar_RR(RR,ci,i0)}")
    except Exception as e:
        logger.info("Ha ocurrido un error en los parámetros.")
        update.message.reply_text("Por favor, digite los parámetros nuevamente.")


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

# GRAFO
def dibujar_grafo(V, E, K):
  if E>(V/2)*K or E>(V/2)*(V-1):
    print("Ese E está malo, salu2")
    return

  print("aqui ando")
  G = nx.Graph()
  A = []
  edges = []

  #Crear los nodos
  for i in range(0,V):
    G.add_node(i)
    A.append(0)

  for i in range(0,E):
    while True:
      nodo1 = random.randint(0, V-1)
      nodo2 = random.randint(0, V-1)
      if nodo1!=nodo2 and A[nodo1]<K and A[nodo2]<K :
        if(nodo1,nodo2) not in edges and (nodo2,nodo1) not in edges:
          A[nodo1]+=1
          A[nodo2]+=1
          edges.append((nodo1,nodo2))   
          print(A)
          break
          
  print(edges)
  G.add_edges_from(edges)
  nx.draw(G, with_labels=True, font_weight='bold')
  plt.savefig('foo.png')
# END GRAFO

#SECUENCIA
def solucionar_RR(RR, ci, i0):
  R = np.roots(RR)
  l = len(ci)
  MR = np.zeros((l,len(R)))

  for i in range(0, l):
    k = 0
    for j in R: 
      MR[i,k] = j**(i0+i)
      k+=1
  b = np.linalg.lstsq(MR,ci,rcond=None )[0]
  sol = ""
  for i in range(0,len(b)):
    if i!=0 :
      sol = sol+" + "+str(round(b[i],5))+"*"+str(R[i])+"^n"
    else:
      sol = sol+str(round(b[i],5))+"*"+str(R[i])+"^n"

  return sol
#END SECUENCIA

def menu(update, context):
    query = update.callback_query
    query.answer()
    answer = query.data
    chat_id = query.message.chat_id
    name = query.message.chat["first_name"]
    last_name = query.message.chat["last_name"]
    if answer == "op1":
        saludar(name, query)
    elif answer == "op2":
        apellido(name, last_name, query)
    elif answer == "op3":
        fibonacci(chat_id, query)
    elif answer == "op4":
        document(chat_id, query)
