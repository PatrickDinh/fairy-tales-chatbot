from typing import List, Tuple
import streamlit as st
from collections.abc import Iterator
from langchain.chat_models.ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from database import get_db

st.set_page_config(
    page_title="Fairy tales chatbot",
)
st.title("Fairy tales chatbot")

def main() -> None:
    query = st.text_input("Ask me about fairy tales")

    answer_container = st.empty()
    source_container = st.empty()
    if query:
        documents = search_for_related_documents(query)
        print(documents)
        if (len(documents) == 0):
            answer_container.write("Sorry, I couldn't find any related documents.")
        else:
            answer_container.write_stream(ask_the_chatbot(query, documents))
            source_container.write("Sources:  \n" + "  \n".join([f"{doc.metadata["source"]} - block: {doc.metadata['start_index']}" for doc, _ in documents]))

PROMPT_TEMPLATE = """
Given the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def search_for_related_documents(query_text: str) -> List[Tuple[Document, float]]:
    db = get_db()
    return db.similarity_search_with_relevance_scores(query_text, k=4)

def ask_the_chatbot(query_text: str, documents: List[Tuple[Document, float]]) -> Iterator:
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in documents])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    model = ChatOllama(model="llama3")
    return model.stream(prompt)

main()