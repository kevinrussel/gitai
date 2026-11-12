def build_prompt(diff):

    return f"""
You are an expert software engineer.

Analyze the following Git diff and generate
a concise, meaningful commit message.

Follow Conventional Commits.

Use one of:
feat, fix, refactor, docs, test, chore.

Requirements:
- Keep the message under 72 characters.
- Describe what changed, not what you think
  the developer intended.
- Do not invent functionality.
- Return only the commit message.

Git diff:{diff}
"""