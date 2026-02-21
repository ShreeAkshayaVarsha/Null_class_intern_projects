from retriever import retrieve

def chatbot():
    print("🤖 Dynamic Knowledge Chatbot (type 'exit' to quit)")
    while True:
        query = input("\nYou: ")
        if query.lower() == "exit":
            break

        docs = retrieve(query)
        response = "\n".join(docs)

        print("\nBot:", response)

chatbot()