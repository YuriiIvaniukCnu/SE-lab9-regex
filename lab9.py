import re

from dateutil.parser import parse

DATETIME_PATTERN = re.compile(r"On (.+?\d{1,2}:\d{2}(?::\d{2})?(?:\s?[ap]m)?)", re.IGNORECASE)


def extract_datetime(line):
    match = DATETIME_PATTERN.search(line)
    return parse(match.group(1)).strftime("%Y-%m-%dT%H:%M:%SZ")


if __name__ == '__main__':
    print(extract_datetime("On Sun, 13 Oct 2024 19:01:18 +0800, Test User <test@test.me> wrote:"))
