# Technical Competencies

## Current Role & Production Systems

Director of Operations at Eon Labs Ltd. (www.eonlabs.com), handling administration, HR, SR&ED (Scientific Research and Experimental Development), feature engineering for quantitative trading systems, and AI agent coding tool adoption across the team. Focus areas include [Claude Code](https://www.claude.com/product/claude-code) [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) popularization, automation workflows, and cloud infrastructure for financial technology systems.

Seeking final career opportunity in team environment at established business, transitioning from independent operations role to hands-on technical contribution.

## Career Background & Experience

**25 years of SaaS development experience** including founding and scaling internet solutions company (2000) to 100+ employees across Hong Kong, Shanghai, and Macau. Built first-generation web analytics tools (pre-Google Analytics era). Understand both scaling challenges and market positioning importance from operator perspective.

Learned critical lessons about technology adoption patterns, market timing, and the importance of established markets with proven customer bases—which directly informs interest in contributing to Netstrata's established position in NSW strata management with proprietary software approaching major milestones (December 2025, July 2026).

## Key Production System

Operational automation system using Telegram bot interface for team workflow orchestration (quantitative trading infrastructure monitoring):

- **launchd supervision**: Automatic crash detection and restart
- **100ms auto-reload**: Rapid iteration and deployment
- **Doppler credential management**: Secure secrets handling
- **24/7 operation**: Continuous monitoring and maintenance

Demonstrates operational reliability patterns applicable to business-critical systems.

## Relevant Technical Expertise

### Python Automation & Workflow Systems

- **Package Management**: `uv` for modern Python dependency management (avoiding legacy pip/conda)
- **Self-Contained Scripts**: PEP 723 inline dependencies for portable automation tools
- **Production Deployment**: Cloud Run serverless jobs, systemd service management for unattended operation
- **Type Safety**: mypy strict mode, PEP 561 compliance for maintainable codebases
- **Async/Streaming**: Real-time data collection via WebSocket with exponential backoff retry logic
- **API Integration**: Web scraping (Playwright + BeautifulSoup), third-party service orchestration
- **Monitoring**: Dead Man's Switch patterns (Healthchecks.io), mobile alerting (Pushover)

**Cost-efficient infrastructure**: Free-tier optimization across cloud providers (Cloud Run, BigQuery, managed databases)

**Recent Example**: Extracted 292 blog posts from Netstrata website using automated web scraping with AJAX pagination handling, rate limiting, and metadata preservation.

### Cloud & Container Infrastructure

- **Google Cloud Platform**: Production deployment expertise
  - Free-tier optimization strategies (Cloud Run, Compute Engine, BigQuery)
  - Serverless cron orchestration (Cloud Scheduler)
  - Secret management and zero-downtime credential rotation
- **Container Runtime**: Colima + Docker CLI on macOS for local development and testing
- **Cloud-native architecture**: Dual-pipeline patterns for zero-downtime migrations
- **Cost-efficient SaaS**: Free tier mastery across cloud providers maximizing value without budget bloat
- **Infrastructure as Code**: Configuration management for reproducible deployments

### Data Engineering & Analytics

- **Embedded analytics databases**: DuckDB for in-process analytics (10-100x speedups vs traditional approaches)
- **Modern Python data tools**: PyArrow for zero-copy data transfers, async/streaming pipelines
- **Cloud data warehouses**: BigQuery query optimization within free-tier limits
- **Real-time streaming**: WebSocket-based data collection with automatic reconnection
- **Performance engineering**: Window functions, ASOF joins, empirical benchmarking methodologies

### System Programming & Performance

- **Rust**: Modern systems programming with cargo toolchain
- **Testing**: cargo nextest for fast test execution
- **Pre-commit Hooks**: Automated code quality checks before deployment

## Production Examples Relevant to Netstrata

### Migration Infrastructure Expertise

**Dual-pipeline migration architecture** enabling zero-downtime system transitions:

- Run legacy and modern systems in parallel with automatic deduplication
- Idempotent operations allowing safe re-runs during failures
- Chunked processing patterns preventing memory failures on large datasets
- Rollback mechanisms for quick recovery from migration issues

**Zero-gap data validation frameworks**:

- Automated completeness verification across entire datasets
- Database-level constraints (CHECK, PRIMARY KEY) enforcing data integrity
- Structured audit trails providing queryable migration history
- Exception-only error handling preventing silent data corruption

**Relevance to Future Migrations**: External customer migrations (when needed) require similar dual-pipeline architecture, gap detection, and rollback capabilities. Richardson (WA) is currently stable on existing modules.

### Data Quality & Integrity Systems

**Multi-layer validation frameworks** for production data pipelines:

- HTTP/API layer validation (status codes, rate limits, authentication)
- Schema validation (Pydantic, type checking)
- Sanity checks (database constraints, business rule validation)
- Gap detection (completeness verification across sequences)
- Anomaly detection (outlier identification, statistical validation)

**Reliability patterns**:

- Atomic file operations preventing partial writes and data corruption
- INSERT OR REPLACE for idempotent database operations
- Structured audit trails stored in compressed formats (Parquet, Arrow)
- Exception-only error handling (no silent failures, no defaults)

**Relevance to Core Development**: Data integrity assurance applies across scheme records, financial history, and compliance documents—critical for the December 2025 DMS migration and ongoing Strata Space development.

### Internal Automation Tools

Created workflow automation systems that:

- **Eliminate Manual Data Entry**: Bulk operations replacing repetitive form filling
- **API Orchestration**: Coordinating multiple third-party services
- **Report Generation**: Automated document creation from structured data
- **Notification Systems**: Real-time alerts via Telegram/email for operational events

**Relevance to Phase 1**: Andrew Tunks' operational efficiency mandate aligns with automation capabilities.

### AI-Augmented Development Tools (Production Context)

Extensive production experience with AI coding agents:

- **[Claude Code](https://www.claude.com/product/claude-code) CLI**: 1000+ hours with [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) development, custom workflow design
- **Anthropic's Claude Code (headless mode)**: Programmatic agent orchestration for automated workflows
- **[Codex](https://openai.com/codex/)**: OpenAI's code generation model for AI-powered development
- **Cursor**: AI-augmented IDE with context-aware code generation

**Focus areas**: Prompt engineering, context window management, systematic workflow integration, reliability patterns, cost management

**NOT speculative AI hype** - this is production experience with measurable outcomes (hours saved, errors reduced, processing speed). Detailed AI methodology described in attached document (01b).

## Technical Environment & Practices

### Development Workflow

- **Unix-Like Systems**: macOS/Linux (POSIX shells, standard conventions)
- **Version Control**: Git with pre-commit hooks for code quality
- **Testing**: Automated test suites with fast feedback loops
- **Documentation**: Machine-readable specs (OpenAPI, JSON Schema, YAML)
- **Cloud-Native Deployment**: Serverless cron jobs, auto-scaling VMs, managed secret rotation
- **Free-Tier Optimization**: Strategic service selection to minimize operating costs
- **Empirical Validation**: POC frameworks testing assumptions before production commitment

### Code Quality Standards

- **Dependency Auditing**: cargo deny check for security vulnerabilities
- **Automated Testing**: Continuous validation before deployment
- **Error Handling**: Graceful failure and recovery patterns
- **Observability**: Logging, monitoring, crash detection

### Rust Production Experience

**rangebar** - Published on Crates.io (v2.0.0, 1,863 downloads) - financial data processing library:

- **Workspace Architecture**: Modular crate design with 8 sub-crates for maintainability
- **Algorithm Specification**: Formal mathematical specifications with invariant testing
- **Documentation Management**: Authoritative spec pattern (single source of truth for algorithm behavior)
- **Production Patterns**: Fixed-point arithmetic, non-lookahead bias guarantees, temporal integrity

**Documentation Standards**:

- Centralized specifications replacing duplicated documentation
- Version-tracked algorithm specs with breaking change history
- Comprehensive testing validating conformance to specifications

**Relevance to December 2025 + July 2026 Milestones**: Software completion requires documentation discipline and specification rigor. Authoritative spec patterns prevent divergence between code, tests, and documentation across Tom Bacani's team (3 squads working in parallel).

### Rapid Prototyping Capability

**Speed**: MVPs in days, not months
**Iteration**: Fast feedback cycles with 100ms reload times
**Production Quality**: From prototype to reliable operation quickly

**Example**: Netstrata blog extraction project went from concept to 292 extracted posts in under 48 hours.

## What This Means for Netstrata

### December 2025 Milestone Contribution

Support DMS, Tasks, Time Recording release - "biggest operational shift since Financials went live" [Tom Q3 Report, p.6]:

- **Modern Tooling**: Python/uv, Rust for performance-critical components
- **Automation Expertise**: Reducing manual operational overhead
- **Production Reliability**: Experience with 24/7 supervised systems
- **Fast Iteration**: Quick turnaround on features and bug fixes
- **Squad Support**: Experience supporting parallel workstreams

### July 2026 Milestone Contribution

Support Buildings, Asset Management, Strata Manager Dashboard - targeting "90-95% of workload in Strata Space" [Tom Q3 Report, p.10]:

- **Data Systems**: Asset management workflow automation
- **Dashboard Development**: Production monitoring interfaces
- **Testing Frameworks**: Automated validation
- **Documentation**: Technical documentation generation

### Post-2026 Contribution (if still contributing)

- **Commercialisation Support**: Deployment automation for external customers
- **Automation Enhancement**: Continued workflow optimization
- **Support Infrastructure**: Issue tracking, documentation, monitoring

## Technical Philosophy

**Focus on Business Value**:

- Automation should save measurable time (hours → minutes)
- Systems should run unattended (launchd supervision, crash recovery)
- Tools should be maintainable (clear code, good documentation)
- Technology serves operations (not technology for its own sake)

**Avoid Hype**:

- No claims about AI capabilities without production evidence
- Focus on solved problems, not potential future benefits
- Honest about limitations and trade-offs
- Measure outcomes (time saved, errors reduced, uptime)

**Prioritize Future-Proof Technologies**:

- **Widely-adopted languages**: Python, Rust, C++ (large ecosystems, strong hiring pools, long-term support)
- **Cost-efficient SaaS**: Free-tier mastery, serverless architectures, pay-per-use models
- **Cloud-native patterns**: Idempotent operations, automatic retries, exponential backoff
- **Type safety**: Static type checking (mypy, rustc) preventing runtime errors
- **Popular frameworks**: Established tools with large communities ensure maintainability
- **Open standards**: OpenAPI, JSON Schema, machine-readable specifications

**Rationale**: Popular technologies = larger talent pool + better tooling + longer support lifecycle. Cost efficiency protects $12-14M software investment from operational bloat.

**Join Existing Team**:

- Work with Tom Bacani's software operations team (3 squads)
- Support Andrew Tunks' operational efficiency mandate
- Contribute to December 2025 and July 2026 milestones
- Team member, not external auditor
- Collaborate with Epi Neto's IT team (AI initiatives are his domain)
