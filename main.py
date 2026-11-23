from pathlib import Path

# Final polished line: specific 6 a.m. detail up front, twist lands on the last word.
LINE = "I set my alarm for 6 a.m. to be productive, then hit snooze like it owes me money."

target = Path("/output/entry.txt")
target.parent.mkdir(parents=True, exist_ok=True)
target.write_bytes((LINE + "\n").encode("utf-8"))
