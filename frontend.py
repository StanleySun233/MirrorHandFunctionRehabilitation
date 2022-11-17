import threading

import frontend

task = threading.Thread(target=frontend.Login.run)

task.start()