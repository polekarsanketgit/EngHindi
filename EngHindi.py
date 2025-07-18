import streamlit as st
from openai import OpenAI

# Page settings
st.set_page_config(page_title="English to Hindi Translator", page_icon="🌐")

# Sidebar: API key input
st.sidebar.title("🔑 OpenAI API Key")
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

# Main title
st.title("🌍 English to Hindi Translator")

# Text input
text_input = st.text_area("✏️ Enter English Text to Translate (Max 100 words):", height=150)

# Word count helper
def count_words(text):
    return len(text.strip().split())

# Submit button
if st.button("Translate"):
    if not api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
    elif not text_input.strip():
        st.warning("Please enter some English text.")
    elif count_words(text_input) > 100:
        st.warning(f"🚫 Text is too long! You entered {count_words(text_input)} words. Please limit to 100 words.")
    else:
        try:
            # Initialize OpenAI client
            client = OpenAI(api_key=api_key)

            prompt = f"Translate the following English text into Hindi:\n{text_input}"

            # GPT-4 Translation
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )

            hindi_translation = response.choices[0].message.content
            st.success("✅ Translation Completed!")
            st.text_area("📝 Hindi Translation:", value=hindi_translation, height=200)
        except Exception as e:
            st.error(f"Error: {str(e)}")
