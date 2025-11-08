.PHONY: install brain-games

install:
    pip install --upgrade pip && pip install -r requirements.txt

brain-games:
    python -m brain_games.run