from google import genai
from google.genai import types
from .ModelInput import ModelInput
from .config import SCHEMA, FEW_SHOT_CONTENT

class GeneDescriptor:
    def __init__(self, apiKey:str, model:str, fewShotContent:list[types.Content]=FEW_SHOT_CONTENT, schema=SCHEMA):
        self.apiKey = apiKey
        self.model = model
        self.fewShotContent = fewShotContent
        self.schema = schema
        self.__client = genai.Client(api_key=apiKey)

    def __getContent(self, inp:ModelInput, remember:bool=False):
        contents = self.fewShotContent.copy()
        if remember:
            self.fewShotContent.append(inp.input)
        contents.append(inp.input)

        return contents
    
    def __getDescription(self, inp:ModelInput, remember:bool=False):
        return self.__client.models.generate_content(
            model=self.model,
            contents=self.__getContent(inp, remember),
            config=self.schema
        ).to_json_dict()
    
    def __getDescriptionStream(self, inp:ModelInput, remember:bool=False):
        return self.__client.models.generate_content_stream(
            model=self.model,
            contents=self.__getContent(inp, remember),
            config=self.schema
        )
    
    def getDescription(self, inp:ModelInput, remember:bool=False, stream:bool=True):
        if stream:
            return self.__getDescriptionStream(inp, remember)
        else:
            return self.__getDescription(inp, remember)
        