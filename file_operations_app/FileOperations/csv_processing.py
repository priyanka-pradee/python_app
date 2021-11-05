import numpy as np
import pandas as pd
from pandas_schema import Column, Schema
from pandas_schema.validation import (
    CustomElementValidation,
    DateFormatValidation,
    InListValidation,
    InRangeValidation,
    IsDtypeValidation,
    LeadingWhitespaceValidation,
    MatchesPatternValidation,
    TrailingWhitespaceValidation,
)

sl_no_validation = [
    CustomElementValidation(lambda d: validate_sl_no(d), "this field cannot be null")
]
structure_header_list = ["Sl No", "Date", "Structure"]
customer_header_list = ["Given Name", "Family Name", "Age", "Gender", "Customer ID"]
structures_schema = Schema(
    [
        Column("Sl No", sl_no_validation),
        Column("Date", [DateFormatValidation("%d/%m/%Y")]),
        Column("Structure", [InListValidation(["Pit", "Pole", "Strand"])]),
    ]
)

customer_schema = Schema(
    [
        Column(
            "Given Name",
            [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
        ),
        Column(
            "Family Name",
            [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()],
        ),
        Column("Age", [InRangeValidation(0, 120)]),
        Column("Gender", [InListValidation(["Male", "Female", "Other"])]),
        Column("Customer ID", [MatchesPatternValidation(r"[A-Z]{4}\d{3}")]),
    ]
)


def check_int(num):
    try:
        int(num)
    except ValueError:
        return False
    return True


def validate_sl_no(d):
    if d is np.nan:
        return False
    elif not check_int(d):
        return False
    else:
        return True


def do_csv_validation(zip_file, filename):
    """
    Validate the columns of the CSV files
    """
    errors = []
    try:
        print(filename)
        csv_file = zip_file.open(filename)
        df = pd.read_csv(zip_file.open(filename))
        import_headers = df.axes[1]
        if filename.endswith("structure.csv"):
            validation_errors = structures_schema.validate(df)
            header_list = structure_header_list
        else:
            validation_errors = customer_schema.validate(df)
            header_list = customer_header_list
        errors = [str(e).replace(",", "") for e in validation_errors]
        a = [i for i in import_headers if i not in header_list]

        return errors
        # error_df.to_csv("errors.csv")
        # print(structure_errors)
    except UnicodeDecodeError:
        errors.append("CSV format is not UTF-8 encoded")
    print(errors)
    return errors
