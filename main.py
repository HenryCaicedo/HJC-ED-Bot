from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
import help
import graph
import rr

def main():
    # TOKEN CAMILO = 1664245450:AAEh6R8xK_iSJ58-TQzI144h_xvQZyRMNY0
    # Establecemos una conexión entre nuestro programa y el bot.
    updater = Updater("TOKEN", use_context=True)  # Insertemos el Token del bot.
    dp = updater.dispatcher
    
    # Establecer los comandos que ejecutará el bot.
    dp.add_handler(CommandHandler("start", help.start))
    dp.add_handler(CommandHandler("help", help.help))

    dp.add_handler(CallbackQueryHandler(help.menu, pattern="RR"))
    dp.add_handler(CallbackQueryHandler(help.menu, pattern="fibonacci"))

    dp.add_handler(CommandHandler("fibonacci", help.fibonacci))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler("sec",rr.input_command_secuencia),
            CallbackQueryHandler(callback = rr.input_callback_secuencia, pattern="sec")
        ],
        states = {
            rr.INPUT_LISTA: [MessageHandler(Filters.text, rr.input_polinomio)],
            rr.INPUT_CI: [MessageHandler(Filters.text, rr.input_ci)],
            rr.INPUT_I: [MessageHandler(Filters.text, rr.input_i0)],
        },
        fallbacks = [],
    ))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler("grafo", graph.input_command_grafo),
            CallbackQueryHandler(callback = graph.input_callback_grafo, pattern="grafo")
        ],
        states = {
            graph.INPUT_VERTICES: [MessageHandler(Filters.text, graph.input_vertices)],
            graph.INPUT_ARISTAS: [MessageHandler(Filters.text, graph.input_aristas)],
            graph.INPUT_K: [MessageHandler(Filters.text, graph.input_k)],
        },
        fallbacks = [],
    ))
    

    # Iniciamos el bot.
    updater.start_polling()
    # Mantener al bot ejecutándose hasta que ocurra una interrupción.
    updater.idle()

if __name__ == '__main__':
    main()