# Philip John Basile

### Principal AI Systems Engineer · Open-Source ML & Runtime Engineering · Apple Silicon

> Contributing to MLX, MLX-LM, Unsloth Studio, and the infrastructure powering local AI.

[![Hugging Face](https://img.shields.io/badge/Hugging_Face-Models_%26_Data-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/philipjohnbasile) [![Writing](https://img.shields.io/badge/Medium-Writing-12100E?style=flat-square&logo=medium&logoColor=white)](https://philipjohnbasile.medium.com/) [![Sponsor](https://img.shields.io/badge/GitHub-Sponsor-EA4AAA?style=flat-square&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/PhilipJohnBasile)

I build AI systems, developer tools, and applications at **Basilcom Inc.** My work spans MLX and Metal inference, speculative decoding, model adaptation, code retrieval, and coding agents that verify their changes with real tests.

I'm especially interested in making capable models useful on hardware people own: understanding memory limits, improving the runtime, and connecting models to workflows that can recover when something goes wrong. I build my own projects and contribute fixes upstream to the libraries and applications they depend on.

---

## Open-source contributions

My upstream work spans **MLX and MLX-LM from Apple's ML research team**, **Unsloth Studio**, and the local inference ecosystem. I contribute kernel and model-correctness fixes, agent infrastructure, and runtime reliability improvements, with both merged contributions and active pull requests.

| Project | Contributions | Status |
|---|---|---|
| [**Apple MLX**](https://github.com/ml-explore/mlx) | [Quantized gather row-overflow fix](https://github.com/ml-explore/mlx/pull/3922) and [quantized-kernel group-size correction](https://github.com/ml-explore/mlx/pull/4202). | Merged |
| [**Apple MLX-LM**](https://github.com/ml-explore/mlx-lm) | [Corrected converted Qwen RMSNorm sanitization](https://github.com/ml-explore/mlx-lm/pull/1623). | Merged |
| [**Unsloth Studio**](https://github.com/unslothai/unsloth) | [Durable coding tasks in owned Git worktrees](https://github.com/unslothai/unsloth/pull/10658), [bounded test and build execution](https://github.com/unslothai/unsloth/pull/10672), confined editing, recovery, and agent-facing UI. | Open proposals |
| [**MTPLX**](https://github.com/youssofal/MTPLX) | [JSON-schema structured output](https://github.com/youssofal/MTPLX/pull/187), [strict tool-call grammars composed with MTP verification](https://github.com/youssofal/MTPLX/pull/188), and [bounded daemon crash recovery](https://github.com/youssofal/MTPLX/pull/221). | Merged; further PRs open |
| [**oMLX**](https://github.com/jundot/omlx) | [MLX memory-pool reclamation](https://github.com/jundot/omlx/pull/2635) and [bundled Python ABI validation for custom kernels](https://github.com/jundot/omlx/pull/3558). | Merged; further PRs open |
| [**AirRunner's MLX-LM**](https://github.com/AirRunner/mlx-lm) | [Transactional MTP cache, log-probability, and guard hardening](https://github.com/AirRunner/mlx-lm/pull/2). | Merged |

I've also submitted work to MLX Serve, vLLM Metal, dflash, Google Ads MCP, Nixpkgs, conda-forge, MacPorts, Rust, Bootstrap, and other community projects.

[Browse my public upstream pull requests →](https://github.com/search?q=is%3Apublic+is%3Apr+author%3APhilipJohnBasile+-user%3APhilipJohnBasile&type=pullrequests)

---

## Selected AI work

### 🧠 Local inference on Apple Silicon

A family of engines and routing tools for running local models with explicit memory budgets, observable behavior, and practical recovery paths.

| Project | What I'm building |
|---|---|
| [**iliria**](https://github.com/PhilipJohnBasile/iliria) | A C/Metal streaming engine for large mixture-of-experts models, loading experts from SSD as needed. Derived from [colibri](https://github.com/JustVugg/colibri). |
| [**trailbrake**](https://github.com/PhilipJohnBasile/trailbrake) | A native MLX inference engine focused on dense Qwen models, bounded KV-cache memory, prefix reuse, and streaming generation on high-end Apple Silicon. |
| [**racecontrol**](https://github.com/PhilipJohnBasile/racecontrol) | An OpenAI-compatible router connecting fast and deep-reasoning engines, with fallback, canary routing, circuit breakers, and decision logs. |
| [**iliria-fm**](https://github.com/PhilipJohnBasile/iliria-fm) | Experimental Swift integration between the local inference stack and Apple's Foundation Models framework. |
| [**ggml-rust**](https://github.com/PhilipJohnBasile/ggml-rust) | Foundations for an independent GGML-compatible Rust runtime, starting with bounded GGUF parsing, model-file mapping, and inspection. |

`MLX` · `Metal` · `C/C++` · `Python` · `Rust` · `Swift` · Quantization · KV caching · Speculative decoding

### 🛠️ Infrastructure for AI coding agents

I work on the parts around the model that make an agent useful: finding the right code, controlling edits, running verifiers, preserving state, and showing what actually happened.

| Project | What it does |
|---|---|
| [**CallSieve**](https://github.com/PhilipJohnBasile/callsieve) | Local codebase retrieval that gives coding agents compact, relevant context before they start searching. Rust CLI, MCP integrations, editor hooks, and auditable retrieval reports. |
| [**merle**](https://github.com/PhilipJohnBasile/merle) | A local coding CLI that generates candidate fixes, runs the requested tests, and presents a verified candidate with its diff. Integrates CallSieve and optional VecStore memory. |
| [**Graph-Native MLX**](https://github.com/PhilipJohnBasile/graph-native-mlx) | A graph-controlled coding-agent runtime with durable checkpoints, isolated Git worktrees, transactional patches, bounded retries, and real verifier execution. |
| [**VecStore**](https://github.com/PhilipJohnBasile/vecstore) | An embeddable vector database for semantic search and RAG: HNSW indexing, metadata filtering, hybrid search, and snapshots, with Rust, Python, and WebAssembly interfaces. |

### 🔬 Model adaptation and reproducible evaluation

My model work explores expert pruning, mixed-precision quantization, LoRA healing, verifier-scored training data, and local serving. The [**Hy3-Demolition-MLX**](https://github.com/PhilipJohnBasile/hy3-demolition-mlx) and [**GLM-5.2 Demolition**](https://github.com/PhilipJohnBasile/glm52-demolition) research pipelines preserve the methods, artifacts, and evaluation results behind those experiments.

I also publish MLX model derivatives and datasets on [**Hugging Face**](https://huggingface.co/philipjohnbasile), including work with Qwen, Hy3, and DeepSeek families.

[**scrutineer**](https://github.com/PhilipJohnBasile/scrutineer) packages performance and correctness claims with a decision rule, positive control, pinned evidence, and a reproducible verdict. My working principle: define the test, preserve the evidence, and publish the limitations alongside the result.

---

## Products, frameworks, and creative work

- [**PhilJS**](https://github.com/PhilipJohnBasile/philjs) — a JavaScript/TypeScript and Rust framework exploring fine-grained reactivity, streaming SSR, WebAssembly, and AI tooling.
- **Concert Echo** — my work on a Flutter live-music social app: concert discovery, show memories, fan profiles, and shared photos and video.
- [**Generative Rust**](https://github.com/PhilipJohnBasile/generative-rust) — companion code for *Generative Rust: Building AI Agents for Art, Audio, and Real-Time Synthesis*, connecting model inference, creative agents, procedural visuals, and sound.

## Focus

Local AI · Inference correctness and performance · Apple Silicon · Agent runtimes · Retrieval and RAG · Reproducible evaluation · Open-source developer tools · Full-stack product engineering

## Let's collaborate

Interested in local inference, coding-agent infrastructure, or useful developer tools? I'd love to compare notes and build something together.

[Email](mailto:PBasile@Basilecom.com) · [Hugging Face](https://huggingface.co/philipjohnbasile) · [Writing](https://philipjohnbasile.medium.com/) · [More links](https://linktr.ee/philipjohnbasile) · [Support my open-source work](https://github.com/sponsors/PhilipJohnBasile)
