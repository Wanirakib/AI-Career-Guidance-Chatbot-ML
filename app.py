import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="AI Career Guidance Chatbot",
    page_icon="🎯",
    layout="wide"
)

# ---------- CSS ----------

st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

.title {
    text-align:center;
    color:white;
    font-size:50px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#9ca3af;
}

.card {
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    margin-bottom:15px;
    border:1px solid #334155;
}

.salary{
    color:#22c55e;
    font-weight:bold;
}

.demand{
    color:#38bdf8;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------

st.markdown(
    "<div class='title'>🎯 AI Career Guidance Chatbot</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Discover your ideal career path using AI</div>",
    unsafe_allow_html=True
)

st.write("")

# ---------- DATA ----------

df = pd.read_csv("AI_Career_Dataset.csv")

# ---------- INPUT ----------

skills = st.text_area(
    "Enter Your Skills / Interests",
    placeholder="Python, SQL, Machine Learning, Data Analysis..."
)

# ---------- RECOMMEND ----------

if st.button("🚀 Find My Career"):

    if skills:

        corpus = df["Skills_Required"].astype(str)

        vectorizer = TfidfVectorizer()

        vectors = vectorizer.fit_transform(corpus)

        query = vectorizer.transform([skills])

        similarity = cosine_similarity(query, vectors)[0]

        top = similarity.argsort()[-5:][::-1]

        st.success("Top Career Matches Found!")

        for idx in top:

            row = df.iloc[idx]

            score = round(similarity[idx] * 100)

            st.markdown(f"""
            <div class="card">

            <h2>{row['Career']}</h2>

            <p>🎯 Match Score: <b>{score}%</b></p>

            <p>🎓 Education:
            {row['Education']}</p>

            <p>🏢 Industry:
            {row['Industry']}</p>

            <p class="salary">
            💰 Salary:
            {row['Salary_Range']}
            </p>

            <p class="demand">
            📈 Demand:
            {row['Future_Demand']}
            </p>

            <p>
            🧠 Skills:
            {row['Skills_Required']}
            </p>

            <p>
            🚀 Growth Path:
            {row['Growth_Path']}
            </p>

            </div>
            """,
            unsafe_allow_html=True)

# ---------- SIDEBAR ----------

with st.sidebar:

    st.title("📊 About")

    st.info(
        """
        AI Career Guidance System

        Features:
        ✔ Career Recommendation
        ✔ Skill Matching
        ✔ Future Demand Analysis
        ✔ Salary Insights
        ✔ Growth Path Prediction
        """
    )

    st.metric("Careers", len(df))

    st.metric("Recommendation Engine", "TF-IDF")

    st.metric("Similarity", "Cosine")