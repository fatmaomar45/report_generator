#!/usr/bin/env python3
"""
Simple student report generator CLI.

Usage:
    python3 report_generator.py
"""
from typing import Dict
import json


def calculate_average(backend: float, frontend: float, design: float) -> float:
    """Return the average of three marks, rounded to 2 decimals."""
    return round((backend + frontend + design) / 3.0, 2)


def get_average_grade(average: float) -> str:
    """Map numeric average to a letter grade."""
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "E"


def student_report(name: str, backend: int, frontend: int, design: int) -> Dict[str, object]:
    """Build a report dict for a student."""
    average = calculate_average(backend, frontend, design)
    grade = get_average_grade(average)
    return {
        "name": name,
        "backend": backend,
        "frontend": frontend,
        "design": design,
        "average": average,
        "grade": grade,
    }


def prompt_for_mark(prompt: str) -> int:
    """Prompt until the user provides an integer mark in 0..100."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a whole number (0-100).")
            continue
        if not 0 <= value <= 100:
            print("Please enter a value between 0 and 100.")
            continue
        return value


def main() -> None:
    name = input("Enter student name: ").strip()
    backend = prompt_for_mark("Enter Backend marks (0-100): ")
    frontend = prompt_for_mark("Enter Frontend marks (0-100): ")
    design = prompt_for_mark("Enter Design marks (0-100): ")

    report = student_report(name, backend, frontend, design)
    # pretty-print as JSON
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
