import streamlit as st
from pathlib import Path
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
# from langchain_core.agents import AgentType
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq


st.set_page_config(page_title="Langchain: Chat with SQL DB")
st.title("Langchain Streamlit SQL Interview")


LOCALDB="USE_LOCALDB"
POSTGRESQL="USE_POSTGRES"

radio_opt=["Use SQLite3 DB", "Connect to your POSTGRESQL DB"]

selected_opt=st.sidebar.radio(label="Choose the DB you want to chat with", options=radio_opt)


if radio_opt.index(selected_opt)==1:
    db_uri=POSTGRESQL
    host=st.sidebar.text_input("Postgres Host")
    user=st.sidebar.text_input("Postgres User")
    pwd=st.sidebar.text_input("Postgres Password", type="password")
    db=st.sidebar.text_input("Postgres Database")
else:
    db_uri=LOCALDB


api_key=st.sidebar.text_input(label="Groq API Key", type="password")


if not db_uri:
    st.info("Pls enter the DB info and URI")

if not api_key:
    st.info("Pls enter your Groq API Key")


llm=ChatGroq(groq_api_key=api_key,model="llama-3.1-8b-instant",streaming=True)


@st.cache_resource(ttl="2h")
def config_db(db_uri,host=None,user=None,pwd=None,db=None):
    if db_uri==LOCALDB:
        db_file_path=(Path(__file__).parent/"student.db").absolute()
        print(db_file_path)
        creator=lambda:sqlite3.connect(f"file:{db_file_path}?mode=ro",uri=True)
        return SQLDatabase(create_engine("sqlite:///", creator=creator))
    elif db_uri==POSTGRESQL:
        if not (host and user and pwd and db):
            st.error("Pls provide all Postgresql connection details")
            st.stop()
        return SQLDatabase(create_engine(f"postgres+postgresconnector://{user}:{pwd}@{host}/{db}"))
    

if db_uri==POSTGRESQL:
    db=config_db(db_uri,host,user,pwd,db)
else:
    db=config_db(db_uri)


################################################################# Toolkit


toolkit=SQLDatabaseToolkit(db=db,llm=llm)

agent=create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    agent_type='zero-shot-react-description'
)

if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"]=[{
        "role":"assistant",
        "content":"How can I help you?"
    }]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_query=st.chat_input(placeholder="Ask anything from the Database")


if user_query:
    st.session_state.messages.append({
        "role":"user",
        "content":user_query
    })
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        streamlit_callback=StreamlitCallbackHandler(st.container())
        response=agent.run(user_query,callbacks=[streamlit_callback])
        st.session_state.messages.appand({
            "role":"assistant",
            "content":response
        })
        st.write(response)