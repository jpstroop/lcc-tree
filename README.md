# lcc-tree
Make a LCC Treemap with a bunch of MARC files

Forked from https://github.com/thisismattmiller/lcc-tree

View here: https://jpstroop.github.io/lcc-tree/

1. Run `pipenv install`
2. Set `ALL_RECORDS_URL` near the top of `get_data.py`
3. Run `get_data.py` (`pipenv run python get_data.py`)
4. Run `build_data.py`
4. Run `build_json_tree.py`
5. Go to https://observablehq.com/@jpstroop/princeton-lcc-treemap
6. Find the line that says `data = FileAttachment("listhierarchy.json").json()` click the paperclip and replace the json file with your own `listhierarchy.json` that was created by the scripts.
