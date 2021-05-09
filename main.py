from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from config import TOKEN
import bot


def main():
    # Establecemos una conexión entre nuestro programa y el bot.
    updater = Updater(TOKEN, use_context=True)  # Insertemos el Token del bot.
    dp = updater.dispatcher

    # Establecer los comandos que ejecutará el bot.
    dp.add_handler(CommandHandler("start", bot.start))
    dp.add_handler(CommandHandler("ayuda", bot.ayuda))
    dp.add_handler(CallbackQueryHandler(bot.menu, pattern="op1"))
    dp.add_handler(CallbackQueryHandler(bot.menu, pattern="op2"))
    dp.add_handler(CallbackQueryHandler(bot.menu, pattern="op3"))
    dp.add_handler(CallbackQueryHandler(bot.menu, pattern="op4"))
    dp.add_handler(CommandHandler("doc", bot.documento))
    dp.add_handler(CommandHandler("img", bot.image))
    dp.add_handler(CommandHandler("grafo", bot.grafo))
    dp.add_handler(CommandHandler("sec", bot.secuencia))
    dp.add_handler(CommandHandler("fibonacci", bot.fibonacci))

    # Iniciamos el bot.
    updater.start_polling()
    # Mantener al bot ejecutándose hasta que ocurra una interrupción.
    updater.idle()

if __name__ == '__main__':
    main()
