import csv
from pathlib import Path
from datetime import datetime as dt
import sys


def _created_at_Linux(path):
    path_object = Path(path)
    ctime = path_object.stat().st_ctime
    cdate = dt.fromtimestamp(ctime)
    return cdate.year, cdate.month


def _created_at_Windows(path):
    path_object = Path(path)
    ctime = path_object.stat().st_birthtime
    cdate = dt.fromtimestamp(ctime)
    return cdate.year, cdate.month


if sys.platform.startswith("win"):
    created_at = _created_at_Windows
else:
    created_at = _created_at_Linux


def path_has_suffix(path):
    return path.is_file() and path.suffix != None and path.suffix != ""


def is_path_white_listed(path, white_list):
    return path_has_suffix(path) and path.suffix in white_list


def kind(extension, code_list, white_list):
    if extension in code_list:
        return "C"
    if extension in white_list:
        return "W"
    return "O"


def lines_counter(path):
    # if path.stat().st_size < 2**20:
    #     raise RuntimeError("File has too many lines")

    notempty_lines = 0

    with open(path, encoding="utf-8", errors="ignore") as f:
        for s in f:
            if not s.isspace() and s != "" and s != None:
                notempty_lines += 1

    return notempty_lines


def create_csv_file(file_name, headers) -> str:
    path = ""
    with open(file_name + ".csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        path = f.name

    return path


def write_row_to_csv_file(file_path, row):
    with open(file_path, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)


def print_row(row):
    row_str_list = []

    for col in row:
        row_str_list.append(f"{col:10}")

    row_str = " ".join(row_str_list)
    print(row_str)
