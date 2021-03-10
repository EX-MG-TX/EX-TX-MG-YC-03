from BiliClient import asyncbili
from .push_message_task import webhook
from .import_once import get_ids
import logging
import random

async def watch_task(biliapi: asyncbili) -> None:
	nub = random.randint(0,3);
    try:
        ret = await get_ids(biliapi)
    except Exception as e:
        logging.warning(f'{biliapi.name}: 获取B站分区视频信息异常，原因为{str(e)}，跳过模拟视频观看')
        webhook.addMsg('msg_simple', f'{biliapi.name}:模拟视频观看失败\n')
        return

    if ret["code"]:
        logging.warning(f'{biliapi.name}: 获取B站分区视频信息异常，原因为{ids["message"]}，跳过视频观看')
        webhook.addMsg('msg_simple', f'{biliapi.name}:模拟视频观看失败\n')
        return
    ids = [{"aid":"204516234","cid":"307178951"},{"aid":"756904275","cid":"304166415"},{"aid":"204502833","cid":"307178835"},{"aid":"459368214","cid":"299736533"}]
			
    try:
	ret = await biliapi.report(ids[nub]["aid"], ids[nub]["cid"], 300)
        if ret["code"] == 0:
            logging.info(f'{biliapi.name}: 成功模拟观看av号为{ids[nub]["aid"]}的视频')
        else:
            logging.warning(f'{biliapi.name}: 模拟观看av号为{ids[nub]["aid"]}的视频投币失败，原因为：{ret["message"]}')
            webhook.addMsg('msg_simple', f'{biliapi.name}:模拟视频观看失败\n')
    except Exception as e: 
        logging.warning(f'{biliapi.name}: 模拟视频观看异常，原因为{str(e)}')
        webhook.addMsg('msg_simple', f'{biliapi.name}:模拟视频观看失败\n')
