# JudgmentOps Positioning

## What JudgmentOps Is

JudgmentOps is an open-source judgment layer for agentic coding and AI-assisted software maintenance.

It exists because the dominant failure modes when using coding agents on real, long-running software work are not failures of code generation. They are failures of preserved human judgment: scope and intent drift, implicit constraints that are never checked, quality definitions that stop at "tests pass," redaction boundaries that are enforced only in human heads, and the repeated reproduction of known failure classes because there is no structured memory.

The project produces:

- A precise protocol for expressing intent contracts, execution constraints, quality gates, redaction gates, failure memory, and human approval checkpoints.
- A growing, public casebook of analyzed failures with explicit judgment rules extracted from them.
- Schemas that are strict enough to be useful to agents and simple enough for humans to author and review.
- A thin agent adapter layer so that existing coding agents can consume these artifacts.
- Evaluation materials and harness ideas so that the value of the layer can be measured.

The project is deliberately positioned as infrastructure that sits *above* coding agents rather than as another coding agent.

## What JudgmentOps Is Not

- **It is not a coding assistant.** It does not generate code, complete functions, or drive an edit loop. It supplies the judgment context that a coding assistant or agent should respect.
- **It is not a prompt collection or "better system prompt" library.** The artifacts are structured (JSON schemas, versioned contracts, queryable memory) rather than free-form text that must be re-interpreted by each model on every turn.
- **It is not a replacement for Codex, GitHub Copilot, or any other generation-focused tool.** It is designed to make those systems more reliable when used for extended tasks, maintenance, migrations, and production software work.
- **It is not a general agent framework.** It does not define tool calling loops, memory architectures, or orchestration. It defines only the narrow judgment surface that many such frameworks could usefully consume.
- **It is not a security or compliance product.** Redaction gates and quality gates are best-effort, illustrative, and always require human review before external delivery or high-stakes automation. The project explicitly disclaims any guarantee of correctness or completeness.
- **It is not an internal or company-specific framework.** All cases, examples, and schemas use only neutral, fictional data. The project is intended for broad public adoption and contribution.

## Relationship to Existing Tools

JudgmentOps is complementary to frontier coding models and agent implementations. A model that is excellent at generation will still produce the failure modes documented in the casebook when it is not given (or does not reliably retain) explicit judgment artifacts. Providing those artifacts is the job of the judgment layer.

Organizations that already have strong internal conventions, review processes, and institutional memory can express those conventions in JudgmentOps form and make them available to any agent they choose to use — including agents built by multiple vendors.

Platform and model providers can treat the judgment layer as an integration surface: a place where governance, policy, audit, and evaluation features can be attached without having to bake all of that logic into the base generation model or a single agent product.

## Tone and Ambition

The project is ambitious in its diagnosis (judgment preservation is a first-class, distinct problem) but modest in its current form (early prototype, minimal CLI, 20 cases, thin adapter). It does not claim that existing agents are useless, nor that this layer will solve all problems. It claims that the marginal value of explicit judgment scaffolding is high for the class of work that actually determines whether agentic coding delivers sustained organizational value, and that this scaffolding is currently missing as portable, evaluable infrastructure.

Contributions and adoption that treat judgment as a real engineering and evaluation problem — rather than hoping longer context or stronger models will eventually make the problem disappear — are the intended audience.
