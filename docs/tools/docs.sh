#!/usr/bin/bash

function gh_pages()
{
  cd docs/_site
  git checkout -b gh-pages
  git add -f *
  git commit -m "_site"
  git push --set-upstream origin gh-pages
  cd -
}

cd docs
bundle exec jekyll build
cd -

module load gettext/0.21/gcc/qnrcglqo
module load libiconv/1.16/gcc/4miyzf3w

if [ "$(uname -n | sed 's/-[0-9]*$//')" == "login-q" ]; then
   echo icelake
   module load ceuadmin/libssh/0.10.6-icelake
   module load ceuadmin/openssh/9.7p1-icelake
fi

git diff --name-only -z | while IFS= read -r -d '' f; do
   echo "Processing $f"
   git add ${f}
   git commit -m "${f}"
done
git push
du -hs --exclude .git --exclude docs/_site
