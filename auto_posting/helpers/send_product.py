import telegram
from emoji import emojize


def send_product(pro_obj):
    token = '604717105:AAGTQje5wWDWXlaJGHy-uylS4WtANe19CjQ'
    chat_id = '@online_shop_saeed'

    bot = telegram.Bot(token=token)
    message = emojize(":heavy_check_mark: {}\n:point_right: {}\n:dollar: {}\n:clock4: {}\n".format(
        pro_obj.name,
        pro_obj.category,
        pro_obj.price,
        pro_obj.publish_date
    ), use_aliases=True)

    status = bot.send_photo(chat_id=chat_id,
                            photo=open(pro_obj.image.path, 'rb'),
                            caption=message,
                            parse_mode=telegram.ParseMode.HTML)
    return status