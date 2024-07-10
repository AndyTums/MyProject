import json
import logging
import csv
import pandas as pd

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../utills.log', "w")
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def read_file_json(filename: str = None) -> list:
    """Функция считывающая информацию c JSON файла"""
    try:
        """Это логер для функции read_file"""
        logger.info("Начал выгрузку с файла JSON формата")
        with open(filename, encoding="utf-8") as file:
            reading = json.load(file)
            logger.info("Оконили выгрузку с файла JSON формата")
        return reading
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        return []


def read_file_csv(filename: str = None) -> list:
    """Функция считывающая информацию c CSV файла"""
    try:
        """Это логер для функции read_file_csv"""
        logger.info("Начал выгрузку с файла csv формата")
        with open(filename, encoding="utf-8") as file:
            reading_csv = csv.DictReader(file, delimiter=";")
            reading = [read for read in reading_csv]
        logger.info("Окончили выгрузку с файла csv формата")
        return reading
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        return []


def read_file_excel(filename: str = None) -> list:
    """Функция считывающая информацию c EXCEL файла"""
    try:
        """Это логер для функции read_file_excel"""
        logger.info("Начал выгрузку с файла excel формата")
        reading_excel = pd.read_excel(filename)
        new_list = []
        while True:
            for index, row in reading_excel.iterrows():
                list_file = {"id": row["id"], 'state': row["state"], 'date': row["date"], 'amount': row["amount"],
                             'currency_name': row["currency_name"],
                             'currency_code': row["currency_code"], 'from': row["from"], 'to': row["to"],
                             'description': row["description"]}
                new_list.append(list_file)
            logger.info("Окончили выгрузку с файла excel формата")
            return new_list
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        return []
