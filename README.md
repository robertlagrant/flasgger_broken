# Repo to illustrate flasgger validation issues

_(Built with Python 3.6, on MacOS.)_

This is attempting to show that the `validation=True` option on the `swag_from` decorator isn't doing anything, and the `validate()` call (which IS doing something) doesn't like following Swagger's allOf option.

## Steps to reproduce environment

1. Pull this repo :-) and go to repo directory in terminal
2. `virtualenv -p python3 venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python -m flasgger_broken`

### With validation=True, valid data produces correct response

```
$ curl -X POST -H "Content-Type: application/json" -d '{ "bar_uuid": "uuid1234", "bar_email": "rob@rob.com", "foo1": "I make it valid", "foo2": "something" }' http://localhost:5000/bar

{
  "message": "it worked!"
}
```

---

### With validation=True, invalid data produces wrong response

```
$ curl -X POST -H "Content-Type: application/json" -d '{ "iaminvalid": "hahaha" }' http://localhost:5000/bar
{
  "message": "it worked!"
}
```

---

### With validate(), invalid data produces wrong response (should say foo1 is required)

```
$ curl -X POST -H "Content-Type: application/json" -d '{ "bar_uuid": "uuid1234", "bar_email": "rob@rob.com", "foo2": "something" }' http://localhost:5000/bar_manual

Unresolvable JSON pointer: 'definitions/FooMixin'
```

---

### With validate(), valid data produces wrong response

```
$ curl -X POST -H "Content-Type: application/json" -d '{ "bar_uuid": "uuid1234", "bar_email": "rob@rob.com", "foo2": "something" }' http://localhost:5000/bar_manual

Unresolvable JSON pointer: 'definitions/FooMixin'
```
