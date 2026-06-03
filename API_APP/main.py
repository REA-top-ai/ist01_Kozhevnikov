# import pprint
# from api_proxy.api_methods import get_everything
# from analytics.article_analytic import top_50_filtered_news
from api_ai import past_day_digest


if __name__ == '__main__':
    # Задание на API methods для News API
    # result = get_everything(q="apple",
    # api_key="c3727352bd3d4fb3b8ebae7b1e1e3d64", language="ru")

    # Задание на аналитику статей
    # result1 = top_50_filtered_news(q="apple",
    #                                api_key="c3727352bd3d4fb3b8ebae7b1e1e3d64")
    # pprint.pprint(result1)

    # Задание на AI Client(краткая выжимка из статей за вчерашний день)
    api_key_news = "c3727352bd3d4fb3b8ebae7b1e1e3d64"
    api_key_mistral = "VIXGyHEpjaSF4JhywuyW4OlKvszdsCEV"
    topic = 'xiaomi'
    report = past_day_digest(api_key_news, api_key_mistral, topic)

    # Сделал несколько проб файлов и с title, и с description
    # По title как по мне получаются намного лучше
    with open("report2_title.txt", "w", encoding="utf-8") as f:
        f.write(report)