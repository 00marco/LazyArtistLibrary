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
        crop_width = self.width 
        crop_height = crop_width
        return self.get_image_crops_from_sliding_window(crop_width=crop_width, crop_height=crop_height)
    
    
    def get_banners(self):
        # 16:9
        crop_width = self.width
        crop_height = int(crop_width / 16 * 9)
        return self.get_image_crops_from_sliding_window(crop_width=crop_width, crop_height=crop_height)
    

    def get_closeups(self, height=None, width=None):
        frames = {}
        for i in range(2,6):
            frames[i] = self.get_image_crops_from_sliding_window(crop_height=height, crop_width=width)
        return 


    def get_image_crops_from_sliding_window(self, crop_width, crop_height):
        width_start = 0
        width_increment = 0.05
        
        image_crops = []
        while width_start + crop_width <= self.width:
            height_start = 0
            height_increment = 0.05
            
            while height_start + crop_height <= self.height:
                print(height_start,height_start+crop_height,width_start,width_start+crop_width, self.height, self.width)
                image_crop = self.image[
                                        height_start:height_start+crop_height,
                                        width_start:width_start+crop_width,
                                       ].copy()
                image_crops.append(image_crop)
                height_start += int(self.height * height_increment)
                
            print(width_start)
            width_start += int(self.width * width_increment)
            print(width_start)
        
        return image_crops
    