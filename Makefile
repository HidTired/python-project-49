.PHONY: install brain-games build package-install clean

install:
    uv sync

brain-games:
    uv run brain-games

build:
    uv build

package-install:
    uv tool install dist/*.whl

clean:
    rm -rf dist build *.egg-info