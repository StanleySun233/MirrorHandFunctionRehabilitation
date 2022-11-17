import threading

import backend
import frontend

taskBackend = threading.Thread(target=backend.controller.run)

taskBackend.start()

taskFrontend = threading.Thread(target=frontend.Login.run)

taskFrontend.start()