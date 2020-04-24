from logger_output.logger_output_interface import LogOutput


class LogOutputAwsS3(LogOutput):

    def sendData(self, data):
        print("Data sent to AWS: " + data)

