import json

def findUnusedImport(report):
    result = []
    for i in range(len(report)):
        if report[i]["symbol"] == "unused-import" or report[i]["symbol"] == "unused-wildcard-import":
            result.append(report[i])
    return result

def findGeneralImport(report):
    result = []
    for i in range(len(report)):
        if "import" in report[i]["symbol"] and report[i]["symbol"] != "import-error":
            result.append(report[i])
    return result

def findMissingReport(report, typeS):
    result = []
    for i in range(len(report)):
        if ("missing-" + typeS) in report[i]["symbol"]:
            result.append(report[i])
    return result

def findErrors(report):
    result = []
    for i in range(len(report)):
        if "error" in report[i]["type"] and report[i]["symbol"] != "import-error":
            result.append(report[i])
    return result

def findRefactors(report):
    result = []
    for i in range(len(report)):
        if "refactor" in report[i]["type"]:
            result.append(report[i])
    return result

def findWarnings(report):
    result = []
    for i in range(len(report)):
        if "warning" in report[i]["type"]:
            result.append(report[i])
    return result

def formalize_strings(report):
    result = []
    for i in range(len(report)):
        current_obj = report[i]
        current_message1 = str(current_obj["path"]) + ":" + str(current_obj["line"]) + ":" + str(current_obj["column"]) + ": "
        current_message2 = str(current_obj["message-id"]) + ": " + str(current_obj["message"]) + " (" + str(current_obj["symbol"]) + ")"
        result.append(current_message1 + current_message2)
    return result

def print_report(report):
    for msg in formalize_strings(report):
        print(msg)

def output_formalized_report(out_file, report):
    formalized_report = formalize_strings(report)
    fid = open(out_file, "w")
    total_size = len(formalized_report)
    for i in range(total_size):
        fid.write(str(formalized_report[i]) + "\r\n")
    fid.close()


if __name__=="__main__":
    f = open("pylint_result.json")
    report = json.loads(f.read())
    f.close()

    unused_imports = findUnusedImport(report)
    output_formalized_report("pylint_import_issue.txt", unused_imports)

    general_imports = findGeneralImport(report)
    output_formalized_report("pylint_general_import.txt", general_imports)

    missing_function_reports = findMissingReport(report, "function")
    output_formalized_report("pylint_missing_function_report.txt", missing_function_reports)

    gengeral_error_reports = findErrors(report)
    output_formalized_report("pylint_all_errors.txt", gengeral_error_reports)

    general_refactor_reports = findRefactors(report)
    output_formalized_report("pylint_all_refactors.txt", general_refactor_reports)

    general_warnings_reports = findWarnings(report)
    output_formalized_report("pylint_all_warning.txt", general_warnings_reports)