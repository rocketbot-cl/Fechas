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
import locale

"""
    Obtengo el modulo que fueron invocados
"""

module = GetParams("module")

if module == "now":
    date = GetParams("date")
    out = GetParams("out")

if module == "dateFormat":
    date = GetParams("date")
    input_ = GetParams("in")
    output = GetParams("out")
    custom_out = GetParams("custom_out")
    custom_in = GetParams("custom_in")
    result = GetParams("result")

    try:
        if "%d de %B del %Y" in [output, input_]:
            locale.setlocale(locale.LC_ALL, '')
            datetime_format = datetime.datetime.strptime(date, input_)
            date = datetime_format.strftime(output)

        else:
            try:
                locale.setlocale(locale.LC_ALL, 'en_US')
            except locale.Error:
                pass

            if not input_:
                input_ = custom_in
            if not output:
                output = custom_out

            datetime_format = datetime.datetime.strptime(date, input_)
            print(date)
            date = datetime_format.strftime(output)

        if result:
            SetVar(result, date)
    
    except ValueError:
        PrintException()
        raise Exception("The selected format does not match with your date")

    except Exception as e:
        PrintException()
        raise e

    
if module == "weekDay":
    date = GetParams("date")
    input_ = GetParams("in")
    result = GetParams("result")
    try:
        if "%d de %B del %Y" in [input_]:
            locale.setlocale(locale.LC_ALL, '')
            datetime_format = datetime.datetime.strptime(date, input_)
        else:
            try:
                locale.setlocale(locale.LC_ALL, 'en_US')
            except locale.Error:
                pass
            if not input_:
                input_ = custom_in
            datetime_format = datetime.datetime.strptime(date, input_)
            weekday_date = datetime_format.weekday()
        SetVar(result, weekday_date)

    except Exception as e:
        PrintException()
        raise e


