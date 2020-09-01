import numpy as np
import json
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set()
def load_json(name_json):
    """ Load configuration from json file """
    data = {}
    with open(name_json + ".json", 'r') as file:
        data = json.load(file)
    return data

def get_times_and_best(json_filename, category, iterations):
    times = {'Tiempo':[], 'Parámetro': [], 'Prueba': []}
    bests_objectives = {'Valor objetivo': [], 'Parámetro': [], 'Prueba': []}
    for i in range(1,iterations+1):
        json_instance = load_json(f"{json_filename}_{i}")
        times['Tiempo'].append(json_instance["elapsed_time"])
        times['Parámetro'].append(category)
        times['Prueba'].append(i)
        bests_objectives['Valor objetivo'].append(int(json_instance["best_objetive"]))
        bests_objectives['Parámetro'].append(category)
        bests_objectives['Prueba'].append(i)

    times = pd.DataFrame.from_dict(times)
    bests_objectives = pd.DataFrame.from_dict(bests_objectives)
    return times, bests_objectives

def get_times_and_best_2(json_filename, category, iterations):
    times = {'Tiempo':[], 'Parámetro': [], 'Prueba': []}
    bests_objectives = {'Valor objetivo': [], 'Parámetro': [], 'Prueba': []}
    for i in range(1,iterations+1):
        numero = str(i).zfill(3)
        json_instance = load_json(f"{json_filename}_{numero}")
        times['Tiempo'].append(json_instance["elapsed_time"])
        times['Parámetro'].append(category)
        times['Prueba'].append(i)
        bests_objectives['Valor objetivo'].append(json_instance["best_objective"])
        bests_objectives['Parámetro'].append(category)
        bests_objectives['Prueba'].append(i)

    times = pd.DataFrame.from_dict(times)
    bests_objectives = pd.DataFrame.from_dict(bests_objectives)
    return times, bests_objectives

def unify_data(parameter_list, filename_list, iterations, format_file):
    parameters = len(parameter_list)
    dataframe_times = pd.DataFrame(columns = ['Tiempo', 'Parámetro', 'Prueba'])
    dataframe_bests = pd.DataFrame(columns = ['Valor objetivo', 'Parámetro', 'Prueba'])

    if format_file==0:

        for i in range(parameters):
            times, bests = get_times_and_best(filename_list[i], parameter_list[i], iterations)
            dataframe_times = dataframe_times.append(times, ignore_index=True)
            dataframe_bests = dataframe_bests.append(bests, ignore_index=True)
        
        
    else:
        for i in range(parameters):
            times, bests = get_times_and_best_2(filename_list[i], parameter_list[i], iterations)
            dataframe_times = dataframe_times.append(times, ignore_index=True)
            dataframe_bests = dataframe_bests.append(bests, ignore_index=True)
    return dataframe_times, dataframe_bests

def graph_boxplot(data, filename, title, evaluation_criteria):
    ax = sns.boxplot(x='Parámetro', y= evaluation_criteria, data= data, palette = "BuGn_r")
    ax = sns.swarmplot(x="Parámetro", y= evaluation_criteria, data= data, color=".25")
    ax.set_title(title)
    ax.figure.savefig(filename,
                    format='jpeg')
    plt.clf()

def graph_scatterplot(data, filename, title, evaluation_criteria):
    
    ax = sns.scatterplot(x="Prueba", y=evaluation_criteria, hue=data.Parámetro.tolist(), style= data.Parámetro.tolist(),
                     data=data)
    ax.set_title(title)
    ax.legend(loc='right', bbox_to_anchor=(1.01, 0.25), ncol=1)
    ax.set(ylabel= "Tiempo[s]")
    #plt.figure(figsize=(10,6))
    ax.figure.savefig(filename,
                    format='jpeg')
    
    plt.clf()



################################ TEMPERATURA ####################################

temperature = ["base", "temperature_x10", "temperature_x0.5"]
###################### INSTANCIA 1 #############################

temperature_filename_chr12a = ["result_sa/chr12a_base_SA", "result_sa/chr12a_temperature_10_SA", "result_sa/chr12a_temperature_05_SA"]

temperature_times, temperature_bests = unify_data(temperature, temperature_filename_chr12a, 30, 0)
df = temperature_times.groupby('Parámetro').describe()
#####      PLOT TIME      #######

graph_scatterplot(temperature_times, "plots_sa/chr12a_temperature_time_boxplot.jpg", "Resultados variando temperatura inicial instancia: chr12a", 'Tiempo')

##### PLOT OBJECTIVE VALUE ######
graph_boxplot(temperature_bests, "plots_sa/chr12a_temperature_obj_value_boxplot.jpg", "Resultados variando temperatura inicial instancia: chr12a", 'Valor objetivo')


######################## INSTANCIA 2 ############################

temperature_filename_esc64a = ["result_sa/esc64a_base_SA", "result_sa/esc64a_temperature_10_SA", "result_sa/esc64a_temperature_05_SA"]
temperature_times, temperature_bests = unify_data(temperature, temperature_filename_esc64a, 30, 0)


#####      PLOT TIME      #######

graph_scatterplot(temperature_times, "plots_sa/esc64a_temperature_time_boxplot.jpg", "Resultados variando temperatura inicial instancia: esc64a", 'Tiempo')

##### PLOT OBJECTIVE VALUE ######
graph_boxplot(temperature_bests, "plots_sa/esc64a_temperature_obj_value_boxplot.jpg", "Resultados variando temperatura inicial instancia: esc64a", 'Valor objetivo')


######################## INSTANCIA 3 ############################

temperature_filename_kra32 = ["result_sa/kra32_base_SA", "result_sa/kra32_temperature_10_SA", "result_sa/kra32_temperature_05_SA"]
temperature_times, temperature_bests = unify_data(temperature, temperature_filename_kra32, 30, 0)


##### PLOT TIME #######

graph_scatterplot(temperature_times, "plots_sa/kra32_temperature_time_boxplot.jpg", "Resultados variando temperatura inicial instancia: kra32", 'Tiempo')

##### PLOT OBJECTIVE VALUE ######
graph_boxplot(temperature_bests, "plots_sa/kra32_temperature_obj_value_boxplot.jpg", "Resultados variando temperatura inicial instancia: kra32", 'Valor objetivo')

######################################## ALPHA #######################################

#### INSTANCIA 1 #######
geometric = ["alpha_0.85(base)", "alpha_0.75", "alpha_0.99"]
geometric_filename_chr12a = ["result_sa/chr12a_base_SA", "result_sa/chr12a_geometric_75_SA", "result_sa/chr12a_geometric_99_SA"]

geometric_times, geometric_bests = unify_data(geometric, geometric_filename_chr12a, 30, 0)


##### PLOT TIME #######

graph_scatterplot(geometric_times, "plots_sa/chr12a_geometric_time_boxplot.jpg", "Resultados variando alpha para enfriamiento instancia: chr12a", 'Tiempo')

##### PLOT OBJECTIVE VALUE #####

graph_boxplot(geometric_bests, "plots_sa/chr12a_geometric_obj_value_boxplot.jpg", "Resultados variando alpha para enfriamiento instancia: chr12a", 'Valor objetivo')


#### INSTANCIA 2 #######

geometric_filename_esc64a = ["result_sa/esc64a_base_SA", "result_sa/esc64a_geometric_75_SA", "result_sa/esc64a_geometric_99_SA"]

geometric_times, geometric_bests = unify_data(geometric, geometric_filename_esc64a, 30, 0)


##### PLOT TIME #######

graph_scatterplot(geometric_times, "plots_sa/esc64a_geometric_time_boxplot.jpg", "Resultados variando alpha para enfriamiento instancia: esc64a", 'Tiempo')

##### PLOT OBJECTIVE VALUE #####

graph_boxplot(geometric_bests, "plots_sa/esc64a_geometric_obj_value_boxplot.jpg", "Resultados variando alpha para enfriamiento instancia: esc64a", 'Valor objetivo')

#### INSTANCIA 3 #######
geometric_filename_kra32 = ["result_sa/kra32_base_SA", "result_sa/kra32_geometric_75_SA", "result_sa/kra32_geometric_99_SA"]

geometric_times, geometric_bests = unify_data(geometric, geometric_filename_kra32, 30, 0)


##### PLOT TIME #######

graph_scatterplot(geometric_times, "plots_sa/kra32_geometric_time_boxplot.jpg", "Resultados variando alpha para enfriamiento instancia: kra32", 'Tiempo')

##### PLOT OBJECTIVE VALUE #####

graph_boxplot(geometric_bests, "plots_sa/kra32_geometric_obj_value_boxplot.jpg", "Resultados variando alpha para enfriamiento instancia: kra32", 'Valor objetivo')

#################### ITERATION #########################

############ INSTANCIA 1 ##################
iteration = ["25 iter.(base)", "50 iter.", "10 iter."]
iteration_filename_chr12a = ["result_sa/chr12a_base_SA", "result_sa/chr12a_iterations_50_SA", "result_sa/chr12a_iterations_10_SA"]

iteration_times, iteration_bests = unify_data(iteration, iteration_filename_chr12a, 30, 0)


##### PLOT TIME #######

graph_scatterplot(iteration_times, "plots_sa/chr12a_iteration_time_boxplot.jpg", "Resultados variando cant. de iteraciones instancia: chr12a", 'Tiempo')

##### PLOT OBJECTIVE VALUE #####

graph_boxplot(iteration_bests, "plots_sa/chr12a_iteration_obj_value_boxplot.jpg", "Resultados variando cant. de iteraciones instancia: chr12a", 'Valor objetivo')

############ INSTANCIA 2 ##################
iteration = ["25 iter.(base)", "50 iter.", "10 iter."]
iteration_filename_esc64a = ["result_sa/esc64a_base_SA", "result_sa/esc64a_iterations_50_SA", "result_sa/esc64a_iterations_10_SA"]

iteration_times, iteration_bests = unify_data(iteration, iteration_filename_esc64a, 30, 0)


##### PLOT TIME #######

graph_scatterplot(iteration_times, "plots_sa/esc64a_iteration_time_boxplot.jpg", "Resultados variando cant. de iteraciones instancia: esc64a", 'Tiempo')

##### PLOT OBJECTIVE VALUE #####

graph_boxplot(iteration_bests, "plots_sa/esc64a_iteration_obj_value_boxplot.jpg", "Resultados variando cant. de iteraciones instancia: esc64a", 'Valor objetivo')

############ INSTANCIA 3 ##################
iteration = ["25 iter.(base)", "50 iter.", "10 iter."]
iteration_filename_kra32 = ["result_sa/kra32_base_SA", "result_sa/kra32_iterations_50_SA", "result_sa/kra32_iterations_10_SA"]

iteration_times, iteration_bests = unify_data(iteration, iteration_filename_kra32, 30, 0)


##### PLOT TIME #######

graph_scatterplot(iteration_times, "plots_sa/kra32_iteration_time_boxplot.jpg", "Resultados variando cant. de iteraciones instancia: kra32", 'Tiempo')

##### PLOT OBJECTIVE VALUE #####

graph_boxplot(iteration_bests, "plots_sa/kra32_iteration_obj_value_boxplot.jpg", "Resultados variando cant. de iteraciones instancia: kra32", 'Valor objetivo')



""""""""""""""""""""" BESTS COMPARATIONS """""""""""""""""""""

###### INSTANCIA 1 #######
algorithm = ["SA", "GA"]
filename_bests_chr12a = ["result_best/chr12a_best_sa","result_best/chr12a_best_ga"]
times, bests = unify_data(algorithm, filename_bests_chr12a, 30, 1)
graph_scatterplot(times, "plots_best/chr12a_best_time_boxplot.jpg", "Tiempos obtenidos por ambas metaheuristicas Instancia: chr12a", 'Tiempo')
graph_boxplot(bests, "plots_best/chr12a_best_obj_value_boxplot.jpg", "Valores objetivos obtenidos por ambas metaheuristicas Instancia: chr12a", 'Valor objetivo')

a = times.groupby('Parámetro').describe()
#print(a)
b = bests.groupby('Parámetro').describe()
#print(b)

filename_bests_chr12a = ["result_best/esc64a_best_sa","result_best/esc64a_best_ga"]
times, bests = unify_data(algorithm, filename_bests_chr12a, 30, 1)
graph_scatterplot(times, "plots_best/esc64_best_time_boxplot.jpg", "Tiempos obtenidos por ambas metaheuristicas Instancia: esc64", 'Tiempo')
graph_boxplot(bests, "plots_best/esc64_best_obj_value_boxplot.jpg", "Valores objetivos obtenidos por ambas metaheuristicas Instancia: esc64", 'Valor objetivo')

a = times.groupby('Parámetro').describe()
#print(a)
b = bests.groupby('Parámetro').describe()
#print(b)

filename_bests_chr12a = ["result_best/kra32_best_sa","result_best/kra32_best_ga"]
times, bests = unify_data(algorithm, filename_bests_chr12a, 30, 1)
graph_scatterplot(times, "plots_best/kra32_best_time_boxplot.jpg", "Tiempos obtenidos por ambas metaheuristicas Instancia: kra32", 'Tiempo')
graph_boxplot(bests, "plots_best/kra32_best_obj_value_boxplot.jpg", "Valores objetivos obtenidos por ambas metaheuristicas Instancia: kra32", 'Valor objetivo')

a = times.groupby('Parámetro').describe()
print(a)
b = bests.groupby('Parámetro').describe()
print(b)
""""""""""""""""""""""" GA RESULTS """""""""""""""""""""""""""

""""""""""""""""""" GENERATIONS """""""""""""""""""

generation = ["20 gen.(base)", "10 gen.", "40 gen."]
###### INSTANCIA 1 #######
filename_generation_chr12a = ["result_ga/chr12a_base_ga", "result_ga/chr12a_generations_10_ga", "result_ga/chr12a_generations_40_ga"]
generation_times, generation_bests = unify_data(generation, filename_generation_chr12a, 30, 1)
graph_scatterplot(generation_times, "plots_ga/chr12a_generation_time_boxplot.jpg", "Resultados variando cant. de generaciones instancia: chr12a", 'Tiempo')
graph_boxplot(generation_bests, "plots_ga/chr12a_generation_obj_value_boxplot.jpg", "Resultados variando cant. de generaciones instancia: chr12a", 'Valor objetivo')
###### INSTANCIA 2 #######
filename_generation_esc64 = ["result_ga/esc64_base_ga", "result_ga/esc64_generations_10_ga", "result_ga/esc64_generations_40_ga"]
generation_times, generation_bests = unify_data(generation, filename_generation_esc64, 30, 1)
graph_scatterplot(generation_times, "plots_ga/esc64_generation_time_boxplot.jpg", "Resultados variando cant. de generaciones instancia: esc64", 'Tiempo')
graph_boxplot(generation_bests, "plots_ga/esc64_generation_obj_value_boxplot.jpg", "Resultados variando cant. de generaciones instancia: esc64", 'Valor objetivo')
###### INSTANCIA 3 #######
filename_generation_kra32 = ["result_ga/kra32_base_ga", "result_ga/kra32_generations_10_ga", "result_ga/kra32_generations_40_ga"]
generation_times, generation_bests = unify_data(generation, filename_generation_kra32, 30, 1)
graph_scatterplot(generation_times, "plots_ga/kra32_generation_time_boxplot.jpg", "Resultados variando cant. de generaciones instancia: kra32", 'Tiempo')
graph_boxplot(generation_bests, "plots_ga/kra32_generation_obj_value_boxplot.jpg", "Resultados variando cant. de generaciones instancia: kra32", 'Valor objetivo')

""""""""""""""""""" POPULATION """""""""""""""""""""

population = ["50 (base)", "30", "100"]
########## INSTANCIA 1 ###########
filename_population_chr12a = ["result_ga/chr12a_base_ga", "result_ga/chr12a_population_30_ga", "result_ga/chr12a_population_100_ga"]
population_times, population_bests = unify_data(population, filename_population_chr12a, 30, 1)
graph_scatterplot(population_times, "plots_ga/chr12a_population_time_boxplot.jpg", "Resultados variando tamaño de población instancia: chr12a", 'Tiempo')
graph_boxplot(population_bests, "plots_ga/chr12a_population_obj_value_boxplot.jpg", "Resultados variando tamaño de población instancia: chr12a", 'Valor objetivo')
###### INSTANCIA 2 #######
filename_population_esc64 = ["result_ga/esc64_base_ga", "result_ga/esc64_population_30_ga", "result_ga/esc64_population_100_ga"]
population_times, population_bests = unify_data(population, filename_population_esc64, 30, 1)
graph_scatterplot(population_times, "plots_ga/esc64_population_time_boxplot.jpg", "Resultados variando tamaño de población instancia: esc64", 'Tiempo')
graph_boxplot(population_bests, "plots_ga/esc64_population_obj_value_boxplot.jpg", "Resultados variando tamaño de población instancia: esc64", 'Valor objetivo')
###### INSTANCIA 3 #######
filename_population_kra32 = ["result_ga/kra32_base_ga", "result_ga/kra32_population_30_ga", "result_ga/kra32_population_100_ga"]
population_times, population_bests = unify_data(population, filename_population_kra32, 30, 1)
graph_scatterplot(population_times, "plots_ga/kra32_population_time_boxplot.jpg", "Resultados variando tamaño de población instancia: kra32", 'Tiempo')
graph_boxplot(population_bests, "plots_ga/kra32_population_obj_value_boxplot.jpg", "Resultados variando tamaño de población instancia: kra32", 'Valor objetivo')

""""""""""""""""""" MUTATION """""""""""""""""""""""""
########## INSTANCIA 1 ###########
mutation = ["20% (base)", "10%", "50%"]
filename_mutation_chr12a = ["result_ga/chr12a_base_ga", "result_ga/chr12a_mutation_01_ga", "result_ga/chr12a_mutation_05_ga"]
mutation_times, mutation_bests = unify_data(mutation, filename_mutation_chr12a, 30, 1)
graph_boxplot(mutation_times, "plots_ga/chr12a_mutation_time_boxplot.jpg", "Resultados variando probabilidad de mutación instancia: chr12a", 'Tiempo')
graph_boxplot(mutation_bests, "plots_ga/chr12a_mutation_obj_value_boxplot.jpg", "Resultados variando probabilidad de mutación instancia: chr12a", 'Valor objetivo')
###### INSTANCIA 2 #######
filename_mutation_esc64 = ["result_ga/esc64_base_ga", "result_ga/esc64_mutation_01_ga", "result_ga/esc64_mutation_05_ga"]
mutation_times, mutation_bests = unify_data(mutation, filename_mutation_esc64, 30, 1)
graph_boxplot(mutation_times, "plots_ga/esc64_mutation_time_boxplot.jpg", "Resultados variando probabilidad de mutación instancia: esc64", 'Tiempo')
graph_boxplot(mutation_bests, "plots_ga/esc64_mutation_obj_value_boxplot.jpg", "Resultados variando probabilidad de mutación instancia: esc64", 'Valor objetivo')
###### INSTANCIA 3 #######
filename_mutation_kra32 = ["result_ga/kra32_base_ga", "result_ga/kra32_mutation_01_ga", "result_ga/kra32_mutation_05_ga"]
mutation_times, mutation_bests = unify_data(mutation, filename_mutation_kra32, 30, 1)
graph_boxplot(mutation_times, "plots_ga/kra32_mutation_time_boxplot.jpg", "Resultados variando probabilidad de mutación instancia: kra32", 'Tiempo')
graph_boxplot(mutation_bests, "plots_ga/kra32_mutation_obj_value_boxplot.jpg", "Resultados variando probabilidad de mutación instancia: kra32", 'Valor objetivo')
