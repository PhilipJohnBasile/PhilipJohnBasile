# Data and models

My model work spans training from scratch, building training data, fine-tuning and pruning existing models, and converting releases for Apple Silicon. Those are different jobs, and I keep the source model and my contribution visible.

[Interactive Local AI Guide](https://huggingface.co/spaces/philipjohnbasile/local-ai-guide) · [Hugging Face profile](https://huggingface.co/philipjohnbasile) · [GitHub profile](README.md)

## The data behind the models

I published [**GLM-5.2 Demolition training and calibration data**](https://huggingface.co/datasets/philipjohnbasile/glm52-demolition-data): **154 JSONL files**, comprising 150 files under `heal/` and four under `calib/`. The material covers code examples, agent tool-use conversations, repair, domain-specific adapters, and expert-pruning calibration.

The default Dataset Viewer indexes **87,586 rows**: 84,231 train, 3,277 validation, and 78 test. It exposes chat messages alongside domain and style metadata. This is the indexed default configuration; the dataset card's broader 272,549-example inventory has a different scope and was not recounted here. Counts were checked September 10, 2026.

The engineering goes beyond uploading files. My import code samples by source and domain, normalizes chat and tool messages, keeps source labels, deduplicates imported message sequences, and writes training and calibration outputs separately. The published import receipt records 338 imported training examples and 1,536 calibration prompts in the Hy3 pipeline, which also used additional repair data and seed examples.

The [**data-to-model case study**](https://github.com/PhilipJohnBasile/engineering-case-studies/blob/main/data-to-models.md) follows that process through the source code, import receipt, verification tools, and pruning evaluation. It also explains the boundaries of deduplication and verification.

### Wisp has its own pretraining corpus

[**Wisp Coder**](https://huggingface.co/philipjohnbasile/wisp-coder-110m) was trained from scratch. Its [published data record](https://huggingface.co/philipjohnbasile/wisp-coder-110m/blob/5919d57a7672623d8afc066032794359350e2ed2/evidence/documents/DATA.md) accounts for about 5.008 billion training-corpus tokens: approximately 92% StarCoderData, including Markdown, and 8% FineWeb-Edu. The 32K-token tokenizer used a separate 400,000-document sample.

I built the model and corpus pipeline using those upstream datasets; I did not author the underlying source corpus. The record distinguishes recovered aggregate token counts from missing row-level provenance, and explains the source terms and filtering limitations. [Wisp training and evaluation case study](https://github.com/PhilipJohnBasile/engineering-case-studies/blob/main/wisp-model-training.md).

## The public model families

This catalog covers the **20 public model repositories** reviewed September 10, 2026. Some are research variants, conversion sources, or components rather than complete standalone models. Exact runtime requirements and evaluation conditions are in each release's card.

| Family and releases | My contribution | Scope |
| --- | --- | --- |
| [Wisp Coder 110M](https://huggingface.co/philipjohnbasile/wisp-coder-110m) | Tokenizer training, pretraining from scratch, FIM and MTP, export checks, and evaluation | Original 108.2M-parameter research model; the [CPU demo](https://huggingface.co/spaces/philipjohnbasile/wisp-coder-demo) runs its standard decoder |
| Fable-Fusion: [4-bit](https://huggingface.co/philipjohnbasile/Qwen3.6-27B-Fable-Fusion-711-MTPLX-4bit), [6-bit](https://huggingface.co/philipjohnbasile/Qwen3.6-27B-Fable-Fusion-711-MTPLX-6bit), [8-bit](https://huggingface.co/philipjohnbasile/Qwen3.6-27B-Fable-Fusion-711-MTPLX-8bit), [BF16 reconstruction](https://huggingface.co/philipjohnbasile/Qwen3.6-27B-Fable-Fusion-711-bf16) | Reconstructed DavidAU's Q8_0 GGUF and packaged MLX releases with MTP and vision | DavidAU's tune of Qwen; BF16 storage does not restore precision lost in the source quantization |
| [Ornith 1.5](https://huggingface.co/philipjohnbasile/ornith-ai-Ornith-1.5-35B-A3B-V2-MTPLX) | Mixed-precision MLX/MTPLX conversion with a BF16 MTP sidecar | Original model by Ornith AI; the card distinguishes packaged features from independently qualified behavior |
| [Akka](https://huggingface.co/philipjohnbasile/Qwen3.6-27B-Akka-6bit-MLX) | 6-bit MLX conversion and source-head calibration audit | nightmedia's merge; released without the MTP head after calibration failed |
| Hy3: [Lite](https://huggingface.co/philipjohnbasile/hy3-demolition-mlx-lite-v1), [REAP25](https://huggingface.co/philipjohnbasile/hy3-demolition-mlx-reap25-v1), [Lite MTP](https://huggingface.co/philipjohnbasile/hy3-demolition-mlx-lite-v1-mtp), [REAP25 MTP](https://huggingface.co/philipjohnbasile/hy3-demolition-mlx-reap25-v1-mtp) | LoRA training and fusion, expert pruning, and MTP-sidecar experiments on Tencent Hy3 | AR releases have recorded runtime recipes; the MTP variants require separate end-to-end qualification |
| Qwen Mini: [base](https://huggingface.co/philipjohnbasile/hy3-family-mini-qwen35b-v1), [REAP](https://huggingface.co/philipjohnbasile/hy3-family-mini-qwen35b-reap-v1), [MTP](https://huggingface.co/philipjohnbasile/hy3-family-mini-qwen35b-mtp-v1) | Applied the project's training approach to Qwen 35B MoE, then explored pruning and a restored MTP head | Qwen architecture; the shared Hy3 project name does not make these Tencent Hy3 models |
| GLM: [Demolition MLX](https://huggingface.co/philipjohnbasile/GLM-5.2-Demolition-q4a4-soul-MLX), [iliria int4 container](https://huggingface.co/philipjohnbasile/GLM-5.2-colibri-int4-with-int8-mtp), [DSA indexer](https://huggingface.co/philipjohnbasile/glm52-idx-extract) | Expert pruning and LoRA experiments, full-model quantization for SSD streaming, and extraction of reusable indexer tensors | Based on Z.ai GLM-5.2; the pruned model, full container, and component have different purposes |
| [DeepSeek V4 Flash target-only MLX](https://huggingface.co/philipjohnbasile/DeepSeek-V4-Flash-0731-MLX-M5Max-TargetOnly) | Experimental conversion, runtime integration, and comparative evaluation | Original model by DeepSeek; retained as a reference with quality regressions and a faster alternative documented |
| Behavior studies: [official Qwen ablation](https://huggingface.co/philipjohnbasile/Qwen3.6-27B-Refusal-Ablation-v2-MTPLX-6bit), [Fable-Fusion ablation](https://huggingface.co/philipjohnbasile/Qwen3.6-27B-Fable-Fusion-711-ReducedRefusal-MTPLX-6bit) | Separate weight interventions and evaluations on two model lineages | Reports refusal-marker measurements and capability tradeoffs; marker counts are not a general measure of response quality |

[More software projects](PROJECTS.md) · [Engineering case studies](https://github.com/PhilipJohnBasile/engineering-case-studies)
