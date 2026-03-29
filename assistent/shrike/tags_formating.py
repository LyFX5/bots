tags_string = "#Turing #patterns #structures #emergence #cyberbiology #reaction #diffusion #complex #systems #swarm #waves #generalsemantics #evaluation #neuroevaluation #abstraction #language #communication #assumption #Korzybski #scientificmethod #thinking #holism #climate #environment #global #warming #earth #future #ecology #ecosystem #system #audiobook #Alanwatts #east #environment #abstraction #pattern #pointofview #thinking #language #communication #organisation #conditioning #generalsemantics #systemic #holism #newsanity #lecture #record #biosonification #Skinner #behaviorism #Skinner #behaviorism #abstraction #math #production #process #осознанноеабстрагирование #philosophy #schizoanalysis #anticapitalism #accelerationism #transhumanism #philosophy #schizoanalysis #anticapitalism"

tags_list = list(map(lambda x: x.replace("#", ""), tags_string.split(" ")))

tags_list_sorted_set = sorted(list(set(tags_list)), key=lambda x: x.lower())

tags_string_formated = "".join(list(map(lambda x: "#" + x + "\n", tags_list_sorted_set)))

print(tags_string_formated)


