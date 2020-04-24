from logger_input.logger_input_interface import LogInput


class LogInputZscaler(LogInput):

    def retrieveData(self):
        print("Get data from Zscaler")
        return "Zscaler data"


