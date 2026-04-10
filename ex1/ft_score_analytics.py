import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    scores = []
    if len(sys.argv) == 1:
        print("No scores provided. \
Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        for argv in sys.argv[1:]:
            try:
                scores.append(int(argv))
            except ValueError:
                print(f"Invalid parameter: '{argv}'")
                continue
        if len(scores) == 0:
            return

        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores)/(len(scores))}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    ft_score_analytics()
