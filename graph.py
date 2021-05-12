import networkx as nx
import random
import os
import matplotlib.pyplot as plt
from telegram.ext import ConversationHandler

INPUT_VERTICES = 0
INPUT_ARISTAS = 1
INPUT_K = 2

vertices = 0
aristas = 0
k = 0


def input_aristas(update, context):
    global aristas
    aristas = int(update.message.text)
    update.message.reply_text(
        f"Digite k (Resticción de aristas por vertice): ")
    return INPUT_K


def input_k(update, context):
    global k
    k = int(update.message.text)
    dibujar_grafo(update, vertices, aristas, k)
    chat_id = update.message.chat_id
    filename = 'grafo.png'
    context.bot.send_photo(chat_id=chat_id, photo=open(filename, 'rb'))
    os.unlink(filename)
    return ConversationHandler.END


def input_vertices(update, context):
    global vertices
    vertices = int(update.message.text)
    update.message.reply_text(f"Digite el número de aristas: ")
    return INPUT_ARISTAS


def input_command_grafo(update, context):
    update.message.reply_text(f"Digite el número de vertices: ")
    return INPUT_VERTICES


def input_callback_grafo(update, context):
    update.callback_query.message.edit_text("Digite el número de vertices:")
    return INPUT_VERTICES


def dibujar_grafo(update, vertices, aristas, k):
    if aristas > (vertices/2)*k or aristas > (vertices/2)*(vertices-1):
        update.message.reply_text(f"El número de vertices ¡No es valido dado!")
        return

    G = nx.Graph()
    A = []
    edges = []

    for i in range(0, vertices):
        G.add_node(i)
        A.append(0)

    for i in range(0, aristas):
        while True:
            nodo1 = random.randint(0, vertices-1)
            nodo2 = random.randint(0, vertices-1)
            if nodo1 != nodo2 and A[nodo1] < k and A[nodo2] < k and (nodo1, nodo2) not in edges and (nodo2, nodo1) not in edges:
                A[nodo1] += 1
                A[nodo2] += 1
                edges.append((nodo1, nodo2))
                print(A)
                break

    print(edges)
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.savefig('grafo.png')
