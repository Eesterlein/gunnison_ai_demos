# Gunnison AI Demos

Two small Streamlit prototypes exploring how AI could support a county assessor's office.

| Demo | What it shows |
|---|---|
| [`ai_change_detection`](ai_change_detection/app.py) | Before/after aerial imagery with a highlighted new structure, illustrating how automated detection could surface unpermitted building changes for review. (A concept mock-up; see [Gunnison Property Eye](https://github.com/Eesterlein/gunnison-property-eye) for the working satellite-based version.) |
| [`document_assistant`](document_assistant/letter_generator_app.py) | A GPT-based assistant that drafts appeal responses, exemption notices, valuation explanations and general inquiry replies in a chosen tone. |

> **Independent project.** This is an independent project and is not an official product of the Gunnison County Assessor's Office or Gunnison County. Any county data it works with comes from publicly available assessor and GIS data, and results may contain errors or out-of-date information. Always verify against official county records.

## Running

```bash
pip install -r requirements.txt
streamlit run ai_change_detection/app.py
# or
echo "OPENAI_API_KEY=sk-..." > .env
streamlit run document_assistant/letter_generator_app.py
```
