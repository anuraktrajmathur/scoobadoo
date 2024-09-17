# Import modules
from picamera2 import Picamera2


class CameraManager:
    def __init__(self):
        self._camera    = Picamera2()
        self._error     = False
        
    @property
    def camera(self):
        return self._camera

    def setup(self):
        self._camera.resolution = (360, 240)
        self._config = self._camera.create_preview_configuration(main={"size": self._camera.resolution})
        self._camera.configure(self._config)
        self._camera.start()
        # self.nnSetup()

    def stop(self):
        self._camera.stop()