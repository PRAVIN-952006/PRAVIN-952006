# Pravin G

**Security Researcher & Systems Engineer** · Integrated M.Tech CS @ **SSN College of Engineering, India**

I focus on **protocol & cryptographic verification**, **applied cryptography**, **parser & boundary security**, and **software supply-chain security**—building reproducible, fail-closed security tooling and formal models.

### Research & Engineering Focus
- **Formal Verification & Symbolic Security:** Dolev-Yao protocol modeling (Tamarin Prover), SMT equivalence checking (Z3), and mechanized soundness proofs (Lean 4)
- **Applied Cryptography & Wire-Format Security:** X.509/PKI, MLS, Sigstore/in-toto, OAuth/DPoP, WebAuthn/COSE, and differential conformance testing
- **AI Agent & Supply-Chain Security:** MCP tool-poisoning & rug-pull auditing, offline policy gates, SBOM auditing, GitHub Actions permission analysis, and transcript/MCP trace sanitization

### Selected Open-Source Projects

| Project | Stack | Focus |
| :--- | :--- | :--- |
| **[mcp-audit](https://github.com/PRAVIN-952006/mcp-audit)** | TypeScript (zero-dep) · GitHub Action · SARIF | Security scanner, live stdio & Streamable-HTTP/SSE JSON-RPC 2.0 prober, Unicode Tag decoder, and SHA-256 rug-pull detector for MCP servers |
| **[wirelint](https://github.com/PRAVIN-952006/wirelint)** | Rust (zero-dependency) · SARIF | Fail-closed structural auditor for ASN.1 DER, RFC 7515 JWS/JWT (`crit` & duplicate-key guards), and RFC 8949/8152 COSE CBOR |
| **[SessionVeil](https://github.com/PRAVIN-952006/sessionveil)** | TypeScript · Vite · CLI | Structure-preserving secret sanitizer & residual-leak verifier for AI coding-agent transcripts (`.jsonl`) and MCP/OTel traces |
| **[AgentGate](https://github.com/PRAVIN-952006/agentgate)** | Python · SARIF · CI | Offline MCP server & tool-manifest approval baseline and drift gate for CI pipelines |
| **[SupplyGuard](https://github.com/PRAVIN-952006/supplyguard)** | Python · CycloneDX · SPDX | Offline SBOM quality, package-URL identity, and supply-chain policy auditor |
| **[ActionScope](https://github.com/PRAVIN-952006/actionscope)** | Python · GitHub Actions | Explainable `GITHUB_TOKEN` permission, inheritance, and third-party action surface reporter |

### Technical Stack
`Rust` · `C++20` · `Go` · `TypeScript` · `Python` · `Java` · `Tamarin Prover` · `Z3 SMT` · `Lean 4` · `OpenSSL` · `SARIF`

### Open-Source Contributions
- [`pyupio/safety#931`](https://github.com/pyupio/safety/pull/931) — pytest-harness fix for distributions with incomplete package metadata.
