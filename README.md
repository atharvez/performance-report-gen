# Performance Report Generator ðŸ“Š

Automated performance report generation â€” produces clean HTML reports from metrics data.

**Live:** [atharvez.github.io/performance-report-gen](https://atharvez.github.io/performance-report-gen)

## Overview

Generate professional performance reports from raw metrics. Input JSON data, get a beautifully formatted HTML report ready to share or print.

## Tech Stack

- HTML5, CSS3, vanilla JavaScript
- Chart.js for visualizations
- GitHub Pages for hosting

## Usage

```bash
git clone https://github.com/atharvez/performance-report-gen.git
cd performance-report-gen
# Open index.html directly in browser
# Or serve locally:
python -m http.server 8080
```

## Input Format

```json
{
  "reportTitle": "Q3 Performance Report",
  "metrics": [
    { "name": "Response Time", "value": 120, "unit": "ms", "target": 200 }
  ]
}
```

## License

MIT Â© [Atharva Desai](https://github.com/atharvez)