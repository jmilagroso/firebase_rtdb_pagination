firebase\_rtdb\_pagination - Firebase RealtimeDB Pagination
===========================================================

Paginate Firebase RealtimeDB records using cursor pagination.

|PyPI version|
|Downloads|



Overview
--------

The ``firebase_rtdb_pagination`` was written to simplify record fetching
with pagination.

Usage
-----

.. code:: sh

    import firebase_admin
    from firebase_admin import credentials, db
    from firebase_rtdb_pagination import FirebaseRTDBPagination


    cred = credentials.Certificate(
        "/path/to/service_account.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://PROJECT-ID-default-rtdb.firebaseio.com'
    })

Sample Firebase data called ``inventory``:

.. code:: sh

    [
      {
        "name": "Pen",
        "qty": 100
      },
      {
        "name": "Pencil",
        "qty": 10000
      },
      {
        "name": "Notebook",
        "qty": 750
      },
      {
        "name": "Eraser",
        "qty": 0
      },
      {
        "name": "Whiteboard Marker",
        "qty": 10
      }
    ]

Firebase Rule:

.. code:: sh

    {
        "rules": {
            ...
            "inventory": {
                ".indexOn": ["qty"]
            }
            ...
        }
    }

Instantiating pagination class

.. code:: sh

    pagination = FirebaseRTDBPagination(
        firebase_admin_db=db,
        path='/inventory',
        child_key='qty',
        sort_by='desc',
        per_page=3
    )

    print(pagination.all())
    [
      {
        'name': 'Pen',
        'qty': 100
      },
      {
        'name': 'Pencil',
        'qty': 10000
      },
      {
        'name': 'Notebook',
        'qty': 750
      },
      {
        'name': 'Eraser',
        'qty': 0
      },
      {
        'name': 'Whiteboard Marker',
        'qty': 10
      },
      {
        'name': 'Whiteboard',
        'qty': 255
      }
    ]

    # page 1
    page1 = pagination.get()
    print('page 1: {}'.format(page1))
    {
      'data': [
        {
          'name': 'Pencil',
          'qty': 10000
        },
        {
          'name': 'Notebook',
          'qty': 750
        },
        {
          'name': 'Whiteboard',
          'qty': 255
        }
      ],
      'cursor': 255,
      'pages': 2,
      'total': 6
    }

    # page 2
    page2 = pagination.get(page1.get('cursor'))
    print('page 2: {}'.format(page2))
    {
      'data': [
        {
          'name': 'Pen',
          'qty': 100
        },
        {
          'name': 'Whiteboard Marker',
          'qty': 10
        },
        {
          'name': 'Eraser',
          'qty': 0
        }
      ],
      'cursor': 0,
      'pages': 2,
      'total': 6
    }

    # page 3
    page3 = pagination.get(page2.get('cursor'))
    print('page 3: {}'.format(page3))
    {
      'data': [],
      'cursor': [],
      'pages': 2,
      'total': 6
    }

    # page 4
    page4 = pagination.get(page3.get('cursor'))
    print('page 4: {}'.format(page4))
    {
      'data': [],
      'cursor': [],
      'pages': 2,
      'total': 6
    }

Getting it
~~~~~~~~~~

To download ``firebase_rtdb_pagination``, either fork this github repo
or simply use Pypi via pip.

.. code:: sh

    $ pip install firebase_rtdb_pagination

License
-------

MIT License

Copyright (c) 2021 Jay Milagroso

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

.. |PyPI version| image:: https://badge.fury.io/py/firebase-rtdb-pagination.svg
   :target: https://badge.fury.io/py/firebase-rtdb-pagination
   
.. |Downloads| image:: https://pepy.tech/badge/firebase-rtdb-pagination
   :target: https://pepy.tech/project/firebase-rtdb-pagination
