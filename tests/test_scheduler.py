import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scheduler import priority_score


def test_unseen_topic_gets_bonus():
    # No attempts yet → +0.3 added on top of the base score
    score = priority_score(weight=0.14, recent_accuracy=0.5, attempt_count=0)
    assert score == 0.14 * (1 - 0.5) + 0.3


def test_mastered_topic_has_zero_base_priority():
    # Perfect accuracy → weight × 0 = 0, no unseen bonus
    score = priority_score(weight=0.14, recent_accuracy=1.0, attempt_count=5)
    assert score == 0.0


def test_all_wrong_gives_full_weight():
    # 0% accuracy → weight × 1 = weight
    score = priority_score(weight=0.11, recent_accuracy=0.0, attempt_count=5)
    assert score == 0.11


def test_unseen_bonus_disappears_after_first_attempt():
    unseen = priority_score(weight=0.14, recent_accuracy=0.5, attempt_count=0)
    seen   = priority_score(weight=0.14, recent_accuracy=0.5, attempt_count=1)
    assert unseen - seen == 0.3


def test_high_weight_weak_beats_low_weight_strong():
    # An important topic you keep failing should outrank a minor topic you've mastered
    struggling_important = priority_score(weight=0.14, recent_accuracy=0.2, attempt_count=3)
    mastered_minor       = priority_score(weight=0.09, recent_accuracy=0.9, attempt_count=3)
    assert struggling_important > mastered_minor


def test_neutral_accuracy_default_score():
    # Default 0.5 accuracy → weight × 0.5
    score = priority_score(weight=0.10, recent_accuracy=0.5, attempt_count=2)
    assert score == 0.05


def test_higher_weight_wins_at_equal_accuracy():
    hi = priority_score(weight=0.14, recent_accuracy=0.4, attempt_count=2)
    lo = priority_score(weight=0.09, recent_accuracy=0.4, attempt_count=2)
    assert hi > lo
