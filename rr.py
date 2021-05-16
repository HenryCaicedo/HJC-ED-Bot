import numpy as np
from telegram.ext.conversationhandler import ConversationHandler


INPUT_LISTA, INPUT_CI, INPUT_I = range(3)

lista = []
ci = []
i0 = 0


def validar_poli(update, context):
    update.message.reply_text(
        f"¡La entrada no es valida!, Comenzemos denuevo.")
    update.message.reply_text(
        f"Digite los coeficientes del polinomio caracteristico en forma de lista: ")
    return INPUT_LISTA

def validar_ci(update, context):
    update.message.reply_text(
        f"¡La entrada no es valida!, Comenzemos denuevo.")
    update.message.reply_text(
                f"Digite los casos base en forma de lista: ")
    return INPUT_CI

def input_i0(update, context):
    global i
    i = int(update.message.text)
    update.message.reply_text(f"f(n) = {solucionar_rr(lista,ci,i)}")
    return ConversationHandler.END

def input_ci(update, context):
    global ci
    try:
        ci = eval(update.message.text)
        if(type(ci) is list):
            sw = True
            for i in ci:
                try:
                    j = float(i)
                except:
                    sw = False
            if sw:
                if(len(ci) != len(lista)-1):
                    validar_ci(update,context)
                else:
                    update.message.reply_text(f"Digite i0:")
                    return INPUT_I
            else:
                validar_ci(update, context)
        else:
            validar_ci(update, context)
    except:
        validar_ci(update, context)


def input_polinomio(update, context):
    global lista
    try:
        lista = eval(update.message.text)
        if(type(lista) is list):
            sw = True
            for i in lista:
                try:
                    j = float(i)
                except:
                    sw = False
            if sw:
                update.message.reply_text(
                f"Digite los casos base en forma de lista: ")
                return INPUT_CI
            else:
                validar_poli(update, context)
        else:
            validar_poli(update, context)
    except Exception as e:
        validar_poli(update, context)


def input_command_secuencia(update, context):
    update.message.reply_text(
        f"Digite los coeficientes del polinomio caracteristico en forma de lista: ")
    return INPUT_LISTA


def input_callback_secuencia(update, context):
    update.callback_query.message.edit_text(
        "Digite los coeficientes del polinomio caracteristico en forma de lista: ")
    return INPUT_LISTA


def solucionar_rr(rr, ci, i0):
    R = np.roots(rr)
    l = len(ci)
    MR = np.zeros((l, len(R)))

    for i in range(0, l):
        k = 0
        for j in R:
            MR[i, k] = j**(i0+i)
            k += 1
    b = np.linalg.lstsq(MR, ci, rcond=None)[0]
    sol = ""
    for i in range(0, len(b)):
        if i != 0:
            sol = sol+" + "+str(round(b[i], 5))+"*"+str(R[i])+"^n"
        else:
            sol = sol+str(round(b[i], 5))+"*"+str(R[i])+"^n"

    return sol
