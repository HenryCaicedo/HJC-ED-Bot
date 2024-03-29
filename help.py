import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Función de iniciar el bot
def start(update, context):
    logger.info("Se ha iniciado el bot.")
    name = update.message.chat["first_name"]
    update.message.reply_text(
        f"¡Hola, {name} \U0001F44B!. Bienvenid@ a HJC Bot.\nDigita /ayuda para ver información acerca del funcionamiento del bot.")


# Función de ayuda
def help(update, context):
    text = f"Hola, este bot posee tres funciones: "
    rr = f"1. /rr, Recibe los coeficientes de un polinomio característico de una relación de recurrencia y muestra cuál sería la forma de la solución."
    examplerr = f"Ej: f(n) = -1/2*f(n-1) + 1/2*f(n-2) con f_0 = 3 y f_1 = -3/2\nEs digitado como:\n[1,0.5,-0.5]\nCasos base:\n[3,-1.5]\nEl i sería:\n0"
    fib = f"2. /fib, Busca una subsecuencia que pueda considerarse como una sucesión de Fibonacci, a partir de una secuencia ingresada por el usuario.\nLa secuencia ingresada debe consistir de números enteros ordenados de menor a mayor y separados por espacios."
    examplefib = f"Ej: 2 3 4 5 7 11 13 18 22 29"
    grafo = f"3. /grafo, Crea un grafo simple no dirigido con V vértices, y E aristas asignadas aleatoriamente, de tal modo que ningún vértice tenga un grado mayor a K.\nSe deben digitar 3 números: El número de vértices 'V', número de aristas 'E' y el máximo número de aristas por vértice 'K'. "
    menut = f"4. /menu, Permite ejecutar las funciones anteriores a través de un menú interactivo."
    cancel = f"5. /cancel, Detiene el proceso que se esté realizando."
    try:     
        update.message.reply_text(text)
        update.message.reply_text(rr)
        update.message.reply_text(examplerr)
        update.message.reply_text(fib)
        update.message.reply_text(examplefib)
        update.message.reply_text(grafo)
        update.message.reply_text(menut)
        update.message.reply_text(cancel)
    except:
        update.callback_query.message.edit_text(text)        
        context.bot.send_message(chat_id=update.callback_query.from_user.id,text = rr)
        context.bot.send_message(chat_id=update.callback_query.from_user.id,text = examplerr)
        context.bot.send_message(chat_id=update.callback_query.from_user.id,text = fib)
        context.bot.send_message(chat_id=update.callback_query.from_user.id,text = examplefib)
        context.bot.send_message(chat_id=update.callback_query.from_user.id,text = grafo)
        context.bot.send_message(chat_id=update.callback_query.from_user.id,text = menut)
        context.bot.send_message(chat_id=update.callback_query.from_user.id,text = cancel)
   


# Mostrar menú interactivo
def menu(update, context):
    name = update.message.chat["first_name"]
    opciones = [[InlineKeyboardButton("Relación de recurrencia", callback_data="rr")],
                [InlineKeyboardButton("Fibonacci", callback_data="fib")],
                [InlineKeyboardButton("Generar grafo", callback_data="grafo")]
                ,[InlineKeyboardButton("Ayuda", callback_data="help")]]
    reply_markup = InlineKeyboardMarkup(opciones)
    text = f"Hola {name}, estos las funciones que puedo ejecutar:"
    update.message.reply_text(text, reply_markup=reply_markup)
