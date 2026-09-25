MASTER_CORE 5 STAGE V2 FINAL

Contents:
- Five stage-locked Core prompts
- Ten sanitized Unicode Knowledge Base PDFs, 100 structured synthetic cases each
- CORE_AUDIT.txt, KB_AUDIT.txt, INSTALL_GUIDE.txt
- PROVENANCE_V1/ preserves the original user-provided V1 core/PDF source files unchanged

Runtime design:
- Stage is fixed by CORE_IDENTITY in each Gem.
- Stage selection and stage elicitation are disabled.
- Knowledge files are reference-only.
- UNKNOWN and CONFIRMED_RELATIONSHIP are historical knowledge labels only, never active runtime stage values.
- Default candidate generation is 3-4 options, exactly 2 sentences each.
