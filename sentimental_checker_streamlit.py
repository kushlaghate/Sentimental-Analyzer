import streamlit as st


def sentiment_checker(text):
    text = text.lower()
    
    happy_words = ['good', 'great', 'amazing', 'wonderful', 'love', 'excellent', 'nice']
    sad_words = ['bad', 'terrible', 'awful', 'horrible', 'hate', 'disappointed']

    happy_count = sum(1 for word in text.split() if word in happy_words)
    sad_count = sum(1 for word in text.split() if word in sad_words)

    if happy_count > sad_count:
        return "😊 Positive"
    elif sad_count > happy_count:
        return "☹️ Negative"
    else:
        return "😐 Neutral"


st.title("Simple Sentiment Checker")
st.write("Enter a sentence below to analyze its sentiment.")


user_input = st.text_area("Enter your text here:", "")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        result = sentiment_checker(user_input)
        st.success(f"**Sentiment:** {result}")
    else:
        st.warning("Please enter some text to analyze.")
