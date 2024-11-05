import cv2
import numpy as np

class VideoWriter:
    def __init__(self, filename="output.mp4", fps=50):
        self.filename = filename
        self.fps = fps
        self.frames = []

    def add(self, frame):
        self.frames.append(np.array(frame))

    def save(self):
        height, width, _ = self.frames[0].shape
        out = cv2.VideoWriter(self.filename, cv2.VideoWriter_fourcc(*'mp4v'), self.fps, (width, height))
        for frame in self.frames:
            out.write(frame)
        out.release()
