import pandas as pd
import numpy as np

def getSevere(report, severity):
    result = []
    for i in range(len(report)):
        if report[i][3] == severity:
            result.append(report[i])
    return np.array(result)

def getConfidence(report, confidence):
    result = []
    for i in range(len(report)):
        if report[i][4] == confidence:
            result.append(report[i])
    return np.array(result)

def getTest(report, testname):
    result = []
    for i in range(len(report)):
        if report[i][1] == testname:
            result.append(report[i])
    return np.array(result)

def formalize_strings(report):
    result = []
    for i in range(len(report)):
        current_m = report[i]
        current_message1 = str(current_m[0][42:]) + ":" + str(current_m[7]) + ":" + str(current_m[8]) + ": "
        current_message2 = str(current_m[1]) + ", severity: " + str(current_m[3]) + ", confidence: " + str(current_m[4])
        current_message3 = ", " + str(current_m[6])
        result.append(current_message1 + current_message2 + current_message3)
    return result

def output_formalized(report, filename):
    formalized_report = formalize_strings(report)
    fid = open(filename, "w")
    total_size = len(formalized_report)
    for i in range(total_size):
        fid.write(str(formalized_report[i]) + "\r\n")
    fid.close()

if __name__ == "__main__":
    df = pd.read_csv("bandit_result.csv")
    report = df.to_numpy()
    
    output_formalized(getSevere(report, "HIGH"), "bandit_HIGH_severe.txt")
    output_formalized(getSevere(report, "MEDIUM"), "bandit_MEDIUM_severe.txt")
    output_formalized(getSevere(report, "LOW"), "bandit_LOW_severe.txt")
    output_formalized(getConfidence(report, "HIGH"), "bandit_HIGH_confidence.txt")
    output_formalized(getConfidence(report, "MEDIUM"), "bandit_MEDIUM_confidence.txt")
    output_formalized(getConfidence(report, "LOW"), "bandit_LOW_confidence.txt")
    output_formalized(getTest(report, "blacklist"), "bandit_blacklist.txt")