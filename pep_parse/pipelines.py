import datetime as dt
from collections import defaultdict

from .settings import DATETIME_FORMAT, BASE_DIR, RESULT_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.d = defaultdict(int)

    def process_item(self, item, spider):
        self.d[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULT_DIR
        now = dt.datetime.now()
        now_format = now.strftime(DATETIME_FORMAT)
        filename = f'status_summary_{now_format}.csv'
        file_path = results_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            total = sum(self.d.value())
            f.write(f'Total,{total}\n')
