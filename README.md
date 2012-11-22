live-py-stylus
==============

Convert stylus to css real time. Easily used by any web framwork.

It depends on the Python Stylus: https://github.com/bkad/python-stylus
And the Python Stylus depends on [Node](http://nodejs.org) and [Stylus](http://learnboost.github.com/stylus/)
So you need install nodejs and stylus node package before .

For example , in a flask project :

```python
from flask import Flask
from live_stylus import ConvStylus

app = Flask(__name__)

from views import *


if __name__ == "__main__":
    app.debug = True
    ConvStylus()
    app.run()
```

In a bottle project :

```python
from bottle import route, run, template
from live_stylus import ConvStylus

@route('/hello/:name')
def index(name='World'):
    return template('<b>Hello {{name}}</b>!', name=name)

if __name__ == "__main__":
    ConvStylus()
    run(host='localhost', port=8080)
```

Then when you modify a .styl file , it will be converted to a same name css file immediately.

If you use other web framwork , just put the ConvStylus() before the .run() or .start() code.

If you want monitor a explicitly directoty's stylus file , you can use:

```python
ConvStylus('/home/xxx/work/project/static/css')
```

## Questions?

If you have any questions, please feel free to ask through [New Issue](https://github.com/allenm/live-py-stylus/issues/new).

## License

SeaJS is available under the terms of the [MIT License](http://seajs.org/LICENSE.md).
