import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# Configuration des broches GPIO
GPIO.setwarnings(False)
GPIO.cleanup()

# Initialisation du lecteur RFID
reader = SimpleMFRC522()

try:
    # Lecture de la carte RFID
    print("Approchez votre carte RFID...")
    id, contenu = reader.read()

    # Affichage des données lues
    print("ID de la carte : {}".format(id))
    print("Contenu de la carte : {}".format(contenu))

finally:
    # Nettoyage des broches GPIO
    GPIO.cleanup()

