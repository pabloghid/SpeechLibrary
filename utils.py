## SORTS
""" 
    'editions': 'edition_count desc',
    'old': 'def(first_publish_year, 9999) asc',
    'new': 'first_publish_year desc',
    'title': 'title_sort asc',
    'scans': 'ia_count desc',
    # Classifications
    'lcc_sort': 'lcc_sort asc',
    'lcc_sort asc': 'lcc_sort asc',
    'lcc_sort desc': 'lcc_sort desc',
    'ddc_sort': 'ddc_sort asc',
    'ddc_sort asc': 'ddc_sort asc',
    'ddc_sort desc': 'ddc_sort desc',
    # Random
    'random': 'random_1 asc',
    'random asc': 'random_1 asc',
    'random desc': 'random_1 desc',
    'random.hourly': lambda: f'random_{datetime.now():%Y%m%dT%H} asc',
    'random.daily': lambda: f'random_{datetime.now():%Y%m%d} asc', 
 """