##############################################################################
# clone, vy, vyapp, github.
cd ~/projects
git clone git@github.com:iogf/vy.git vy-code
##############################################################################
# clone, vy, wiki.
cd ~/projects
git clone git@github.com:iogf/vy.wiki.git vy.wiki-code
##############################################################################
cd /home/tau/projects/vy.wiki-code/
git pull
##############################################################################
# push, vy, vyapp, github, code, wiki.
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
# push, vy, vyapp, github, code.
cd /home/tau/projects/vy-code/
git status
git add *
git commit -a 
git push
##############################################################################
# check, pull, request, vy, avamsi.
cd /home/tau/projects/vy-code/
git checkout -b avamsi-patch-1 master
git pull https://github.com/avamsi/vy.git patch-1
##############################################################################
# merge, patch, pull, into, development, vy, avamsi, contribution.
git checkout development
git merge --no-ff avamsi-patch-1
git push origin development
##############################################################################
# vy, checkout, all, *.
cd /home/tau/projects/vy-code/
git checkout *
##############################################################################
# create, development, branch, vy.
cd /home/tau/projects/vy-code/
git branch -a
git checkout -b development
git push --set-upstream origin development
##############################################################################
# merge development into master, vy.
cd /home/tau/projects/vy-code/
git checkout master
git merge development
git push
git checkout development
##############################################################################
# merge master into development, vy.
cd /home/tau/projects/vy-code/
git checkout development
git merge master
git checkout development
git push

##############################################################################
# delete the development branch, vy.
cd /home/tau/projects/vy-code/
git branch -d development
git push origin :development
git fetch -p 
##############################################################################
# commit, undo, vy, vyapp, checkout.
cd /home/tau/projects/vy-code/
git diff
git checkout *
##############################################################################
# install, vy, from, pip2, requeriments.
cd ~/projects/vy-code
sudo bash -i
pip2 install -r requirements.txt
##############################################################################

# install, vy. 
cd ~/projects/vy-code
sudo bash -i
python2 setup.py install
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

