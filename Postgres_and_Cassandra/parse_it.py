# -*- coding: utf-8 -*-
import connections, search_grabber, group_grabber, users_in_groups_parcer


def parse_it():
    connections.create_tables()
    queries_list = ['не платят зарплату', 'работа вахтовым методом', 'увольнение', 'штрафы ГИБДД','продажа недвижимости',
                    'судебные приставы','купля продажа земельных участков','кредиты',
                    'материнский капитал', 'молодая семья','алименты','капитальный ремонт','очередь в детский сад']
    for query in queries_list:
        search_grabber.get_groups(query)
    group_grabber.write_to_cassandra_db()
    users_in_groups_parcer.parse_users_from_groups()

parse_it()