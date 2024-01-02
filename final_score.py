def score_calc(gaa, qz1, qz2):
    if gaa < 40 or qz1 + qz2 <= 0:
        return "You are not eligible for End Term Exam.\nBetter Luck Next Time!", "Not Eligible for End Term", "red"

    T = 40 - .1 * gaa
    m1 = .2 * max(qz1, qz2)
    m2 = (.2 * qz1) + (.3 * qz2)

    x1 = (T - m1) / .6
    x2 = (T - m2) / .4
    if x1 < x2:
        F = x1
    else:
        F = x2

    F = round(F, 2)
    if F <= 0:
        F = 0
        return "You just have to attend the End Term Exam to pass this Course.", F, "green"
    else:
        return f"You have to score at least {F} marks in End Term Exam to pass this Course.", F, "yellow"
    

def python_calc(gaa, qz1, pe1, pe2, wta):
    if pe1 + pe2 < 40:
        return "You have to repeat the Course as your OPPE Scores are not good.\nBetter Luck Next Time!", "Not Eligible for End Term", "red"

    T = 40 - (.1 * gaa) - (.1 * qz1) - (.05 * wta)
    x1 = (T - (.2 * max(pe1, pe2))) / .4
    x2 = (T - (.25 * max(pe1, pe2) - .15 * min(pe1, pe2))) / .4
    if x1 < x2:
        F = x1
    else:
        F = x2

    F = round(F, 2)
    if F <= 0:
        F = 0
        return "You just have to attend the End Term Exam to pass this Course.", F, "green"
    else:
        return f"You have to score at least {F} marks in End Term Exam to pass this Course.", F, "yellow"
    

if __name__ == "__main__":
    print(score_calc(95, 66, 98))
    gaa = int(input("Enter Average of best 10 Graded Assignment: "))
    qz1 = int(input("Enter Quiz 1 Score: "))
    pe1 = int(input("Enter OPPE 1 Score: "))
    pe2 = int(input("Enter OPPE 2 Score: "))
    wta = int(input("Enter Average of your best 6 Mock Scores: "))
    python_calc(gaa, qz1, pe1, pe2, wta)