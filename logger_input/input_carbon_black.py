from logger_input.logger_input_interface import LogInput


class LogInputCarbonBlack(LogInput):

    def retrieveData(self):
        print("Get data from Carbon Black")
        return "Carbon black data"


def testPrint():
    print("test print")