import cv2

name_image = "paisaje.png"
name_window = "Soy una foto"


def separete_channels_rgb():
    """Se muestra una imagen a color"""
    img = cv2.imread(name_image)  # Se lee la imagen a color
    b, g, r = cv2.split(img)  # Se separan los canales de color

    cv2.imshow("Canal azul", b)
    cv2.imshow("Canal verde", g)
    cv2.imshow("Canal rojo", r)

    cv2.waitKey()


def separete_channels_hsv():
    """Se muestra una imagen a color"""
    img = cv2.imread(name_image)  # Se lee la imagen a color
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # Se convierte la imagen a HSV
    h, s, v = cv2.split(hsv)  # Se separan los canales de color

    cv2.imshow("Canal H", h)
    cv2.imshow("Canal S", s)
    cv2.imshow("Canal V", v)
    cv2.imshow("Imagen HSV", hsv)

    cv2.waitKey()


def set_image_color():
    """Se muestra una imagen a color"""
    img = cv2.imread(name_image)  # Se lee la imagen a color
    gray_img = cv2.imread(name_image, 0)  # Se lee la imagen en escala de grises

    cv2.imshow(name_window, img)
    cv2.imshow("Soy una foto gris", gray_img)

    cv2.waitKey()


if __name__ == "__main__":
    # separete_channels_rgb()
    separete_channels_hsv()
    # set_image_color()
