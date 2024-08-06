from flask import Flask, flash, jsonify, redirect, request, url_for
from werkzeug.utils import secure_filename
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import time
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp'
ALLOWED_EXTENSIONS = {'txt', 'csv'}


class CSVHandler(FileSystemEventHandler):
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def on_modified(self, event):
        if event.src_path == self.csv_file:
            print(f"{self.csv_file} has been modified")
            self.import_csv_to_db()

    def import_csv_to_db(self):
        # Lógica para importar los datos del CSV a la base de datos
        print("Importing CSV data to database...")


def run_flask_app():
    app.run(host="0.0.0.0", debug=True, use_reloader=False)  # use_reloader=False para evitar doble ejecución en modo debug


def run_watchdog(path):
    event_handler = CSVHandler(path)
    observer = Observer()
    observer.schedule(event_handler, os.path.dirname(path), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


@app.route('/api/data', methods=['GET'])
def get_data():
    # Lógica para manejar la petición
    return jsonify({"message": "Hello, World!"})


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # logic for proccessing file
            data = file.read()
            print(data)
            # filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(request.url)
            return redirect(request.url)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    csv_file_path = "/config/requirements.txt"  # Reemplaza con la ruta de tu archivo CSV

    # Crear hilos para ejecutar Flask y Watchdog simultáneamente
    flask_thread = threading.Thread(target=run_flask_app)
    watchdog_thread = threading.Thread(target=run_watchdog, args=(csv_file_path,))

    # Iniciar los hilos
    flask_thread.start()
    watchdog_thread.start()

    # Esperar a que los hilos terminen (esto ocurre cuando se recibe una señal de interrupción)
    try:
        flask_thread.join()
    except KeyboardInterrupt:
        watchdog_thread.join()
