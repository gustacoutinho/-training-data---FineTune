import csv
import json

data = []

with open('basketball_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        prompt = f"Write a summary for {row['Player']}."
        completion = f"{row['Player']} is a {row['Position']} for the {row['Team']}. In {row['GP  Games played']} games, they averaged {row['MPG  Minutes Per Game']} minutes per game and scored {row['PPG  Points Per Game']} points per game. They made {row['FGM  Field Goals Made']} out of {row['FGA  Field Goals Attempted']} field goals attempted, with a field goal percentage of {row['FG%  Field Goal Percentage']}. They also made {row['3FGM  Three-Point Field Goals Made']} out of {row['3FGA  Three-Point Field Goals Attempted']} three-point field goals attempted, with a three-point field goal percentage of {row['3FG%  Three-Point Field Goal Percentage']}. Finally, they made {row['FTM  Free Throws Made']} out of {row['FTA  Free Throws Attempted']} free throws attempted, with a free throw percentage of {row['FT%  Free Throw Percentage']}."
        data.append({"prompt": prompt, "completion": completion})

with open('prompt_completion_pairs.json', 'w') as outfile:
    json.dump(data, outfile)
