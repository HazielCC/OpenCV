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

def g
if __name__ == "__main__":
    img = create_black_image()
    change_pixel_color(img)
    # cv2.waitKey()
