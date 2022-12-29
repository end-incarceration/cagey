from cagey.slick.pipeline import DBPipeline


class CageyPipeline(DBPipeline):
    def open_spider(self, spider, db_filename):
        super().open_spider(spider, db_filename)

    def close_spider(self, spider):
        super().close_spider(spider)
