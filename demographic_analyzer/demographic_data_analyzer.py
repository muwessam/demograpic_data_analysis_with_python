import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male'].age.mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df[df['education'] == 'Bachelors']) / len(df['education'])*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    highEd = ['Bachelors', 'Masters', 'Doctorate']
    lowEd = ['HS-grad', '11th', '9th', 'Some-college',
       'Assoc-acdm', 'Assoc-voc', '7th-8th', 'Prof-school',
       '5th-6th', '10th', '1st-4th', 'Preschool', '12th']
    higher_education = higher_education = df.loc[df.education.isin(highEd)]
    lower_education = lower_education = df.loc[df.education.isin(lowEd)]


    # percentage with salary >50K
    higher_education_rich = round((len(higher_education[higher_education['salary'] == '>50K'])/len(higher_education))*100, 1)
    lower_education_rich = round((len(lower_education[lower_education['salary'] == '>50K'])/len(lower_education))*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = round((len(num_min_workers[num_min_workers['salary'] == '>50K'])/len(num_min_workers))*100, 1)

    # What country has the highest percentage of people that earn >50K?
    country_count = df['native-country'].value_counts()
    allrich = df[df['salary'] == '>50K']['native-country'].value_counts()

    highest_earning_country = (allrich/country_count).idxmax()
    highest_earning_country_percentage = round(((allrich/country_count)*100).max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    Indians = df[df['native-country'] == 'India']
    richIndians = Indians[Indians['salary'] == '>50K']
    top_IN_occupation = richIndians['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
