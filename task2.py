from pathlib import Path
import utils


def task2_solution(folders, white_list, code_list):
    d = {}

    for folder in folders:
        root = Path(folder)
        for element in root.glob("**/*"):
            if not utils.is_path_white_listed(element, white_list):
                continue

            element_created_at = utils.created_at(element)

            created_at_year = element_created_at[0]
            created_at_month = element_created_at[1]
            SEPTEMBER = 9

            if created_at_year < 2024 and created_at_month < SEPTEMBER:
                continue

            line_count = 0
            size = element.stat().st_size

            if utils.kind(element.suffix, code_list, white_list) == "C":
                line_count = utils.lines_counter(element)

            if element_created_at not in d:
                d[element_created_at] = [
                    1,
                    size,
                    line_count,
                ]
                continue

            value_from_dict = d[element_created_at]
            value_from_dict[0] += 1
            value_from_dict[1] += size
            value_from_dict[2] += line_count

    dict_values = list(d.items())
    dict_values.sort(key=lambda x: (x[0][0], x[0][1]))

    for file_created_at, file_info in dict_values:
        year = file_created_at[0]
        month = file_created_at[1]
        file_count = file_info[0]
        size = file_info[1]
        line_count = file_info[2]
        mean_size = size // file_count
        mean_line_count = line_count // file_count

        utils.print_row(
            (year, month, file_count, size, line_count, mean_size, mean_line_count)
        )
