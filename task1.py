from pathlib import Path
import utils


def task1_solution(folders, white_list, code_list):
    d = {}

    for folder in folders:
        root = Path(folder)
        for element in root.glob("**/*"):
            if not utils.path_has_suffix(element):
                continue

            if element.suffix not in d:
                d[element.suffix] = 1
                continue

            d[element.suffix] += 1

    suffix_counts = list(d.items())
    suffix_counts.sort(key=lambda el: el[1], reverse=True)

    for suffix, file_count in suffix_counts:
        utils.print_row((suffix, file_count, utils.kind(suffix, code_list, white_list)))
