import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from app.backend.src.alerts.domain.contracts.file_handler_contract import FileHandler


class WatchdogAdapter(FileSystemEventHandler):
    def __init__(self, handler: FileHandler, path: str):
        self.handler = handler
        self.path = path
        self.observer = Observer()

    def on_created(self, event):
        if not event.is_directory:
            self.handler.on_file_created(event)

    def on_modified(self, event):
        if not event.is_directory:
            self.handler.on_file_modified(event)

    def start(self):
        self.observer.schedule(self, self.path, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()

    def stop(self):
        self.observer.stop()
        self.observer.join()
