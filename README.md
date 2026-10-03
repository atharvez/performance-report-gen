# Performance Report Generator

Automated performance report generation -- produces clean HTML reports from metrics data.

## Overview

Generate professional performance reports from raw metrics. Input JSON data, get a formatted HTML report ready to share or print. Built with a Python data layer and HTML template engine.

## Tech Stack

- Python (data.py) -- data processing and report generation
- HTML / CSS / JS -- report template and rendering
- Chart.js -- visualizations embedded in reports

## Usage

```bash
git clone https://github.com/atharvez/performance-report-gen.git
cd performance-report-gen
python data.py           # generates report.html from your data
# Or open report.html directly in the browser
```

## Files

| File | Purpose |
|------|---------|
| data.py | Data processing and template rendering |
| template.html | Report HTML template |
| report.html | Generated output report |

## License

MIT (c) Atharva Desai