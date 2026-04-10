---
name: guance-best-practice-writing
description: Use when writing or rewriting Guance product, integration, observability, or solution material into a public-facing best-practice article, especially when the source is an internal SOP, rough draft, config note, or Feishu document and the target style should feel like guance.com/learn.
---

# Guance Best Practice Writing

## Overview

Use this skill to turn raw Guance material into a single polished, public-facing best-practice article. The goal is not to preserve the source structure. The goal is to produce a readable article that feels close to `guance.com/learn`: value-first, scenario-led, implementation-grounded, and concise.

## When To Use

Use this skill when the user wants any of the following:

- Rewrite an internal Guance document into an external best-practice article
- Convert a Feishu wiki, integration note, or troubleshooting SOP into a publishable article
- Write a Guance practice article for a product feature, integration, technical stack, or observability scenario
- Make an article sound closer to `guance.com/learn`

Do not use this skill for:

- Pure bug diagnosis with no writing deliverable
- API reference writing
- Internal runbooks that should remain operator-facing checklists

## Output Contract

Unless the user asks otherwise, output one final article only.

The default deliverable is:

- One title suitable for external publication
- One complete article body in Chinese
- Tone close to `guance.com/learn`
- No parallel versions, no notes to the editor, no change log

If the user explicitly asks for screenshot placement or Feishu publishing markup, provide that as a separate variant.

## Style Rules

- Lead with business or operational context before configuration details
- Explain why the practice matters before explaining how to configure it
- Keep paragraphs short and readable
- Use confident, practical language, not internal memo language
- Sound professional and product-aware, but do not drift into ad copy
- Prefer "场景/收益/方案/步骤/验证/总结" over raw step dumps
- Keep implementation details accurate and concrete
- If a config block is necessary, explain the 2 to 4 critical fields outside the code block first
- Do not put comments inside JSON examples

## Article Shape

Use this default structure unless the source material clearly needs a tighter variant:

1. Background
2. Why this matters or expected gains
3. Solution overview
4. Preconditions
5. Implementation steps
6. Validation or expected effect
7. Common issues or key considerations
8. Summary

For a shorter article, compress sections 2 and 3, and merge sections 6 and 7 if needed.

Read [references/article-pattern.md](references/article-pattern.md) before drafting.

## Rewrite Workflow

### 1. Classify the source

Decide what the user gave you:

- Internal SOP
- Feishu wiki
- Config tutorial
- Product capability note
- Mixed draft with screenshots and config

Then strip away internal-only structure such as:

- Repeated "步骤 1/步骤 2"
- Screen-by-screen click records with no explanation
- Self-referential notes like "见本文配置"
- Raw troubleshooting bullets with no narrative bridge

### 2. Extract the real message

Before writing, identify:

- The target reader
- The core scenario
- The main outcome after adoption
- The 2 to 4 implementation details that actually decide success

If the source is heavy on configuration, make sure the article still answers:

- Why would a Guance user do this
- What changes after it is implemented
- What are the key integration constraints

### 3. Rebuild into public article form

Reshape the source into a reading experience:

- Start from scenario and value
- Introduce the solution path
- Then explain steps
- End with validation and takeaways

Do not preserve internal section names by default. Rename aggressively when it improves clarity.

### 4. Control the tone

The target tone is:

- More polished than an internal knowledge base
- More technical than a marketing poster
- More readable than a product manual

Good signals:

- "对于已经使用飞书作为统一办公入口的企业来说..."
- "完成接入后，团队通常可以获得以下几项直接收益..."
- "需要重点关注的两个实现细节是..."

Bad signals:

- "点击这里然后点击那里"
- "具体配置见上文"
- "这个地方非常重要一定要注意"
- Overstated claims with no technical grounding

### 5. Treat code and config carefully

When keeping JSON, YAML, TOML, or code snippets:

- Keep them syntactically valid
- Remove inline comments that would break literal parsing
- Summarize the important fields before or after the block
- Keep only the minimum example needed for the article

### 6. Produce one clean final draft

Unless the user asked for alternatives, output one article only.

The final draft should be ready to paste into Feishu, a CMS, or a publishing workflow with minimal cleanup.

## Default Response Shape

Use this pattern for the final answer:

```markdown
# 标题

## 背景
...

## 为什么值得做
...

## 方案说明
...

## 前提条件
...

## 配置步骤
...

## 效果验证
...

## 常见问题
...

## 总结
...
```

## Common Mistakes

- Turning the article into a long screenshot script
- Copying internal section order directly into the final article
- Keeping broken JSON comments inside a code block
- Writing only configuration steps and skipping business context
- Making the tone too sales-heavy
- Returning multiple versions when the user asked for one final article
