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

import traceback
import os
import sys
import datetime
import locale


base_path = tmp_global_obj["basepath"] # type: ignore
cur_path = base_path + 'modules' + os.sep + 'Fechas' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from dateController import DateController # type: ignore

"""
    Obtengo el modulo que fueron invocados
"""

global myDateObject

GetParams = GetParams # type: ignore
SetVar = SetVar # type: ignore
PrintException = PrintException # type: ignore

module = GetParams("module")



def date_to_string(date, format_='%d/%m/%Y'):
    import locale
    try:
        locale.setlocale(locale.LC_ALL, 'en_US')
    except:
        locale.setlocale(locale.LC_ALL, '')
    
    
    if "%d de %B del %Y" in [format_]:
        try:
            locale.setlocale(locale.LC_ALL, 'es_ES')
        except:
            locale.setlocale(locale.LC_ALL, 'spanish')
        return date.strftime(format_)
    elif "%d %B de %Y %H:%M:%S" in [format_]:
        try:
            locale.setlocale(locale.LC_ALL, 'es_ES')
        except:
            locale.setlocale(locale.LC_ALL, 'spanish')
        return date.strftime(format_)

    return date.strftime(format_)


def string_to_date(string, format_):
    from dateController import DateController # type: ignore
    import locale
    try:
        locale.setlocale(locale.LC_ALL, 'en_US')
    except:
        locale.setlocale(locale.LC_ALL, '')
    
    if "%d de %B del %Y" in [format_]:
        try:
            locale.setlocale(locale.LC_ALL, 'es_ES')
        except:
            locale.setlocale(locale.LC_ALL, 'spanish')
        return datetime.datetime.strptime(string, format_)
    elif "%d %B de %Y %H:%M:%S" in [format_]:
        try:
            locale.setlocale(locale.LC_ALL, 'es_ES')
        except:
            locale.setlocale(locale.LC_ALL, 'spanish')
        return datetime.datetime.strptime(string, format_)
    
    if string in ["today", "hoy", "now", "ahora"]:
        return datetime.datetime.now()

    return DateController(string, format_).myDate


def number_of_day(date, input_):
    from dateController import DateController # type: ignore

    myDateObject = DateController(date, input_)
    weekday_date = myDateObject.getWeekDay()
            
    return weekday_date


def calculate_date(date, input_, amount, type_of_date):
    from dateutil import relativedelta # type: ignore
    import locale
    try:
        locale.setlocale(locale.LC_ALL, 'en_US')
    except:
        locale.setlocale(locale.LC_ALL, '')
    
    datetime_format = datetime.datetime.strptime(date, input_)


    args = {type_of_date: int(amount)}
    final_date = datetime_format + relativedelta.relativedelta(**args)
    
    
    return final_date.strftime(input_)


def get_week_number(date, input_):
    import locale
    from dateController import DateController # type: ignore
    try:
        locale.setlocale(locale.LC_ALL, 'en_US')
    except:
        locale.setlocale(locale.LC_ALL, '')
        
    datetime_format = datetime.datetime.strptime(date, input_) 
    
    datetime_format.strftime(input_)
    myDateObject = DateController(date, input_)
        
    return myDateObject.getWeekNumber()


def week_of_month(dt, input_):
    from math import ceil
    import locale

    try:
        locale.setlocale(locale.LC_ALL, 'en_US')
    except:
        locale.setlocale(locale.LC_ALL, '')

    dttime = datetime.datetime.strptime(dt, input_) 

    first_day = dttime.replace(day=1)

    dom = dttime.day
    adjusted_dom = dom + first_day.weekday()

    return int(ceil(adjusted_dom/7.0))


def resultComparation(date, date2, input_, custom_in, operation):
    from dateController import DateController # type: ignore
    
    if not input_ or input_ == "None":
        input_ = custom_in
    
    if date in ["today", "hoy", "now", "ahora"]:
        date = datetime.datetime.now().__str__()[:10]
        input_ = "%Y-%m-%d"
    
    myDateObject = DateController(date, input_)

    if date2 in ["today", "hoy", "now", "ahora"]:
        date2 = datetime.datetime.now().__str__()[:10]
        input_ = "%Y-%m-%d"

    return myDateObject.compareDate(date2, input_, operation)

def calcular_edad(fecha_nacimiento):
    
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    hoy = datetime.today()
    diferencia = relativedelta(hoy, nacimiento)
    return diferencia.years


try:
    if module == "get_birth":
        fecha_nacimiento = GetParams("date")
        result = GetParams("result")

        if not fecha_nacimiento:
            SetVar(result,"Error: The date format is not correct, it should be YYYY-MM-DD")
        else:
            try:
                edad = calcular_edad(fecha_nacimiento)
                SetVar(result, edad)
            except Exception as e:
                raise e


    if module == "dateFormat":
        date = GetParams("date")
        input_ = GetParams("in")
        output = GetParams("out")
        custom_out = GetParams("custom_out")
        custom_in = GetParams("custom_in")
        result = GetParams("result")
        

        if not input_ or input_ == "None":
            input_ = custom_in
        if not output or output == "None":
            output = custom_out
        
        date = string_to_date(date, input_)
        
        date = date_to_string(date, output)

        SetVar(result, date)

    
    if module == "weekDay":
        date = GetParams("date")
        input_ = GetParams("in")
        result = GetParams("result")
        dayone = GetParams("dayone")

        
        f_date = string_to_date(date, input_)
        f_string = date_to_string(f_date, "%d/%m/%Y")
        day = number_of_day(f_string, "%d/%m/%Y")
        
        if dayone == "True":
            day += 1

        SetVar(result, day)
        
        
    if module == "weekNumber":
        date = GetParams("date")
        input_ = GetParams("in")
        result = GetParams("result")


        f_date = string_to_date(date, input_)
        f_string = date_to_string(f_date)
        weekday_number = get_week_number(f_string, "%d/%m/%Y")

        SetVar(result, weekday_number)

    if module == "weekOfMonth":
        date = GetParams("date")
        input_ = GetParams("in")
        result = GetParams("result")

        week_number = week_of_month(date, input_)

        SetVar(result, week_number)


    if module == "calculateDate":
        date = GetParams("date")
        input_ = GetParams("in")
        result = GetParams("result")
        type_of_date = GetParams("type_of_date")
        amount = GetParams("amount")
        
        
        f_date = string_to_date(date, input_)
        f_string = date_to_string(f_date)
        calculo = calculate_date(f_string, "%d/%m/%Y", amount, type_of_date)
        f_date = string_to_date(calculo, "%d/%m/%Y")
        if input_ == "None":
            input_ = "%d/%m/%Y"
        calculo2 = date_to_string(f_date, input_)

        
        SetVar(result, calculo2)


    if module == "compareDates":

        date = GetParams("date")
        date2 = GetParams("date2")
        input_ = GetParams("in")
        custom_in = GetParams("custom_in")
        operation = GetParams("operation")
        result = GetParams("result")


        resultComparation_ = resultComparation(date, date2, input_, custom_in, operation)
        
        SetVar(result, resultComparation_)

    if module == "daysBetweenDates":
        date = GetParams("date")
        date2 = GetParams("date2")
        input_ = GetParams("in")
        custom_in = GetParams("custom_in")
        result = GetParams("result")

        if not input_ or input_ == "None":
            input_ = custom_in

        if date in ["today", "hoy", "now", "ahora"]:
            date = datetime.datetime.now().__str__()[:10]
            print("date", date)
            input_today = "%Y-%m-%d"
            date = string_to_date(date, input_today)
        else:
            date = string_to_date(date, input_)

        if date2 in ["today", "hoy", "now", "ahora"]:
            date2 = datetime.datetime.now().__str__()[:10]
            input_today = "%Y-%m-%d"
            date2 = string_to_date(date2, input_today)
        else:
            date2 = string_to_date(date2, input_)

        days = (date - date2).days
        # if negative, change the sign
        if days < 0:
            days = days * -1
        print("days", days)
        SetVar(result, days)


except Exception as e:
    traceback.print_exc()
    PrintException()
    raise e
