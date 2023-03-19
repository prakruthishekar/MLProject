import sys
from src.logger import logging

#sys module in python provides various funtions and varibles that are used to manupulate 
# different parts of pythin runtime env. It allows operating on the 

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # it gives the exception info
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number \
                    [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno,str(error))
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_messgae = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_messgae



if __name__=="__main__":
    try:
        a=1/0
    except Exception as e: 
        logging.info("Divide by zero eroror")
        raise CustomException(e,sys)
    
    