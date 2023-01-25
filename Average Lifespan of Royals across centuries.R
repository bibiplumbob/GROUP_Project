library(tidyverse)
final_royal <- read_csv('final_royal.csv')

lifespan <- final_royal|>
  select(title,`ontology/birthYear`,`ontology/deathYear`,num_spouses)|>
  rename(birthyear = `ontology/birthYear`, deathyear = `ontology/deathYear`)|>
  na.omit()|>
  filter(num_spouses <= 3)|>
  filter(birthyear >= 0, deathyear >=0)|>
  filter(deathyear > birthyear)

life_mutated <- lifespan |> 
  mutate(life = deathyear - birthyear)|>
  filter(life < 700) |>
  mutate(century = ceiling(birthyear / 100))
  
#PART2: calculating average life span according to different time periods
grouped_by_century <- life_mutated |>
  group_by(century) |>
  summarise(avg_lifespan = mean(life))


#PART3: Average Plot
line_plot <- ggplot(data = grouped_by_century)+
  aes (x = century, y = avg_lifespan)+
  geom_line()+
  theme_grey()+
  ylim(c(0,80))+
  xlim(c(9, 20))


line_plot <- line_plot + labs (title = 'Average Lifespan of Royals Across Centuries',
                                     x = 'Centuries',
                                     y = 'Average Life Span')

print(line_plot)

#PART4: Scatter Plot
scatter_plot <- ggplot(data = life_mutated)+
  aes (x = birthyear, y = life, color = as.factor(num_spouses))+
  geom_point()+
  theme_grey()+
  ylim(c(0,110))+
  xlim(c(1000, 2000)) 


scatter_plot <- scatter_plot + labs (title = 'Lifespan of Royals during A.D. 1000-2000',
                               x = 'Birth Year',
                               y = 'Life Span',
                               color = "Number of Spouses")

print(scatter_plot)

