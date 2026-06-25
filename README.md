# Textile Manufacturing Ontology

A formal ontology and comprehensive validation framework for the carpet weaving process, demonstrating the integration of knowledge engineering, semantic modeling, and data quality assurance.

## Overview

This repository contains a complete knowledge engineering solution for carpet weaving manufacturing. It showcases how to apply semantic modeling principles and rigorous data validation to a real-world manufacturing scenario.

## Features

- **Formal Ontology**: A structured knowledge representation of the carpet weaving process, including entities, relationships, and constraints
- **Validation Framework**: Comprehensive validation rules to ensure data quality and consistency
- **Semantic Modeling**: Well-defined concepts and relationships in the textile manufacturing domain
- **Real-World Application**: Practical implementation demonstrating knowledge engineering best practices

## Repository Structure

```
textile-manufacturing-ontology/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── ontology/                 # Ontology definitions and models
├── validation/               # Validation framework and rules
├── data/                     # Sample data and test cases
├── scripts/                  # Utility scripts (batch and Python)
├── run_validation.bat        # Windows batch script to run validation
└── validator.py              # Python validation script
```

## Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package installer)
- Windows (for `.bat` script) or command line terminal for manual execution

### Installation

1. Clone the repository:
```bash
git clone https://github.com/elena33e/textile-manufacturing-ontology.git
cd textile-manufacturing-ontology
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running Validation

There are two ways to run the validation framework:

#### Option 1: Using the Batch Script (Windows)

Simply double-click or run the `run_validation.bat` file:
```bash
run_validation.bat
```

This script will:
1. Automatically install all dependencies from `requirements.txt`
2. Execute the SHACL validation with `validator.py`
3. Display results and wait for user input before closing

#### Option 2: Manual Python Execution

Run the validation script directly:
```bash
python validator.py
```

Or install dependencies first:
```bash
pip install -r requirements.txt
python validator.py
```

### Exploring the Ontology

Load and query the ontology:
```python
from ontology import load_ontology

# Load the carpet weaving ontology
ontology = load_ontology()

# Query entities, relationships, and properties
```

## Technology Stack

- **Python** (81.7%) - Core logic, ontology processing, and validation
- **Batch** (18.3%) - Utility scripts for Windows environments

## Key Concepts

### Ontology Components
- **Entities**: Key concepts in carpet weaving (e.g., materials, equipment, processes)
- **Relationships**: How entities interact and relate to each other
- **Properties**: Attributes and constraints for each entity
- **Rules**: Validation constraints and business logic

### Validation Framework
- Data type validation
- Relationship integrity checks
- Constraint enforcement
- Completeness verification

## Use Cases

- Manufacturing process documentation and standardization
- Data quality assurance in production systems
- Knowledge management and organizational learning
- Training and onboarding for manufacturing teams
- Integration with MES (Manufacturing Execution Systems) and ERP systems

## Contributing

Contributions are welcome! Please feel free to:
- Report issues
- Suggest improvements
- Submit pull requests
- Enhance the ontology with new concepts

## License

This project is provided as-is for educational and professional use.

## Author

**Elena33e**

## Contact & Support

For questions, suggestions, or issues related to this project, please open an issue in the repository.

---

**Last Updated**: 2026

*Building better manufacturing through semantic knowledge engineering.*
