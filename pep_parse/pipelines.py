import datetime as dt
from pathlib import Path


BASE_DIR = Path(__file__).parent


class PepParsePipeline:
    results = {}

    def open_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        try:
            results_dir.mkdir(exist_ok=True)
        except PermissionError:
            raise PermissionError('Нет прав для создания папки.')

    def process_item(self, item, spider):
        if item['status'] not in self.results:
            self.results[item['status']] = 1
        else:
            self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        total = 0
        date = dt.datetime.now().replace(microsecond=0)
        date = str(date).replace(' ', '_').replace(':', '-')
        filename = f'status_summary_{date}.csv'
        file_path = BASE_DIR / 'results' / filename
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status in self.results:
                total += self.results[status]
                f.write(f'{status},{self.results[status]}\n')
            f.write(f'Total,{total}\n')
