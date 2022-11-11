import logging
import os
import config
from fastapi import FastAPI
from exceptions import IncorrectLoggerConfiguration


def configure_logger(level: str) -> None:
    format = "%(asctime)s %(name)s %(levelname)s:%(message)s"

    if level == "ERROR":
        logging.basicConfig(level=logging.ERROR, format=format)

    elif level == "INFO":
        logging.basicConfig(level=logging.INFO, format=format)

    elif level == "DEBUG":
        logging.basicConfig(level=logging.DEBUG, format=format)

    else:
        raise IncorrectLoggerConfiguration("Такой уровень, logger не поддерживает!")


configure_logger(level="DEBUG")
logger = logging.getLogger(__name__)


app = FastAPI()


@app.get("/api")
@app.get("/api/{path_to_dir}")
async def root(path_to_dir: str = ""):
    response = []
    path = f"{config.ROOT_DIR}/{path_to_dir}"
    try:
        repository = os.listdir(path)
        for element in repository:
            response.append({
                "name": element,
                "type": "folder" if os.path.isdir(f"{path}/{element}") else "file",
                "time": int(os.path.getctime(f"{path}/{element}")),
            })
    except FileNotFoundError or NotADirectoryError as e:
        return {"success": False, "error": f"{e}"}

    return {"data": response}
