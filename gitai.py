
from llm_handler import llmhandler
from generate_message import build_prompt

def main():




    while True:
        message = input("Enter a message")
        response = llmhandler.llm_response(message)
        print(response)


if __name__ == '__main__':
    main()