---
name: doc-to-image2-prompt
description: Use when the user wants a document, article, wiki page, or pasted notes turned into a ready-to-send GPT Image 2 prompt for generating an explanation image, infographic, cover graphic, or summary visual.
---

# Doc to GPT Image 2 Prompt

## Overview

This skill converts source documents into a single high-quality prompt for GPT Image 2.

The output should preserve the document's meaning, compress the content into a visual hierarchy, and be ready to copy into an image model without further cleanup.

## When to Use

Use this skill when the user wants any of the following:

- "Summarize this document into an image prompt"
- "Give me a GPT Image 2 prompt based on this article"
- "Turn this wiki into an infographic prompt"
- "Generate a prompt for a documentation explanation image"
- "Make a visual summary prompt from this page"

Do not use this skill when:

- The user wants the final image generated directly in this conversation
- The user wants a prose summary rather than an image-generation prompt
- The source material is too incomplete to infer the topic safely

## Input Types

Handle any of these sources:

- A pasted document or article
- A public documentation URL
- A Feishu/Lark wiki or doc URL if the content is available through connected tools
- Notes, outlines, or internal SOP text

If the source is long, extract only the core structure:

- What the thing is
- Why it matters
- Key concepts or comparisons
- Main workflow or steps
- Common pitfalls or FAQ

## Output Contract

Unless the user asks otherwise, output only one final prompt.

The prompt should:

- Be written for GPT Image 2
- Be ready to copy and send
- Specify language, layout, tone, and visual structure
- Keep the original document meaning intact
- Prefer Chinese if the source and user request are Chinese

If the user explicitly asks for "only the final prompt", output only the prompt text.

## Workflow

### 1. Read the source

Identify:

- Title or topic
- Audience
- Core message
- 3 to 6 major sections worth visualizing

Ignore low-value details such as:

- Repeated screenshots
- Long code listings
- Raw command noise unless central to the concept
- Decorative wording

### 2. Choose a visual form

Pick the most suitable visual format:

- **Information poster**: for "what it is + how it works + quick start"
- **Infographic**: for comparisons, structured guidance, FAQ, or workflows
- **Documentation cover illustration**: for high-level topic summaries
- **Architecture explanation graphic**: for systems, components, or interactions

If the user does not specify, default to:

- `Chinese technical infographic poster`

### 3. Rebuild content for visuals

Convert the source into image-friendly sections:

- Title
- Subtitle
- 3 to 6 content blocks
- Optional flowchart or comparison
- Optional FAQ or summary strip

Do not dump the article into the prompt verbatim. Compress it into visual logic.

### 4. Write the prompt

A strong prompt usually includes:

- Image goal
- Style direction
- Layout structure
- Section-by-section content
- Typography and language constraints
- What to avoid

## Default Prompt Shape

Use this structure unless the user wants another format:

```text
请根据以下主题生成一张中文技术信息图海报。

主题：
...

目标：
...

整体风格：
...

版面结构：
1. 顶部标题区
2. 核心概念区
3. 对比 / 流程区
4. 实战 / 示例区
5. FAQ / 总结区

内容要求：
...

输出要求：
...
```

## Writing Rules

- Keep the prompt specific enough to control layout
- Keep the wording compact enough to remain usable
- Preserve the source meaning; do not invent claims
- Prefer section labels over dense paragraphs
- If examples exist in the source, abstract them into visual blocks instead of copying full code
- If the user wants a one-shot prompt, do not add explanation outside the prompt

## Common Mistakes

- Copying the whole document into the prompt
- Turning a summary request into a prose article
- Losing the distinction between "what it is" and "how to use it"
- Overfocusing on code and underfocusing on visual hierarchy
- Adding extra interpretation not supported by the source

## Final Check

Before responding, verify:

- The prompt matches the document topic
- The prompt is suitable for GPT Image 2
- The structure is visually clear
- The output language matches the user's request
- If requested, the response contains only the final prompt
