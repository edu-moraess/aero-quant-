from typing import Optional

import numpy as np

def apply_augmentation(image: np.ndarray, augmentation_type: str = "horizontal_flip") -> np.ndarray:
    if augmentation_type == "horizontal_flip":
        return np.fliplr(image)
    elif augmentation_type == "vertical_flip":
        return np.flipud(image)
    elif augmentation_type == "rotate_90":
        return np.rot90(image)
    else:
        return image