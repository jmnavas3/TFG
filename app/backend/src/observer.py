import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CambioArchivoHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == file_path:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    print(line.strip())

if __name__ == "__main__":
    file_path = 'ruta/al/archivo.txt'
    event_handler = CambioArchivoHandler()
    observer = Observer()
    observer.schedule(event_handler, path='ruta/al/', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
