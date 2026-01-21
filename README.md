# 📊 LangChain-Streamlit: SQL Interview

---
Repo: https://github.com/iceyisaak/langchain-streamlit-sql-interview


An interactive Streamlit application that allows users to query their SQL databases (SQLite or PostgreSQL) using natural language. Powered by **LangChain**, **Groq (Llama 3.1)**, and **SQLAlchemy**.

## 🚀 Features

* **Natural Language to SQL**: Ask questions in plain English and get data insights without writing a single line of SQL.
* **Multi-Database Support**: Connect seamlessly to a local **SQLite** database or a remote **PostgreSQL** instance.
* **Real-time Chain of Thought**: View the agent's reasoning process (SQL generation, execution, and observation) directly in the UI via `StreamlitCallbackHandler`.
* **Powered by Groq**: Leverages high-speed inference with the `llama-3.1-8b-instant` model.

---

## 🛠️ Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/)
* **LLM Framework**: [LangChain](https://www.langchain.com/)
* **Inference Engine**: [Groq Cloud](https://groq.com/)
* **Database Tooling**: SQLAlchemy, SQLite3, Psycopg2

---

## 📋 Prerequisites

Before running the app, ensure you have:

1. A **Groq API Key** (Get one at [console.groq.com](https://console.groq.com/)).
2. Python 3.9+ installed.
3. (Optional) A PostgreSQL database URI if you intend to use the Postgres feature.

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/iceyisaak/langchain-streamlit-sql-interview.git
cd langchain-streamlit-sql-interview

```


2. **Install dependencies:**
```bash
pip install streamlit langchain langchain-groq langchain-community sqlalchemy psycopg2-binary

```


3. **Database Setup:**
* For **SQLite**: Ensure a file named `student.db` exists in the root directory.
* For **PostgreSQL**: Have your host, user, password, and database name ready.


4. **Run the application:**
```bash
streamlit run app.py

```



---

## 📖 How to Use

1. **API Access**: Enter your **Groq API Key** in the sidebar.
2. **Select Database**: Choose between "Use SQLite3 DB" or "Use POSTGRESQL DB".
* If using PostgreSQL, fill in the connection credentials.


3. **Chat**: Type your question in the chat input at the bottom (e.g., *"Who are the top 5 students by grade?"*).
4. **Observe**: Watch the agent interact with the database schema and return the final result.
5. **Reset**: Use the "Clear message history" button in the sidebar to start a fresh session.

---

## 🏗️ Architecture

The app uses a **LangChain SQL Agent** with the `zero-shot-react-description` agent type. This allows the model to:

1. **Search** the database schema to understand table structures.
2. **Create** an optimized SQL query.
3. **Execute** the query and **Analyze** the results to provide a human-readable answer.

---

## ⚠️ Important Notes

* **Security**: The SQLite connection is currently set to `mode=ro` (Read Only) to prevent accidental data modification.
* **Performance**: The agent is configured with `max_iterations=50` to handle complex multi-step queries.

---