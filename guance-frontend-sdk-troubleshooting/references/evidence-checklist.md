# Evidence Checklist

Use this file when the user has reported a symptom but not enough proof to diagnose it.

## Minimum Case Bundle

Request these items first:

- Which platform this issue belongs to, if known
- SDK package names and versions
- App framework and build tool
- The SDK init block exactly as shipped
- Whether the app sends data through DataKit or direct Guance ingestion
- One screenshot or export from transport evidence filtered to SDK requests
- One screenshot or copy of Console, native log, or build errors
- The exact missing signal
- The environment, service, version, and app name the user expects to query
- The exact page, route, request, or screen used during reproduction

## Signal-Specific Extras

### RUM basics

- Whether manual view tracking is enabled
- Whether the missing item is view, action, resource, long task, or error

### Browser logs

- How logs are produced: explicit logger API, console forwarding, or error forwarding
- Whether the log level threshold excludes the expected record

### Session replay

- Whether replay recording is enabled and when it starts
- Whether privacy masking settings hide the data the user expected to see

### Frontend tracing

- The API origin being called
- The tracing config, especially link-RUM and auto-trace options
- One request header sample showing whether trace headers were injected
- Whether the project uses a custom HTTP client stack that may need manual header injection

### Sourcemap

- The release or version string in the frontend bundle
- The upload command or pipeline step
- The exact minified stack trace and whether Guance resolves it

## Quick Questions

Use a short sequence rather than a long questionnaire:

1. What exact signal is missing: RUM, logs, replay, trace, or sourcemap
2. Which platform is this issue on
3. Do you see the SDK request or client trace activity in transport logs
4. If yes, what status code and endpoint does it hit
5. If it returns success, what app and environment are you searching in

## Red Flags

- User says "nothing reported" but shares no Network screenshot
- User says "Android or iOS trace missing" but shares no platform-specific trace config
- User says "trace missing" but provides no request headers
- User says "sourcemap failed" but version or release is not shared
- User says "SDK configured like docs" without the actual init snippet
