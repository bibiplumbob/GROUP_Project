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

filtered_count <- filtered_count|>
  filter(continent == "Europe")

#count = count(region_mapping,region)

royals_country <- ggplot(data = filtered_count)+
  aes(x = birthCountry, fill = region)+
  geom_bar(aes(y = lifespan),
           stat = "summary",
           fun = "mean") +
  geom_text(aes(label=after_stat(count)), stat="count", size = 2, y=3)+
  theme(text = element_text(family = 'sans'))+
  labs(
       fill = "Region")+
  xlab("Country of Birth")+
  ylab("Lifespan (years)")+
  coord_flip()

print(royals_country)

#ggsave("birth_country_lifespan.pdf")

#violin plot
royals_violin <- ggplot(data = filtered_count)+
  aes(x = region, y = lifespan)+
  geom_violin(fill = '#B3DAF1') +
  geom_text(aes(label=after_stat(count)), stat="count", size = 3.5, y=5, color = 'white')+
  theme(text = element_text(family = 'sans'))+
  labs(
       fill = "Region")+
  xlab("Region of Birth")+
  ylab("Lifespan (years)")+
  geom_boxplot(width = 0.1)+
  stat_summary(fun.y=mean, geom="point", size=2.5, color="#F5AD94")+
  coord_flip()  
  
#print(royals_violin)

#ggsave("birth_region_lifespan.pdf")