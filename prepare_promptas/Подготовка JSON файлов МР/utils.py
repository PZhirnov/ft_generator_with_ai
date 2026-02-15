def save_to_csv(path_file_output, result_rows):
    with open(path_file_output, 'w', encoding='utf-8') as file:
        for row in result_rows:
            file.write(str(row))
            file.write('\n')