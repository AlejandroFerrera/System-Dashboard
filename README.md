
# System Metrics Dashboard WhereX

<p align="center">
  <img src="https://github.com/user-attachments/assets/815ea6de-6cd1-4f44-907c-88c8fffa361d" width="400">
</p>



Este proyecto es un dashboard de métricas del sistema construido con Flask, que permite monitorear en tiempo real el uso de CPU y memoria del sistema.

## Instalación y Ejecución

### Requisitos

- Python 3.12
- Docker (para despliegue)

### Configuración Local

1. **Clonar el repositorio:**
   ```sh
   git clone https://github.com/AlejandroFerrera/System-Dashboard.git
   cd System-Dashboard
   ```

2. **Crear un entorno virtual e instalar dependencias:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación:**
   ```sh
   flask run
   ```

   La aplicación estará disponible en `http://localhost:5000`.

### Despliegue con Docker

1. **Construir y ejecutar la aplicación en un contenedor Docker:**
   ```sh
   ./deploy.sh
   ```

   La aplicación estará disponible en `http://localhost:8000`, se ejecuta utilizando [gunicorn](https://docs.gunicorn.org/en/stable/) como servidor WSGI.

## Integración Continua

Este proyecto utiliza GitHub Actions para la integración continua. El flujo de trabajo definido en `main.yml` ejecuta pruebas automáticas en cada push o pull request a la rama `main`, asegurando la calidad y estabilidad del código.
