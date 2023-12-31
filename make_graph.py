import os
import yaml
import matplotlib.pyplot as plt


def extract_university_years(folder_path):
    university_years = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".yml"):
            if filename == "template.yml":
                continue
            filepath = os.path.join(folder_path, filename)

            with open(filepath, "r") as file:
                try:
                    data = yaml.safe_load(file)["student"]

                    # Check if the YAML file has the 'university_year' attribute
                    if "university_year" in data:
                        university_years.append(data["university_year"])
                except:
                    pass

    return university_years


def plot_histogram(university_years):
    plt.hist(
        university_years,
        bins=range(1, max(university_years) + 2),
        align="left",
        rwidth=0.8,
    )
    plt.xlabel("University Year")
    plt.ylabel("Number of Students")
    plt.title("Distribution of University Years")
    plt.xticks(range(1, max(university_years) + 1))
    plt.savefig("graph.png")


if __name__ == "__main__":
    folder_path = "students"
    university_years = extract_university_years(folder_path)

    if university_years:
        plot_histogram(university_years)
    else:
        print("No valid university year data found in the specified folder.")
