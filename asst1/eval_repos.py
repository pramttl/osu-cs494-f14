"""
CS494: Oregon State University: Assigment 1: Evaluation tool

This code assumes that it is being run in a current a directory which contains all
the git repositories to be examined.

* This code does not clone repositories so please clone all the repositories before hand
  and put their names in a text file say 'repos.txt' like this:

    repo1_name
    repo2_name
    ...

* python eval_repos.py < repos.txt
"""

import os
import subprocess
repo_names = raw_input()


def run_command(cmd):
    process = subprocess.Popen(cmd, shell=True,
	                           stdout=subprocess.PIPE, 
	                           stderr=subprocess.PIPE)
	# wait for the process to terminate
    out, err = process.communicate()
    return out


repo_names = repo_names.split('\n')
for repo in repo_names:

    # Initalizating grading_conditions for current repo
    grading_conditions = {'programming-bio-present': False, 'programming-bio-merged': False, 'bio-md-present': False,}

    # Checking if programming-bio branch is present
    out = run_command('cd ' + repo + '&& git branch -a')
    l = out.split('\n ')
    l = [e.strip() for e in l]
    if 'remotes/origin/programming-bio' in l:
        grading_conditions['programming-bio-present'] = True


    # To see which branches are merged in master and check whether programming-bio is merged.
    out = run_command('cd ' + repo + '&& git branch -a --merged')
    l = out.split('\n ')
    l = [e.strip() for e in l]
    if 'remotes/origin/programming-bio' in l:
        grading_conditions['programming-bio-merged'] = True

    out = run_command('cd ' + repo + '&& ls')
    files = out.split('\n')
    if 'bio.md' in files:
        grading_conditions['bio-md-present'] = True

    print repo, grading_conditions
