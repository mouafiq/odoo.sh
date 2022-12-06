#!/usr/bin/env python3

import subprocess
import json
from pathlib import Path
import yaml
import os
gimera_file = Path("gimera.yml")
gimera = yaml.load(gimera_file.read_text())
root = Path(os.getcwd())

versions = [12.0, 13.0, 14.0, 15.0, 16.0]

repos = json.loads(
    subprocess.check_output(
        ["gh", "repo", "list", "OCA", "--json", "name,url"], encoding="utf8"
    )
)

for repo in repos:
    for version in versions:
        subfolder = root / "OCA" / repo['name'] + "." + str(version)

        existing = [x for x in gimera if gimera['url'] == repo['ur'] and gimera['branch'] == str(version)]
        if not existing:
            gimera['repos'].append({
                'url': repo['url'],
                'path': str(subfolder.relative_to(root)),
                'branch': str(version),
            })
