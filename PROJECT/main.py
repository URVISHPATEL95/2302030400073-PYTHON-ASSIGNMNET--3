import matplotlib.pyplot as plt

# Sample data
countries = ['USA', 'India', 'Brazil', 'Russia', 'UK']
cases = [100000, 85000, 70000, 50000, 30000]
deaths = [5000, 4000, 3000, 2500, 2000]

# Bar Chart - Deaths by Country
plt.figure(figsize=(8,5))
plt.bar(countries, deaths, color='red')
plt.title("COVID-19 Deaths by Country")
plt.xlabel("Country")
plt.ylabel("Number of Deaths")
plt.show()

# Line Graph - Cases Over Days
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
daily_cases = [5000, 7000, 8000, 6500, 9000]

plt.plot(days, daily_cases, marker='o', color='blue')
plt.title("Daily COVID-19 Cases")
plt.xlabel("Days")
plt.ylabel("Cases")
plt.grid(True)
plt.show()

# Pie Chart - Case Distribution
plt.pie(cases, labels=countries, autopct='%1.1f%%', startangle=140)
plt.title("COVID-19 Case Distribution")
plt.axis('equal')
plt.show()
