# Installation

```sh
pip3 install -r requirements.txt
```

Note that python 3 is required.


# Run

```sh
./app.py
```


# GUI

Browse to http://127.0.0.1:5000


# REST

With [httpie](https://httpie.org/):

```sh
$ http http://127.0.0.1:5000/api/weighted-scores/euclidean/Mike
HTTP/1.0 200 OK
Content-Length: 118
Content-Type: application/json
Date: Sun, 18 Nov 2018 09:34:52 GMT
Server: Werkzeug/0.14.1 Python/3.5.3

[
    {
        "movie": "Just My Luck",
        "score": 2.602209944751381
    },
    {
        "movie": "You, Me and Dupree",
        "score": 2.4095373283204173
    }
]
```

```sh
$ http http://127.0.0.1:5000/api/user-list
HTTP/1.0 200 OK
Content-Length: 60
Content-Type: application/json
Date: Sun, 18 Nov 2018 09:36:29 GMT
Server: Werkzeug/0.14.1 Python/3.5.3

[
    "Lisa",
    "Gene",
    "Mike",
    "Claudia",
    "Mick",
    "Jack",
    "Toby"
]
```

```sh
$ http http://127.0.0.1:5000/api/measure-list
HTTP/1.0 200 OK
Content-Length: 25
Content-Type: application/json
Date: Sun, 18 Nov 2018 09:38:33 GMT
Server: Werkzeug/0.14.1 Python/3.5.3

[
    "pearson",
    "euclidean"
]
```
