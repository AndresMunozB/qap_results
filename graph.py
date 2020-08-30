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

def make_dataframe(dict_1, dict_2, dict_3):
    data_1 = pd.DataFrame.from_dict(dict_1)
    data_2 = pd.DataFrame.from_dict(dict_2)
    data_3 = pd.DataFrame.from_dict(dict_3)
    return pd.concat([data_1, data_2, data_3])

def graph_boxplot(data, filename, title, evaluation_criteria):
    ax = sns.boxplot(x='Parámetro', y= evaluation_criteria, data= data)
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
    #plt.figure(figsize=(10,6))
    ax.figure.savefig(filename,
                    format='jpeg')
    
    plt.clf()
############## TEMPERATURA ###########################

#### INSTANCIA 1 ######
temperature = ["base", "temperature_x10", "temperature_x0.5"]
times_base, bests_base = get_times_and_best("result_sa/chr12a_base_SA", temperature[0], 30)
times_temperature_10, best_temperature_10_obj = get_times_and_best("result_sa/chr12a_temperature_10_SA", temperature[1], 30)
times_temperature_05, best_temperature_05_obj = get_times_and_best("result_sa/chr12a_temperature_05_SA", temperature[2], 30)

times_temperature = make_dataframe(times_base, times_temperature_10, times_temperature_05)
bests_temperature = make_dataframe(bests_base, best_temperature_10_obj, best_temperature_05_obj)


##### PLOT TIME #######

graph_scatterplot(times_temperature, "chr12a_temperature_time_boxplot.jpg", "Instancia: chr12a", 'Tiempo')

##### PLOT OBJECTIVE VALUE ######
graph_boxplot(bests_temperature, "chr12a_temperature_obj_value_boxplot.jpg", "Instancia: chr12a", 'Valor objetivo')


################ ALPHA ##################

geometric = ["alpha_0.85(base)", "alpha_0.75", "alpha_0.99"]
times_base_geo, bests_base_geo = get_times_and_best("result_sa/chr12a_base_SA", geometric[0], 30)

times_geometric_75, best_geometric_75_obj = get_times_and_best("result_sa/chr12a_geometric_75_SA", geometric[1], 30)
times_geometric_99, best_geometric_99_obj = get_times_and_best("result_sa/chr12a_geometric_99_SA", geometric[2], 30)

times_geometric = make_dataframe(times_base_geo, times_geometric_75, times_geometric_99)
bests_geometric = make_dataframe(bests_base_geo, best_geometric_75_obj, best_geometric_99_obj)


##### PLOT TIME #######

graph_scatterplot(times_geometric, "chr12a_geometric_time_boxplot.jpg", "Instancia: chr12a", 'Tiempo')

##### PLOT OBJECTIVE VALUE #####

graph_boxplot(bests_geometric, "chr12a_geometric_obj_value_boxplot.jpg", "Instancia: chr12a", 'Valor objetivo')


############## ITERATION ######################

iteration = ["25 iter.(base)", "50 iter.", "10 iter."]
times_base_it, bests_base_it = get_times_and_best("result_sa/chr12a_base_SA", iteration[0], 30)

times_iterations_50, best_iterations_50_obj = get_times_and_best("result_sa/chr12a_iterations_50_SA", iteration[1], 30)
times_iterations_10, best_iterations_10_obj = get_times_and_best("result_sa/chr12a_iterations_10_SA", iteration[2], 30)

times_iterations = make_dataframe(times_base_it, times_iterations_50, times_iterations_10)
bests_iterations = make_dataframe(bests_base_it, best_iterations_50_obj, best_iterations_10_obj)


##### PLOT TIME #######

graph_scatterplot(times_iterations, "chr12a_iterations_time_boxplot.jpg", "Instancia: chr12a", 'Tiempo')

##### PLOT OBJECTIVE VALUE #####

graph_boxplot(bests_iterations, "chr12a_iterations_obj_value_boxplot.jpg", "Instancia: chr12a", 'Valor objetivo')
