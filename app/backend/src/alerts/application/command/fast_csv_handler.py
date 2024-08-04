from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, LoggingEventHandler


class FastCSVHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == file_path:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    print(line.strip())