from src import GeneDescriptor, ModelInput
from env import GEMINI_API_KEY, GEMINI_MODEL_NAME


inp = ModelInput("TP53")

descriptor = GeneDescriptor(GEMINI_API_KEY, GEMINI_MODEL_NAME)
print(descriptor.getDescription(inp, False, False))