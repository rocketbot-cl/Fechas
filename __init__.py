# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import datetime

"""
    Obtengo el modulo que fueron invocados
"""


module = GetParams("module")

if module == "dateFormat":
    date = GetParams("date")
    format = GetParams("format")
    type = GetParams("type")
    result = GetParams("result")

    separators = ["-", "-", "."]

    for sep_date in separators:
        if sep_date in date:
            sep = sep_date

    try:
        if format == "word":
            date = date.split(sep)
            month = datetime.date(int(date[2]), int(date[1]), int(date[0])).strftime('%B')
            date = "{} de {} del {}".format(date[0], month, date[2])
        else:
            date = date.replace(sep, format)

        if type == "american":
            if format != "word":
                date = date.split(format)
                day = date[0]
                date[0] = date[1]
                date[1] = day
                date = format.join(date)

        elif type == "invert":
            if format != "word":
                date = date.split(format)
                date.reverse()
                date = format.join(date)

        if result:
            SetVar(result, date)

    except Exception as e:
        PrintException()
        raise e







