# Repo to illustrate flasgger validation issues

_(Built with Python 3.6, on MacOS.)_

This is attempting to show that the `validation=True` option on the `swag_from` decorator isn't doing anything, and the `validate()` call (which IS doing something) doesn't like following Swagger's allOf option.

The Swagger definition is an entity called Bar, which pulls in fields from FooMixin. I can't get `validation=True` to fail validation at all, and calling `validate()` fails if Bar's fields are all correct, as it can't find FooMixin. 

## Steps to reproduce environment

1. Pull this repo :-) and go to repo directory in terminal
2. `virtualenv -p python3 venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python -m flasgger_broken`

## Tests to run

##### With validation=True, valid data produces correct response

```
$ curl -X POST -H "Content-Type: application/json" -d '{ "bar_uuid": "uuid1234", "bar_email": "rob@rob.com", "foo1": "I make it valid", "foo2": "something" }' http://localhost:5000/bar

{
  "message": "it worked!"
}
```

---

##### With validation=True, invalid data produces wrong response

```
$ curl -X POST -H "Content-Type: application/json" -d '{ "iaminvalid": "hahaha" }' http://localhost:5000/bar
{
  "message": "it worked!"
}
```
---

##### With validate(), direct invalid data produces correct response

```
$ curl -X POST -H "Content-Type: application/json" -d '{ "bar_uuid": "uuid1234", "bar_email": "rob@rob.com" }' http://localhost:5000/bar_manual
'foo2' is a required property

Failed validating 'required' in schema:
    {'allOf': [{'$ref': '#/definitions/FooMixin'}],
     'definitions': {},
     'example': {'bar_email': 'me@email.com',
                 'bar_uuid': '1ab091c8-7567-4420-ab01-5427c991ef2f',
                 'foo1': 'A good foo',
                 'foo2': 'Another good foo'},
     'properties': {'bar_email': {'description': 'The bar email',
                                  'example': 'me@email.com',
                                  'type': 'string'},
                    'bar_uuid': {'description': 'the bar uuid',
                                 'example': '1ab091c8-7567-4420-ab01-5427c991ef2f',
                                 'type': 'string'}},
     'required': ['bar_uuid', 'bar_email', 'foo2'],
     'title': 'Bar',
     'type': 'object'}

On instance:
    {'bar_email': 'rob@rob.com', 'bar_uuid': 'uuid1234'}
```

---

##### With validate(), inherited invalid data produces wrong response (should say foo1 is required, as FooMixin needs it)

```
$ curl -X POST -H "Content-Type: application/json" -d '{ "bar_uuid": "uuid1234", "bar_email": "rob@rob.com", "foo2": "something" }' http://localhost:5000/bar_manual

Unresolvable JSON pointer: 'definitions/FooMixin'
```

---

##### With validate(), valid data produces wrong response

```
$ curl -X POST -H "Content-Type: application/json" -d '{ "bar_uuid": "uuid1234", "bar_email": "rob@rob.com", "foo2": "something" }' http://localhost:5000/bar_manual

Unresolvable JSON pointer: 'definitions/FooMixin'
```
