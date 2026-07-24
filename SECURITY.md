# Security Policy

Thank you for helping keep **AegisAI** and its community secure.

We take the security of this project seriously and appreciate responsible disclosure of potential vulnerabilities.

---

# Supported Versions

The following table indicates which versions of AegisAI currently receive security updates.

| Version | Supported |
|----------|-----------|
| Main Branch | ✅ Yes |
| Development Branch | ✅ Yes |
| Older Releases | ❌ No |

As the project matures and versioned releases are introduced, this policy will be updated accordingly.

---

# Reporting a Vulnerability

If you discover a security vulnerability, **please do not create a public GitHub issue**.

Instead, report the issue privately with as much detail as possible.

Please include:

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Proof of Concept (if available)
- Suggested mitigation (optional)
- Affected version or commit

---

# Response Process

After receiving a report, the project maintainers will:

1. Acknowledge receipt of the report.
2. Investigate and validate the issue.
3. Assess severity and impact.
4. Develop and test a fix.
5. Release a security update if required.
6. Publicly disclose the issue after a fix is available.

---

# Responsible Disclosure

We kindly ask that you:

- Allow sufficient time for investigation before public disclosure.
- Avoid exploiting vulnerabilities beyond what is necessary to demonstrate the issue.
- Avoid accessing or modifying data that does not belong to you.
- Avoid disrupting public services or other users.

Responsible disclosure helps protect everyone using the project.

---

# Security Best Practices

When deploying AegisAI, we recommend:

- Keep dependencies up to date.
- Rotate secrets regularly.
- Never commit secrets or API keys.
- Use HTTPS in production.
- Enable authentication and authorization.
- Restrict network access where appropriate.
- Regularly review logs and monitoring dashboards.
- Apply operating system and container security updates.

---

# Scope

This policy covers vulnerabilities affecting:

- FastAPI backend
- Next.js frontend
- Authentication and authorization
- AI services
- Agent framework
- RAG pipeline
- Database integrations
- Docker and Kubernetes deployment
- GitHub Actions workflows
- Third-party integrations maintained by this repository

---

# Third-Party Dependencies

AegisAI relies on a number of open-source dependencies.

Security issues affecting third-party libraries should also be reported to the respective maintainers when appropriate.

We regularly update project dependencies to address known vulnerabilities.

---

# Security Documentation

Technical security architecture is documented separately in:

```

architecture/security.md

```

This document focuses specifically on vulnerability reporting and repository security policies.

---

# Contact

Until a dedicated security contact is established, please use GitHub's private vulnerability reporting feature (if enabled) or contact the project maintainers through the repository.

---

Thank you for helping improve the security of AegisAI.