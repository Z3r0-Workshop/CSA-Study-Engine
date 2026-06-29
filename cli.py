from db import init_db, seed_db
from quiz import next_question, submit_answer

_LINE = "-" * 54


def _show(topic_name: str, question) -> dict[str, str]:
    """Print the question and return a letter->answer map for MCQ."""
    print(f"\n{_LINE}")
    print(f"Topic: {topic_name}")
    print(_LINE)
    print(f"\n{question.stem}\n")

    letter_map: dict[str, str] = {}
    if question.kind == "mcq":
        for i, opt in enumerate(question.options):
            letter = chr(65 + i)
            letter_map[letter] = opt
            print(f"  {letter})  {opt}")
    return letter_map


def _prompt(letter_map: dict[str, str]) -> str:
    """Ask for the user's answer; return the answer text or 'Q' to quit."""
    if letter_map:
        keys = "/".join(letter_map)
        while True:
            raw = input(f"\nAnswer [{keys}]  or q to quit: ").strip().upper()
            if raw == "Q":
                return "Q"
            if raw in letter_map:
                return letter_map[raw]
            print(f"  Please enter one of: {keys}")
    else:
        return input("\nYour answer (or q to quit): ").strip()


def main() -> None:
    init_db()
    seed_db()

    print("\n  CSA Study Engine")
    print("  Type q at any answer prompt to end the session.\n")

    correct = total = 0

    while True:
        topic, question = next_question()
        letter_map = _show(topic.name, question)

        user_answer = _prompt(letter_map)
        if user_answer == "Q":
            break

        is_correct, score, rationale = submit_answer(question, user_answer)
        total += 1
        correct += is_correct

        if is_correct:
            print("\n  [+] Correct!")
        else:
            print(f"\n  [-] Wrong.  The answer is: {question.answer}")

        # Free-text: show LLM rationale + score; MCQ: show baked-in explanation
        if rationale:
            print(f"  Score: {score:.0%}  —  {rationale}")
        else:
            print(f"  {question.explanation}")
        print(f"\n  Score: {correct}/{total}", end="")
        if total:
            print(f"  ({correct / total:.0%})")
        input("\n  Enter for next question...")

    print(f"\n  Session over: {correct}/{total} correct", end="")
    print(f"  ({correct / total:.0%})" if total else "")


if __name__ == "__main__":
    main()
