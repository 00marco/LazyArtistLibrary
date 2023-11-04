# TODO -- must wokr for serverless; stateless, read file directly. maybe take CV2 videocaptures instead of filenames?


import cv2
import logging

logging.basicConfig(
    format="{levelname: <8}:{asctime}:{name: <30}:{lineno: <4}:{message}",
    level=logging.DEBUG,
    style="{",
)
logger = logging.getLogger(__name__)
import numpy as np


class VideoPostProcessing:
    def __init__(self, video_capture):
        self.video_capture = video_capture
        self.frame_count = self.video_capture.get(cv2.CAP_PROP_FRAME_COUNT)
        return

    def get_last_frame(self):
        frame = self.__get_frame(self.frame_count - 1)
        return frame

    def get_wip_frames(self, n=4):
        frames = []
        frame_numbers = np.linspace(10, self.frame_count - 1, n).tolist()
        for frame_num in frame_numbers:
            frames.append(self.__get_frame(frame_num))

        return frames

    def get_closeups_from_frame(self, frame, zoom_level=3, closeup_count=6):
        """
        frame: numpy.ndarray
        """
        crops = []
        for i in range(closeup_count):
            crops.append(
                self.zoom_image(
                    zoom_level=zoom_level,
                    center_x_pct=random.random(),
                    center_y_pct=random.random(),
                    image=frame,
                )
            )
        return crops

    def __calculate_zoom_thresholds(self, image, zoom_level):
        """
        zoom_level: > 1 representing denominator
        """
        original_height, original_width, channels = image.shape

        min_center_y = original_height / zoom_level / 2
        max_center_y = original_height - original_height / zoom_level / 2
        min_center_x = original_width / zoom_level / 2
        max_center_x = original_width - original_width / zoom_level / 2
        data = {
            "min_center_y": min_center_y,
            "max_center_y": max_center_y,
            "min_center_x": min_center_x,
            "max_center_x": max_center_x,
        }
        return data

    def zoom_image(self, image, zoom_level, center_x_pct, center_y_pct):
        """
        zoom_level: > 1 representing denominator
        """
        zoom_thresholds = self.__calculate_zoom_thresholds(image, zoom_level)
        original_height, original_width, channels = image.shape
        zoom_height = original_height / zoom_level
        zoom_width = original_width / zoom_level

        center_x = (
            zoom_thresholds["min_center_x"]
            + (zoom_thresholds["max_center_x"] - zoom_thresholds["min_center_x"])
            * center_x_pct
        )
        center_y = (
            zoom_thresholds["min_center_y"]
            + (zoom_thresholds["max_center_y"] - zoom_thresholds["min_center_y"])
            * center_y_pct
        )

        y_start = int(round(center_y - zoom_height / 2))
        y_end = int(round(center_y + zoom_height / 2))
        x_start = int(round(center_x - zoom_width / 2))
        x_end = int(round(center_x + zoom_width / 2))

        zoomed_image = image[y_start:y_end, x_start:x_end].copy()
        zoomed_image = cv2.resize(zoomed_image, (original_width, original_height))
        return zoomed_image

    def __get_frame(self, frame_num):
        self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = self.video_capture.read()
        return frame

    def __generate_n_separated_numbers(self, target, n=4):
        return