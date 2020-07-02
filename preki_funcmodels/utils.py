import os
from neomodel import db


def init_db(neo4j_user_key, neo4j_pass_key, neo4j_host_key, protocol='bolt', port=7687):
    NEO4J_USER = os.environ[neo4j_user_key]
    NEO4J_PASS = os.environ[neo4j_pass_key]
    NEO4J_HOST = os.environ[neo4j_host_key]
    db.set_connection(f'{protocol}://{NEO4J_USER}:{NEO4J_PASS}@{NEO4J_HOST}:{port}')
