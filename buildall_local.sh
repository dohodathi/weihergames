
source ./buildall_netlify.sh

# TODO: make this work to allow local testing of embedded files
# TODO: Python: can't open file '–m': [Errno 2] No such file or directory
# TODO: not investigated deeper though :D need python insights from THEEEEEEEL
python –m SimpleHTTPServer 8000