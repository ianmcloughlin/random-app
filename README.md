# Random numerical app.

# Linux
```bash
export FLASK_APP=rando.py
python3 -m flask run
```

# Windows
```bash
set FLASK_APP=rando.py
python -m flask run
```

```bash
docker build . -t rando-image
docker run --name rando-container -d -p 5000:5000 rando-image
```