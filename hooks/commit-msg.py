#!/usr/bin/env python3
"""
Git commit hook:
./hooks/commit-msg
Check commit message according to guidelines
"""

#REGEX = '^(JR|jr)\: [A-Z]-[0-9]+; .'
import git
import sys, re, subprocess

repo = git.Repo(search_parent_directories=True)
branch = repo.active_branch

print("[INFO]: Currnet branch name:" + branch.name)
print("[INFO]: Start to commit the change in git")

#Required parts
requiredRegex = "^(JR|jr)\: [A-Z]-[0-9]+; ."
requiredLength = 15

#Get the commit file
commitMessageFile = open(sys.argv[1]) #The first argument is the file
commitMessage = commitMessageFile.read().strip()

if branch.name == "main":
    print("[INFO]: Ready to commit the change in master")
    sys.exit(0)

if len(commitMessage) < requiredLength:
    print("[ERROR]: Commit message is less than the required 15 characters.")
    sys.exit(1)

if re.search(requiredRegex, commitMessage) is None:
    print("[ERROR]: A JIRA Keyword must be filled with a commit")
    sys.exit(1)
    
print("[INFO]: Commit message is validated")
sys.exit(0)
