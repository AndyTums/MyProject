import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../utills.log', "w")
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def read_file(filename: str = None) -> list:
    """Функция считывающая информацию JSON формата с заданного файла"""
    try:
        """Это логер для функции read_file"""
        logger.info("Начал выгрузку с файла")
        with open(filename, encoding="utf-8") as file:
            reading = json.load(file)
            logger.info("Окончил выгрузку с файла")
            return reading
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        return []
