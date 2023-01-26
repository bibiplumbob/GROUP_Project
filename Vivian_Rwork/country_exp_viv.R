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

region_mapping = read_csv("region_mapping.csv")

filtered_count <- left_join(filtered_count, region_mapping, by="birthCountry")

royals_country <- ggplot(data = filtered_count)+
  aes(x = region, y = lifespan, fill = continent
      )+
  geom_bar(stat = "summary",
           fun = "mean",
           width = 0.5)+
  theme(text = element_text(family = 'sans'))+
  labs(title = "Lifespan across birth regions",
       subtitle = "A smaller sample size")+
  xlab("Region of Birth")+
  ylab("Lifespan (years)")+
  coord_flip()

print(royals_country)

  
  