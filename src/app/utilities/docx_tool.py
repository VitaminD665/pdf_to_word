""" Module that controls the involvement of creating and filling in a docx (MS Word Document)"""

from dataclasses import dataclass, field


@dataclass
class DocxArguments:
    input_filename_path: str
    output_docx_filename: str
    output_font_size: int = 12 
    output_font_style: str = field(default="Times New Roman")



class DocxTool:
    """ Tool for creating and fillout out .docx documents"""




    def _create_document():
        """ Private method to create a document"""