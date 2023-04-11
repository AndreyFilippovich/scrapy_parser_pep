import datetime as dt

from .settings import DATETIME_FORMAT, BASE_DIR, RESULT_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.results = {}

    def process_item(self, item, spider):
        if item['status'] not in self.results:
            self.results[item['status']] = 1
        else:
            self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULT_DIR
        now = dt.datetime.now()
        now_format = now.strftime(DATETIME_FORMAT)
        filename = f'status_summary_{now_format}.csv'
        file_path = results_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            total = 0
            for key, value in self.results.items():
                total += value
                f.write(f'{key},{value}\n')
            f.write(f'Total,{total}\n')
