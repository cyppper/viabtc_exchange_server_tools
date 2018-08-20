class balance:
    @staticmethod
    def query(user_id):
        return {
            "method": "balance.query",
            "params": [user_id],
            "jsonrpc": "2.0",
            "id": 0,
        }

    @staticmethod
    def update(user_id, coin, change, timestamp, business):
        return {
            "method": "balance.update",
            "params": [user_id, coin, business, timestamp, change, {}],
            "jsonrpc": "2.0",
            "id": 0,
        }

    @staticmethod
    def history(user_id, coin, business, start_time, end_time, offset, limit):
        return {
            "method": "balance.history",
            "params": [user_id, coin, business, start_time, end_time, offset, limit],
            "jsonrpc": "2.0",
            "id": 0,
        }


class order:
    @staticmethod
    def put_limit(user_id, market, side, amount, price, taker_fee_rate, maker_fee_rate, source):
        return {
            "method": "order.put_limit",
            "params": [user_id, market, side, amount, price, taker_fee_rate, maker_fee_rate, source],
            "jsonrpc": "2.0",
            "id": 0,
        }

    @staticmethod
    def put_market(user_id, market, side, amount, taker_fee_rate, source):
        return {
            "method": "order.put_market",
            "params": [user_id, market, side, amount, taker_fee_rate, source],
            "jsonrpc": "2.0",
            "id": 0,
        }

    @staticmethod
    def cancel(user_id, market, order_id):
        return {
            "method": "order.cancel",
            "params": [user_id, market, order_id],
            "jsonrpc": "2.0",
            "id": 0,
        }

    @staticmethod
    def deals(order_id, offset, limit):
        return {
            "method": "order.deals",
            "params": [order_id, offset, limit],
            "jsonrpc": "2.0",
            "id": 0,
        }

    @staticmethod
    def book(market, side, offset, limit):
        return {
            "method": "order.book",
            "params": [market, side, offset, limit],
            "jsonrpc": "2.0",
            "id": 0,
        }

    @staticmethod
    def depth(market, limit, interval):
        return {
            "method": "order.depth",
            "params": [market, limit, interval],
            "jsonrpc": "2.0",
            "id": 0,
        }

    @staticmethod
    def pending(user_id, market, offset, limit):
        return {
            "method": "order.pending",
            "params": [user_id, market, offset, limit],
            "jsonrpc": "2.0",
            "id": 0,
        }

    @staticmethod
    def pending_detail(market, order_id):
        return {
            "method": "order.pending_detail",
            "params": [market, order_id],
            "jsonrpc": "2.0",
            "id": 0,
        }

    @staticmethod
    def finished(user_id, market, start_time, end_time, offset, limit, side):
        return {
            "method": "order.finished",
            "params": [user_id, market, start_time, end_time, offset, limit, side],
            "jsonrpc": "2.0",
            "id": 0,
        }

    @staticmethod
    def finished_detail(order_id):
        return {
            "method": "order.finished_detail",
            "params": [order_id],
            "jsonrpc": "2.0",
            "id": 0,
        }


class market:
    @staticmethod
    def last(market):
        return {
            "method": "market.last",
            "params": [market],
            "jsonrpc": "2.0",
            "id": 0,
        }

    @staticmethod
    def deals(market, limit, last_id):
        return {
            "method": "market.deals",
            "params": [market, limit, last_id],
            "jsonrpc": "2.0",
            "id": 0,
        }

    @staticmethod
    def user_deals(user_id, market, offset, limit):
        return {
            "method": "market.user_deals",
            "params": [user_id, market, offset, limit],
            "jsonrpc": "2.0",
            "id": 0,
        }

    @staticmethod
    def kline(market, start_time, end_time, interval):
        return {
            "method": "market.kline",
            "params": [market, start_time, end_time, interval],
            "jsonrpc": "2.0",
            "id": 0,
        }

    @staticmethod
    def status(market, period):
        return {
            "method": "market.status",
            "params": [market, period],
            "jsonrpc": "2.0",
            "id": 0,
        }

    @staticmethod
    def status_today(market):
        return {
            "method": "market.status_today",
            "params": [market],
            "jsonrpc": "2.0",
            "id": 0,
        }
