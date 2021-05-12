import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def start(update, context):
  logger.info("Se ha iniciado el bot.")
  name = update.message.chat["first_name"]
  update.message.reply_text(f"¡Hola, {name} \U0001F44B!, un gusto tenerte por acá.")
  menu(update, context)

def help(update,context):
  menu(update,context)

def menu(update, context):
  name = update.message.chat["first_name"]
  opciones = [[InlineKeyboardButton("Relación de recurrencia", callback_data="sec")],
                [InlineKeyboardButton("Fibonacci", callback_data="fib")],
                [InlineKeyboardButton("Generar grafo", callback_data="grafo")]]
  reply_markup = InlineKeyboardMarkup(opciones)
  text = f"Hola {name}, estos los comandos que puedo ejecutar:"
  update.message.reply_text(text, reply_markup=reply_markup)







