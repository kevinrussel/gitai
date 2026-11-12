import subprocess

class githandler:

    def run_git(self,args):

        return subprocess.run(
            ["git"] + args,
            capture_output=True,
            check=True,
            text=True
        )


    def check_if_valid_repo(self):

        try:
            self.run_git(["rev-parse", "--is-inside-work-tree"])
            return True
        except subprocess.CalledProcessError:
            return False
    
            