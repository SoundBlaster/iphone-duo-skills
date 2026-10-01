---
name: iphone-duo-examples
description: Find and apply SwiftUI examples for iPhone Duo APIs and adaptive layouts. Use for API usage, fold-aware composition, and related implementation patterns.
---

# iPhone Duo Examples

For requests for iPhone Duo API examples, use the upstream example repository as the canonical source:

[artemnovichkov/iPhone-Duo-by-Examples](https://github.com/artemnovichkov/iPhone-Duo-by-Examples)

Read the upstream repository files directly, or use an available checkout selected through `IPHONE_DUO_EXAMPLES_REPO` or discovered in the current workspace. Clone the repository when source inspection requires local files. The skill does not require a particular directory layout.

Search the example catalog and source files first. The project is a SwiftUI-only catalog for iOS 27.1 iPhone Duo APIs, including hinge changes, reserved regions, `ArrangementView`, vertical bar toolbar APIs, and container content margins. Do not assume it contains UIKit examples.

When answering, point to the relevant source file and explain the pattern in context. Preserve the repository's observed API behavior and conventions documented in its `AGENTS.md` and README. Treat those findings as simulator observations for this project, not universal guarantees beyond the documented environment.

When adapting a stateful screen around a fold, keyboard, or changing pane size, read [adaptive layout lessons](references/adaptive-layout-lessons.md). It covers composition stability, state ownership, tabletop fallback, and pure layout policy. Choose patterns according to the application's requirements and verify their behavior in the target environment.

If the upstream source cannot be accessed or the requested API is not covered, explain the limitation and distinguish guidance based on other sources. Do not modify the example repository unless the user asks for a code change there.
