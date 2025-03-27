# Payment Scraping and Visualization Project

## Overview
This project involves web scraping payment data from **doge.gov**, and creating an interactive **Tableau visualization** to interactively visualize the size of payments that are made through a Tree Map.

---

## Features
- Automated web scraping to collect payment data from doge.gov.
- Tableau dashboard showcasing interactive visualizations.

---

## Data Source
- **Website**: [doge.gov](https://doge.gov)  
The data includes payment records such as:
  - **Payment amount**
  - **Recipient**
  - **Payment date**
  - **Award Description**

The scraped data is stored locally in CSV format for further processing.

---

## Tech Stack
- **Web Scraping**: Python (Selenium, Firefox Webdriver)
- **Data Preprocessing**: Pandas
- **Visualization**: Tableau

---

## Tableau Visualization
The Tableau dashboard includes:
1. **Tree Map**: Interactive Tree Map or payments that can be used as a filter
2. **Top payments Table**: Table in descending order of payment size

You can find my visualization here: 
[Tableau Public Link](https://public.tableau.com/app/profile/yuji.tanaka4089/viz/ProgramSupportCenterPayments/Dashboard1)

---

## Project Structure
```
├── data
│   ├── rall_data.csv          # Scraped data
│   ├── by_org.csv              # Includes an added column for org info
├── webscraper
│   ├── scrape_all.py            # Web scraping script for All data
│   ├── scrape_by_org.py         # Clicks through the org button and scrapes
├── README.md                 # Project documentation
```

---

## Future Scope
- Adding a map to show payments where the beneficiaries are ultimately international.
- Use Agenting LLM workflow to add aditional information where there is a sparse description
- Cluster analysis to identify payment types and functions i.e international, veterans, etc

---

## Contact Information
- **GitHub**: [https://github.com/yujintanaka]
- **LinkedIn**: [https://www.linkedin.com/in/yuji-tanaka/]
- **Email**: [yntanaka2000@gmail.com]

---

Feel free to adapt this README based on specific project details or add any creative touches! Let me know if there’s anything you'd like expanded or modified. 🚀