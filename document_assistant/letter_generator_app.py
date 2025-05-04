import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="GPT Document Assistant", layout="centered")
st.title("📄 GPT-Based Correspondence & Document Assistant")

st.markdown("""
This assistant generates professional letters and summaries for the Gunnison County Assessor’s Office. Choose a document type and provide relevant details below.
""")

# Letter types
letter_types = {
    "Appeal Response Letter": "Respond to a property owner’s appeal of their property valuation.",
    "Exemption Notice": "Notify a property owner of their exemption approval or denial.",
    "Valuation Explanation": "Explain the basis of a property’s assessed value.",
    "General Inquiry Response": "Respond to a resident’s question or complaint."
}

letter_type = st.selectbox("Select Document Type:", list(letter_types.keys()))

user_input = st.text_area("Enter relevant details or paste the email/request text:")
tone = st.selectbox("Select Tone:", ["Professional", "Friendly", "Formal"])

if st.button("Generate Document"):
    if not user_input:
        st.warning("Please enter some information to generate a response.")
    else:
        prompt = f"""
You are an AI assistant helping a county assessor's office generate professional correspondence.
Create a {tone.lower()} {letter_type.lower()} based on the following details:

{user_input}

Ensure the response is clear, concise, and appropriate for public communication.
        """

        with st.spinner("Generating document..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a professional assistant for a county assessor's office."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                document = response.choices[0].message.content
                st.success("Document generated!")
                st.text_area("Generated Document:", document, height=300)
            except Exception as e:
                st.error(f"Error generating document: {str(e)}")
