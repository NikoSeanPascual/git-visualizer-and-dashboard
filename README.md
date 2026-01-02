# Niko’s Local Git Pulse

Niko’s Local Git Pulse is a desktop GUI application that visualizes activity from your local Git repositories. It provides a GitHub-style contribution heatmap and a list of recent commits, all rendered locally using Python.

The goal of this project is to help developers quickly understand how active their projects are without relying on GitHub or remote repositories.

## Features

- Automatically scans a local directory for Git repositories
- Displays repositories in a scrollable sidebar
- Shows a 52-week contribution heatmap based on commit history
- Displays recent commits with date, hash, and message
- Modern dark UI using CustomTkinter

## MUST DO BEFORE RUNNING THE CODE
- Change the base_path at line 36 tto work with your projects folder

## Technologies Used

- Python
- CustomTkinter
- GitPython
- datetime
- os

## Installation

1. Clone the repository or download the source code.

2. Install required dependencies:

```bash
pip install customtkinter GitPython
