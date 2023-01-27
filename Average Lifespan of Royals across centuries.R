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


print(grouped_by_century)

#PART3: Average Plot
line_plot <- ggplot(data = grouped_by_century)+
  aes (x = century, y = avg_lifespan)+
  geom_line()+
  theme_grey(base_family = "sans")+
  ylim(c(0,80))+
  xlim(c(9, 20))


line_plot <- line_plot + labs (x = 'Centuries',
                                     y = 'Average Life Span')

print(line_plot)


#PART5: Line graphs for different number of spouses

spouses_lineplot <- ggplot(data = life_mutated)+
  aes(x = birthyear, y = life) +
  geom_point()+
  theme_grey(base_family = "sans")+
  ylim(c(0,110))+
  xlim(c(1000, 2000))+
  geom_line(data = grouped_by_spouses, mapping = aes(y=avg_spouselifespan, x = century *100, color = as.factor(num_spouses)), linewidth=1.2)

spouses_lineplot <- spouses_lineplot + labs (
                                     x = 'Birth Year',
                                     y = 'Average Life Span',
                                     color = "Number of Spouses")

#print(spouses_lineplot)