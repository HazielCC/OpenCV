import cv2
import numpy as np


def create_black_image():
    # Se crea una imagen en blanco de 300x300 píxeles y 3 canales
    return np.zeros((300, 300, 3), np.uint8)


def change_pixel_color(base_image):
    """Se cambia el color de un pixel en la imagen"""
    pixel = base_image[150, 150]  # Se obtiene el pixel en la posición (150, 150)
    print(pixel)  # [0 0 0]
    base_image[150, 150] = [
        255,
        255,
        255,
    ]  # Se cambia el color del pixel en la posición (150, 150)
    pixel = base_image[150, 150]  # Se obtiene el pixel en la posición (150, 150)
    print(pixel)

    cv2.imshow("Image", base_image)


def get_all_pixels(base_image):
    """Se obtienen todos los píxeles de la imagen"""
    for x in range(300):
        for y in range(300):
            pixel = base_image[x, y]
            print(pixel)


def change_color_pixels(base_image):
    """Modifica el color de todos los píxeles de la imagen"""
    for x in range(300):
        for y in range(300):
            pixel = base_image[x, y]
            if pixel[0] == 0:
                base_image[x, y] = [255, 255, 255]

    cv2.imshow("Image_white", base_image)
    cv2.waitKey()


if __name__ == "__main__":
    img = create_black_image()
    change_pixel_color(img)
    # get_all_pixels(img)
    change_color_pixels(img)
    # get_all_pixels(img)

    # cv2.waitKey()
