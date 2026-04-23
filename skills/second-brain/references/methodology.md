# LLM Wiki Methodology

## Core Idea

An LLM wiki is a personal knowledge base maintained by an agent. Raw sources remain available for provenance, while the agent continually compiles them into a human-readable and LLM-readable Markdown wiki.

The core shift is from "retrieve the best chunks at query time" to "incrementally maintain a durable synthesis layer." The wiki becomes a reusable memory artifact: indexed, cross-linked, source-aware, versionable, and editable by both human and agent.

## Canonical Layers

| Layer | Purpose | Typical Path |
|-------|---------|--------------|
| Raw sources | Immutable source material and provenance | `raw/` |
| Compiled wiki | Summaries, entities, concepts, questions, links | `wiki/` |
| Schema/rules | Agent instructions and page conventions | `AGENTS.md`, `CLAUDE.md`, `schema/` |
| Logs | Audit trail for ingest, query captures, and maintenance | `wiki/log.md`, `logs/` |

## Core Operations

| Operation | Purpose | Output |
|-----------|---------|--------|
| Init | Create the folder structure and agent rules | `raw/`, `wiki/`, `schema/`, `AGENTS.md` |
| Ingest | Convert sources into durable knowledge pages | Source summary plus updated concept/entity/project pages |
| Query | Answer from the compiled wiki, falling back to raw sources only as needed | Source-aware answer, optionally captured as reusable knowledge |
| Health/Lint | Keep the wiki trustworthy and navigable | Broken-link fixes, stale-page review, contradiction backlog |

## LLM Wiki vs RAG

| Dimension | Conventional RAG | LLM Wiki |
|-----------|------------------|----------|
| Primary artifact | Vector index / retriever over raw chunks | Curated Markdown synthesis layer |
| Main work time | Query time | Ingest and maintenance time |
| Memory shape | Non-parametric retrieval store | Human-readable compiled knowledge |
| Best at | Grounding answers in large changing corpora | Building durable personal or team understanding |
| Weakness | Retrieved chunks can be redundant, stale, or poorly synthesized | Requires maintenance discipline and agent judgment |
| Auditability | Depends on retriever and citation design | Native git diff, links, logs, and readable pages |
| Scale path | Embeddings, rerankers, hybrid search, GraphRAG | Index pages first, then optional BM25/vector/graph/MCP export |

RAG remains useful inside an LLM wiki once the raw archive or wiki grows beyond simple navigation. The important distinction is architectural: RAG is usually a retrieval mechanism; LLM Wiki is a knowledge-maintenance workflow.

## Good Use Cases

- Personal research notebooks and reading systems.
- Project memory across long-running agent sessions.
- Meeting notes, decisions, and design rationales.
- Learning systems where questions and explanations should compound.
- Team knowledge bases where human-readable diffs matter.
- Local-first private notes where cloud indexing is undesirable.

## Poor Fit

- One-off Q&A over a document where no durable memory is needed.
- High-volume enterprise search where raw retrieval is enough.
- Data that cannot be safely summarized or persisted.
- Workflows without any maintenance owner.

## Frontier Extensions

- Hybrid retrieval over wiki and raw sources: BM25, embeddings, rerankers.
- Graph overlays: entity/relation extraction, community summaries, GraphRAG-style global search.
- Lifecycle metadata: confidence, supersession, retention, source freshness, and forgetting.
- Privacy gates: redaction, sensitive-source quarantine, local model ingest.
- Agent-session compilers: convert dormant chat histories into reusable project memory.
- Obsidian/local-first workflows: manifests, incremental sync, review queues, git undo.

## Sources

- Andrej Karpathy, `llm-wiki.md`: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Lewis et al., Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks: https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html
- Microsoft GraphRAG project: https://www.microsoft.com/en-us/research/project/graphrag/
- GraphRAG paper page: https://graphrag.com/appendices/research/2404.16130/
- LLM Wiki v2 / agentmemory extension gist: https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2
- Obsidian Wiki framework: https://github.com/Ar9av/obsidian-wiki
- Local Obsidian LLM Wiki implementation: https://github.com/kytmanov/obsidian-llm-wiki-local
- Agent-session llmwiki implementation: https://github.com/Pratiyush/llm-wiki
- LLM Wiki demo site: https://llmwiki.app/
