# Adaptive layout lessons from CityChain

## Scope and evidence

These patterns were inspected in the local CityChain implementation on 2026-10-01. They complement the API examples in iPhone-Duo-by-Examples. The CityChain specification records a successful simulator build and policy tests; that record does not establish correct rendering, focus, accessibility, or keyboard behavior on every Duo configuration. Full runtime validation remains pending. Recheck the source and its validation record before claiming an observed result.

Use these patterns when the requested screen has stateful input or animations and changes composition around a fold or keyboard. Keep application-specific dimensions, artwork, interaction rules, and dependencies out of general Duo guidance.

## Resting composition versus currently usable space

Distinguish the viewport without the software keyboard from the space currently available above it. In CityChain, a separate background measurement using `.ignoresSafeArea(.keyboard)` supplies `restingHeight`, while the main geometry supplies the keyboard-adjusted viewport.

- A composition that should stay stable during typing can use the resting height: for example, retaining two panes or keeping a route animation mounted.
- Placement and fit around an active division must still use currently usable regions. A stable composition does not justify covering the input with the keyboard.
- Do not infer software-keyboard visibility solely from focus; a hardware keyboard may be in use. Do not subtract keyboard height again from geometry that already excludes it.

Treat the background measurement as an implementation candidate, not a universal recipe. Check it during rotation, window resizing, keyboard dismissal, floating/split keyboards, and fold transitions. It must follow the current window, rather than retain a historical maximum height. Some products intentionally collapse secondary content while typing; preserve that requirement when it is explicit.

## Preserve identity where state and animation matter

Switching between unrelated view branches can recreate input controls or animated children. When continuity matters, keep the stateful child in a stable structural position and change its frame or arrangement. Avoid assigning changing identifiers merely to force layout updates.

CityChain keeps its game pane mounted as it moves between regions. Its `ScoutMapTapTarget` also keeps the same button and animated content while interaction eligibility changes. If adopting the button pattern elsewhere, account for keyboard activation and accessibility as well as touch hit testing; the exact interaction gate is application policy.

Do not keep every expensive pane mounted just to preserve identity. CityChain now creates the atlas only when visible; its selected city survives because the parent owns that state. Decide separately whether scroll position or other pane-local state also needs to survive removal.

## Own durable UI state above rearranged panes

Keep the draft, selection, pending operation, and shared presentation state with an owner that survives the arrangement change. Panes consume bindings or immutable values and actions from that owner. Recreating a pane must not restart the game, submit an input again, or discard an in-flight result.

This does not require moving all local state upward. Preserve only the state whose lifetime extends across removal of that pane.

## Tabletop keyboard priority

For a screen with an upper exploration area and lower input area, define what yields when the lower region becomes too small. CityChain prioritizes the active turn and composer, allowing secondary exploration to disappear and the game to occupy a suitable region above or below the division.

Use active reserved-region geometry, in the same coordinate space as the viewport, to determine usable regions. A fallback should not accidentally place important controls across an active fold. When fold information is absent, retain the ordinary adaptive layout.

Choose fit thresholds from the actual controls and text sizes. Do not copy CityChain's thresholds or its policy of preferring a particular region into every application. Verify the transition with an unfinished draft and an operation still in progress.

## Keep layout policy separate from geometry

The UI adapter reads environment values, available dimensions, and active reserved regions. A pure policy selects a semantic arrangement from typed facts. SwiftUI applies that result and owns focus, presentation, geometry, and animation.

SpecificationCore is one optional implementation: CityChain uses ordered predicates with `FirstMatchSpec`, named layout plans, and an explicit fallback. Existing applications can use their own policy mechanism. Do not add the dependency just to follow this reference or turn every rendering-level conditional into a specification.

Test decision boundaries and precedence independently from runtime UI behavior. A passing rule test establishes which plan is selected; it does not prove the resulting views fit or retain focus.

## Local source pointers

CityChain repository: `/Users/egor/Development/GitHub/Specification Project/SwiftDecision-Examples`.

- `Sources/CityChainPresentation/CityChainLayoutPolicy.swift`: resting versus usable height, ordered fold/expanded/focused choices, and local atlas-width policy.
- `CityChainApp/pages/city-chain/ui/CityChainPage.swift`: geometry adapter, resting-height measurement, game-pane identity, atlas lifetime, and tabletop composition.
- `CityChainApp/entities/scout/ui/ScoutView.swift`: `ScoutMapTapTarget` and animated-content identity.
- `Tests/CityChainPresentationTests/CityChainLayoutPolicyTests.swift`: size boundaries, keyboard-related policy cases, and fold precedence.
- `DOCS/CITY_CHAIN_ADAPTIVE_LAYOUT_SPEC.md`: requirements and validation record. Compare descriptive prose with current code; the inspected version still described selected-city details beside the notebook map after that composition had changed to a map with a Scout overlay.

For platform API syntax and the reference project's simulator observations, start with `Examples/TabletopExample.swift`, `Examples/AvoidDivisionExample.swift`, and `Examples/SplitArrangementExample.swift` under `iPhoneDuoByExamples` in the [upstream examples repository](https://github.com/artemnovichkov/iPhone-Duo-by-Examples). Keep application implementation evidence separate from SDK contracts and observed simulator behavior.
