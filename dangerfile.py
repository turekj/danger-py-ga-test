title = danger.github.pr.title
message(title)
warn(f"Modified {len(danger.git.modified_files)} files in the PR")
fail(f"{danger.github.pr.user.login} can't code for hell")
