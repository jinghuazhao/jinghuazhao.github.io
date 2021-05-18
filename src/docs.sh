#!/usr/bin/bash

cd docs
bundle exec jekyll build
cd -
for f in $(ls)
do
  git add ${f}
  git commit -m "${f}"
done
git push
