# Adaptive layout principles

## Scope and evidence

Use these patterns for screens with stateful input or animations whose composition changes around a fold, keyboard, or resized pane. Choose dimensions, interaction rules, and dependencies from the application being adapted.

Distinguish SDK contracts, observations from a particular simulator or device, and application design choices. A successful build establishes compile compatibility. Policy tests establish which arrangement is selected. Rendering, focus, accessibility, and keyboard behavior require runtime checks in the intended configurations.

## Stable composition and usable space

Distinguish the viewport without the software keyboard from the space currently available above it. When composition should remain stable during typing, an independent measurement that ignores the keyboard safe area can provide a baseline while the main geometry supplies the usable viewport.

- Use the baseline for composition choices that should remain stable, such as retaining an input pane or animated child.
- Use currently usable regions to place controls around an active division and keep input reachable.
- Account for hardware keyboards: focus alone does not establish software-keyboard visibility.
- Avoid subtracting keyboard height from geometry that already excludes it.

Use independent measurements only when needed by the product's behavior. They must follow the current window rather than retain a historical maximum size. Check rotation, window resizing, keyboard dismissal, floating or split keyboards, and fold transitions. If secondary content should collapse during typing, make that an explicit composition rule.

## Preserve identity where continuity matters

Switching between unrelated view branches can recreate input controls or animated children. Keep a stateful child in a stable structural position when its draft, focus, or animation must survive arrangement changes. Change its frame or arrangement without assigning changing identifiers merely to force updates.

For an animated control whose interaction eligibility changes, preserve the control's identity and update its interaction state. Account for keyboard activation and accessibility as well as touch hit testing.

Create expensive secondary panes only when needed. Keep durable selection or presentation state in an owner that survives their removal. Decide separately whether pane-local state, such as scroll position, also needs to survive.

## Own durable state above rearranged panes

Keep drafts, selection, pending operations, and shared presentation state with an owner that survives arrangement changes. Panes consume bindings or immutable values and actions from that owner. Recreating a pane must preserve unfinished input and must not duplicate an operation or discard an in-flight result.

Choose ownership according to state lifetime. State used only while a pane is visible can remain within that pane.

## Tabletop keyboard priority

For a screen with exploration in one region and input in another, define which content yields when the input region becomes too small. Prioritize the active task and composer; secondary content can collapse or disappear, and primary content can move into a region where it fits.

Use active reserved-region geometry in the viewport's coordinate space to determine usable regions. Fallback arrangements must keep important controls clear of an active fold. When fold information is unavailable, retain the ordinary adaptive layout.

Choose fit thresholds from the actual controls, text sizes, and required content. Define region preference explicitly rather than assuming the upper or lower region always wins. Verify transitions with an unfinished draft and an operation still in progress.

## Separate layout policy from geometry

The UI adapter reads environment values, available dimensions, and active reserved regions. A pure policy selects a semantic arrangement from typed facts. SwiftUI applies that result and owns focus, presentation, geometry, and animation.

For decisions with competing requirements, named predicates, explicit precedence, and a fallback make the policy easier to inspect. Use the application's existing policy mechanism when it fits. Keep simple rendering choices within the view when extracting them would add no useful structure.

Check decision boundaries and precedence independently from runtime UI behavior. A passing policy test establishes the selected plan; runtime checks establish whether its views fit and retain focus.

## Public API examples

For platform API syntax and simulator observations, start with `Examples/TabletopExample.swift`, `Examples/AvoidDivisionExample.swift`, and `Examples/SplitArrangementExample.swift` under `iPhoneDuoByExamples` in the [upstream examples repository](https://github.com/artemnovichkov/iPhone-Duo-by-Examples). Read its current README and source before adopting a pattern, and record the SDK and runtime used for verification.
