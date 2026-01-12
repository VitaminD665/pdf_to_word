""" Module to handle the initial pdf intake """



from src.app.utilities.app_logger import AppLogger



class PDFIntake:
    """ Logic to intake a pdf"""

    def __init__(self) -> None:
        self.log = AppLogger.init_logger()



