from google.genai import types
from google import genai

with open("examples/prompt.md", "r") as f:
    PROMPT = f.read()


SCHEMA = types.GenerateContentConfig(
        temperature=0.65,
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type = genai.types.Type.OBJECT,
            required = ["summary", "function", "importance_in_cancer", "therapeutic_target", "li_fraumeni_syndrome", "conclusion"],
            properties = {
                "summary": genai.types.Schema(
                    type = genai.types.Type.STRING,
                    description = "A concise textual summary of the findings.",
                ),
                "function": genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["description", "actions"],
                    properties = {
                        "description": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            description = "A detailed description of the gene's function and role in cellular processes.",
                        ),
                        "actions": genai.types.Schema(
                            type = genai.types.Type.ARRAY,
                            items = genai.types.Schema(
                                type = genai.types.Type.STRING,
                                description = "Specific actions triggered by the gene product (e.g., p53 protein).",
                            ),
                        ),
                    },
                ),
                "importance_in_cancer": genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["description", "mutations"],
                    properties = {
                        "description": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            description = "How the gene and its mutations are involved in cancer development.",
                        ),
                        "mutations": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            description = "Information on specific mutations found in the gene and their impact on cancer.",
                        ),
                    },
                ),
                "therapeutic_target": genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["description", "approaches"],
                    properties = {
                        "description": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            description = "An overview of the therapeutic significance of the gene and its product.",
                        ),
                        "approaches": genai.types.Schema(
                            type = genai.types.Type.ARRAY,
                            items = genai.types.Schema(
                                type = genai.types.Type.STRING,
                                description = "Therapeutic approaches targeting the gene or its product.",
                            ),
                        ),
                    },
                ),
                "li_fraumeni_syndrome": genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["description"],
                    properties = {
                        "description": genai.types.Schema(
                            type = genai.types.Type.STRING,
                            description = "Description of Li-Fraumeni syndrome, associated with mutations in TP53.",
                        ),
                    },
                ),
                "conclusion": genai.types.Schema(
                    type = genai.types.Type.STRING,
                    description = "A concluding statement summarizing the role of the gene in maintaining genomic stability and its therapeutic relevance.",
                ),
            },
        ),
        system_instruction=[
            types.Part.from_text(text=PROMPT),
        ],
    )


FEW_SHOT_CONTENT = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""{
  \"input\": \"TP53\"
}
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""The user wants information about the gene TP53 based on the provided schema. I need to generate a JSON object containing details about its function, role in cancer, association with Li-Fraumeni syndrome, and therapeutic relevance.

1.  **summary**: A brief overview of TP53's role.
2.  **function**:
    *   `description`: Describe TP53's function as a tumor suppressor, transcription factor, etc.
    *   `actions`: List key actions like cell cycle arrest, apoptosis, DNA repair.
3.  **li_fraumeni_syndrome**:
    *   `description`: Explain the link between germline TP53 mutations and LFS.
4.  **importance_in_cancer**:
    *   `description`: Explain why TP53 is frequently mutated in various cancers and its role as 'guardian of the genome'.
    *   `mutations`: Mention that various mutations (missense, nonsense, deletions) occur across the gene, often leading to loss of function or dominant-negative effects.
5.  **therapeutic_target**:
    *   `description`: Discuss TP53 as a target for cancer therapy.
    *   `approaches`: List strategies like gene therapy, small molecules to reactivate mutant p53, or targeting downstream pathways.
6.  **conclusion**: Summarize TP53's critical role in genomic stability and its importance in cancer research and therapy."""),
                types.Part.from_text(text="""{
  \"conclusion\": \"TP53 is a cornerstone of genomic stability and a critical tumor suppressor. Its frequent mutation in cancer highlights its importance, making it a key focus for therapeutic strategies aimed at restoring its function or targeting downstream pathways.\",
  \"function\": {
    \"actions\": [
      \"Cell cycle arrest\",
      \"Apoptosis induction\",
      \"DNA repair activation\",
      \"Senescence induction\",
      \"Metabolic regulation\"
    ],
    \"description\": \"TP53 encodes the p53 protein, a crucial tumor suppressor often called the 'guardian of the genome'. It acts primarily as a transcription factor that responds to cellular stress (like DNA damage, hypoxia, oncogene activation) by regulating genes involved in critical cellular processes to prevent uncontrolled cell growth and tumor formation.\"
  },
  \"importance_in_cancer\": {
    \"description\": \"TP53 is the most frequently mutated gene across human cancers. Its inactivation, through mutation or other mechanisms, disrupts critical checkpoints and repair pathways, allowing damaged cells to proliferate and accumulate further mutations, contributing significantly to tumorigenesis and cancer progression.\",
    \"mutations\": \"A wide range of mutations occur in TP53, including missense mutations (often in the DNA-binding domain, leading to loss of function or dominant-negative effects), nonsense mutations, frameshifts, and deletions. The specific mutation can influence tumor phenotype and response to therapy.\"
  },
  \"li_fraumeni_syndrome\": {
    \"description\": \"Li-Fraumeni Syndrome (LFS) is a rare, inherited cancer predisposition syndrome primarily caused by germline mutations in the TP53 gene. Individuals with LFS have a significantly increased risk of developing a wide spectrum of cancers, often at an early age.\"
  },
  \"summary\": \"TP53 is a critical tumor suppressor gene encoding the p53 protein, which regulates cell cycle arrest, apoptosis, and DNA repair in response to cellular stress. Mutations in TP53 are extremely common in human cancers and are the primary cause of Li-Fraumeni Syndrome. Its central role makes it a significant target for cancer therapy.\",
  \"therapeutic_target\": {
    \"approaches\": [
      \"Gene therapy (replacing or restoring wild-type p53)\",
      \"Small molecules to reactivate mutant p53\",
      \"Drugs targeting downstream pathways affected by p53 loss\",
      \"Inhibiting proteins that degrade p53 (e.g., MDM2 inhibitors)\"
    ],
    \"description\": \"The p53 pathway represents a major target for cancer therapeutics. Strategies focus on restoring wild-type p53 function in tumors where it is mutated or inactivated, or exploiting the consequences of p53 loss to selectively kill cancer cells.\"
  }
}"""),
            ],
        ),
    ]