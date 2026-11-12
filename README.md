# gitai

A small command-line tool that writes your Git commit messages for you using a local LLM. Run it from inside any repo and it stages your changes, reads the diff, asks a local model (via [Ollama](https://ollama.com)) for a [Conventional Commits](https://www.conventionalcommits.org) message, and commits (and optionally pushes) for you.

Everything runs locally. Your code never leaves your machine.

## How it works

1. Checks that the current directory is inside a Git repository (exits if not).
2. Stages all changes with `git add -A`.
3. Grabs the staged diff with `git diff --cached`.
4. Sends the diff to Ollama with a prompt asking for a concise Conventional Commits message under 72 characters.
5. Shows you the generated message and asks for confirmation (`y` / `yes` to continue, anything else exits).
6. Commits with that message.
7. Pushes to your remote, if auto-push is enabled.

## Requirements

- Linux (developed on Ubuntu)
- Python 3.8+
- Git
- [Ollama](https://ollama.com) running locally
- The `requests` Python package

## Setup

### 1. Install Ollama and pull a model

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen2.5-coder:7b
```

Make sure the Ollama server is running (it listens on `http://localhost:11434` by default).

### 2. Install the Python dependency

```bash
pip install requests
```

### 3. Get the code

Clone or copy the project somewhere permanent, for example `~/tools/gitai/`. The folder should contain:

```
gitai.py
git_handler.py
llm_handler.py
generate_message.py
config.py
```

### 4. Add a shell alias

So you can run it from any repo, add an alias to your `~/.bashrc`:

```bash
alias gitai='python3 ~/tools/gitai/gitai.py'
```

Then reload your shell:

```bash
source ~/.bashrc
```

## Usage

From inside any Git repository:

```bash
gitai
```

Example session:

```
$ gitai
Commit Message: feat: add user login validation Type yes | y to continue or no | n to exit. y
```

If you're not inside a Git repo, it prints `Not in valid repo. Goodbye` and exits.

## Configuration

All settings live in `config.py`:

| Setting | Default | Description |
| --- | --- | --- |
| `OLLAMA_URL` | `http://localhost:11434` | Where your Ollama server is running. |
| `MODEL_NAME` | `qwen2.5-coder:7b` | The Ollama model used to generate messages. Any model you've pulled will work. |
| `AUTO_PUSH` | `True` | If `True`, runs `git push` after committing. If `False`, it commits only and tells you nothing was pushed. |
| `REQUIRE_CONFIRMATION` | `True` | If `True`, shows the message and asks before committing. If `False`, commits immediately. |
| `COMMIT_FORMAT` | `"conventional"` | Reserved for future use. Not currently read by the code. |
| `MAX_DIFF_SIZE` | `12000` | Reserved for future use. Not currently enforced, so very large diffs are sent in full. |

## The prompt

The prompt lives in `generate_message.py`. It asks the model to:

- Follow Conventional Commits (`feat`, `fix`, `refactor`, `docs`, `test`, `chore`)
- Keep the message under 72 characters
- Describe what changed rather than guess at intent
- Avoid inventing functionality
- Return only the commit message

Edit it there if you want a different style.

## Things to know

- **It stages everything.** `git add -A` runs every time, so all modified, new, and deleted files get included in the commit. Check `git status` first if you only want part of your work committed.
- **Auto-push is on by default.** Set `AUTO_PUSH = False` in `config.py` if you'd rather push manually.
- **Declining the confirmation prompt leaves files staged.** Exiting at the prompt skips the commit, but the `git add -A` has already happened. Use `git reset` to unstage.
- **Message quality depends on the model.** A 7B model is fast but can occasionally miss the mark, which is why confirmation is on by default.

## Project structure

| File | Purpose |
| --- | --- |
| `gitai.py` | Entry point. Runs the overall flow. |
| `git_handler.py` | Wraps the Git commands (`add`, `diff`, `commit`, `push`, repo check). |
| `llm_handler.py` | Sends the diff to Ollama and returns the response. |
| `generate_message.py` | Builds the prompt sent to the model. |
| `config.py` | User-editable settings. |
