import datetime as dt
from pathlib import Path
import csv


BASE_DIR = Path(__file__).parent


class PepParsePipeline:
    """Класс pipeline для pep."""
    results = {}
    total = 0

    def open_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        try:
            results_dir.mkdir(exist_ok=True)
        except PermissionError:
            raise PermissionError('Нет прав для создания папки.')

    def process_item(self, item, spider):
        self.results[item['status']] = self.results.get(item['status'], 0) + 1
        self.total += 1
        return item

    def close_spider(self, spider):
        field_names = ['Статус', 'Количество']
        result = [
            {field_names[0]: status, field_names[1]: self.results[status]}
            for status in self.results
        ]
        result.append({field_names[0]: 'Total', field_names[1]: self.total})
        date = dt.datetime.now().replace(microsecond=0)
        date = str(date).replace(' ', '_').replace(':', '-')
        filename = f'status_summary_{date}.csv'
        file_path = BASE_DIR / 'results' / filename
        with open(file_path, mode='w', encoding='utf-8') as f:
            writer = csv.DictWriter(
                f, fieldnames=field_names, lineterminator='\n'
            )
            writer.writeheader()
            writer.writerows(result)
