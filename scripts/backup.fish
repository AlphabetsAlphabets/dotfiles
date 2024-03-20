#!/usr/bin/fish

set note_dir /home/star/Documents/notes/

cd $note_dir

set today (date "+(%A) %B-%d-%G %T")

git add . 
git commit -am $today
env GIT_SSH_COMMAND='ssh -i ~/.ssh/obsidian_notes' git push
