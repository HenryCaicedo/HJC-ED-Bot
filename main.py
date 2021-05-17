from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
import help
import graph
import rr
import fibonacci

def cancel(update, context):
    update.message.reply_text(f"El proceso se ha detenido")
    return ConversationHandler.END

def main():
    # TOKEN CAMILO = 1664245450:AAEh6R8xK_iSJ58-TQzI144h_xvQZyRMNY0
    # TOKEN HENRY = 1600741375:AAGjGuD_jOvTQvw7qbqFcGF9zuQTM3OztA8
    # Establecemos una conexión entre nuestro programa y el bot.
    updater = Updater("1664245450:AAEh6R8xK_iSJ58-TQzI144h_xvQZyRMNY0", use_context=True)  # Insertemos el Token del bot.
    dp = updater.dispatcher
    
    # Establecer los comandos que ejecutará el bot.
    dp.add_handler(CommandHandler("start", help.start))
    dp.add_handler(CommandHandler("ayuda", help.help))
    dp.add_handler(CommandHandler("menu", help.menu))


    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler("fib", fibonacci.input_command_fibonacci),
            CallbackQueryHandler(callback = fibonacci.input_callback_fibonacci, pattern="fib")
        ],
        states = {
            fibonacci.INPUT_FIB: [MessageHandler(Filters.text, fibonacci.input_serie)],
        },
        fallbacks = [CommandHandler("cancel",cancel)],
    ))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler("rr",rr.input_command_secuencia),
            CallbackQueryHandler(callback = rr.input_callback_secuencia, pattern="rr")
        ],
        states = {
            rr.INPUT_LISTA: [MessageHandler(Filters.text& ~Filters.command, rr.input_polinomio)],
            rr.INPUT_CI: [MessageHandler(Filters.text& ~Filters.command, rr.input_ci)],
            rr.INPUT_I: [MessageHandler(Filters.regex(r'^\d+$')& ~Filters.command, rr.input_i0)],
        },
        fallbacks = [CommandHandler("cancel",cancel)],
    ))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler("grafo", graph.input_command_grafo),
            CallbackQueryHandler(callback = graph.input_callback_grafo, pattern="grafo")
        ],
        states = {
            graph.INPUT_VERTICES: [MessageHandler(Filters.regex(r'^\d+$') & ~Filters.command, graph.input_vertices)],
            graph.INPUT_ARISTAS: [MessageHandler(Filters.regex(r'^\d+$')& ~Filters.command, graph.input_aristas)],
            graph.INPUT_K: [MessageHandler(Filters.regex(r'^\d+$')& ~Filters.command, graph.input_k)],
        },
        fallbacks = [CommandHandler("cancel",cancel)],
    ))

    
    

    # Iniciamos el bot.
    updater.start_polling()
    # Mantener al bot ejecutándose hasta que ocurra una interrupción.
    updater.idle()

if __name__ == '__main__':
    main()