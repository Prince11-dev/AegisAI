# ADR-0007: Adopt ChromaDB as the Default Vector Database

- **Status:** Accepted
- **Date:** YYYY-MM-DD
- **Decision Makers:** AegisAI Core Engineering Team

---

# Context

AegisAI relies heavily on Retrieval-Augmented Generation (RAG), semantic search, embeddings, and document retrieval. The platform requires a dedicated vector database optimized for similarity search while keeping structured application data in PostgreSQL.

---

# Decision Drivers

- Native vector search
- Simple deployment
- Open-source
- Python integration
- Local development support
- Scalability for initial workloads

---

# Considered Options

## ChromaDB

### Advantages

- Open-source
- Python-first API
- Simple deployment
- Tight integration with LangChain/LangGraph
- Well suited for local development

### Disadvantages

- Fewer enterprise features than some managed solutions

---

## pgvector

### Advantages

- Single database technology
- PostgreSQL ecosystem

### Disadvantages

- Increased load on transactional database
- Less specialized for vector workloads

---

## Milvus / Qdrant / Weaviate

### Advantages

- Enterprise-scale vector search
- Advanced indexing
- Distributed deployment

### Disadvantages

- Higher operational complexity
- Additional infrastructure

---

# Decision

ChromaDB will be the default vector database.

Responsibilities include:

- Embedding storage
- Similarity search
- Semantic retrieval
- RAG document indexing

PostgreSQL remains the system of record for metadata.

---

# Consequences

## Positive

- Clear separation of responsibilities
- Optimized semantic search
- Easy contributor setup
- Lower operational complexity

## Negative

- Additional datastore to operate
- Synchronization between metadata and vectors

---

# Future Evolution

If workload requirements increase significantly, ChromaDB may be replaced or complemented by a distributed vector database such as Milvus or Qdrant without changing business logic.

---

# Related Documents

- architecture/ai-architecture.md
- architecture/database-design.md
- architecture/scalability-strategy.md

---