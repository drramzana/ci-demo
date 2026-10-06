def grade(score):
    if score < 0 or score > 100:
        return "Invalid"   # r1
    if score >= 90:
        return "A"         # r2
    if score >= 60:
        return "Pass"      # r3
    if score > 100:
        return "Bonus"     # r4
    return "Fail"          # r5
