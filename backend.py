import threading
import backend


task = threading.Thread(target=backend.controller.run)

task.start()