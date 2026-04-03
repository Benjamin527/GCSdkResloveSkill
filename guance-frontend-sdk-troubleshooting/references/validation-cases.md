# Validation Cases

Use these cases to pressure-test the skill after edits. A good answer should ask for missing evidence, route to the correct platform, classify the issue, and propose the smallest next step.

## Case 1: No network request

Prompt:
"We added the Guance browser SDK in a Vite React app but the platform shows nothing. I only know that the page loads."

Expected direction:

- Request init snippet and DevTools Network proof
- Start in the `init` bucket
- Do not claim endpoint problems before confirming any request exists

## Case 2: Request returns 200 but no data

Prompt:
"The SDK POST succeeds with 200, but I still cannot find the data in Guance."

Expected direction:

- Check app, env, service, version, and time-range query scope
- Mention ingestion versus search mismatch

## Case 3: Errors visible, no logs

Prompt:
"Runtime errors show in RUM, but our custom business logs do not."

Expected direction:

- Distinguish RUM error capture from browser log collection
- Ask how logs are emitted and whether logger or console forwarding is enabled

## Case 4: SPA route changes missing

Prompt:
"The first page view exists, but route navigation in our React SPA does not create new views."

Expected direction:

- Check manual versus automatic view tracking
- Ask whether the app calls the relevant start-view API during route changes

## Case 5: Replay missing

Prompt:
"We can see RUM data, but session replay is empty for the sessions we tested."

Expected direction:

- Check replay enablement, sampling, and recording start behavior
- Avoid blaming transport first if base RUM is healthy

## Case 6: Frontend trace not linked

Prompt:
"The page request exists in RUM but we cannot jump to the backend trace."

Expected direction:

- Ask for target API origin and request headers
- Check tracing allowlist, propagated headers, and backend compatibility

## Case 7: Sourcemap unresolved

Prompt:
"Frontend errors are coming in, but stack traces are still minified after sourcemap upload."

Expected direction:

- Check release or version match between bundle and upload
- Ask for upload command and one unresolved stack trace sample

## Case 8: Wrong environment

Prompt:
"The SDK looks alive, but production data seems to appear under another environment."

Expected direction:

- Inspect env and version tags in init code
- Check build-time environment substitution and query filters

## Case 9: React Native trace config missing

Prompt:
"We are using Expo with `@cloudcare/react-native-mobile`. Errors are visible in Guance, but there is no backend trace linkage."

Expected direction:

- Route to `react-native` without asking the user again
- Inspect RN trace config through the native workflow before discussing web allowlists
- Check whether `FTReactNativeTrace.setConfig()` is ever called with `enableLinkRUMData` and `enableNativeAutoTrace`

## Case 10: Android auto trace expectation

Prompt:
"Android 端已经有 RUM 和日志，但 OkHttp 请求没有链路关联。"

Expected direction:

- Route to `android`
- Inspect `FTTraceConfig` and OkHttp-related entrypoints through the native workflow
- Check the actual config path for auto trace and RUM linkage instead of assuming they are on by default

## Case 11: Ambiguous mobile issue

Prompt:
"移动端 SDK 有错误上报，但没有链路关联。"

Expected direction:

- Try quick inference from repo and package markers first
- If platform is still unclear, ask one short clarification question
- Do not inspect all mobile repos in parallel by default
- Do not fall back to browser-only checks until the platform is identified
