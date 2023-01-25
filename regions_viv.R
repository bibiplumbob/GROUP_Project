library(tidyverse)
library(ggthemes)

royal_data = read_csv("final_royal.csv")

#renaming columns
royal_data <- royal_data |>
  rename('title_label' = 'ontology/title', 
         'birthYear' = 'ontology/birthYear', 'deathYear' = 'ontology/deathYear')|>
  filter(deathYear > birthYear)

#Calculating age 
royals_age <- royal_data |>
  mutate(lifespan = deathYear - birthYear )|>
  filter(lifespan < 700)

#Distinct Regions