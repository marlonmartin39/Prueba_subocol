# Prueba Técnica de Automatización en Python

Este proyecto es una solución de automatización de pruebas desarrollada en Python, que utiliza el patrón Screenplay para simular la funcionalidad de login de un API de prueba. La solución se caracteriza por:

- **Configuración centralizada:** Un archivo `config.json` para gestionar parámetros globales (URL base, timeout, nivel de logging, etc.).
- **Datos de prueba separados:** Dos archivos JSON ubicados en la carpeta `data/` (uno para el login exitoso y otro para el login fallido).
- **Gestión de dependencias:** Un archivo `requirements.json` que especifica las dependencias necesarias (se recomienda usarlo como referencia; en producción es más habitual usar un `requirements.txt`).
- **Ejecución parametrizada y logging:** El script principal permite ejecutar ambos escenarios de prueba y muestra logs detallados y formateados.
- **Facilidad de integración en CI/CD:** El proyecto está diseñado para integrarse fácilmente en pipelines de integración continua, por ejemplo, utilizando Jenkins.

---

## Estructura del Proyecto

La estructura recomendada del proyecto es la siguiente:

mi_proyecto/ ├── data/ │ ├── login_exitoso.json # Datos para simular login exitoso │ └── login_fallido.json # Datos para simular login fallido ├── config.json # Configuración global (URL, timeout, log_level) ├── requirements.json # Dependencias del proyecto (formato JSON) ├── login_test.py # Script principal de pruebas └── README.md # Documentación del proyecto (este archivo)


---

## Archivos de Configuración y Datos

### config.json

Define los parámetros globales del proyecto, por ejemplo:

```json
{
  "base_url": "https://castlemockdemo.subocol.com/castlemock/mock/rest/project/NpJ1A9/application/eu72DD/login",
  "timeout": 30,
  "log_level": "DEBUG"
}
