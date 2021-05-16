import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def start(update, context):
    logger.info("Se ha iniciado el bot.")
    name = update.message.chat["first_name"]
    update.message.reply_text(
        f"¡Hola, {name} \U0001F44B!, un gusto tenerte por acá. \n Digita /help para obtener ayuda sobre el uso del bot.")


def help(update, context):
    name = update.message.chat["first_name"]
    text = f"Hola, {name}. Este bot posee tres funciones: "
    rr = f"1. /rr, Esta función recibe los coeficientes de un polinomio característico de una relación de recurrencia y muestra cuál sería la forma de la solución."
    examplerr = f"Ej.: f(n) = -1/2*f(n-1) + 1/2*f(n-2) con f_0 = 3 y f_1 = -3/2 \n Es digitado como: \n [1, 0.5,-0.5] \n casos base: \n [3,-1.5] \n El i sería:\n 0"
    fib = f"2. /fib, Busca una subsecuencia que pueda considerarse como una sucesión de Fibonacci, a partir de una secuencia ingresada por el usuario. La secuencia ingresada debe consistir de números enteros ordenados de menor a mayor y separados por espacios."
    examplefib = f"Ej: 2 3 4 5 7 11 13 18 22 29"
    grafo = f"3. /grafo, el usuario digita 3 números: El número de vértices V, número de aristas E y máximo de aristas por vértice K. EL bot crea un grafo simple no dirigido con V vértices, y E aristas asignadas aleatoriamente, de tal modo que ningún vértice tenga un grado mayor a K."
    menut = f"4. /menu, Este comando le permite ejecutar los comandos anteriores a través de botones interactivos."
    cancel = f"5. /cancel, Detiene el proceso que se este realizando."
    update.message.reply_text(text)
    update.message.reply_text(rr)
    update.message.reply_text(examplerr)
    update.message.reply_text(fib)
    update.message.reply_text(examplefib)
    update.message.reply_text(grafo)
    update.message.reply_text(menut)
    update.message.reply_text(cancel)


def menu(update, context):
    name = update.message.chat["first_name"]
    opciones = [[InlineKeyboardButton("Relación de recurrencia", callback_data="rr")],
                [InlineKeyboardButton("Fibonacci", callback_data="fib")],
                [InlineKeyboardButton("Generar grafo", callback_data="grafo")]]
    reply_markup = InlineKeyboardMarkup(opciones)
    text = f"Hola {name}, estos las funciones que puedo ejecutar:"
    update.message.reply_text(text, reply_markup=reply_markup)
