from loguru import logger
from poetry_test.wrapper import PoetryTest

def start(): 
    list_data = ["TELO"]
    poetry_test = PoetryTest(datas=list_data)
    poetry_test.run()