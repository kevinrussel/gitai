
from llm_handler import llmhandler
from generate_message import build_prompt
from git_handler import githandler
import config
def main():

    git_check = githandler()
    if(not git_check.check_if_valid_repo()):
        print("Not in valid repo. Goodbye")
        return
    else:
        git_check.git_add()
        difference = git_check.git_diff()
        llm_response = llmhandler.llm_response(difference)

        if(config.REQUIRE_CONFIRMATION):
            user_agreement = input(f"Commit Message: {llm_response} Type yes | y to continue or no | n to exit. ")
            if(not user_agreement == "y" and not user_agreement == "yes"):
                return
        
        git_check.git_commit(llm_response)

        if( not config.AUTO_PUSH):
            print("All files have been added, none have been pushed")
            return
        git_check.git_push()


if __name__ == '__main__':
    main()