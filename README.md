# 🎯 AI Career Guidance Chatbot

An intelligent career recommendation system that helps students and professionals discover suitable career paths based on their skills, interests, and educational background.

Built using **Python**, **Streamlit**, **Pandas**, and **Scikit-Learn**, the system analyzes user input and recommends the most relevant careers using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 🚀 Features

* Career recommendations based on skills and interests
* Match score calculation
* Salary insights
* Future demand analysis
* Industry information
* Career growth path suggestions
* Modern and interactive Streamlit UI
* Dataset-driven recommendations
* No external API required

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-Learn
* TF-IDF Vectorizer
* Cosine Similarity

---

## 📂 Project Structure

```text
AI_Career_Guidance_Chatbot/
│
├── app.py
├── AI_Career_Dataset_75_Careers.csv
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The dataset contains career-related information including:

* Career Name
* Skills Required
* Education Requirements
* Industry
* Salary Range
* Future Demand
* Work Mode
* Growth Score
* AI Impact
* Career Growth Path
* Career Description

The dataset currently contains **75 career profiles** across multiple domains such as:

* Artificial Intelligence
* Data Science
* Software Development
* Cloud Computing
* Cyber Security
* DevOps
* UI/UX Design
* Finance
* Healthcare
* Marketing
* Robotics
* Blockchain

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Career-Guidance-Chatbot.git

cd AI-Career-Guidance-Chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. User enters skills, interests, or background.
2. The system converts skills into numerical vectors using TF-IDF.
3. Cosine Similarity is calculated between user input and all careers in the dataset.
4. Top matching careers are ranked.
5. Career recommendations are displayed with:

   * Match Score
   * Salary Range
   * Future Demand
   * Industry
   * Growth Path

---

## 🎯 Example Input

```text
Python, SQL, Machine Learning, Statistics
```

### Recommended Careers

* Data Scientist
* Machine Learning Engineer
* AI Engineer

---

## 📈 Future Enhancements

* Skill Gap Analysis
* Career Comparison Dashboard
* Career Roadmap Generation
* Resume-Based Career Recommendations
* PDF Career Reports
* AI Chat Assistant Integration
* Personalized Learning Recommendations

---

## 📸 Screenshots

### Home Page

<img width="1920" height="1080" alt="Screenshot (33)" src="https://github.com/user-attachments/assets/ce3e448b-a761-4631-af11-7115be2e20b1" />


### Career Recommendations

<img width="1920" height="1080" alt="Screenshot (34)" src="https://github.com/user-attachments/assets/ec130145-8b1b-459a-9ad8-84783408dfc3" />


---

## 👨‍💻 Author

**Rakibul Islam**

Registration Number: 12317006

Lovely Professional University

---

## 📄 License

This project is licensed under the MIT License.
