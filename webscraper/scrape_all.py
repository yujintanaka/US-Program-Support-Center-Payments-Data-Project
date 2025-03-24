from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


driver =  webdriver.Firefox()

driver.get("https://doge.gov/payments")


# Unselect the date filter to access all days
date_filter_btn = driver.find_element(By.XPATH, "//div[text()='March 7, 2025']")
date_filter_btn.click()

# Locate the buttons (one is hidden and shows dynamically based on page size)
view_all_buttons = driver.find_elements(By.XPATH, "//div[text()='View All']")

# Iterate through buttons and click the visible one
for view_all_btn in view_all_buttons:
    if view_all_btn.is_displayed():
        view_all_btn.click()
        break  # Exit the loop after clicking the visible button

# Locate the table header
header = driver.find_element(By.TAG_NAME, "thead")

# Extract the headers
header_elements = header.find_elements(By.TAG_NAME, 'th')
headers = [header.text for header in header_elements]

print(headers)

# Create an empty list to hold table data
data = []

# Pagination Loop for extracting table data
while True:
    # Locate the table body
    table_body = driver.find_element(By.TAG_NAME, "tbody")

    # Extracts the rows
    rows = table_body.find_elements(By.TAG_NAME, "tr")

    # Iterate through rows
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        # Get the text from each cell
        cell_data = [cell.text for cell in cells]
        # Append the row data to the list
        data.append(cell_data)
        
    # Locate the "Next" buttons (again, we have two)
    next_buttons = driver.find_elements(By.XPATH, "//button[text()='Next']")
    # initializes selected button
    selected_next_btn = None
    # Iterate through buttons and click the visible one
    for next_btn in next_buttons:
        # Picks the visible button
        if next_btn.is_displayed():
            selected_next_btn = next_btn
    # Checks if there are any more pages
    if selected_next_btn.get_attribute("disabled"):
        print("Reached the last page.")
        break # Exits loop since the next button is disabled
    else:
        selected_next_btn.click()

# Close the WebDriver
driver.quit()

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Optionally, set column headers if known
df.columns = headers

# Check, if it shows 37218 entries it has worked
print(df.info())

# Save the DataFrame to a CSV file
df.to_csv("data/all_data.csv", index=False)  # 'index=False' excludes the row index from the CSV

print("DataFrame saved to table_data.csv")
