
import matplotlib.pyplot as plt
import json

def save_sa_graph(objectives_list, best_objectives_list, probabilities_list, temperature_list, best_objective, elapsed_time,file_name):
    plt.figure(figsize=(10,8))
    plt.subplot(4, 1, 1)
    graficoMejores = plt.plot(best_objectives_list)
    plt.setp(graficoMejores,"linestyle","none","marker","s","color","b","markersize","1")
    plt.title(f"Simulated annealing QAP\nValor óptimo:{best_objective} - Tiempo:{elapsed_time:.2f} segundos") 
    plt.ylabel(u"Mejor valor")
    plt.grid(True)
    plt.subplot(4, 1, 2)
    grafico = plt.plot(objectives_list)
    plt.setp(grafico,"linestyle","none","marker","s","color","r","markersize","1")
    plt.ylabel(u"Valor actual")
    plt.grid(True)
    plt.subplot(4, 1, 3)
    grafico = plt.plot(temperature_list)
    plt.setp(grafico,"linestyle","none","marker","s","color","black","markersize","1")
    plt.ylabel(u"Temperatura")
    plt.grid(True)
    plt.subplot(4, 1, 4)
    grafico = plt.plot(probabilities_list)
    plt.setp(grafico,"linestyle","none","marker","s","color","g","markersize","1")
    plt.ylabel(u"Probabilidad")
    plt.xlabel(f"Iteraciones")
    plt.grid(True)
    plt.savefig(file_name)
    

def save_ga_graph(average_objectives_list, best_objective_list, best_objective, elapsed_time,file_name):
    plt.figure(figsize=(10,8))
    plt.subplot(2, 1, 1)
    graficoMejores = plt.plot(best_objective_list)
    plt.setp(graficoMejores,"linestyle","none","marker","s","color","b","markersize","1")
    plt.title(f"Evolutive Algorithm QAP\nValor óptimo:{best_objective} - Tiempo:{elapsed_time:.2f}") 
    plt.ylabel(u"Mejor valor")
    plt.grid(True)
    plt.subplot(2, 1, 2)
    grafico = plt.plot(average_objectives_list)
    plt.setp(grafico,"linestyle","none","marker","s","color","r","markersize","1")
    plt.ylabel(u"Valor promedio")
    plt.xlabel(f"Generaciones")
    plt.grid(True)
    plt.savefig(file_name)

def load_json(name_json):
    """ Load configuration from json file """
    data = {}
    with open(name_json + ".json", 'r') as file:
        data = json.load(file)
    return data




def save_plots(file_names, iterations):
    for i in range(len(file_names)):
        file_name = file_names[i]
        for j in range(1,iterations+1):
            num_iteration = str(j).zfill(3)
    
            #sa_data = load_json(f'result_new/result/{file_name}_sa_{num_iteration}')
            ga_data = load_json(f'result_new/result/{file_name}_ga_{num_iteration}')
            #save_sa_graph(sa_data['objective_list'],sa_data['best_objective_list'],sa_data['probabilities_list'],sa_data['temperature_list'],sa_data['best_objective'],sa_data['elapsed_time'],f'plot_best_iterations/{file_name}_sa_{num_iteration}.png')
            save_ga_graph(ga_data['average_objectives_list'],ga_data['best_objective_list'],ga_data['best_objective'],ga_data['elapsed_time'],f'plot_best_iterations_new/{file_name}_ga_{num_iteration}.png')
            print(i,j)

#file_names = ['chr12a_best', 'esc64a_best', 'kra32_best']
file_names = [ 'esc64a_best', 'kra32_best']

save_plots(file_names, 30)