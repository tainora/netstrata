# AI Coding Principle: The Left-Right Balance (⊣ Framework)

**Source**: Recovered from `02-ai-augmented-development-methodology.md` (commit 6e00cf5, before Phase 2 compression)

**Date Recovered**: 2025-11-12

**Context**: This principle was part of the original AI-augmented development methodology document but was removed during Phase 2 compression (281 → 118 lines). Preserved here as standalone reference for future use.

---

## The Fundamental Tension

**The fundamental tension**: In most businesses, margins come from secrets—proprietary knowledge, non-obvious insights, and idiosyncratic processes create advantage. That is **not** how modern software engineering works.

In software today, the opposite is usually true: the more we conform to shared idioms, the **more future-proof** we become.

- Idiomatic UI patterns → easier for users to understand and designers to extend
- Idiomatic language features → easier for other engineers and tools to reason about
- Widely adopted libraries used idiomatically → easier to hire for, easier to maintain, easier to replace

So while business advantage is often _bespoke_, software robustness and maintainability are often _idiomatic_.

---

## The Three-Axis Framework for AI-Augmented Development

Through 1000+ hours of production AI agent usage, I've identified three critical tensions not adequately addressed in current industry discourse.

We write **A ⊣ B** to mean: "A is constrained / bounded by B."

### The Three Relations

**Exploration ⊣ Specification**: The agent's ability to explore new methods, libraries, and architectures is constrained by how prescriptive we are in the specification. If we stuff the prompt with bespoke, highly specific implementation details, we increase Specification and shrink Exploration. We prevent the agent from roaming the current ecosystem, discovering state-of-the-art, future-proof idioms.

**Autonomy ⊣ Supervision**: The agent's autonomy is constrained by the level and frequency of human supervision. If we intervene at every small decision, require approvals at every step, or constantly redirect it, we reduce Autonomy. That defeats the point of using an autonomous AI to free up human time.

**Idiomatic patterns ⊣ Bespoke constraints**: The agent's ability to choose idiomatic, community-tested patterns is constrained by bespoke constraints we impose. If we insist on custom frameworks, unusual architectures, and local "house styles" that diverge from the ecosystem, we block it from using the idioms that maximize compatibility, tooling support, and long-term maintainability.

---

## Design Rule for Effective AI Agent Usage

If we overload an AI agent with bespoke instructions and micro-specifications, we do two things at once:

1. We import the "business secret sauce" mindset into a domain where it is often harmful—telling the agent to ignore the ecosystem and instead re-implement our quirks.

2. We mathematically reduce the left-hand side of each relation: heavy specification throttles exploration, frequent supervision throttles autonomy, bespoke constraints throttle idiomaticity.

**As AI coding agents get smarter, the optimal balance tilts further left.** We as humans must learn to let go while keeping just the right elements on the right side.

The design rule:

- Keep goals, constraints, and safety requirements **clear**
- Keep implementation details **non-bespoke and non-prescriptive** where possible

---

## Iterative Boundary Discovery

The design rule above suggests maximizing the left side (Exploration, Autonomy, Idiomaticity) while maintaining essential constraints. But how do we know which constraints are essential?

**My practice after 1000+ hours**: Start maximally left, discover boundaries empirically through audit, constrain only when necessary.

### The Process

1. **Default to maximum left**: Begin with minimal specification, minimal supervision, minimal bespoke constraints. Let AI agents explore freely within business requirements.

2. **Audit outputs systematically**: Review generated code, test results, architecture decisions. Don't assume problems—discover them through evidence.

3. **Identify boundary conditions**: When audit reveals issues (inconsistent patterns, suboptimal choices, misunderstood requirements), these indicate model capability boundaries.

4. **Add targeted constraints**: Constrain only the specific areas where audit revealed problems. Don't pre-emptively restrict based on assumptions about what might go wrong.

5. **Iterate as models improve**: As AI models get smarter (new versions, better training), loosen constraints and re-test boundaries. Yesterday's necessary constraint may be tomorrow's unnecessary restriction.

### Key Insight

Each AI model (Anthropic's Sonnet 4.5 Thinking for coding, OpenAI's GPT-5 Thinking for holistic reasoning, OpenAI's GPT-5 Deep Research for comprehensive analysis, etc.) has unique capability boundaries. You discover these through practice, not prediction. Start loose, audit carefully, constrain precisely.

### Why This Works

Pre-emptive restriction limits what agents can accomplish. Empirical boundary discovery maximizes agent capabilities while maintaining quality through systematic audit. You only pay the supervision cost where it demonstrably adds value.

---

## Summary: The Left-Right Balance

**Maximize LEFT** (agent capabilities):

- Exploration (let agents discover state-of-the-art solutions)
- Autonomy (reduce human intervention frequency)
- Idiomatic patterns (embrace community-tested approaches)

**Minimize RIGHT** (human constraints):

- Specification (avoid prescriptive implementation details)
- Supervision (intervene only when audit reveals issues)
- Bespoke constraints (avoid custom frameworks and house styles)

**The Symbol**: **A ⊣ B** means "A is constrained by B"

**The Practice**: Start maximally left, audit systematically, constrain only when empirical evidence demands it.

---

## Why This Was Removed

During Phase 2 document compression (commit cead05a), Doc 02 was reduced from 281 to 118 lines (58% reduction) to address repetition and improve conciseness. This three-axis framework, while conceptually valuable, was deemed too detailed for the strategic materials being sent to Ted Middleton.

However, the principle remains valuable for:

- Personal AI coding methodology reference
- Future technical documentation
- Training materials for teams adopting AI-augmented development
- Explaining the theoretical foundation behind "start loose, audit carefully, constrain precisely" practice

---

## Related Concepts

- **Progressive Disclosure**: Revealing information incrementally (mentioned in current Doc 02)
- **Agent Skills**: Composable prompt modules that load on-demand (mentioned in current Doc 02)
- **Empirical boundary discovery**: Testing AI model limits through practice, not prediction
- **Idiomatic over bespoke**: Preferring ecosystem-standard patterns over custom solutions
