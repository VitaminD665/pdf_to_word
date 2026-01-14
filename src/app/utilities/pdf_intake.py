""" Module to handle the initial pdf intake """


import os
from pathlib import Path

from pdf2image import convert_from_path

from src.app.utilities.app_logger import AppLogger


class PDFIntake:
    """ Logic to intake a pdf"""

    def __init__(self) -> None:
        self.log = AppLogger.init_logger()

    def _convert_pdf_file_to_jpeg(self, pdf_file: Path, out_dir: str = "out_images", format: str = "jpeg") -> None:
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        pages = convert_from_path(pdf_file, fmt=format.lower())

        for i, page in enumerate(pages):
            out_dir = os.path.join(out_dir, f"page_{i + 1}.jpg")
            page.save(out_dir, format.upper())

        self.log.info(f"Converted {len(pages)} pages to JPEG format in '{out_dir} directory'")

    def pdf_to_jpeg(self, pdf_file: Path) -> None: 
        """
        Convert a pdf file to a jpeg file. Default Naming is 'page_X.jpg'
        
        :param pdf_file: Path object of the inputted pdf file
        :type pdf_file: Path
        """
        if not pdf_file:
            raise RuntimeError(f"File Path {pdf_file} is None")
        
        self._convert_pdf_file_to_jpeg(pdf_file)

