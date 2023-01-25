library(tidyverse)
library(ggthemes)

royals_countries = read_csv("country_royals.csv")
filtered_count <- royals_countries|>
  rename('title_label' = 'ontology/title', 
         'birthYear' = 'ontology/birthYear', 'deathYear' = 'ontology/deathYear')|>
  filter(deathYear > birthYear)|>
  mutate(lifespan = deathYear - birthYear )|>
  filter(lifespan < 700)|>
  filter(!is.na(birthCountry))

regions = read_csv("region_mapping.csv")
