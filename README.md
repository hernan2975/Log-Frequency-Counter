# 📊 Log Frequency Counter

Herramienta de línea de comandos en Python para analizar archivos de logs y calcular la frecuencia de eventos por nivel (`INFO`, `WARNING`, `ERROR`, etc.). Diseñada para ser modular, extensible y fácilmente integrable en suites de herramientas CLI.

---

## 🚀 Características

- 📥 Entrada parametrizable: acepta archivos `.log` como argumento.
- 🔎 Conteo de ocurrencias por palabra clave (`INFO`, `ERROR`, etc.).
- 📈 Top N eventos más frecuentes.
- ⚙️ CLI con `Click`: flags como `--top`, `--keywords`, `--export`.
- 🧩 Extensible: permite agregar nuevos niveles o patrones.
- 🧪 Tests unitarios incluidos.
- 📄 Exportación opcional a JSON.

---

## 🧰 Tecnologías utilizadas

- Python 3.8+
- Click (CLI)
- Pytest (testing)
- Regex + Counter (parser)

---

## 📦 Instalación

```bash
git clone https://github.com/tu-usuario/log-frequency-counter.git
cd log-frequency-counter
pip install -r requirements.txt
