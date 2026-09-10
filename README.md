# Philip John Basile

I'm a principal AI systems engineer at **Basilcom Inc.**, with **27+ years of building and shipping software**. My work has taken me through healthcare, enterprise systems, cybersecurity, and defense. Today I build AI platforms for businesses and work on the runtimes that let large models run locally on Apple Silicon.

I work across architecture, implementation, performance, and team development. The [case studies](https://github.com/PhilipJohnBasile/engineering-case-studies) show how I approach that work.

[![Hugging Face](https://img.shields.io/badge/Hugging_Face-Models_%26_Data-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/philipjohnbasile) [![Writing](https://img.shields.io/badge/Medium-Writing-12100E?style=flat-square&logo=medium&logoColor=white)](https://philipjohnbasile.medium.com/) [![Sponsor](https://img.shields.io/badge/GitHub-Sponsor-EA4AAA?style=flat-square&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/PhilipJohnBasile)

## Open-source contributions

I contribute to the tools I use. That includes merged fixes in **Apple's MLX and MLX-LM**, along with ongoing work on **Unsloth Studio**, **MTPLX**, and **oMLX**.

| Project | What I've been working on | Status |
|---|---|---|
| [**Apple MLX**](https://github.com/ml-explore/mlx) | Fixed issues in quantized matrix multiplication involving [row overflow](https://github.com/ml-explore/mlx/pull/3922) and [small quantization groups](https://github.com/ml-explore/mlx/pull/4202). | Merged |
| [**Apple MLX-LM**](https://github.com/ml-explore/mlx-lm) | Fixed a [Qwen model conversion bug](https://github.com/ml-explore/mlx-lm/pull/1623) that applied a normalization adjustment twice. | Merged |
| [**Unsloth Studio**](https://github.com/unslothai/unsloth) | Working on agents that [make changes in separate Git worktrees](https://github.com/unslothai/unsloth/pull/10658) and [run tests and builds with execution limits](https://github.com/unslothai/unsloth/pull/10672). | Open PRs |
| [**MTPLX**](https://github.com/youssofal/MTPLX) | Added [JSON-schema output](https://github.com/youssofal/MTPLX/pull/187), [structured tool calls with MTP verification](https://github.com/youssofal/MTPLX/pull/188), and [recovery after daemon crashes](https://github.com/youssofal/MTPLX/pull/221). | Merged; more PRs open |
| [**oMLX**](https://github.com/jundot/omlx) | Fixed [MLX memory reclamation](https://github.com/jundot/omlx/pull/2635) and [Python version compatibility checks for bundled kernels](https://github.com/jundot/omlx/pull/3558). | Merged; more PRs open |
| [**AirRunner's MLX-LM**](https://github.com/AirRunner/mlx-lm) | Improved [MTP cache handling, token probabilities, and validation](https://github.com/AirRunner/mlx-lm/pull/2). | Merged |

I've also submitted PRs to MLX Serve, vLLM Metal, dflash, Google Ads MCP, Nixpkgs, conda-forge, MacPorts, Rust, and Bootstrap.

[See my upstream pull requests](https://github.com/search?q=is%3Apublic+is%3Apr+author%3APhilipJohnBasile+-user%3APhilipJohnBasile&type=pullrequests)

## Hugging Face contributions

I publish model conversions, experimental derivatives, and training data on [**Hugging Face**](https://huggingface.co/philipjohnbasile). My part of the work is making existing models usable in new runtimes, checking what survives conversion, and sharing the results.

**19 public model repositories · 1 public dataset · 11,272 model downloads in the preceding month**  
*Hugging Face Hub snapshot, September 10, 2026; downloads summed across my public model repositories.*

- **[Qwen Fable-Fusion for MLX and MTPLX](https://huggingface.co/philipjohnbasile/Qwen3.6-27B-Fable-Fusion-711-MTPLX-8bit)** — Reconstructed DavidAU's GGUF release for MLX, published 4-, 6-, and 8-bit builds, and preserved the vision tower and multi-token prediction head. The cards include conversion details and measured decoding results.
- **[Ornith 1.5 for MTPLX](https://huggingface.co/philipjohnbasile/ornith-ai-Ornith-1.5-35B-A3B-V2-MTPLX)** — Published an Apple Silicon conversion with mixed-precision weights, a BF16 MTP head, and documented source provenance and runtime requirements.
- **[DeepSeek V4 Flash for MLX](https://huggingface.co/philipjohnbasile/DeepSeek-V4-Flash-0731-MLX-M5Max-TargetOnly)** — Built an experimental conversion and published comparisons against the original model, including a full 198-question GPQA Diamond run. Retained as a reference, with the quality regressions and faster alternative documented.
- **[GLM-5.2 Demolition training and calibration data](https://huggingface.co/datasets/philipjohnbasile/glm52-demolition-data)** — Released the data behind my pruning and LoRA experiments, including code examples checked by the project's verifier pipeline and calibration material others can reuse.

[Browse all models](https://huggingface.co/philipjohnbasile/models) · [Browse datasets](https://huggingface.co/philipjohnbasile/datasets)

## The career behind the code

I started building university websites at Fordham. Since then, I've worked on **IBM's enterprise search**, **Atlas Air's flight scheduling**, **Dragos's cybersecurity products**, and **U.S. Air Force mission-planning software** through client engagements. My healthcare work includes **Teladoc** and **IntegraMed**; earlier, I helped build commerce at **BaubleBar** and campaign experiences at **360i**.

That range matters when a project gets complicated. I've had to balance user experience, sensitive data, uptime, budgets, and deadlines—and help other engineers do the same.

A few examples from my recent work:

- **AI platform ownership:** Architecture and technical direction for a global agency, supporting 120 staff across the UK, US, and APJ, including 12+ production MCP integrations.
- **Operating cost:** A Snowflake permissions and governance cleanup that reduced credit consumption by 35%, about £2,800 a month.
- **Team development:** Led teams of 4–20 and coached five engineers into senior roles.

[Career background and case studies](https://philipjohnbasile.com)

## Engineering case studies

Three examples of the work behind the project list:

- [**Fixing a Metal quantization bug in Apple MLX**](https://github.com/PhilipJohnBasile/engineering-case-studies/blob/main/mlx-quantized-matmul.md): the boundary case, root cause, final upstream change, and regression tests.
- [**Measuring local inference fairly**](https://github.com/PhilipJohnBasile/engineering-case-studies/blob/main/local-inference-measurement.md): matching outputs and workloads, separating streaming behavior from speed, and reporting the actual margin.
- [**Connecting enterprise systems to AI agents**](https://github.com/PhilipJohnBasile/engineering-case-studies/blob/main/enterprise-ai-platform.md): integrations, identity, operational controls, and adoption across a global agency.

## Selected projects

- [**iliria**](https://github.com/PhilipJohnBasile/iliria): C/Metal inference that streams large MoE models from SSD, built on colibri.
- [**racecontrol**](https://github.com/PhilipJohnBasile/racecontrol): routing and failure recovery across local inference engines, with a runnable HTTP demo.
- [**CallSieve**](https://github.com/PhilipJohnBasile/callsieve): local code retrieval for coding agents, with CLI and MCP interfaces.
- [**VecStore**](https://github.com/PhilipJohnBasile/vecstore): embedded vector search with metadata filtering and persistence.
- [**PhilJS**](https://github.com/PhilipJohnBasile/philjs): an experimental TypeScript UI framework with a dependency-free signals demo.

[More projects, model experiments, and creative work](PROJECTS.md)

## Say hello

I'm interested in principal and staff engineering roles where I can own the architecture, stay close to the code, and help a team ship useful AI systems. If that sounds like your team—or you've tried one of these projects—I'd like to hear from you.

[Email](mailto:PBasile@Basilecom.com) · [Portfolio](https://philipjohnbasile.com) · [Hugging Face](https://huggingface.co/philipjohnbasile) · [Writing](https://philipjohnbasile.medium.com/) · [More links](https://linktr.ee/philipjohnbasile) · [Support my open-source work](https://github.com/sponsors/PhilipJohnBasile)
