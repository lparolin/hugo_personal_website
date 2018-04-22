#!/bin/sh

echo "Creating language files"
cd scripts
python generate_other_language_files.py
rc=$?; if [[ $rc != 0 ]]; then cd .. && exit $rc; fi
cd ..

echo "Compiling website"
rm -rf public/*
hugo
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi

echo "Minimizing public folder content"
css-html-js-minify --overwrite ./public
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi

echo "Adding .htaccess file to public folder"
cp .htaccess public/
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi

echo "Uploading website"
rsync -avz --delete public/ a2_website:/home/annmarie/lucaparolini.com
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi

echo "Deployment succesful"
exit 0
