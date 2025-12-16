from openai import OpenAI
import streamlit as st

# 🔑 OpenAI Client
client = OpenAI(
    api_key="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"
)

st.set_page_config(page_title="ELI5 Code Explainer", page_icon="🤖")

st.title("ELI5 Code Explainer")
st.write("Explain your Python code in very simple words.")

code_input = st.text_area(
    "Paste your Python code here:",
    height=200
)

age = st.slider(
    "Explain like I am this many years old:",
    min_value=5,
    max_value=18,
    value=5
)

if st.button("Explain Code"):
    if code_input.strip() == "":
        st.warning("Please paste some code first.")
    else:
        with st.spinner("Thinking... "):
            prompt = f"""
Explain the following Python code like I am {age} years old.
Use very simple words.

Code:
{code_input}
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You explain code very simply."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5
            )

            st.success("Explanation:")
            st.write(response.choices[0].message.content)
