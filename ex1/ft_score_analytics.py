import sys


def ft_score_analytics():
    print("=== Player Score Analytics ===")
    scores = []
    if len(sys.argv) == 1:
        print("No scores provided. \
Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            i = 1
            error = 0
            for argv in sys.argv[1:]:
                scores.append(int(sys.argv[i]))
                i += 1
        except ValueError:
            print(f"oops, I typed '{sys.argv[i]}' instead of an actual score \
:D")
            error = 1
        if error == 0:
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(sys.argv) - 1}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores)/(len(sys.argv) - 1)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    ft_score_analytics()
