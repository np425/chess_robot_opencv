from src.robot import setup_communication
from src.camera import CameraBoardDetection, default_camera_setup

from src.gui import gui_main
from src.game import Game

from ultralytics import YOLO
import chess.engine
import logging

def main():
    try:
        logging.basicConfig(format='%(asctime)s %(levelname)s:%(name)s:%(message)s', datefmt='%x %X', level=logging.INFO)
        
        setup_communication()

        model = YOLO("chess_200.pt")

        engine = chess.engine.SimpleEngine.popen_uci("stockfish")
        camera = default_camera_setup()

        detection = CameraBoardDetection(model, camera=camera)

        game = Game(detection, engine)

        gui_main(game)

    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    main()
