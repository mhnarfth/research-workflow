# Tooling Ledger

## Adopted
| Tool | Since | Replaces | Notes |
|---|---|---|---|
| GitHub | 2026-08 | HCC `/work` as source of truth | `/work` is not backed up |
| Obsidian | 2026-08 | — | One vault per repo, so the Obsidian Git plugin works |

## Queued — adopt in this order
| Tool | Replaces | Why |
|---|---|---|
| Zotero + Better BibTeX | hand-assembled BibTeX | Auto-exports `.bib` into `paper/`, stores PDFs and annotations. Benefits compound with every paper read — start first |
| jupytext + nbstripout | manual `.py` ↔ `.ipynb` conversion | Already `# %%` compatible |
| Hydra / OmegaConf | hand-rolled `config.py` | Composable configs, auto-logs the config with every run |
| MLflow | `config_signature()` + manifests | Logs config, metrics, git hash, artifacts per run |
| Snakemake or Makefile | numbered scripts run by hand | Declares the stage DAG, reruns only what's stale |
| Apptainer / Singularity | venv on HCC | The only thing that actually reproduces in five years |

## Considered, deferred
| Tool | When | Why deferred |
|---|---|---|
| Slurm job arrays | 2026-08 | Worth it above ~6h per stage or ~20 configs. Below that, interactive is less friction |
| Agentic overnight literature tools | 2026-08 | Revisit after one full pass through the framework |

## Tried and dropped
| Tool | When | Why |
|---|---|---|
