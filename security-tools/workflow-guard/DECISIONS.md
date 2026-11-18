# Architecture decisions

## 2026-11-18: Start with a focused static checker

The first release targets a narrow, observable gap: small repositories often need actionable GitHub Actions checks without installing a server, granting credentials, or adopting a large platform. The checker therefore uses the Python standard library, reads local files only, and emits stable text or JSON findings.

The initial rules focus on controls explicitly documented by GitHub and OpenSSF: least-privilege token permissions, immutable action references, risky `pull_request_target` trust boundaries, and shell interpolation of untrusted pull-request data. Broader policy and semantic analysis are intentionally deferred until false-positive data is available.

## 2026-11-18: Prefer conservative findings over inferred safety

The parser recognizes common workflow syntax and reports missing permissions policy rather than assuming a safe default. It does not resolve remote actions or claim that a SHA is authentic; those checks require repository and release metadata that the local prototype deliberately does not fetch.
