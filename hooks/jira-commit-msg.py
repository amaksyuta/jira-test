#!/usr/bin/env python
"""
Git commit hook:
./hooks/commit-msg
Check commit message according to guidelines
"""

import sys
import re
import subprocess

#REGEX = '^(JR|jr)\: [A-Z]-[0-9]+; .'

#e.g. ^(feat|fix|docs|style|refactor|test|build|ci|perf)((.+))?\:\s(.{3,})
GUIDELINE_LINK = 'https://confluence.zultys.com:8443'

#e.g. https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit

#commit_msg_filepath = sys.argv[1]

#with open(commit_msg_filepath) as commit:
#    lines = commit.readlines()
#    if len(lines) == 0:
#        sys.stderr.write("\n[ERROR]: Empty commit message\n")
#        sys.stderr.write("\n - Refer commit guide: {}\n\n".format(help_address))
#        sys.exit(1)
#    match_regex = re.match('({})'.format(REGEX), lines[0])
#    if match_regex is None:
#        sys.stderr.write("\n[ERROR]: Your commit message subject line does not follow the guideline\n")
#        sys.stderr.write("\n - Refer commit guideline: {}\n\n".format(GUIDELINE_LINK))
#        sys.exit(1)
#    else:
#        sys.stderr.write("\n[INFO]: Your commit message looks good! \n\n")
#        sys.exit(0)

MESSAGE_REGEX = '^DDC-[\d]{4}\. [\w\d .,:;+]*\.$'
BRANCHNAME_REGEX = '*main*' #should contain a capturing group

def get_jira_issue_hint(branch_name):
    """Extracts the Jira issue number from the branch name.
    Args:
        branch_name (str): The branch name to parse.
    Returns:
        string: The Jira issue number, or sample issue number.
    """
    match = re.findall(BRANCHNAME_REGEX, branch_name)
    if match and match[0]:
        return match[0]
    return 'DDC-XXXX'

def current_branch_name():
    """Gets the current GIT branch name.
    Returns:
        string: The current branch name.
    """
    return subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])


def valid_commit_message(message):
    """Function to validate the commit message.
    Args:
        message (str): The message to validate.
    Returns:
        bool: True for valid messages, False otherwise.
    """
    with open(message) as commit:
        lines = commit.readlines()
        if len(lines) == 0:
            sys.stderr.write("\n[ERROR]: Empty commit message\n")
            sys.stderr.write("\n - Refer commit guide: {}\n\n".format(help_address))
            sys.exit(1)
    if not re.match(MESSAGE_REGEX, message):
        name = current_branch_name()
       # issue_number = get_jira_issue_hint(name)
        print("[INFO]: Current branch is %s", name)
        print("[ERROR]: Missing Jira number in commmit message.")
        #print 'Hint: {0}. Commit message.'.format(issue_number)
        return False
    print("Commit message is valid.")
    return True

def main():
    """Main function."""
    message_file = sys.argv[1]
    try:
        txt_file = open(message_file, 'r')
        commit_message = txt_file.read()
    finally:
        txt_file.close()
    if not valid_commit_message(commit_message):
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
