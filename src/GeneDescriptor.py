from google import genai
from google.genai import types
from .ModelInput import ModelInput
from .config import SCHEMA, FEW_SHOT_CONTENT

class GeneDescriptor:
    """
    A class for generating gene descriptions and predictions using Google's GenAI API.
    """

    def __init__(self, apiKey: str, model: str, fewShotContent: list[types.Content] = FEW_SHOT_CONTENT, schema=SCHEMA):
        """
        Initializes the GeneDescriptor instance.

        Args:
            apiKey (str): The API key for accessing Google's GenAI API.
            model (str): The name of the model to use for generating content.
            fewShotContent (list[types.Content], optional): Few-shot examples to provide context for the model. Defaults to FEW_SHOT_CONTENT.
            schema: The schema configuration for the model. Defaults to SCHEMA.
        """
        self.apiKey = apiKey
        self.model = model
        self.fewShotContent = fewShotContent
        self.schema = schema
        self.__client = genai.Client(api_key=apiKey)

    def __getContent(self, inp: ModelInput, remember: bool = False):
        """
        Prepares the content to be sent to the model for processing.

        Args:
            inp (ModelInput): The input data containing the genomic sequence and optional image.
            remember (bool, optional): Whether to remember the input for future requests. Defaults to False.

        Returns:
            list[types.Content]: A list of content objects to be sent to the model.
        """
        contents = self.fewShotContent.copy()
        if remember:
            self.fewShotContent.append(inp.input)
        contents.append(inp.input)

        return contents

    def __getDescription(self, inp: ModelInput, remember: bool = False):
        """
        Generates a description based on the input data.

        Args:
            inp (ModelInput): The input data containing the genomic sequence and optional image.
            remember (bool, optional): Whether to remember the input for future requests. Defaults to False.

        Returns:
            dict: The generated description in JSON format.
        """
        return self.__client.models.generate_content(
            model=self.model,
            contents=self.__getContent(inp, remember),
            config=self.schema
        ).to_json_dict()

    def __getDescriptionStream(self, inp: ModelInput, remember: bool = False):
        """
        Streams the generated description based on the input data.

        Args:
            inp (ModelInput): The input data containing the genomic sequence and optional image.
            remember (bool, optional): Whether to remember the input for future requests. Defaults to False.

        Returns:
            generator: A generator that streams the content chunks.
        """
        return self.__client.models.generate_content_stream(
            model=self.model,
            contents=self.__getContent(inp, remember),
            config=self.schema
        )

    def getDescription(self, inp: ModelInput, remember: bool = False, stream: bool = True):
        """
        Generates a description based on the input data, with an option to stream the output.

        Args:
            inp (ModelInput): The input data containing the genomic sequence and optional image.
            remember (bool, optional): Whether to remember the input for future requests. Defaults to False.
            stream (bool, optional): Whether to stream the output. Defaults to True.

        Returns:
            dict or generator: The generated description in JSON format or a generator for streamed output.
        """
        if stream:
            return self.__getDescriptionStream(inp, remember)
        else:
            return self.__getDescription(inp, remember)
