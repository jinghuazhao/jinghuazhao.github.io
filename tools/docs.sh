#!/usr/bin/bash

function gh_pages()
{
  cd docs/_site || return
  git init
  git checkout -B gh-pages
  git add -A
  git commit -m "Deploy site $(date +'%Y-%m-%d %H:%M:%S')" || echo "No changes to commit"
  git remote remove origin 2>/dev/null
  git remote add origin https://github.com/jinghuazhao/jinghuazhao.github.io
  git push --force origin gh-pages
  cd - || return
}

rm -rf docs/_site/*
cd docs
bundle exec jekyll build
cd -
gh_pages

module load gettext/0.21/gcc/qnrcglqo
module load libiconv/1.16/gcc/4miyzf3w

if [ "$(uname -n | sed 's/-[0-9]*$//')" == "login-q" ]; then
   echo icelake
   module load ceuadmin/libssh/0.10.6-icelake
   module load ceuadmin/openssh/9.7p1-icelake
fi

git ls-files --others --exclude-standard -z | while IFS= read -r -d '' f; do
    echo "Adding new file $f"
    git add "$f"
    git commit -m "Add $f"
done

git diff --name-only -z | while IFS= read -r -d '' f; do
   echo "Processing $f"
   git add ${f}
   git commit -m "${f}"
done
git push
du -hs --exclude .git --exclude docs/_site
