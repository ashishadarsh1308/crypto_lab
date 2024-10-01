def student_ranking(student_scores, student_names):
    """Generate a ranked list of students and their scores."""
    rankings = []
    for rank, (name, score) in enumerate(zip(student_names, student_scores), start=1):
        ranking_str = f"{rank}. {name}: {score}"
        rankings.append(ranking_str)
    return rankings

def main():
    scores_input = input("Enter student scores separated by spaces: ")
    student_scores = list(map(int, scores_input.split()))
    names_input = input("Enter student names separated by commas: ")
    student_names = [name.strip() for name in names_input.split(',')]
    
    if len(student_scores) != len(student_names):
        print("The number of scores and names must be the same.")
        return

    rankings = student_ranking(student_scores, student_names)
    for ranking in rankings:
        print(ranking)

if __name__ == "__main__":
    main()
