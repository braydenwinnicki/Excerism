"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores."""

    scores = []
    
    for score in student_scores:
        rounded = round(score)
        scores.append(rounded)
    return scores

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided."""

    count = 0
    
    for score in student_scores:
        if score <= 40:
            count += 1
    return count 

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold."""

    best = []

    for score in student_scores:
        if score >= threshold:
            best.append(score)
        continue 
    return best

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade."""

    interval = round((highest - 41) / 4)

    return [41 + interval * step for step in range(4)]
  
def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order."""

    new_list = []

    for index, score in enumerate(student_scores):
        new_index = index + 1
        new_list.append(f"{new_index}. {student_names[index]}: {score}")

    return new_list

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam."""

    list_empty = []

    for student in student_info:
        if 100 in student:
            return student
    return list_empty