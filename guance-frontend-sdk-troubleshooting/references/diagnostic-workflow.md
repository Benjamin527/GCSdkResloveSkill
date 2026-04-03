# Diagnostic Workflow (Web and Miniapp)

Use this file for `web` and `miniapp` init, transport, and ingestion style failures.

## Step 1: Confirm runtime and init path

Check whether the SDK init code actually executes in the browser or miniapp runtime.

Common issues:

- Init placed in code that never loads on the affected page
- SSR frameworks invoking browser-only code on the server
- Build-time environment guards disabling init in the deployed bundle
- Miniapp lifecycle code never reaching the page or app hook where init should run
- Exceptions during init caused by bad config or missing globals

Evidence to prefer:

- The built init snippet
- Console errors at page load
- A breakpoint or log that proves init runs

## Step 2: Confirm endpoint model

Guance browser-style SDK access is usually configured in one of two ways:

- Direct Guance DataWay style access using site and client token
- DataKit style access using a DataKit origin

If the user mixes configuration models, requests may hit the wrong target or never authenticate correctly. Confirm which path the project intends to use before checking anything else.

## Step 3: Confirm request behavior

Look for SDK requests in DevTools Network or the platform's request inspector.

Interpretation:

- No request: init did not run, did not flush, or all relevant events were filtered out
- Blocked request: browser policy or adblock issue
- Non-2xx request: endpoint, auth, proxy, CORS, or payload issue
- 2xx request: move to ingestion and query-scope checks

High-value transport checks:

- Request URL host and path
- Status code
- CSP violation messages
- CORS failure text
- Miniapp legal-domain or platform request-policy failures
- Reverse proxy rewrites
- HTTP to HTTPS mixed content

## Step 4: Confirm the user is querying the right scope

When requests succeed, many "missing data" reports are actually search mismatches.

Check:

- Correct app or workspace
- Correct environment
- Correct service or version
- Correct time range
- Correct query filters

Do not skip this step just because the code "looks right".

## Step 5: Distinguish drop or sample behavior

If traffic arrives inconsistently:

- Check sample rates and feature-level sampling
- Check filters that intentionally exclude internal users, bots, or local hosts
- Check whether the event type is only emitted after a specific trigger
- Check whether replay or view tracking requires extra API calls

## Step 6: Narrow to the missing feature

Once base transport is proven healthy, switch to [signal-matrix.md](signal-matrix.md).

## Official Source Anchors

Use official Guance docs before a final answer:

- Web app access: https://docs.guance.com/real-user-monitoring/web/app-access/
- Miniapp app access: https://docs.guance.com/real-user-monitoring/miniapp/app-access/
- Session replay: https://docs.guance.com/real-user-monitoring/session-replay/web/
- Browser logs: https://docs.guance.com/logs/browser-collection/
- Sourcemap: https://docs.guance.com/real-user-monitoring/sourcemap/

If a doc detail conflicts with memory, trust the doc and say so.
