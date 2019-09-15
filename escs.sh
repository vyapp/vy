##############################################################################
# clone repo.
cd ~/projects
git clone git@github.com:iogf/vy.git vy-code
##############################################################################
# clone wiki.
cd ~/projects
git clone git@github.com:iogf/vy.wiki.git vy.wiki-code
##############################################################################
cd /home/tau/projects/vy.wiki-code/
git pull
##############################################################################
# push vy wiki docs.
cd /home/tau/projects/vy.wiki-code/
git status
git add *
git commit -a 
git push

##############################################################################
# delete, remove, clean, *.pyc files, vy, vyapp.
cd /home/tau/projects/vy-code/
find . -name "*.pyc" -exec rm -f {} \;
##############################################################################
# push vy code.
cd /home/tau/projects/vy-code/
git status
git add *
git commit -a 
git push
##############################################################################
git commit -m 'Fixing setup.py version.'
##############################################################################
# check avamsi patch.
cd /home/tau/projects/vy-code/
git checkout -b avamsi-patch-1 master
git pull https://github.com/avamsi/vy.git patch-1

# merge the patch.
git checkout development
git merge --no-ff avamsi-patch-1
git push origin development
##############################################################################
# check pull request by yetone.
cd /home/tau/projects/vy-code/
git checkout -b yetone-patch-1 master
git pull https://github.com/yetone/vy.git patch-1

git checkout development
git merge --no-ff avamsi-patch-1
git push origin development

##############################################################################
# check out all.
cd /home/tau/projects/vy-code/
git checkout *
##############################################################################
# create dev branch.
cd /home/tau/projects/vy-code/
git branch -a
git checkout -b development
git push --set-upstream origin development
##############################################################################
# merge development into master.
cd /home/tau/projects/vy-code/
git checkout master
git merge development
git push
git checkout development
##############################################################################
# merge master into development.
cd /home/tau/projects/vy-code/
git checkout development
git merge master
git checkout development
git push

##############################################################################
# delete the development branch.
cd /home/tau/projects/vy-code/
git branch -d development
git push origin :development
git fetch -p 
##############################################################################
# check diffs.
cd /home/tau/projects/vy-code/
git diff
git checkout *
##############################################################################
# install from pip requirements.
cd ~/projects/vy-code
sudo bash -i
pip2 install -r requirements.txt
##############################################################################
# install, vy. 
cd ~/projects/vy-code
sudo bash -i
python setup.py install
rm -fr build
exit
##############################################################################
# preview, check, markdown, vy, github, compile, transform, convert, html.
cd /home/tau/projects/vy-code
markdown README.md > README.html
google-chrome README.html
rm README.html
##############################################################################
# generate, table of contents, vy, markdown, BOOK.md
cd /home/tau/projects/vy-code
gh-md-toc BOOK.md >> table.md
vy table.md
rm table.md
##############################################################################
# remove, uninstall, delete global, vy, vyapp, installation, package.
sudo bash -i
rm -fr /home/tau/.vy
rm -fr /usr/local~/projects/python2.7/dist-packages/vyapp
rm /usr/local~/projects/python2.7/dist-packages/vy-*.egg-info
exit
##############################################################################
# build, make, a tarball, tar.gz, sdist, vy, vyapp.
cd /home/tau/projects/vy-code
python2.6 setup.py sdist 
rm -fr dist
rm MANIFEST
##############################################################################
# share, put, place, host, package, python, pip, application, vy, pypi.

cd ~/projects/vy-code
python setup.py sdist register upload
rm -fr dist
##############################################################################

# install, tern-chrome-extesion, get, autocompletion, chrome, plugins, development, vy.

# BROKEN!

sudo npm -g install tern-chrome-extension

# example tern-project, tern-config.

# {
  # "libs":["ecma5"],
  # "plugins": {
    # "chrome-extension": {}
  # }
# }

vy ~/.tern-config
##############################################################################

grep -rl  'CompletionWindow' . | xargs sed -i 's/CompletionWindow/CompletionWindow/g' 


ls -dla -1 $PWD/*
ls -d --all  /home/tau/*
ls -d --all  /home/tau/*.*
grep -rl  '<Key-g>' .
grep -rl  '<Control-g>' .

##############################################################################
# futurize code.

cd ~/projects/vy-code

# Apply them.
2to3  -w .

find . -name "*.bak" -exec rm -f {} \;

##############################################################################
git rm --cached -r build

l Control-bar
l Key-bar
##############################################################################
# install ycmd from source.

cd ~/bin/
git clone git@github.com:ycm-core/ycmd.git ycmd-code
cd ycmd-code
ls
git submodule update --init --recursive
ls

# typescript is for tsserver. clang is for c-family completion.
pacman -S clang cmake gcc-c++ make python3-devel typescript python3-dev

# Compiling ycmd with all features. The --cs-completer, -go-completer are 
# flags to install the necessary tools.
python3 install.py --all --cs-completer -go-completer --rust-completer --java-completer --clang-completer




