# Platform Routing

Use this file before reading source.

## Goal

Choose one platform first, then inspect only that platform's key source entrypoints from [source-registry.yaml](source-registry.yaml).

## Routing Order

1. If the user explicitly says the platform, trust that first.
2. Otherwise infer from package names, import names, file paths, build files, or issue wording.
3. If multiple platforms remain plausible, ask one short clarification question.

Do not inspect all platform repos by default.

## Explicit Platform Keywords

- `web`: `web`, `browser`, `vite`, `webpack`, `next`, `react`, `vue`, `allowedTracingOrigins`, `fetch`, `xhr`
- `miniapp`: `小程序`, `微信小程序`, `miniapp`, `wx.request`
- `android`: `android`, `gradle`, `kotlin`, `java`, `okhttp`
- `ios`: `ios`, `swift`, `objective-c`, `cocoapods`, `NSURLSession`
- `react-native`: `react native`, `expo`, `@cloudcare/react-native-mobile`
- `flutter`: `flutter`, `dart`, `pubspec.yaml`, `dio`
- `uniapp`: `uniapp`, `uni-app`, `uni.request`, `hbuilder`
- `harmony`: `harmony`, `鸿蒙`, `ohos`
- `unity`: `unity`, `c#`, `UnityWebRequest`

## Source Inference Hints

- `@cloudcare/react-native-mobile`, `FTMobileReactNative`, `FTReactNativeRUM`, `FTReactNativeTrace` strongly indicate `react-native`
- `FTMobileFlutter`, `FTTracer`, `ft_mobile_agent_flutter`, `dio` wrappers indicate `flutter`
- `GCUniPlugin-RUM`, `GCUniPlugin-Tracer`, `uni.requireNativePlugin` indicate `uniapp`
- `FTUnityBridge`, `FTSDK.cs`, `TraceConfig`, `UnityWebRequest` indicate `unity`
- `FTSDKConfig`, `FTRUMConfig`, `FTTraceConfig`, `FTSdk.initTraceWithConfig` indicate `android`
- `FTMobileAgent`, `FTTracer`, `FTURLSessionInterceptor`, `FTRumConfig` indicate `ios`
- `DATAFLUX_RUM.init`, `allowedTracingOrigins`, `injectTraceHeader` indicate `web`
- `datafluxRum.init`, `wx.request`, `allowedTracingOrigins` indicate `miniapp`

## Version Handling

- If the SDK version is known, prefer the matching release or tag.
- If only a package range is known, state that source analysis is based on the latest visible implementation in the registered source.
- If the platform source is a static hosted JS bundle, treat that exact URL as the current implementation snapshot.

## Common Trace Entry Checks

For trace-linkage issues, inspect these before anything else:

- Whether trace config is initialized at all
- Whether `enableLinkRUMData` or equivalent association switch is enabled
- Whether `enableAutoTrace` or `enableNativeAutoTrace` is enabled when the user expects automatic header injection
- Whether manual `getTraceHeader` style APIs are used for custom HTTP stacks
- Whether web or miniapp origin allowlists include the target API origin

## When To Ask The User

Ask the user only if the platform cannot be inferred from:

- The repo or file tree
- Import statements
- Package names
- The user's wording

Good clarification:

- "这是 Web、React Native、还是原生 Android/iOS 的 SDK 问题？"
