# Signal Matrix

Use this file when base SDK access works but a specific signal is missing or malformed.

## RUM views and actions

Check:

- Whether the SDK is initialized on the affected route
- Whether view tracking is automatic or manual
- If manual, whether the app actually calls the start-view API
- Whether action tracking or interaction tracking is enabled

Typical symptoms:

- Errors appear but no page views
- First page has data, SPA route changes do not
- User actions never appear

## Resource and performance timing

Check:

- Whether the browser or privacy settings block timing collection
- Whether the missing page actually triggers the performance entry type
- Whether the issue is limited to cross-origin resources without timing allow headers

## Browser logs

Check:

- Which logger API is used
- Whether console forwarding is enabled
- Whether log level filters remove the expected entry
- Whether error forwarding is mistaken for generic logs

Typical symptom:

- Errors exist in RUM, but application logs are absent because only RUM error capture is enabled.

## Session replay

Check:

- Whether replay is enabled in config
- Whether replay recording starts automatically or requires an explicit start call
- Whether privacy masking hides what the user expected to inspect
- Whether the page reproduces under the sampling rate currently configured

Typical symptom:

- RUM data is present, but replay is empty or missing for only some sessions.

## Frontend-backend tracing

Check:

- Whether the target API origin is included in the tracing allowlist
- Whether the browser request contains injected trace headers
- Whether the backend accepts the propagator type the frontend sends
- Whether CORS allows the custom tracing headers

Typical symptom:

- RUM request data exists, but the related backend span is not linked.

## Sourcemap

Check:

- Whether the frontend release or version matches the uploaded sourcemap metadata
- Whether the uploaded files correspond to the deployed minified bundle
- Whether the stack trace belongs to the same build
- Whether the environment used during upload matches the environment where the error is queried

Typical symptom:

- Error events arrive, but stack traces stay minified.

## High-Confidence Heuristics

- "No trace link" with no request headers shared: treat as unproven until headers are checked
- "No replay" with healthy RUM: check replay enablement and sampling before transport
- "No SPA views" with first page working: check manual versus automatic view tracking
- "No logs" with errors visible: inspect logger init and forwarding options
