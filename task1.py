from pathlib import Path
import utils
import constants


d = {}

for folder in constants.FOLDERS:
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
    utils.print_row(
        (
            suffix,
            file_count,
            utils.kind(suffix, constants.CODE_LIST, constants.WHITE_LIST),
        )
    )
