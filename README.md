#!/bin/bash

# Backup first
cp README.md README.md.backup

# Rewrite Daily Tracking: Keep only detailed entries, in order Day 1 to 7
cat <<EOF > README.md
# Career Acceleration Challenge

## Description
This repository tracks my 120-day journey in the Career Acceleration Program, focusing on building professional Python skills, object-oriented programming (OOP) concepts (encapsulation, inheritance, abstraction, polymorphism), Django projects, Streamlit apps, and cloud deployment (local and Google Cloud). It simulates industry workflows, including schema design with Prisma, Docker setup, and front-end UI, to prepare for remote jobs in ML engineering, data science, or AI.

## Personal Goals
- Master Python typing speed and avoid copy-pasting to build a developer mindset.
- Complete weekly official tasks from the PDF handbook and bonus practices.
- Deploy a production-level Django project by month 4.
- Secure a remote internship or contractual scholarship (e.g., \$500–\$3000) in the UK, Canada, or similar.
- Prepare for interviews with 1500+ practice questions and mock sessions.

## What This Covers
- **Month 1:** Python basics, weekly page-by-page tasks, OOP fundamentals.
- **Month 2:** Advanced OOP, developer professionalism, extra practices for enhancement.
- **Month 3:** Collaborative projects, use case studies, schema/Docker/UI design.
- **Month 4:** Django applications, local/cloud deployment (e.g., 3000 BDT local or free Google Cloud), ERP/MBB systems discussion.

## Daily Tracking
Use this section to log progress. Update after each day with date and key achievements.

- **01. Day 1 - 2025-12-15** - Completed all Day 1 micro-challenges: identity swap, type auditor, precision banker, modulo architect.
- **02. Day 2 - 2025-12-16** - Completed logic flow: guard clause, floating point trap, truthiness inspector, ternary packer.
- **03. Day 3 - 2025-12-17** - Completed loops: infinite guardian, accumulator pattern, efficient skipper, string walker.
- **04. Day 4 - 2025-12-18** - Completed lists: reference trap, slicing surgeon, stack emulator, one-line architect (list comprehension).
- **05. Day 5 - 2025-12-19** - Completed dictionaries: speed trap lookup, safe vault access, frequency counter, database merger.
- **06. Day 6 - 2025-12-20** - Completed functions: scope fortress, pure return, default gateway, logic gate (is_even).
- **07. Day 7 - 2025-12-21** - Completed error handling: input guard, math safety net, cleanup crew (finally), custom signal (raise).

## Repository Structure
- **01. Day 1/** → **07. Day 7/**: Daily micro-challenge solutions (.py files with docstrings).
- **projects/**: Future Django/Streamlit apps and capstone.
- **notes/**: Concept summaries (e.g., heap memory, garbage collector).
- **LICENSE**: MIT license.
- **README.md**: This file.

## Best Practices Followed
- All code typed manually (no copy-pasting).
- Professional naming, comments, docstrings.
- Submissions via Google Classroom links.
- English communication for job readiness.

<center><i>Committed to perseverance and leadership in team dynamics.</i></center>
EOF

git add README.md
git commit -m "Cleaned README: Removed duplicates, ordered Daily Tracking Day 1-7 with detailed achievements"
git push origin main

echo "README cleaned and professional! Week 1 fully showcased."