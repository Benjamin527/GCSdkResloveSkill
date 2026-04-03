---
name: guance-frontend-sdk-troubleshooting
description: Use when analyzing Guance SDK integration issues across web, miniapp, React Native, Android, iOS, Flutter, uniapp, HarmonyOS, or Unity, especially for no data, partial data, trace linkage gaps, replay failures, or sourcemap and tagging problems.
---

# Guance Frontend SDK Troubleshooting

## Overview

Use this skill to debug Guance client-side SDK integrations in a disciplined way across web and mobile-adjacent platforms. Start from evidence, route to the correct platform source, choose the matching web or native workflow, inspect the smallest relevant set of entrypoints, then narrow to the likely root cause instead of guessing from symptoms.

## When To Use

Use this skill when the user reports any of the following:

- Guance frontend or client SDK data never appears after access
- Only some signals arrive, such as errors but no performance, logs but no RUM, or replay but no traces
- Data appears in the wrong app, wrong environment, or wrong version
- Requests exist but Guance does not show the expected data
- Session replay, sourcemap, or frontend-backend trace correlation is broken
- The user wants a repeatable diagnostic checklist for Guance SDK access on web, miniapp, Android, iOS, React Native, Flutter, uniapp, HarmonyOS, or Unity

Do not use this skill for backend DataKit deployment, server-side tracing with no client SDK involvement, or generic app bugs unrelated to Guance SDK behavior.

## Core Rules

- Gather evidence before concluding. If the user has not shared enough proof, ask for the minimum missing artifacts first.
- Route to the correct platform before reading source. Do not inspect every SDK repo by default.
- Separate `init`, `transport`, `ingest`, `feature`, and `postprocess` failures.
- For native-family platforms, prefer platform logs, bridge config, and interceptor state over browser-only checks.
- Prefer official Guance behavior and public source over memory.
- Prefer version-matched source when available. If the user version is unknown, say that source analysis is based on the latest visible implementation.
- Read only the 2 to 5 most relevant source entrypoints for the chosen platform unless evidence forces a wider search.
- Never say "configured correctly" unless you have matching code, network, or source evidence.

## Minimum Intake

Before diagnosing deeply, collect as many of these as possible:

- The target platform, if the user already knows it
- SDK package names and versions
- Framework and build tool
- The initialization snippet
- Whether the project uses DataKit or direct Guance DataWay access
- Screenshot or copy of SDK network requests
- Console errors and CSP, CORS, or permission failures
- The exact signal missing: RUM, resource, action, error, log, trace, replay, sourcemap
- Environment, version, service, release, or app identifiers expected by the user
- Time range and query conditions used in Guance when they say data is missing

If the evidence is sparse, use `scripts/intake_template.py` to generate a short checklist for the user.

## Workflow

### 1. Route to the correct platform

Use [platform-routing.md](references/platform-routing.md) and [source-registry.yaml](references/source-registry.yaml).

Routing order:

- If the user explicitly says a platform, route there first
- Otherwise infer from package names, import names, file paths, frameworks, build files, and issue wording
- If still ambiguous after quick inspection, ask the user which platform they mean before reading more source

After routing, open only that platform's key entrypoints from the registry.

### 2. Classify the failure surface

Put the case into one primary bucket first:

- `init`: SDK code never runs, runs too late, or crashes during init
- `transport`: request is absent, blocked, malformed, or sent to the wrong endpoint
- `ingest`: request succeeds but data is dropped, sampled, filtered, or queried under the wrong app or environment
- `feature`: base SDK works but one feature is missing, such as replay, tracing, logs, view tracking, or user action tracking
- `postprocess`: data arrived but sourcemap, release tagging, or correlation fields are wrong

### 3. Check whether the client emitted anything

Ask first:

- Do you see SDK network requests or native trace activity for the failing flow
- Are the requests sent to the expected Guance endpoint
- Are they blocked by CSP, CORS, adblock, proxy, TLS, or platform-specific permission rules

Interpretation:

- No request usually means `init` or aggressive filtering before send
- Failed request usually means `transport`
- Successful request but no data usually means `ingest`, `feature`, or wrong query scope

### 4. Run the matching branch

For platform selection, source entrypoints, and version handling, read [platform-routing.md](references/platform-routing.md).

For per-platform repository and key file metadata, read [source-registry.yaml](references/source-registry.yaml).

For `web` and `miniapp` `init` and `transport`, read [diagnostic-workflow.md](references/diagnostic-workflow.md).

For `android`, `ios`, `react-native`, `flutter`, `uniapp`, `unity`, and `harmony` `init` and `transport`, read [native-diagnostic-workflow.md](references/native-diagnostic-workflow.md).

For signal-specific gaps, read [signal-matrix.md](references/signal-matrix.md).

For what to request from the user, read [evidence-checklist.md](references/evidence-checklist.md).

For realistic validation prompts and expected diagnoses, read [validation-cases.md](references/validation-cases.md).

### 5. Produce an evidence-based conclusion

End with this shape:

1. What is proven by the current evidence
2. Most likely root cause
3. What is still uncertain
4. The next smallest confirming step
5. A concrete fix snippet or configuration change if the cause is known

## Fast Checks

Use these checks often because they eliminate many branches quickly:

- Whether the chosen platform's trace config actually exists in code and is initialized
- Whether endpoint configuration matches the chosen ingestion path
- Whether environment, app ID, version, and release values match what the user is querying
- Whether feature toggles are enabled for the missing signal
- Whether time range, app selection, and search filters in Guance match the test request
- Whether tracing config enables RUM linkage and automatic header injection when the user expects auto trace
- Whether web or miniapp origin allowlists include the target API origin
- Whether sourcemap upload uses the same version and environment as the minified bundle

If the case still looks broad, use the platform-specific priority checks in [source-registry.yaml](references/source-registry.yaml) plus the signal branches in [signal-matrix.md](references/signal-matrix.md) before widening the search.

## Response Style

- Keep the first answer focused on the most likely branch, not every possibility at once
- Use short evidence statements like "Trace config missing in init" or "POST returns 200 but app/env query may be wrong"
- When using source evidence, cite the platform file or class that supports the conclusion
- If you infer rather than prove, label it as a hypothesis
- Offer one next action at a time when the user is actively debugging
