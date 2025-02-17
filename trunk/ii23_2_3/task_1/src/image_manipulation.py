from PIL import Image, ImageDraw
import numpy as np
import random

def add_noise_dot(image_path, noise_level=100):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    width, height = img.size

    for _ in range(noise_level):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        draw.point((x, y), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    return img

def add_noise_line(image_path, lines_num=100):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    width, height = img.size
    for _ in range(lines_num):
        x1 = random.randint(0, width - 1)
        y1 = random.randint(0, height - 1)
        x2 = random.randint(0, width - 1)
        y2 = random.randint(0, height - 1)
        draw.line((x1, y1, x2, y2), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), width=1)

    return img

def median_filter_1d(image_path, filter_size=3, axis=0):
    image = Image.open(image_path)
    image_array = np.array(image)

    height, width = image_array.shape[:2]

    filtered_image_array = np.zeros_like(image_array)

    pad = filter_size // 2

    if axis == 0:
        for j in range(width):
            for i in range(pad, height - pad):
                neighborhood = image_array[i - pad:i + pad + 1, j]
                if len(image_array.shape) == 3:
                    for channel in range(image_array.shape[2]):
                        filtered_image_array[i, j, channel] = np.median(neighborhood[:, channel])
                else:
                    filtered_image_array[i, j] = np.median(neighborhood)
    elif axis == 1:
        for i in range(height):
            for j in range(pad, width - pad):
                neighborhood = image_array[i, j - pad:j + pad + 1]
                if len(image_array.shape) == 3:
                    for channel in range(image_array.shape[2]):
                        filtered_image_array[i, j, channel] = np.median(neighborhood[:, channel])
                else:
                    filtered_image_array[i, j] = np.median(neighborhood)
    else:
        raise ValueError(
            "Неправильное значение параметра axis. Допустимые значения: 0 (по столбцам) или 1 (по строкам).")

    filtered_image = Image.fromarray(filtered_image_array)
    return filtered_image