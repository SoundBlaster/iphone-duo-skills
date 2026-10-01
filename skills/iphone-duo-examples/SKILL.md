---
name: iphone-duo-examples
description: Find and use SwiftUI examples for iPhone Duo APIs from the user's reference repository. Apply when asked for an iPhone Duo example, API usage, or a related implementation pattern.
---

# iPhone Duo Examples

For requests for iPhone Duo API examples, use the upstream example repository as the canonical source:

[artemnovichkov/iPhone-Duo-by-Examples](https://github.com/artemnovichkov/iPhone-Duo-by-Examples)

If a local checkout is useful for source inspection, use the configured `IPHONE_DUO_EXAMPLES_REPO` path when available, or discover a checkout in the current workspace. The author's current checkout is `/Users/egor/Development/GitHub/iPhone-Duo-by-Examples`, but that path is machine-specific and must not be assumed to exist. If there is no local checkout, read the upstream repository files directly; clone it only when local file access is needed and available.

Search the example catalog and source files first. The project is a SwiftUI-only catalog for iOS 27.1 iPhone Duo APIs, including hinge changes, reserved regions, `ArrangementView`, vertical bar toolbar APIs, and container content margins. Do not assume it contains UIKit examples.

When answering, point to the relevant source file and explain the pattern in context. Preserve the repository's observed API behavior and conventions documented in its `AGENTS.md` and README. Treat those findings as simulator observations for this project, not universal guarantees beyond the documented environment.

When adapting a stateful screen around a fold, keyboard, or changing pane size, read [adaptive layout lessons](references/adaptive-layout-lessons.md). It covers composition stability, state ownership, tabletop fallback, and pure layout policy using CityChain as an implementation example. Its application patterns are not additional Apple API guarantees.

If the repository is absent or the requested API is not covered, say so and then provide a clearly distinguished answer based on other available sources. Do not modify the example repository unless the user asks for a code change there.
