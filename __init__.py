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

locale.setlocale(locale.LC_ALL, 'en_US')
module = GetParams("module")

if module == "dateFormat":
    date = GetParams("date")
    input_ = GetParams("in")
    output = GetParams("out")
    result = GetParams("result")

    try:
        if "%d de %B del %Y" in [output, input_]:
            locale.setlocale(locale.LC_ALL, '')
            datetime_format = datetime.datetime.strptime(date, input_)
            date = datetime_format.strftime(output)
            
        else:
            print('aaa',input_)
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

    


