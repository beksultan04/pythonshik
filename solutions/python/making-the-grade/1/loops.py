"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores."""
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided."""
    return len([score for score in student_scores if score <= 40])


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold."""
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade."""
    # Разница между 40 и highest делится на 4 интервала
    interval = (highest - 40) // 4
    return [41 + interval * i for i in range(4)]


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order."""
    return [f"{i + 1}. {student_names[i]}: {student_scores[i]}" for i in range(len(student_scores))]


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam."""
    for student in student_info:
        if student[1] == 100:
            return student
    return []
