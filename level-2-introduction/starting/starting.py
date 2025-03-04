import cv2

name_image = "paisaje.png"
name_window = "Soy una foto"


def read_img():
    """Se muestra una imagen"""
    img = cv2.imread(name_image)  # Se lee la imagen

    cv2.imshow(name_window, img)  # Se crea la ventana
    cv2.waitKey()  # Espera que se presione una tecla
    cv2.destroyAllWindows()

    # ? Guarda la image
    # cv2.imwrite("paisaje2.png", img)


def read_gray_img():
    """Se muestra una imagen en escala de grises"""
    img = cv2.imread(
        name_image, cv2.IMREAD_GRAYSCALE
    )  # Se lee la imagen en escala de grises

    cv2.imshow(name_window, img)  # Se crea la ventana
    cv2.waitKey()  # Espera que se presione una tecla
    cv2.destroyAllWindows()

    # ? Guarda la image
    # cv2.imwrite("paisaje2.png", img)


def show_two_images():
    """Se muestra una imagen en escala de grises"""
    image = name_image
    color_img = cv2.imread(image)  # Se lee la imagen
    gray_img = cv2.imread(image, 0)  # Se lee la imagen en escala de grises

    cv2.imshow(name_window, color_img)  # Se crea la ventana
    cv2.imshow("Soy una foto gris", gray_img)  # Se crea la ventana
    cv2.waitKey()  # Espera que se presione una tecla
    cv2.destroyAllWindows()

    # ? Guarda la image
    user_option = input("¿Desea guardar la imagen gris? (s/n): ")
    if user_option == "s":
        cv2.imwrite("paisaje2.png", gray_img)

    user_option = input("¿Desea guardar la imagen a color? (s/n): ")
    if user_option == "s":
        cv2.imwrite("paisaje2.png", color_img)


def show_complete_window_img():
    """Se muestra una imagen en una ventana completa"""

    img = cv2.imread(name_image)

    # * Ventana en pantalla completa
    # cv2.namedWindow(name_window, cv2.WND_PROP_FULLSCREEN)

    # * Ventana redimensionable
    cv2.namedWindow(name_window, cv2.WINDOW_NORMAL)

    # * Establecer pantalla completa
    # cv2.setWindowProperty(
    #     name_window, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN
    # )

    cv2.imshow(name_window, img)  # Mostrar imagen
    cv2.waitKey()  # Esperar tecla
    cv2.destroyAllWindows()  # Cerrar ventanas

    # Guardar imagen (opcional)
    # cv2.imwrite("paisaje2.png", img)


if __name__ == "__main__":
    # read_img()
    # read_gray_img()
    # show_two_images()
    show_complete_window_img()
