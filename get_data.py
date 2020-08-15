from os import makedirs
from os import remove
from os.path import abspath
from os.path import dirname
from os.path import join
from os.path import sep
from requests import get
from gzip import open as gz_open
from shutil import copyfileobj

ALL_RECORDS_URL = "https://bibdata.princeton.edu/dumps/21750.json"

def set_up():
    out_dir = join(dirname(abspath(__file__)), 'data')
    makedirs(out_dir, exist_ok=True)
    return out_dir

def download(url, file_path):
    r = get(url, stream=True)
    with open(file_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=1024):
            fd.write(chunk)
    mrc_path = file_path.replace('.gz', '.mrc')
    with gz_open(file_path, 'rb') as f_in:
        with open(mrc_path, 'wb') as f_out:
            copyfileobj(f_in, f_out)
    remove(file_path)


if __name__ == '__main__':
    out_dir = set_up()

    all_records_json = get(ALL_RECORDS_URL).json()
    for entry in all_records_json['files']['bib_records']:
        url = entry['dump_file']
        download_path = f"{out_dir}{sep}{url.split('/')[-1]}.gz"
        print(url)
        download(url, download_path)
