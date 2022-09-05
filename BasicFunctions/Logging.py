import logging

logging.basicConfig(filename= "D:\Selenium\logFile1.log",
                    level= logging.DEBUG,
                    format= '%(asctime)s -  <%(levelname)s> %(message)s',
                    datefmt= '%d-%m-%Y %I:%M %p')

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

