#!/bin/sh

echo "Creating language files"
cd scripts
python generate_other_language_files.py
rc=$?; if [[ $rc != 0 ]]; then cd .. && exit $rc; fi
cd ..

echo "Compiling website"
hugo
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi

echo "Minimizing public folder content"
css-html-js-minify --overwrite ./public
rc=$?; if [[ $rc != 0 ]]; then exit $rc; fi
exit 0
#
# echo "Uploading website"
# exit 0
