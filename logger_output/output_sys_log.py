from logger_output.logger_output_interface import LogOutput


class LogOutputSysLog(LogOutput):

    def sendData(self, data):
        print("Data sent to Sys Log: " + data)

