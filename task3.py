from pathlib import Path
import utils
import constants


d = {}

for folder in constants.FOLDERS:
    root = Path(folder)
    for element in root.glob("**/*"):
        if not utils.is_path_white_listed(element, constants.WHITE_LIST):
            continue

        element_created_at = utils.created_at(element)
        element_created_at_year = element_created_at[0]
        element_created_at_month = element_created_at[1]

        key = (element_created_at_year, element_created_at_month, element.suffix)

        element_size = element.stat().st_size

        line_count = 0

        if utils.kind(element.suffix, constants.CODE_LIST, constants.WHITE_LIST) == "C":
            line_count = utils.lines_counter(element)

        if key not in d:
            d[key] = [
                1,
                element_size,
                line_count,
            ]
            continue

        value_from_dict = d[key]
        value_from_dict[0] += 1
        value_from_dict[1] += element_size
        value_from_dict[2] += line_count

dict_values = list(d.items())
dict_values.sort(key=lambda x: (x[0][0], x[0][1]))

CSV_FILE_NAME = "lab1_1"

csv_headers = ["year", "mon", "ext", "cnt", "size", "lines", "avg_size", "avg_line"]

csv_file_path = utils.create_csv_file(CSV_FILE_NAME, csv_headers)

for key, value in dict_values:
    year = key[0]
    month = key[1]
    extension = key[2]
    file_count = value[0]
    size = value[1]
    line_count = value[2]
    mean_size = size // file_count
    mean_line_count = line_count // file_count

    line_count_str = " "
    mean_line_count_str = " "
    if utils.kind(extension, constants.CODE_LIST, constants.WHITE_LIST) == "C":
        line_count_str = str(line_count)
        mean_line_count_str = str(mean_line_count)

    row = (
        year,
        month,
        extension,
        file_count,
        size,
        line_count_str,
        mean_size,
        mean_line_count_str,
    )

    utils.print_row(row)
    utils.write_row_to_csv_file(csv_file_path, row)
