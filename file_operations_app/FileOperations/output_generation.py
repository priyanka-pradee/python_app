headers = ["SL  NO", "File Name", "ERROR"]
import os


def generate_error(errors, output_filepath):
    generate_error_html(errors, output_filepath)
    generate_error_csv(errors, output_filepath)


def generate_error_csv(errors, output_filepath):
    if not os.path.isdir(output_filepath):
        os.makedirs(output_filepath)
    CSV = "\n".join([k + "," + val for k, v in errors.items() for val in v])
    # You can store this CSV string variable to file as below
    with open(os.path.join(output_filepath, "errors.csv"), "w") as file:
        file.write(CSV)


def generate_error_html(errors, output_filepath):
    html = (
        "<html><head><title>"
        + "Errors"
        + '</title></head><body><H1>Errors generated during file Validation</H1><table border="1"><tr><th>'
        + "</th><th>".join(headers)
        + "</th></tr>"
    )
    count = 0
    for key, values in errors.items():
        print(key, values)
        for value in values:
            count += 1
            html += (
                "<tr><td>"
                + str(count)
                + "</td><td>"
                + key
                + "</td><td>"
                + value
                + "</td></tr>"
            )

    html += "</table></body></html>"
    print(html)
    file_ = open(os.path.join(output_filepath, "result.html"), "w")
    file_.write(html)
    file_.close()
