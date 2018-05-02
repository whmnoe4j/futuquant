#引用futuquant包
import futuquant as ft
import numpy as np
import pandas as pd
import time
#防止输出过程中由于数据太多出现省略号,忽略数据
from futuquant.quote.response_handler import *
from futuquant.common.constant import *
#设置dataframe结构的显示------pandas display设置
pd.set_option('display.height',1000)
pd.set_option('display.max_rows',None)#pandas.set_option() 可以设置pandas相关的参数，从而改变默认参数。 打印pandas数据事，默认是输出100行，多的话会输出....省略号。
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
pd.set_option('colheader_justify', 'right')#value显示居右

from time import sleep
from futuquant import *

class StockQuoteTest(StockQuoteHandlerBase):
    """
    获得报价推送数据
    """

    def on_recv_rsp(self, rsp_str):
        """数据响应回调函数"""
        ret_code, content = super(StockQuoteTest, self).on_recv_rsp(rsp_str)
        if ret_code != RET_OK:
            logger.debug("StockQuoteTest: error, msg: %s" % content)
            return RET_ERROR, content
        logger.debug("StockQuoteTest", content)
        return RET_OK, content

class HeartBeatTest(HeartBeatHandlerBase):
    """
    心跳的推送
    """
    def on_recv_rsp(self, rsp_str):
        """数据响应回调函数"""
        ret_code, timestamp = super(HeartBeatTest, self).on_recv_rsp(rsp_str)
        if ret_code == RET_OK:
            print("heart beat server timestamp = ", timestamp)
        return ret_code, timestamp

if __name__ =="__main__":
    # 实例化行情上下文对象
    quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111, proto_fmt=ProtoFMT.Json)

    # 获取推送数据
    code_list = ['HK.00700', 'HK.02318']
    sub_type_list = [SubType.RT_DATA, SubType.BROKER]
    # print(quote_ctx.get_global_state())
    print(quote_ctx.subscribe(code_list, sub_type_list, push=True))
    # print(quote_ctx.get_stock_basicinfo(Market.HK, SecurityType.ETF))
    # print(quote_ctx.get_cur_kline(code_list[0], 10, SubType.K_DAY, AuType.QFQ))
    # print(quote_ctx.get_rt_data(code_list[0]))
    # print(quote_ctx.get_rt_ticker(code_list[0], 10))

    # print(quote_ctx.get_broker_queue(code_list[0]))
    # print(quote_ctx.get_order_book(code_list[0]))
    # print(quote_ctx.get_history_kline('HK.00700', start='2017-06-20', end='2017-06-22'))

    # print(quote_ctx.get_multi_points_history_kline(code_list, ['2017-06-20', '2017-06-22', '2017-06-23'], KL_FIELD.ALL, KLType.K_DAY, AuType.QFQ))
    # print(quote_ctx.get_autype_list("HK.00700"))

    # print(quote_ctx.get_trading_days(Market.HK, '2018-11-01', '2018-11-20'))
    # print(quote_ctx.get_suspension_info('SZ.300104', '2010-02-01', '2018-11-20'))

    # print(quote_ctx.get_market_snapshot('HK.21901'))
    # print(quote_ctx.get_market_snapshot(code_list))

    # print(quote_ctx.get_plate_list(Market.HK, Plate.ALL))
    # print(quote_ctx.get_plate_stock('HK.BK1001'))

    sleep(3)
    quote_ctx.close()