import requests


def request_biz(webinar_id):
    headers = {"X-Token": "Skp0KguaoBylTRtgOTjrkbaRtgdair1faAtx_poSJQT0tgO6j"}
    url = f"https://online.bizon365.ru/api/v1/webinars/reports/getviewers?webinarId={str(webinar_id)}&skip=0&limit=100"
    response = requests.get(url, headers=headers)
    return response