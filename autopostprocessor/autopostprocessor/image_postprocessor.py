import cv2
import logging
import random

logging.basicConfig(
    format="{levelname: <8}:{asctime}:{name: <30}:{lineno: <4}:{message}",
    level=logging.DEBUG,
    style="{",
)
logger = logging.getLogger(__name__)
import numpy as np


class ImagePostProcessor:
    def __init__(self, image):
        self.image = image
        self.width = int(self.image.shape[1])
        self.height = int(self.image.shape[0])
        return
    

    def get_thumbnails(self):
        # 1:1
        print("get thumbnails")
        crop_width = self.width 
        crop_height = crop_width
        return self.get_image_crops_from_sliding_window(crop_width=crop_width, crop_height=crop_height)
    
    
    def get_banners(self):
        # 16:9
        print("get banners")
        crop_width = self.width
        crop_height = int(crop_width / 16 * 9)
        return self.get_image_crops_from_sliding_window(crop_width=crop_width, crop_height=crop_height)
    

    def get_closeups(self):
        print("get closeups")
        frames = []
        for i in range(2,4):
            frames += self.get_image_crops_from_sliding_window(crop_height=self.height/i, crop_width=self.width/i, restore_size=True)
        return frames


    def get_image_crops_from_sliding_window(self, crop_width, crop_height, restore_size=False):
        width_start = 0
        width_end = int(width_start + crop_width)
        width_increment = 0.05
        
        image_crops = []
        while width_end <= self.width:
            height_start = 0
            height_end = int(height_start + crop_height)
            height_increment = 0.05
            
            while height_end <= self.height:
                # print(height_start, height_end, width_start, width_end, self.height, self.width)
                image_crop = self.image[
                                        height_start:height_end,
                                        width_start:width_end,
                                       ].copy()
                if restore_size:
                    image_crop = cv2.resize(image_crop, (self.width, self.height))
                image_crops.append(image_crop)
                height_start += int(self.height * height_increment)
                height_end = int(height_start + crop_height)
                
            # print(width_start)
            width_start += int(self.width * width_increment)
            width_end = int(width_start + crop_width)
            # print(width_start)
        
        return image_crops
    