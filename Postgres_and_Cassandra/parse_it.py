# -*- coding: utf-8 -*-
import connections, search_grabber, group_grabber, users_in_groups_parcer


def parse_it():
    connections.create_tables()
    queries_list = ['материнский капитал', 'штрафы гибдд', 'алименты',
                    'капитальный ремонт', 'кредит', 'алименты',
                    'не платят зарплату']
    for query in queries_list:
        search_grabber.get_groups(query)
    group_grabber.write_to_cassandra_db()
    users_in_groups_parcer.parse_users_from_groups()

parse_it()