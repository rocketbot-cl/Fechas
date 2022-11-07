from datetime import datetime
import time
import locale

class DateController:

    def __init__(self, myDate, inputFormat):
        try:
            locale.setlocale(locale.LC_ALL, 'en_US')
        except:
            locale.setlocale(locale.LC_ALL, '')
        self.myDate = datetime.strptime(myDate, inputFormat)

    def changeFormat(self, outputFormat):
        dateFormatChanged = self.myDate.strftime(outputFormat)
        return dateFormatChanged

    def getWeekDay(self):
        weekDay = self.myDate.weekday()
        return weekDay

    def getWeekNumber(self):
        weekNumber = self.myDate.strftime("%W")
        return weekNumber

    def compareDate(self, dateToCompare, inputFormat, operation):
        
        dateToCompare = datetime.strptime(dateToCompare, inputFormat)
        result = ""

        if operation == "==":
            result = self.myDate == dateToCompare
        if operation == "<=":
            result = self.myDate <= dateToCompare
        if operation == ">=":
            result = self.myDate >= dateToCompare
        if operation == "!=":
            result = self.myDate != dateToCompare
        if operation == ">":
            result = self.myDate > dateToCompare
        if operation == "<":
            result = self.myDate < dateToCompare

        if result == "":
            result = "Operation Invalid"
        
        return result
    

if __name__ == "__main__":

    myDateObject = DateController("18-03-2021", "%d-%m-%Y")