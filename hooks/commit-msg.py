#!/usr/bin/env python3
"""
Git commit hook:
./hooks/commit-msg
Check commit message according to guidelines
"""

#REGEX = '^(JR|jr)\: [A-Z]-[0-9]+; .'
import git
import sys, re, subprocess

def main(message):
    """Main function."""
    #Required parts
    repo = git.Repo(search_parent_directories=True)
    branch = repo.active_branch

    print("[INFO]: Currnet branch name:" , branch.name)
    projectIDs = ['WBS', 'MX']
    jiraIDs = ['JR', 'jr']

    regexpJiraIDs = '|'.join(jiraIDs)
    regexpProjectIDs = '|'.join(projectIDs)

    requiredRegex = '^((?:{})): ((?:{})-[\d]{{1,5}}); .+\.?$'.format(regexpJiraIDs, regexpProjectIDs)
    requiredLength = 15

    guidelineUrl = 'https://confluence.zultys.com:8443'

    #Get the commit file
    commitMessageFile = open(message) #The first argument is the file
    commitMessage = commitMessageFile.read().strip()

    if branch.name == "main":
        print("[INFO]: Ready to commit the change in master")
        sys.exit(0)

    if len(commitMessage) < requiredLength:
        print("[ERROR]: Commit message is less than the required 15 characters.")
        sys.exit(1)

    if not re.match(requiredRegex, commitMessage):
        sys.stderr.write("\n[ERROR]: Your commit message subject line does not follow the guideline\n")
        sys.stderr.write("\n - Refer commit guideline: {}\n\n".format(guidelineUrl))
        sys.exit(1)
    else:
        print("[INFO]: Commit message is validated")
        sys.exit(0)
            
    

if __name__ == "__main__":
    main(sys.argv[1])

