# ADR-0005: Adopt Ollama as the Default LLM Provider

- **Status:** Accepted
- **Date:** YYYY-MM-DD
- **Decision Makers:** AegisAI Core Engineering Team

---

# Context

AegisAI must support local AI inference while allowing optional integration with cloud providers.

The default provider should:

- Operate offline
- Protect user privacy
- Support multiple open-source models
- Reduce operational cost
- Integrate easily with Python

---

# Decision Drivers

- Privacy
- Offline capability
- Cost efficiency
- Open-source ecosystem
- Flexibility
- Local inference

---

# Considered Options

## Ollama

### Advantages

- Local execution
- Multiple model support
- Easy deployment
- Open-source
- No API cost

### Disadvantages

- Requires local compute resources

---

## OpenAI

### Advantages

- State-of-the-art hosted models
- No local hardware required

### Disadvantages

- Usage costs
- External dependency
- Data leaves local environment

---

## Azure OpenAI / Gemini / Anthropic

### Advantages

- Enterprise-grade hosted services
- Managed infrastructure

### Disadvantages

- Vendor dependency
- Operational cost
- Internet connectivity required

---

# Decision

Ollama will be the default LLM provider.

The platform will expose a provider abstraction allowing cloud providers to be configured without changing business logic.

---

# Consequences

## Positive

- Improved privacy
- Lower operating cost
- Offline support
- Greater model flexibility

## Negative

- Local hardware requirements
- Model performance depends on available resources

---

# Future Evolution

Support additional providers through the provider abstraction while keeping Ollama as the default local runtime.

---

# Related Documents

- architecture/ai-architecture.md
- architecture/security.md
- architecture/system-design.md

---