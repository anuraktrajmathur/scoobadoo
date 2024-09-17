class DetectedBlock:
    def __init__(self, nnImage, recognized_object_label, recognized_object_score, bbox_center_x, bbox_center_y, image_center_x, image_center_y):
        self._nnImage = nnImage                                     # image with bounding box (only the one with max score)
        self._recognized_object_label = recognized_object_label     # recognized object label (only the one with max score)
        self._recognized_object_score = recognized_object_score     # recognized object score(only the one with max score)
        self._bbox_center_x = bbox_center_x                         # center of the bounding box of the recognized object (x)
        self._bbox_center_y = bbox_center_y                         # center of the bounding box of the recognized object (y)
        self._image_center_x = image_center_x                       # center of the image (x)
        self._image_center_y = image_center_y                       # center of the image (y)
    
    