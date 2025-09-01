from dotenv import load_dotenv
import os
import openai
import streamlit as st

# Load environment variables from .env file
load_dotenv()
# Debugging: Print all environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")


# Debugging: Ensure API key is loaded correctly
if not openai.api_key:
    st.error("OpenAI API key is not set. Please check your .env file.")
    st.stop()

# Streamlit app title and descriptionr
st.title("マーケティングと商品開発相談AI")
st.write("### 下記AとBのどちらのAIモデルを選択してください")
st.write("#### 選択A: マーケティングに関する質問")
st.write("#### 選択B: 商品開発に関する質問")

# User input for question type
select = st.radio(
    "質問の種類を選択してください",
    ["A:マーケティング", "B:商品開発"]
)

# Determine genre based on selection
genre = "マーケティング" if select == "A" else "商品開発"

st.divider()

# User input for question
question = st.text_input(f"{genre}に関する質問を入力してください:")

# Generate response when button is clicked
if st.button("回答を生成") and question:
    st.divider()
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"あなたは、{genre}の領域においての専門家です。ユーザーからの質問に100文字以内で回答してください。"},
                {"role": "user", "content": question}
            ],
            temperature=0.5,
        )
        st.write(response.choices[0].message["content"])
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")