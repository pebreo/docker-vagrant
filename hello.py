# http://stackoverflow.com/questions/11747527/how-to-connect-javascript-to-python-sharing-data-with-json-format-in-both-ways
from bottle import hook, response, route, run, static_file, request, static_file


@route('/')
def foo():
    return 'Hello World!'

run(host='0.0.0.0',port=5000)