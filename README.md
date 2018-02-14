# Repo to illustrate flasgger validation issue

_(Built with Python 3.6, on MacOS.)_

## Steps to reproduce environment

1. Pull this repo :-) and go to repo directory in terminal
2. `virtualenv -p python3 venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python -m flasgger_broken`

## Curl commands



This is an unexpected response - this should be invalid because foo1 is required from the FooMixin:

Running
`$ curl -X POST -H "Content-Type: application/json" -d '{ "bar_uuid": "uuid1234", "bar_email": "rob@rob.com", "foo2": "something" }' http://localhost:5000/bar_manual`

Gives
`Unresolvable JSON pointer: 'definitions/FooMixin'`


This is an unexpected response - this should be valid:

Running
`curl -X POST -H "Content-Type: application/json" -d '{ "bar_uuid": "uuid1234", "bar_email": "rob@rob.com", "foo1": "I make it valid", "foo2": "something" }' http://localhost:5000/bar_manual`

Gives
`Unresolvable JSON pointer: 'definitions/FooMixin'`
