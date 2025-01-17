# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 16:03:33 2022

@author: minghuiw
"""
from pathlib import Path

from nni.experiment import Experiment

min_green = 7

search_space = {
    "min1H": {"_type": "randint", "_value": [min_green, 20]},
    "priority1H": {"_type": "randint", "_value": [2, 20]},
    "release1H": {"_type": "randint", "_value": [2, 20]},

    "min2H": {"_type": "randint", "_value": [0, 20]},
    "priority2H": {"_type": "randint", "_value": [2, 20]},
    "release2H": {"_type": "randint", "_value": [2, 20]},

    "min3H": {"_type": "randint", "_value": [min_green, 20]},
    "priority3H": {"_type": "randint", "_value": [2, 20]},
    "release3H": {"_type": "randint", "_value": [2, 20]},

    "min4H": {"_type": "randint", "_value": [0, 20]},
    "priority4H": {"_type": "randint", "_value": [2, 20]},
    "release4H": {"_type": "randint", "_value": [2, 20]},

    "weight1H": {"_type": "uniform", "_value": [0.1, 1]},
    "weight2H": {"_type": "uniform", "_value": [0.1, 1]},
    "weight3H": {"_type": "uniform", "_value": [0.1, 1]},
    "weight4H": {"_type": "uniform", "_value": [0.1, 1]},

    "min1G": {"_type": "randint", "_value": [min_green, 20]},
    "priority1G": {"_type": "randint", "_value": [2, 20]},
    "release1G": {"_type": "randint", "_value": [2, 20]},

    "min2G": {"_type": "randint", "_value": [0, 20]},
    "priority2G": {"_type": "randint", "_value": [2, 20]},
    "release2G": {"_type": "randint", "_value": [2, 20]},

    "min3G": {"_type": "randint", "_value": [min_green, 20]},
    "priority3G": {"_type": "randint", "_value": [2, 20]},
    "release3G": {"_type": "randint", "_value": [2, 20]},

    "min4G": {"_type": "randint", "_value": [0, 20]},
    "priority4G": {"_type": "randint", "_value": [2, 20]},
    "release4G": {"_type": "randint", "_value": [2, 20]},

    "weight1G": {"_type": "uniform", "_value": [0.1, 1]},
    "weight2G": {"_type": "uniform", "_value": [0.1, 1]},
    "weight3G": {"_type": "uniform", "_value": [0.1, 1]},
    "weight4G": {"_type": "uniform", "_value": [0.1, 1]},
}

experiment = Experiment('local')

experiment.config.trial_command = 'python optimizer.py'
experiment.config.trial_code_directory = '.'
experiment.config.search_space = search_space
experiment.config.tuner.name = 'GP'

experiment.config.tuner.class_args = {
    'optimize_mode': 'minimize',
    'utility': 'poi',
    'kappa': 5.0,
    'xi': 0.0,
    'nu': 2.5,
    'alpha': 1e-6,
    'cold_start_num': 20,
    'selection_num_warm_up': 100000,
    'selection_num_starting_points': 250
}
experiment.config.max_trial_number = 500
experiment.config.trial_concurrency = 1

experiment.run(8080)
