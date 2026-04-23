# GCSdkResolveSkill

Installable Codex skills for Guance-related troubleshooting and writing workflows.

## Install

Use your Codex skill installer to install this repo path:

- Repo: `Benjamin527/GCSdkResloveSkill`
- Paths:
  - `guance-frontend-sdk-troubleshooting`
  - `guance-best-practice-writing`
  - `doc-to-image2-prompt`

If you are using the built-in GitHub installer flow, install that path from this repo and then restart Codex.

## Skill Path

- `guance-frontend-sdk-troubleshooting`
- `guance-best-practice-writing`
- `doc-to-image2-prompt`

## What It Does

- `guance-frontend-sdk-troubleshooting`
  - Routes to the correct Guance client platform before source inspection
  - Splits browser-style and native-style diagnostics so platform checks stay relevant
  - Uses platform-specific public source or docs as evidence
  - Helps diagnose no-data, partial-data, trace-linkage, replay, log, and sourcemap issues
  - Includes a source registry covering Web, Miniapp, Android, iOS, HarmonyOS, React Native, Flutter, uniapp, and Unity
- `guance-best-practice-writing`
  - Rewrites internal Guance material into public-facing best-practice articles
  - Targets a style close to `guance.com/learn`
  - Converts SOP-style notes into readable "背景/收益/方案/步骤/验证/总结" structures
  - Keeps technical details accurate while removing internal-document tone
- `doc-to-image2-prompt`
  - Turns docs, wiki pages, and pasted notes into ready-to-send GPT Image 2 prompts
  - Compresses long technical material into visual sections such as concepts, flows, comparisons, and FAQ
  - Preserves source meaning while producing copy-ready infographic or explanation-image prompts
