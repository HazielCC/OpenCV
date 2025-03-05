import os

import cv2
import pyttsx3
from deepface import DeepFace

from proyectFace.databse import DataBase
from proyectFace.utilities.files_utilities import DB_FILE


class FaceRecognition:
    """This class is used to recognize faces."""

    def __init__(self):
        self.engine = pyttsx3.init()
        self.db = DataBase()
        self.db.create_table()

    def saludar(self, mensaje):
        """This method is used to greet the person."""
        self.engine.say("hola" + mensaje)
        self.engine.runAndWait()

    def start_stream(self):
        """Uso de OpenCV para capturar video"""
        try:
            video = cv2.VideoCapture(0)
            while True:
                ret, frame = video.read()
                if not ret:
                    break

                mensaje = recognizer_face(frame)
                if mensaje != "" and mensaje != "Rostro no detectado":
                    self.db.add_guy(mensaje)
                    self.saludar(mensaje)

                cv2.putText(
                    frame,
                    mensaje,
                    (0, 115),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                )

                cv2.imshow("Proyecto", frame)
                if cv2.waitKey(1) == ord("q"):
                    break

        except Exception as e:
            print(e)


def recognizer_face(frame):
    """Uso de OpenCV para capturar video"""
    try:
        recognizer = DeepFace.find(
            frame, db_path=DB_FILE, model_name="VGG-Face", silent=True
        )
        print(recognizer)
        # Verifica si el DataFrame no está vacío
        if len(recognizer) > 0 and not recognizer[0].empty:
            recognizer_df = recognizer[0]  # Access the first DataFrame in the list
            identity = recognizer_df["identity"].iloc[0]  # Get the first identity
            name = os.path.basename(os.path.dirname(identity))
            print(name)
            return name
        else:
            print("Rostro no detectado")
            return "Rostro no detectado"
    except ValueError:
        return "Rostro no detectado"
    except KeyError:
        return "Rostro no detectado"


if __name__ == "__main__":
    fc = FaceRecognition()
    fc.start_stream()
