# spotify-check-duplicates

Check if there are duplicates in your Spotify library.

## Getting started

```bash
pip install .
SPOTIPY_CLIENT_ID="<your spotify client ID>"
SPOTIPY_CLIENT_SECRET="<your spotify client secret>"
SPOTIPY_REDIRECT_URI=http://localhost:9000
spotify-check-duplicates
```

## Contributing

### Prerequisites
- [pre-commit](https://pre-commit.com/)

### Getting started

```bash
git clone https://github.com/leroyguillaume/spotify-check-duplicates
cd spotify-check-duplicates
pre-commit install
python -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

### How to run

```bash
spotify-check-duplicates
```
