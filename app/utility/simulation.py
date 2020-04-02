import json

from app import config as config

"""
This module provides simulation functionality 
"""


def get_simulated_domain_data(domain=None):
    try:
        with open('~/projects/adversary/conf/simulation.json' ) as sims:
            world = json.load(sims)
            if domain:
                return next(item for item in world['domains'] if item['name'] == domain)
            return world['domains']
    except:
        return None