from chatgpt import generate_response

def main():
    print("ChatGPT Initialized. Ask a question or type 'exit' to quit.")

    while True:
        user_input = input("User: ")

        if user_input.lower() == "exit":
            print("ChatGPT session ended.")
            break

        response = generate_response(user_input)
        print("ChatGPT: " + response)

if __name__ == "__main__":
    main()
