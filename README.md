# Pravin G

**Security Researcher & Systems Engineer** · Integrated M.Tech CS @ **SSN College of Engineering, India**

I focus on **protocol & cryptographic verification**, **applied cryptography**, **C/C++ parser & memory-safety hardening**, and **AI agent / supply-chain security**—building reproducible, fail-closed security tooling and upstream fixes.

### Featured Project: [mcp-audit](https://github.com/PRAVIN-952006/mcp-audit)
Zero-dependency security scanner, live `stdio` & Streamable-HTTP/SSE JSON-RPC 2.0 prober, auto-hardener (`fix`), and cryptographic SHA-256 rug-pull detector for Model Context Protocol (MCP) servers (21 rules + GitHub Code Scanning SARIF 2.1.0).

```bash
npx github:PRAVIN-952006/mcp-audit demo
```

### Research & Engineering Focus
- **C/C++ Memory Safety & Codec/Parser Hardening:** Bounds checking, integer-overflow prevention, ARM64 NEON edge-case safety, and `-Wunsafe-buffer-usage` hardening verified with ASan/UBSan
- **Formal Verification & Symbolic Security:** Dolev-Yao protocol modeling (Tamarin Prover), SMT equivalence checking (Z3), and mechanized soundness proofs (Lean 4)
- **Applied Cryptography & Wire-Format Security:** X.509/PKI, MLS, Sigstore/in-toto, OAuth/DPoP, WebAuthn/COSE, and differential conformance testing
- **AI Agent & Supply-Chain Security:** MCP tool-poisoning & rug-pull auditing, offline policy gates, SBOM auditing, GitHub Actions permission analysis, and transcript/MCP trace sanitization

### Selected Open-Source Projects

| Project | Stack | Focus |
| :--- | :--- | :--- |
| **[mcp-audit](https://github.com/PRAVIN-952006/mcp-audit)** | TypeScript (zero-dep) · GitHub Action · SARIF | Security scanner (21 rules), live `stdio` & Streamable-HTTP/SSE prober, Unicode Tag decoder, auto-hardener, and SHA-256 rug-pull detector for MCP servers |
| **[wirelint](https://github.com/PRAVIN-952006/wirelint)** | Rust (zero-dependency) · SARIF | Fail-closed structural auditor for ASN.1 DER, RFC 7515 JWS/JWT (`crit` & duplicate-key guards), and RFC 8949/8152 COSE CBOR |
| **[SessionVeil](https://github.com/PRAVIN-952006/sessionveil)** | TypeScript · Vite · CLI | Structure-preserving secret sanitizer & residual-leak verifier for AI coding-agent transcripts (`.jsonl`) and MCP/OTel traces |
| **[SupplyGuard](https://github.com/PRAVIN-952006/supplyguard)** | Python · CycloneDX · SPDX | Offline SBOM quality, package-URL identity, and supply-chain policy auditor |
| **[ActionScope](https://github.com/PRAVIN-952006/actionscope)** | Python · GitHub Actions | Explainable `GITHUB_TOKEN` permission, inheritance, and third-party action surface reporter |

### Upstream Open-Source Contributions
- **google/libultrahdr** — Safe-buffer, ICC profile, encoder bounds, resize-overflow, and ARM64 NEON tail-handling fixes: [`#527`](https://github.com/google/libultrahdr/pull/527), [`#528`](https://github.com/google/libultrahdr/pull/528), [`#529`](https://github.com/google/libultrahdr/pull/529), [`#531`](https://github.com/google/libultrahdr/pull/531), [`#532`](https://github.com/google/libultrahdr/pull/532), [`#533`](https://github.com/google/libultrahdr/pull/533)
- **webm/libwebp** (Chromium Gerrit) — ARM64 NEON rescaler overflow, SharpYUV 32-bit widened SIMD saturation, and demux NULL-iterator guards: [`CL 8869769`](https://chromium-review.googlesource.com/c/webm/libwebp/+/8869769), [`CL 8869770`](https://chromium-review.googlesource.com/c/webm/libwebp/+/8869770), [`CL 8867389`](https://chromium-review.googlesource.com/c/webm/libwebp/+/8867389)
- **pnggroup/libpng** — Defensive parser hardening: [`#991`](https://github.com/pnggroup/libpng/pull/991), [`#992`](https://github.com/pnggroup/libpng/pull/992), [`#993`](https://github.com/pnggroup/libpng/pull/993)
- **AOMediaCodec/libavif** — Codec boundary and memory-safety hardening: [`#3482`](https://github.com/AOMediaCodec/libavif/pull/3482), [`#3483`](https://github.com/AOMediaCodec/libavif/pull/3483), [`#3484`](https://github.com/AOMediaCodec/libavif/pull/3484), [`#3498`](https://github.com/AOMediaCodec/libavif/pull/3498), [`#3499`](https://github.com/AOMediaCodec/libavif/pull/3499)
- **libjxl/libjxl** — Safe-buffer and decoder hardening: [`#5167`](https://github.com/libjxl/libjxl/pull/5167), [`#5168`](https://github.com/libjxl/libjxl/pull/5168), [`#5170`](https://github.com/libjxl/libjxl/pull/5170)
- **lz4/lz4** — Bounds and safety hardening: [`#2186`](https://github.com/lz4/lz4/pull/2186)
- **nih-at/libzip** — Archive parser hardening: [`#657`](https://github.com/nih-at/libzip/pull/657), [`#658`](https://github.com/nih-at/libzip/pull/658), [`#659`](https://github.com/nih-at/libzip/pull/659)
- **pyupio/safety** — Pytest-harness fix for distributions with incomplete package metadata: [`#931`](https://github.com/pyupio/safety/pull/931)

### Technical Stack
`C / C++20` · `Rust` · `Go` · `TypeScript` · `Python` · `Java` · `Tamarin Prover` · `Z3 SMT` · `Lean 4` · `OpenSSL` · `ASan / UBSan` · `SARIF`
