import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


CSV_FILE_PATH = get_path(filename="books.csv")
JSON_FILE_PATH = get_path(filename="users.json")
JSON_FILE_FORMAT = get_path(filename="reference.json")
JSON_FILE_RESULT = get_path(filename="result.json")
