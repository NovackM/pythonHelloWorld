from logger_input.input_carbon_black import LogInputCarbonBlack
from logger_input.input_zscaler import LogInputZscaler
from logger_output.output_aws_s3 import LogOutputAwsS3
from logger_output.output_sys_log import LogOutputSysLog

inputSources = [LogInputCarbonBlack(), LogInputZscaler()]
outputSources = [LogOutputAwsS3(), LogOutputSysLog()]

for input in inputSources:
    data = input.retrieveData()
    for output in outputSources:
        output.sendData(data)
