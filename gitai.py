
from llm_handler import llmhandler
from generate_message import build_prompt
from git_handler import githandler
def main():




    while True:
        # response = llmhandler.llm_response(message)
        git_check = githandler()
        if(git_check.check_if_valid_repo()):
            print("In a repo")
        else:
            print("not in a repo")
        break
        # print(response)


if __name__ == '__main__':
    main()