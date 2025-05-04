from google.genai import types
from PIL import Image
import requests
import base64
import json
import io
import os
import re

class ModelInput:
    """
    A class for preparing input data for the GenAI model, including genomic sequences and optional images.
    """

    def __init__(self, sequence: str, image: str | Image.Image = "", imageBase64: str = ""):
        """
        Initializes the ModelInput instance.

        Args:
            sequence (str): The genomic sequence (FASTA format) to be analyzed.
            image (str | Image.Image, optional): The image file path, URL, or PIL Image object. Defaults to an empty string.
            imageBase64 (str, optional): A base64-encoded string of the image. Defaults to an empty string.

        Raises:
            ValueError: If both `image` and `imageBase64` are provided, or if the image is invalid.
        """
        self.seqeuence = sequence

        if image != "" and imageBase64 != "":
            raise ValueError("Invalid input: Provide either an image file path or a base64-encoded image string, but not both.")

        if image != "":
            if type(image) == str:
                if os.path.isfile(image):
                    self.image = Image.open(image)
                elif re.match(r'^https?:\/\/.*\.(?:png|jpg|jpeg|gif|bmp|tiff)$', image, re.IGNORECASE):
                    self.image = Image.open(io.BytesIO(requests.get(image).content))
                else:
                    raise ValueError(f"Invalid input: {image} is not a valid file path or URL.")
            else:
                self.image = image
        elif imageBase64 != "":
            self.image = Image.open(io.BytesIO(base64.b64decode(imageBase64)))

        if image == "" and imageBase64 == "":
            self.imageBytes = None
        else:
            image_bytes_io = io.BytesIO()
            self.image.save(image_bytes_io, format=self.image.format)
            self.imageBytes = image_bytes_io.getvalue()

    @property
    def input(self):
        """
        Prepares the input data for the GenAI model.

        Returns:
            list[types.Part]: A list of parts containing the genomic sequence and optional image data.
        """
        inp = [types.Part.from_text(text=json.dumps({
            "input": self.seqeuence,
        }))]

        if self.imageBytes is not None:
            image = types.Part.from_bytes(data=self.imageBytes, mime_type=self.image.get_format_mimetype())
            inp.append(image)

        return inp
