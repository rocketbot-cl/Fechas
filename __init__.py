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

try:      

    if module == "dateFormat":
        date = GetParams("date")
        input_ = GetParams("in")
        output = GetParams("out")
        custom_out = GetParams("custom_out")
        custom_in = GetParams("custom_in")
        result = GetParams("result")

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

            datetime_format = datetime.datetime.now()
            if date not in ["today", "hoy", "now", "ahora"]:
                datetime_format = datetime.datetime.strptime(date, input_)
            print(date)
            date = datetime_format.strftime(output)

        if result:
            SetVar(result, date)

    
    if module == "weekDay":
        date = GetParams("date")
        input_ = GetParams("in")
        result = GetParams("result")

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


    if module == "calculateDate":
        date = GetParams("date")
        input_ = GetParams("in")
        result = GetParams("result")
        type_of_date = GetParams("type_of_date")
        type_operation = GetParams("type_operation")
        amount = GetParams("amount")
        
        from datetime import timedelta
        from dateutil import relativedelta
        import dateutil
        import dateutil.relativedelta


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

            datetime_format = datetime.datetime.now()
            if date not in ["today", "hoy", "now", "ahora"]:
                datetime_format = datetime.datetime.strptime(date, input_)
            args = {type_of_date: int(amount)}
            final_date = datetime_format + relativedelta.relativedelta(**args)
            SetVar(result, final_date.strftime(input_))

except Exception as e:
    PrintException()
    raise e
