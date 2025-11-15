# Maya AI

Maya AI is a cloud-based autonomous VTuber that runs entirely in the cloud with zero maintenance required.

## Features

- **Cloud-Based Brain**: Runs on Google Colab with free GPU
- **Automated Deployment**: GitHub Actions keep Maya running automatically
- **Zero Maintenance**: Set it and forget it
- **Free Cloud Storage**: Uses GitHub as storage backend

## Quick Start

```bash
./scripts/start_maya.sh
```

Then upload `colab/maya_brain.ipynb` to Google Colab and run all cells.

## Architecture

- **Brain**: Ollama + Llama2:7b running on Google Colab
- **Storage**: GitHub-based cloud storage
- **Automation**: GitHub Actions for continuous operation
- **Testing**: Self-testing system for reliability

Maya handles everything automatically once set up!
