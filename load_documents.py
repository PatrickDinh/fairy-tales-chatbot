from langchain_community.document_loaders.directory import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from database import clean_db, get_db

DATA_PATH = "data"

def main():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)

# Load the documents from the data directory.
def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.txt")
    documents = loader.load()
    return documents

# Split the documents into smaller chunks.
def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )

    # Each chunk has
    # - the text content
    # - metadata (e.g. filename, location)
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    return chunks

# Save the chunks to the database.
def save_to_chroma(chunks: list[Document]):
    print(f"Saving {len(chunks)} chunks to Chroma.")

    # Clear out the database first.
    clean_db()

    # Create a new DB and load the chunks into it.
    db = get_db()
    db.add_documents(chunks)

    print(f"Saved {len(chunks)} chunks to Chroma.")


if __name__ == "__main__":
    main()