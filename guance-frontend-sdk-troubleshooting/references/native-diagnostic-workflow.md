# Native Diagnostic Workflow

Use this file for `android`, `ios`, `react-native`, `flutter`, `uniapp`, `unity`, and `harmony` init, transport, and ingestion style failures.

## Step 1: Confirm the real init path

Check whether the SDK init code executes in the app lifecycle that matches the failing flow.

Common issues:

- Init is behind a feature flag, build variant, or environment branch
- Init happens in JavaScript but the native bridge config never runs
- Init is present in code, but not on the startup path for the affected screen or process
- The app uses different config for debug and release builds
- Exceptions during init are visible only in native logs

Evidence to prefer:

- The shipped init snippet or config object
- Native logs such as Logcat, Xcode console, Expo logs, or Flutter run output
- One proof that the trace or RUM config method is actually called

## Step 2: Confirm the config object that owns the missing behavior

Separate the relevant config surface before debugging transport:

- Base SDK or agent init
- RUM config
- Trace config
- Log config
- Replay config where supported

Do not assume trace linkage is enabled just because base RUM or logs are healthy.

## Step 3: Confirm the instrumentation path

Decide whether the app depends on automatic instrumentation or a custom network stack.

High-value checks:

- Whether the platform's trace config is initialized at all
- Whether automatic tracing is enabled for the SDK version in use
- Whether RUM linkage is enabled where the platform supports it
- Whether the app uses a custom HTTP client, bridge layer, or wrapper that needs manual trace header injection
- Whether the relevant interceptor, bridge, or helper is actually wired into requests

Interpretation:

- No trace config usually means `init` or `feature`
- Healthy RUM or logs without linkage usually means trace config or request instrumentation is incomplete
- Requests visible on the backend but not linked usually means propagation, linkage flags, or query-scope mismatch

## Step 4: Confirm transport or native evidence

For the failing request or action, collect the smallest proof that the client emitted anything:

- Native logs or bridge logs showing request interception
- Header samples for the target request
- Error text from the SDK, bridge, or platform network layer
- Any platform permission or allowlist failures relevant to transport

Avoid browser-only checks unless the platform is actually `web` or `miniapp`.

## Step 5: Confirm ingestion and query scope

When the client appears healthy, verify the user is searching in the right place:

- Correct app or workspace
- Correct environment
- Correct service, version, release, or app ID
- Correct time range and filters

This step matters just as much on native platforms as on web.

## Step 6: Narrow to the missing feature

Once init and transport evidence are proven, switch to [signal-matrix.md](signal-matrix.md).

## Official Source Anchors

Use official Guance docs before a final answer:

- Android app access: https://docs.guance.com/real-user-monitoring/android/app-access/
- iOS app access: https://docs.guance.com/real-user-monitoring/ios/app-access/
- React Native app access: https://docs.guance.com/real-user-monitoring/react-native/app-access/
- Flutter app access: https://docs.guance.com/real-user-monitoring/flutter/app-access/
- Uniapp app access: https://docs.guance.com/real-user-monitoring/uniapp/app-access/
- HarmonyOS app access: https://docs.guance.com/real-user-monitoring/harmonyos/app-access/
- Unity app access: https://docs.guance.com/real-user-monitoring/unity/app-access/

If a doc detail conflicts with memory, trust the doc and say so.
