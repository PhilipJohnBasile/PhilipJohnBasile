<h1>
  <a href="https://philipjohnbasile.com/">
    <picture>
      <source media="(max-width: 600px)" srcset="assets/profile-hero-mobile.svg" />
      <img src="assets/profile-hero.svg" width="100%" alt="Philip John Basile — Make something matter. AI engineer and open-source contributor." />
    </picture>
  </a>
</h1>

<p align="center">
  <a href="https://philipjohnbasile.com/work"><strong>WORK ↗</strong></a> &nbsp; · &nbsp;
  <a href="https://philipjohnbasile.com/open-source"><strong>OPEN SOURCE ↗</strong></a> &nbsp; · &nbsp;
  <a href="https://philipjohnbasile.com/writing"><strong>WRITING ↗</strong></a> &nbsp; · &nbsp;
  <a href="https://philipjohnbasile.com/about"><strong>ABOUT ↗</strong></a>
</p>

**I’m Philip John Basile.** I’m a principal AI systems engineer at **Basilcom Inc.**, building AI systems that teams can rely on and contributing to the open-source tools that make them possible.

From enterprise agents to small code models and Apple Silicon. I work across architecture, implementation, performance, and team development, with **27+ years of building and shipping software** behind it.

## <img src="assets/section-upstream.svg" width="100%" alt="01 / Contributing upstream — Good code travels." />

I contribute to the tools I use. Three merged fixes in **Apple’s MLX and MLX-LM**:

- **[Correct results beyond 32K rows ↗](https://github.com/ml-explore/mlx/pull/3922)** · Apple MLX #3922<br />Fixed row-count overflow in sorted quantized matrix multiplication.
- **[Repair quantized loader indexing ↗](https://github.com/ml-explore/mlx/pull/4202)** · Apple MLX #4202<br />Corrected scale and bias indexing for small quantization groups.
- **[Keep converted Qwen weights correct ↗](https://github.com/ml-explore/mlx-lm/pull/1623)** · Apple MLX-LM #1623<br />Prevented a second normalization shift during model conversion.

I also work on **Unsloth Studio, MTPLX, oMLX, and AirRunner’s MLX-LM**.

<details>
<summary><strong>More upstream work — patches, projects, and status</strong></summary>

I contribute to the tools I use. That includes merged fixes in **Apple's MLX and MLX-LM**, along with ongoing work on **Unsloth Studio**, **MTPLX**, and **oMLX**.

| Project | What I've been working on | Status |
|---|---|---|
| [**Apple MLX**](https://github.com/ml-explore/mlx) | Fixed issues in quantized matrix multiplication involving [row overflow](https://github.com/ml-explore/mlx/pull/3922) and [small quantization groups](https://github.com/ml-explore/mlx/pull/4202). | Merged |
| [**Apple MLX-LM**](https://github.com/ml-explore/mlx-lm) | Fixed a [Qwen model conversion bug](https://github.com/ml-explore/mlx-lm/pull/1623) that applied a normalization adjustment twice. | Merged |
| [**Unsloth Studio**](https://github.com/unslothai/unsloth) | Working on agents that [make changes in separate Git worktrees](https://github.com/unslothai/unsloth/pull/10658) and [run tests and builds with execution limits](https://github.com/unslothai/unsloth/pull/10672). | Open PRs |
| [**MTPLX**](https://github.com/youssofal/MTPLX) | Contributed [Hy3 and Qwen native MTP backends](https://github.com/youssofal/MTPLX/pull/142#issuecomment-5001984512), plus [JSON-schema output](https://github.com/youssofal/MTPLX/pull/187), [structured tool calls](https://github.com/youssofal/MTPLX/pull/188), and [recovery after daemon crashes](https://github.com/youssofal/MTPLX/pull/221). | Shipped upstream; more PRs open |
| [**oMLX**](https://github.com/jundot/omlx) | Fixed [MLX memory reclamation](https://github.com/jundot/omlx/pull/2635) and [Python version compatibility checks for bundled kernels](https://github.com/jundot/omlx/pull/3558). | Merged; more PRs open |
| [**AirRunner's MLX-LM**](https://github.com/AirRunner/mlx-lm) | Improved [MTP cache handling, token probabilities, and validation](https://github.com/AirRunner/mlx-lm/pull/2). | Merged |

I've also submitted PRs to MLX Serve, vLLM Metal, dflash, Google Ads MCP, Nixpkgs, conda-forge, MacPorts, Rust, and Bootstrap.

[See my upstream pull requests](https://github.com/search?q=is%3Apublic+is%3Apr+author%3APhilipJohnBasile+-user%3APhilipJohnBasile&type=pullrequests)

</details>

## <img src="assets/section-work.svg" width="100%" alt="02 / Selected work — Less talk. More built." />

<table>
<tr>
<td width="50%" valign="top">
<sub>OPEN SOURCE / MODEL TRAINING</sub>
<h3><a href="https://philipjohnbasile.com/work/wisp-coder">WISP CODER ↗</a></h3>
<p>A code model I trained from scratch on Apple Silicon, with fill-in-the-middle and native multi-token prediction.</p>
<p><code>MLX</code> <code>108.2M parameters</code></p>
<p><a href="https://huggingface.co/spaces/philipjohnbasile/wisp-coder-demo">Try the demo</a> · <a href="https://github.com/PhilipJohnBasile/engineering-case-studies/blob/main/wisp-model-training.md">Read the experiments</a></p>
</td>
<td width="50%" valign="top">
<sub>ENTERPRISE AI / AGENT SYSTEMS</sub>
<h3><a href="https://philipjohnbasile.com/mcp-agent-platform">ENTERPRISE AGENT PLATFORM ↗</a></h3>
<p>MCP integrations, reusable skills, and approval workflows connecting AI to the systems a business already uses.</p>
<p><code>MCP</code> <code>Agents</code> <code>Identity</code></p>
<p><a href="https://github.com/PhilipJohnBasile/engineering-case-studies/blob/main/enterprise-ai-platform.md">Read the case study</a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<sub>OPEN SOURCE / APPLE SILICON</sub>
<h3><a href="https://philipjohnbasile.com/work/local-inference">LOCAL INFERENCE ON THE MAC ↗</a></h3>
<p>MLX conversions, native MTP work in MTPLX, and SSD-backed expert streaming with iliria.</p>
<p><code>MLX + Metal</code> <code>Inference</code></p>
<p><a href="https://github.com/PhilipJohnBasile/iliria">Explore iliria</a> · <a href="https://github.com/PhilipJohnBasile/engineering-case-studies/blob/main/local-inference-measurement.md">Measurement notes</a></p>
</td>
<td width="50%" valign="top">
<sub>ENTERPRISE AI / EVALUATION</sub>
<h3><a href="https://philipjohnbasile.com/rag-eval-harness">RETRIEVAL WITH RELEASE CHECKS ↗</a></h3>
<p>RAG systems with evaluation across retrieval, answer grounding, latency, cost, and regression behavior.</p>
<p><code>RAG</code> <code>Evaluation</code> <code>Reliability</code></p>
<p><a href="https://philipjohnbasile.com/rag-eval-harness">Explore the system</a></p>
</td>
</tr>
</table>

<details>
<summary><strong>More projects — iliria, racecontrol, CallSieve, VecStore, and PhilJS</strong></summary>

- [**iliria**](https://github.com/PhilipJohnBasile/iliria): C/Metal inference that streams large MoE models from SSD, built on colibri. I also published the [GLM-5.2 int4 container](https://huggingface.co/philipjohnbasile/GLM-5.2-colibri-int4-with-int8-mtp) it serves.
- [**racecontrol**](https://github.com/PhilipJohnBasile/racecontrol): routing and failure recovery across local inference engines, with a runnable HTTP demo.
- [**CallSieve**](https://github.com/PhilipJohnBasile/callsieve): local code retrieval for coding agents, with CLI and MCP interfaces.
- [**VecStore**](https://github.com/PhilipJohnBasile/vecstore): embedded vector search with metadata filtering and persistence.
- [**PhilJS**](https://github.com/PhilipJohnBasile/philjs): an experimental TypeScript UI framework with a dependency-free signals demo.

[More projects, model experiments, and creative work](PROJECTS.md)

</details>

<details>
<summary><strong>Five engineering case studies — decisions, evidence, and limitations</strong></summary>

Browse the [engineering case studies](https://github.com/PhilipJohnBasile/engineering-case-studies).

Five examples of the work behind the project list:

- [**Fixing a Metal quantization bug in Apple MLX**](https://github.com/PhilipJohnBasile/engineering-case-studies/blob/main/mlx-quantized-matmul.md): the boundary case, root cause, final upstream change, and regression tests.
- [**Training and releasing Wisp Coder**](https://github.com/PhilipJohnBasile/engineering-case-studies/blob/main/wisp-model-training.md): tokenizer training, model pretraining, runtime compatibility, and controlled experiments.
- [**Taking training data into model releases**](https://github.com/PhilipJohnBasile/engineering-case-studies/blob/main/data-to-models.md): data imports with source records, verification tools, expert-pruning calibration, and measured model tradeoffs.
- [**Measuring local inference fairly**](https://github.com/PhilipJohnBasile/engineering-case-studies/blob/main/local-inference-measurement.md): matching outputs and workloads, separating streaming behavior from speed, and reporting the actual margin.
- [**Connecting enterprise systems to AI agents**](https://github.com/PhilipJohnBasile/engineering-case-studies/blob/main/enterprise-ai-platform.md): integrations, identity, operational controls, and adoption across a global agency.

</details>

## <img src="assets/section-models.svg" width="100%" alt="03 / Models, data & demos — Local AI. Shared progress." />

**[Explore the whole Apple Silicon AI collection ↗](https://huggingface.co/spaces/philipjohnbasile/local-ai-guide)**

Original models, MLX conversions, training data, live demos, and technical guides. My Local AI Guide connects the releases to their model cards, inspected revisions, runtime requirements, and evaluation records.

**20 public model repositories · 1 public dataset · 2 public Spaces**<br />
<sub>Hugging Face Hub snapshot, September 10, 2026.</sub>

[Models ↗](https://huggingface.co/philipjohnbasile/models) · [Training data ↗](https://huggingface.co/datasets/philipjohnbasile/glm52-demolition-data) · [Try Wisp ↗](https://huggingface.co/spaces/philipjohnbasile/wisp-coder-demo) · [Full catalog ↗](DATA-AND-MODELS.md)

<details>
<summary><strong>Model training, conversions, datasets, and published results</strong></summary>

My [**Hugging Face**](https://huggingface.co/philipjohnbasile) work covers original models, conversions, experimental derivatives, and training data. I work on both the models themselves and the engineering needed to run them locally.

**20 public model repositories · 1 public dataset · 2 public Spaces · 11,388 monthly model downloads**

*Hugging Face Hub snapshot, September 10, 2026; downloads summed across my public model repositories.*

**[Explore my Local AI Guide](https://huggingface.co/spaces/philipjohnbasile/local-ai-guide).** I built a searchable catalog of the releases so you can browse by project, use case, artifact type, and download size. Each entry links to the model card, the inspected revision, and available evaluation records, with the runtime requirements explained alongside it.

### Wisp Coder: a model I built from scratch

**[Try Wisp in your browser](https://huggingface.co/spaces/philipjohnbasile/wisp-coder-demo).** Edit the code around the cursor and ask it to fill the gap. The free demo runs the standard decoder on CPU.

With [**Wisp Coder 110M**](https://huggingface.co/philipjohnbasile/wisp-coder-110m), I took the work from tokenizer training to released weights. I trained a 32K-token tokenizer on 400,000 documents and a 108.2M-parameter code model on 5 billion tokens using MLX on Apple Silicon. Fill-in-the-middle and multi-token prediction were part of training from the start.

I checked the export against Transformers, published decoding correctness checks, and evaluated five models across 1,372 code-completion tasks. I published the comparisons even when they didn't favor Wisp. The [Wisp case study](https://github.com/PhilipJohnBasile/engineering-case-studies/blob/main/wisp-model-training.md) covers the design decisions, evidence, and limitations.

### Model compression and conversions

- **[Hy3](https://huggingface.co/philipjohnbasile/hy3-demolition-mlx-reap25-v1) and [GLM-5.2](https://huggingface.co/philipjohnbasile/GLM-5.2-Demolition-q4a4-soul-MLX) compression** — Pruned mixture-of-experts models, trained LoRA adapters, and published smaller MLX builds. The Hy3 release removes 25% of experts per layer, then uses LoRA training to recover capability. The cards include evaluations, regressions, and the exact runtime recipes.
- **[Qwen Fable-Fusion for MLX and MTPLX](https://huggingface.co/philipjohnbasile/Qwen3.6-27B-Fable-Fusion-711-MTPLX-6bit)** — Reconstructed DavidAU's GGUF release for MLX, published 4-, 6-, and 8-bit builds, and calibrated the multi-token prediction head. The featured 6-bit build includes vision support through MTPLX, with conversion details and measured decoding results in the card.
- **[Ornith 1.5 for MTPLX](https://huggingface.co/philipjohnbasile/ornith-ai-Ornith-1.5-35B-A3B-V2-MTPLX)** — Converted Ornith AI's model for Apple Silicon with mixed-precision weights and a BF16 MTP head. The card documents source provenance, runtime requirements, and what has and hasn't been validated.
- **[Akka for MLX](https://huggingface.co/philipjohnbasile/Qwen3.6-27B-Akka-6bit-MLX)** — Converted nightmedia's merge to 6-bit MLX and checked its draft head against the target model. Calibration failed, so I released it without the MTP head and published the results.
- **[DeepSeek V4 Flash for MLX](https://huggingface.co/philipjohnbasile/DeepSeek-V4-Flash-0731-MLX-M5Max-TargetOnly)** — Built an experimental conversion and published comparisons against the original model, including a full 198-question GPQA Diamond run. Retained as a reference, with the quality regressions and faster alternative documented.

### Datasets and training pipelines

I published [**GLM-5.2 Demolition training and calibration data**](https://huggingface.co/datasets/philipjohnbasile/glm52-demolition-data): **154 JSONL files** covering code training, agent tool-use examples, repair, domain-specific adapters, and expert-pruning calibration.

I also built the import and verification tools around it: sampling by domain, normalizing chat and tool messages, keeping source labels, and separating training examples from calibration prompts. The [**data-to-model case study**](https://github.com/PhilipJohnBasile/engineering-case-studies/blob/main/data-to-models.md) follows the public code and records into the Hy3 model experiments.

[**Explore the datasets, training methods, and all 20 model repositories**](DATA-AND-MODELS.md)

I also group featured releases in [**Selected Work**](https://huggingface.co/collections/philipjohnbasile/start-here-selected-work-6aa309b179b2a196db52a12b) and research artifacts in [**Apple Silicon — Experimental Models**](https://huggingface.co/collections/philipjohnbasile/apple-silicon-experimental-models).

[Browse all models](https://huggingface.co/philipjohnbasile/models) · [Browse datasets](https://huggingface.co/philipjohnbasile/datasets)

</details>

## <img src="assets/section-about.svg" width="100%" alt="04 / The person behind the patches — Still building. Still questioning." />

I started building university websites at Fordham. Since then, I’ve worked across healthcare, enterprise systems, cybersecurity, and defense—turning complicated systems into things people can use.

That range shapes how I build AI: correctness, clear boundaries, and a path someone else can follow. I stay close to the code and help other engineers do the same.

[More about my background ↗](https://philipjohnbasile.com/about)

<details>
<summary><strong>The career behind the code — platforms, outcomes, and team development</strong></summary>

I started building university websites at Fordham. Since then, I've worked on **IBM's enterprise search**, **Atlas Air's flight scheduling**, **Dragos's cybersecurity products**, and **U.S. Air Force mission-planning software** through client engagements. My healthcare work includes **Teladoc** and **IntegraMed**; earlier, I helped build commerce at **BaubleBar** and campaign experiences at **360i**.

That range matters when a project gets complicated. I've had to balance user experience, sensitive data, uptime, budgets, and deadlines—and help other engineers do the same.

A few examples from my recent work:

- **AI platform ownership:** Architecture and technical direction for a global agency, supporting 120 staff across the UK, US, and APJ, including 12+ production MCP integrations.
- **Operating cost:** A Snowflake permissions and governance cleanup that reduced credit consumption by 35%, about £2,800 a month.
- **Team development:** Led teams of 4–20 and coached five engineers into senior roles.

[Career background and case studies](https://philipjohnbasile.com)

</details>

## <img src="assets/section-writing.svg" width="100%" alt="05 / Notes from the work — Leave a paper trail." />

- **[MCP is a governance problem ↗](https://philipjohnbasile.com/notes/mcp-is-a-governance-problem)**<br />What changes when a model can act on a company’s tools and data.
- **[Learn by building the loop ↗](https://philipjohnbasile.com/agent-engineering-beginner-deep-dive)**<br />Eight practical missions covering agents, prompting, retrieval, evaluation, and tool use.
- **[What the Wisp experiments showed ↗](https://huggingface.co/philipjohnbasile/wisp-coder-110m/blob/5919d57a7672623d8afc066032794359350e2ed2/fim-competitive-v1/FIM_RESULTS.md)**<br />Methods, comparisons, null results, and the limits of a small code model.

[More writing ↗](https://philipjohnbasile.com/writing) · [Medium ↗](https://philipjohnbasile.medium.com/)

<a href="https://philipjohnbasile.com/contact"><img src="assets/contact.svg" width="100%" alt="Let’s make a useful dent. Start a conversation." /></a>

I'm interested in principal and staff engineering roles where I can own the architecture, stay close to the code, and help a team ship useful AI systems. If that sounds like your team—or you've tried one of these projects—I'd like to hear from you.

[Email](mailto:PBasile@Basilecom.com) · [Portfolio](https://philipjohnbasile.com) · [Hugging Face](https://huggingface.co/philipjohnbasile) · [Writing](https://philipjohnbasile.com/writing) · [More links](https://linktr.ee/philipjohnbasile) · [Support my open-source work](https://github.com/sponsors/PhilipJohnBasile)
