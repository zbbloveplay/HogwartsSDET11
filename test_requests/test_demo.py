from pprint import pprint

import requests


def test_requests():
    r = requests.get("https://home.testing-studio.com/categories.json")
    pprint(r)
    print(r.status_code)
    print(r.json())
    assert r.status_code == 200


def test_get():
    r = requests.get("https://httpbin.testing-studio.com/get",
                     params={
                         "a": 1,
                         "b": 2,
                         "c": "cccc"
                     })
    print(r.json())
    assert r.status_code == 200


def test_post():
    r = requests.post("https://httpbin.testing-studio.com/post",
                      data={
                          "a": 1,
                          "b": 2,
                          "c": "cccc"
                      })
    print(r.json())
    assert r.status_code == 200


def test_upload():
    r = requests.post("https://httpbin.testing-studio.com/post",
                      files={
                          "file": open("__init__.py", 'rb')
                      },
                      headers={
                          "Content-Type": ""
                      })
    print(r.json())
    assert r.status_code == 200
