from loguru import logger


class PoetryTest: 
    def __init__(self, datas: list) -> None:
        self.__datas = datas


    def run(self): 
        for data in self.__datas: 
            logger.info(data)
        