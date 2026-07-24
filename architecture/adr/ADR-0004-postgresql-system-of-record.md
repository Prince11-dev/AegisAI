# ADR-0004: Adopt PostgreSQL as the System of Record

- **Status:** Accepted
- **Date:** YYYY-MM-DD
- **Decision Makers:** AegisAI Core Engineering Team

---

# Context

AegisAI requires a reliable transactional database for user accounts, workspaces, documents, metadata, permissions, audit logs, and application configuration.

The primary datastore must provide:

- ACID transactions
- Strong consistency
- Rich SQL capabilities
- Mature ecosystem
- High reliability
- Scalability
- Excellent Python support

---

# Decision Drivers

- Data integrity
- Transaction support
- Mature ecosystem
- Performance
- Open-source
- Extensibility
- Long-term maintainability

---

# Considered Options

## PostgreSQL

### Advantages

- ACID compliance
- Rich SQL support
- JSONB support
- Mature ecosystem
- Excellent indexing
- Strong community

### Disadvantages

- Requires tuning for very large workloads

---

## MySQL

### Advantages

- Mature ecosystem
- Widely adopted

### Disadvantages

- Less advanced JSON capabilities
- Fewer advanced indexing options

---

## MongoDB

### Advantages

- Flexible schema
- Document-oriented

### Disadvantages

- Not ideal for strongly relational data
- Eventual consistency in some deployment models

---

# Decision

PostgreSQL will serve as the **system of record** for all structured application data.

Vector embeddings will remain in ChromaDB, while PostgreSQL stores metadata and transactional information.

---

# Consequences

## Positive

- Strong consistency
- Reliable transactions
- Mature tooling
- Excellent reporting capabilities

## Negative

- Requires schema migrations
- Vertical scaling limits before sharding

---

# Future Evolution

Future enhancements may include read replicas, partitioning, logical replication, and managed PostgreSQL services.

---

# Related Documents

- architecture/database-design.md
- architecture/deployment.md
- architecture/scalability-strategy.md

---