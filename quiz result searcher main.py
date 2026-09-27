def get_score_by_index(scores, index):
    if 0 <= index < len(scores):
        return scores[index]
    return None


def linear_search_score(scores, target):
    for i in range(len(scores)):
        if scores[i] == target:
            return i
    return -1


def find_score_pairs(scores):
    pairs = []
    n = len(scores)
    for i in range(n):
        for j in range(i + 1, n):
            pairs.append((scores[i], scores[j]))
    return pairs


if __name__ == "__main__":
    quiz_scores = [85, 92, 78, 90, 88]
    target_score = 90

    print(f"Quiz Scores: {quiz_scores}")

    score_at_index = get_score_by_index(quiz_scores, 2)
    print(f"[O(1) Direct Access] Score at index 2: {score_at_index}")

    found_index = linear_search_score(quiz_scores, target_score)
    print(f"[O(n) Linear Search] Score {target_score} found at index: {found_index}")

    all_pairs = find_score_pairs(quiz_scores)
    print(f"[O(n^2) Pair Comparison] Unique score pairs: {all_pairs}")
