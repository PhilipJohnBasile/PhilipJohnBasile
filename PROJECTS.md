# Projects

[Profile and contributions](README.md) · [Engineering case studies](https://github.com/PhilipJohnBasile/engineering-case-studies)

## Things I'm building

### Local AI on a Mac

Getting large models to run locally has turned into a few related projects:

- [**iliria**](https://github.com/PhilipJohnBasile/iliria) streams parts of large mixture-of-experts models from SSD as they're needed. It's written in C/Metal and builds on [colibri](https://github.com/JustVugg/colibri).
- [**trailbrake**](https://github.com/PhilipJohnBasile/trailbrake) is a native MLX inference engine for dense Qwen models, with careful control over memory and caching.
- [**racecontrol**](https://github.com/PhilipJohnBasile/racecontrol) puts both engines behind one API, routing requests between them and handling fallback when an engine fails.
- [**iliria-fm**](https://github.com/PhilipJohnBasile/iliria-fm) is an experiment connecting that stack to Apple's Foundation Models framework through Swift.
- [**ggml-rust**](https://github.com/PhilipJohnBasile/ggml-rust) is the beginning of an independent GGML-compatible runtime in Rust. The first pieces handle GGUF parsing, file mapping, and model inspection.

### Tools for coding agents

I want a coding agent to find the right file and run the tests before it tells me it's done. These projects tackle different parts of that:

- [**CallSieve**](https://github.com/PhilipJohnBasile/callsieve) helps agents find relevant code through a local index, with a CLI, MCP support, and editor integrations.
- [**merle**](https://github.com/PhilipJohnBasile/merle) uses a local model to generate fixes, runs the requested tests, and shows the resulting diff.
- [**Graph-Native MLX**](https://github.com/PhilipJohnBasile/graph-native-mlx) gives coding agents a defined workflow, saved progress, separate worktrees, and limits on retries.
- [**VecStore**](https://github.com/PhilipJohnBasile/vecstore) adds vector search directly to an application, without a separate database server. It has Rust, Python, and browser interfaces.

### Models and experiments

[**Wisp Coder 110M**](https://huggingface.co/philipjohnbasile/wisp-coder-110m) is my own code-completion model, trained from scratch on 5 billion tokens with native fill-in-the-middle and multi-token prediction. The weights and model card are available on Hugging Face. The [engineering case study](https://github.com/PhilipJohnBasile/engineering-case-studies/blob/main/wisp-model-training.md) follows the work through tokenizer training, export verification, and controlled evaluation.

My [**Hy3-Demolition-MLX**](https://github.com/PhilipJohnBasile/hy3-demolition-mlx) and [**GLM-5.2 Demolition**](https://github.com/PhilipJohnBasile/glm52-demolition) projects explore pruning, quantization, and LoRA training to make large models more practical on local hardware.

I keep the results and the dead ends. [**scrutineer**](https://github.com/PhilipJohnBasile/scrutineer) is a small tool for recording a claim, the test used to check it, and the evidence behind the result.

## A few other things

There's a music and creative coding side to my work, too.

- [**PhilJS**](https://github.com/PhilipJohnBasile/philjs) is my experimental TypeScript UI framework, with a [runnable signals demo](https://github.com/PhilipJohnBasile/philjs#try-the-reactive-core) and related rendering and Rust work.
- **Concert Echo** is a Flutter app for live-music fans to keep their show memories, photos, and videos together.
- [**Generative Rust**](https://github.com/PhilipJohnBasile/generative-rust) contains the companion code for *Generative Rust: Building AI Agents for Art, Audio, and Real-Time Synthesis*. It brings together model inference, procedural visuals, and sound.
