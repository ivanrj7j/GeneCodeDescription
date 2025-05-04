# GeneCodeDescription

**A Python-based tool for analyzing genomic sequences and optional cellular images to predict gene functions and phenotypes.**

---

## 🔑 Key Features

* Genomic sequence analysis (FASTA format)
* Cellular image analysis (JPEG/PNG)
* Multimodal integration of genomic and image data
* Customizable schema for output formats and validation protocols
* Streamed output for real-time processing

---

## ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ivanrj7j/GeneCodeDescription
   ```
2. Navigate to the project directory:

   ```bash
   cd GeneCodeDescription
   ```
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Set up an API key from [Google's GenAI platform](https://genai.google.com/)

---

## 🚀 Usage

```python
from src import GeneDescriptor, ModelInput
from env import GEMINI_API_KEY, GEMINI_MODEL_NAME

inp = ModelInput("TP53", image="...")

descriptor = GeneDescriptor(GEMINI_API_KEY, GEMINI_MODEL_NAME)
print(descriptor.getDescription(inp, False, False))
```

---

## 📥 Input Requirements

* **Genomic sequence**: Valid nucleotide sequence (A, T, C, G)
* **Cellular image**: High-resolution JPEG/PNG (optional)

---

## 📤 Output Format

Returns a JSON object:

```json
{
  "summary": "TP53 is a critical tumor suppressor gene encoding the p53 protein, which regulates cell cycle arrest, apoptosis, and DNA repair in response to cellular stress. Mutations in TP53 are extremely common in human cancers and are the primary cause of Li-Fraumeni Syndrome. Its central role makes it a significant target for cancer therapy.",
  "function": {
    "description": "TP53 encodes the p53 protein, a crucial tumor suppressor often called the 'guardian of the genome'. It acts primarily as a transcription factor that responds to cellular stress (like DNA damage, hypoxia, oncogene activation) by regulating genes involved in critical cellular processes to prevent uncontrolled cell growth and tumor formation.",
    "actions": [
      "Cell cycle arrest",
      "Apoptosis induction",
      "DNA repair activation",
      "Senescence induction",
      "Metabolic regulation"
    ]
  },
  "importance_in_cancer": {
    "description": "TP53 is the most frequently mutated gene across human cancers. Its inactivation, through mutation or other mechanisms, disrupts critical checkpoints and repair pathways, allowing damaged cells to proliferate and accumulate further mutations, contributing significantly to tumorigenesis and cancer progression.",
    "mutations": "A wide range of mutations occur in TP53, including missense mutations (often in the DNA-binding domain, leading to loss of function or dominant-negative effects), nonsense mutations, frameshifts, and deletions. The specific mutation can influence tumor phenotype and response to therapy."
  },
  "therapeutic_target": {
    "description": "The p53 pathway represents a major target for cancer therapeutics. Strategies focus on restoring wild-type p53 function in tumors where it is mutated or inactivated, or exploiting the consequences of p53 loss to selectively kill cancer cells.",
    "approaches": [
      "Gene therapy (replacing or restoring wild-type p53)",
      "Small molecules to reactivate mutant p53",
      "Drugs targeting downstream pathways affected by p53 loss",
      "Inhibiting proteins that degrade p53 (e.g., MDM2 inhibitors)"
    ]
  },
  "li_fraumeni_syndrome": {
    "description": "Li-Fraumeni Syndrome (LFS) is a rare, inherited cancer predisposition syndrome primarily caused by germline mutations in the TP53 gene. Individuals with LFS have a significantly increased risk of developing a wide spectrum of cancers, often at an early age."
  },
  "conclusion": "TP53 is a cornerstone of genomic stability and a critical tumor suppressor. Its frequent mutation in cancer highlights its importance, making it a key focus for therapeutic strategies aimed at restoring its function or targeting downstream pathways."
}
```

---

## ⚙️ Configuration

* Located in `config.py`
* Schema and prompt can be customized for different needs

---

## 📁 Examples

* Refer to `prompt.md` for example prompts and outputs

---

## 📜 License

MIT License

---

## 🤝 Contributing

* Open to pull requests and issue submissions

---

## 📬 Contact

* Email: [ivanrj7j@gmail.com](mailto:ivanrj7j@gmail.com)
* GitHub: [GeneCodeDescription](https://github.com/ivanrj7j/GeneCodeDescription)