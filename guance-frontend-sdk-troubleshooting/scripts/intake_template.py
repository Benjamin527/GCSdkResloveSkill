#!/usr/bin/env python3
"""
Render a compact intake checklist for Guance frontend SDK troubleshooting.
"""

from __future__ import annotations

import argparse


BASE_ITEMS = [
    "SDK package names and versions",
    "Framework and build tool",
    "Exact SDK init snippet",
    "Whether ingestion uses DataKit or direct Guance access",
    "DevTools Network screenshot or request details",
    "Console errors or browser security warnings",
    "Exact missing signal",
    "Expected app/env/version/service values",
]

EXTRA_BY_KIND = {
    "rum": [
        "Whether view tracking is automatic or manual",
        "Which signal is missing: view, action, resource, long task, or error",
    ],
    "logs": [
        "How logs are emitted: logger API, console forwarding, or error forwarding",
        "Configured log level threshold",
    ],
    "replay": [
        "Whether replay is enabled",
        "Whether recording starts automatically or via explicit call",
    ],
    "trace": [
        "Target API origin",
        "One request header sample showing trace propagation",
        "Frontend tracing config, including allowlist and propagator type",
    ],
    "sourcemap": [
        "Frontend release or version string",
        "Upload command or CI step",
        "One unresolved minified stack trace sample",
    ],
}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Print a compact intake checklist for Guance frontend SDK issues."
    )
    parser.add_argument(
        "--kind",
        choices=sorted(EXTRA_BY_KIND),
        help="Optional signal type to append focused questions.",
    )
    args = parser.parse_args()

    print("Please share the following so I can narrow this down:")
    for item in BASE_ITEMS:
        print(f"- {item}")

    if args.kind:
        print("")
        print(f"Extra items for {args.kind}:")
        for item in EXTRA_BY_KIND[args.kind]:
            print(f"- {item}")


if __name__ == "__main__":
    main()
