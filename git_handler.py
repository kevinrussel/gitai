import subprocess

class githandler:

    def run_git(self,args):

        return subprocess.run(
            ["git"] + args,
            capture_output=True,
            check=True,
            text=True
        )