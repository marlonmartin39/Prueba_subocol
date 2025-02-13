import requests
import json
import os
import logging

def configurar_logging(nivel):
    logging.basicConfig(
        level=getattr(logging, nivel.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def leer_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

class Actor:
    def __init__(self, name):
        self.name = name

    def attempts_to(self, task):
        logging.info(f"[{self.name}] está intentando: {task.__class__.__name__}")
        result = task.perform_as(self)
        return result

class LoginTask:
    def __init__(self, login_data, base_url, timeout=30):
        self.login_data = login_data
        self.base_url = base_url
        self.timeout = timeout

    def perform_as(self, actor):
        try:
            response = requests.post(self.base_url, json=self.login_data, timeout=self.timeout)
            logging.info(f"Datos enviados: {self.login_data}")
            logging.info(f"Código de respuesta: {response.status_code}")
            # Intentamos formatear la respuesta como JSON legible
            try:
                respuesta_json = response.json()
                pretty_response = json.dumps(respuesta_json, indent=4, ensure_ascii=False)
                logging.info(f"Contenido de la respuesta:\n{pretty_response}")
            except Exception:
                logging.info(f"Contenido de la respuesta: {response.text}")

            if response.status_code == 200:
                logging.info("Resultado: Login exitoso")
                return True
            else:
                logging.info("Resultado: Login fallido")
                return False
        except Exception as e:
            logging.error(f"Error durante la ejecución del login: {e}")
            return False

def cargar_datos(caso):
    # El archivo se llama login_exitoso.json o login_fallido.json según el caso
    file_name = f"login_{caso}.json"
    file_path = os.path.join(os.path.dirname(__file__), "data", file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    config = leer_config()
    configurar_logging(config.get("log_level", "INFO"))
    base_url = config.get("base_url")
    timeout = config.get("timeout", 30)
    
    actor = Actor("Tester")

    # Ejecutar ambos casos de prueba en una sola ejecución:
    for caso in ["exitoso", "fallido"]:
        logging.info(f"\n---- Test: Login {caso.capitalize()} ----")
        try:
            login_data = cargar_datos(caso)
        except Exception as e:
            logging.error(f"Error al leer el archivo para el caso {caso}: {e}")
            continue
        task = LoginTask(login_data, base_url, timeout)
        actor.attempts_to(task)

if __name__ == "__main__":
    main()
