#!/usr/bin/env python3

import subprocess
import re
from collections import OrderedDict

def get_tags():
    raw_tags = subprocess.check_output(["git", "tag", "--sort=-creatordate"]).decode().splitlines()
    return [tag for tag in raw_tags if re.match(r"^v\d+\.\d+\.\d+$", tag)]

def get_commits_between(old_tag, new_tag):
    log = subprocess.check_output(["git", "log", f"{old_tag}..{new_tag}", "--oneline"]).decode()
    return log.strip().splitlines()

def generate_changelog():
    tags = get_tags()
    changelog = OrderedDict()

    for i in range(len(tags) - 1):
        newer, older = tags[i], tags[i + 1]
        entries = get_commits_between(older, newer)
        changelog[newer] = entries

    # First release commits (from initial commit to oldest tag)
    if tags:
        initial_commits = subprocess.check_output(["git", "log", tags[-1], "--oneline"]).decode().strip().splitlines()
        changelog[tags[-1]] = initial_commits

    return changelog

def write_changelog(changelog):
    with open("CHANGELOG.md", "w") as f:
        f.write("# 🔄 Changelog\n\n")
        for version, commits in changelog.items():
            f.write(f"## [{version}]\n")
            for commit in commits:
                f.write(f"- {commit}\n")
            f.write("\n")

if __name__ == "__main__":
    print("🚀 Generating changelog from Git tags...")
    changelog_data = generate_changelog()
    write_changelog(changelog_data)
    print("✅ CHANGELOG.md created!")
