import random
from copy import copy
import base_class
import character


class ClubAttr(object):
    """俱乐部类型所具有的属性;
    用于修改俱乐部类型实例的属性时引用"""
    NAME = "name"
    CITY = "city"
    COACH = "coach"
    HONOUR = "honour"
    PLAYERS = "players"
    BIRTHDAY = "birthday"
    FOOTBALL_COURT = "football_court"
    LEAGUE_MATCHES = "league_matches"


class Club(base_class.BaseClub):
    """ 俱乐部类

    Used:
        description = {
            "city": "曼彻斯特",
            "coach": Coach("朗尼克", location="主教练"),
            "honour": {"英超冠军杯": "5"},
            "players": [Players("克里斯蒂亚诺·罗纳尔多", location="前锋"), Players("德赫亚", location="守门员")],
            "birthday": "1878",
            "football_court": "老特拉福德球场",
            "league_matches": "英超",
        }
        # 创建对象
        club = Club("曼彻斯特联", **description)
        # 增加球员
        club.add_players(Players("杰登·桑乔", location="中场"))
        # 移除球员
        club.remove_players(by=PlayersAttr.CH_NAME, value="杰登·桑乔")
    """

    def __init__(self, name: str, **kwargs):
        """
        :param name: 俱乐部名称
        :param kwargs: 俱乐部属性集合
        """
        self.__name = name
        self.__descript = kwargs.copy()

    def __str__(self):
        return "<{}({}), {}>".format(
            self.__class__.__name__, self.__name, self.players
        )

    def __repr__(self):
        return "<{}({}), {}>".format(
            self.__class__.__name__, self.__name, self.players
        )

    def __iter__(self):
        return ((k, v) for k, v in self.description().items())

    def __len__(self):
        return len(self.__name)

    def __bool__(self):
        return bool(self.__name)

    @property
    def locations(self):
        """返回球员各个位置的精确名称"""
        return {
            "后卫": ['左后卫', '后卫', '右后卫'],
            "中场": ['中场', '前腰', '中卫', '后腰', '中前卫'],
            "前锋": ['前锋', '中锋', '左边锋', '右边锋'],
            "守门员": ['守门员']
        }

    @property
    def name(self) -> str:
        """返回俱乐部名称"""
        return self.__name

    @property
    def city(self) -> str:
        """返回俱乐部所在城市"""
        return self.__descript.get(ClubAttr.CITY, str())

    @property
    def birthday(self) -> str:
        """返回俱乐部成立日期"""
        return self.__descript.get(ClubAttr.BIRTHDAY, str())

    @property
    def football_court(self) -> str:
        """返回俱乐部所属球场"""
        return self.__descript.get(ClubAttr.FOOTBALL_COURT, str())

    @property
    def league_matches(self) -> str:
        """返回俱乐部所在联赛"""
        return self.__descript.get(ClubAttr.LEAGUE_MATCHES, str())

    @property
    def honour(self) -> dict:
        """返回俱乐部取得的所有荣誉"""
        return self.__descript.get(ClubAttr.HONOUR, dict())

    @property
    def coach(self) -> character.Coach:
        """返回俱乐部现任主教练"""
        return self.__descript.get(ClubAttr.COACH, character.Coach('', ''))

    @property
    def players(self) -> list:
        """返回俱乐部目前有所的球员"""
        return self.__descript.get(ClubAttr.PLAYERS, list())

    def modify(self, by=ClubAttr.NAME, value=None):
        """根据传入的属性名称来修改对应的属性值"""
        if by not in ClubAttr.__dict__.values():
            raise ValueError(
                f"{self.__class__.__name__} object not attribute: '{by}'"
            )
        self.__descript[by] = value

    def description(self) -> dict:
        """返回俱乐部的所有属性信息"""
        desc = dict()
        attributes = [value for key, value in ClubAttr.__dict__.items()
                      if isinstance(key, str) and key.isupper()]
        for name in attributes:
            desc[name] = copy(self.__descript.get(name))
        desc["name"] = self.__name
        return desc

    def add_players(self, players: character.Players):
        """增加单个球员; 球员类型必须为Players"""
        if not isinstance(players, character.Players):
            raise ValueError(f"Parameter is not of type Players")
        self.__descript.get(ClubAttr.PLAYERS, list()).append(players)

    def remove_players(self, by=character.PlayersAttr.CH_NAME, value=None):
        """移除单个球员; 根据球员的某一个属性进行判断,移除第一个匹配到的球员"""
        self_players = self.__descript.get(ClubAttr.PLAYERS)
        if not self_players:
            return False
        if isinstance(self_players, character.Players):
            if eval(f"self_players.{by}") == value:
                self.__descript[ClubAttr.PLAYERS] = list()
                return True
        for players in self.__descript.get(ClubAttr.PLAYERS):
            if eval(f"players.{by}") == value:
                self.__descript.get(ClubAttr.PLAYERS).remove(players)
                return True
        return False

    def query_players(self, by=character.PlayersAttr.CH_NAME, value=None):
        """查询球员; 根据球员的某一个属性进行判断,返回第一个匹配到的球员"""
        self_players = self.__descript.get(ClubAttr.PLAYERS)
        if not self_players:
            return None
        if isinstance(self_players, character.Players):
            if eval(f"self_players.{by}") == value:
                return self_players
        for players in self.__descript.get(ClubAttr.PLAYERS):
            if eval(f"players.{by}") == value:
                return players

    def starting_lineup(self, guard=4, midfield=4, forward=2):
        """返回11位首发球员; 如果当前俱乐部存的所有球员不足11位则抛出异常
        球员阵型:
            "442": 4 后卫, 4 中场, 2 前锋
            "451": 4 后卫, 5 中场, 1 前锋
            "433": 4 后卫, 3 中场, 3 前锋
            ...
        如果当前俱乐部球员不够以固定位置安排阵型时,则会随机使用其他位置球员进行占位
        :param guard: 后卫球员人数
        :param midfield: 中场球员人数
        :param forward: 前锋球员人数
        :return: list
        """
        if sum([guard, midfield, forward]) != 10:
            raise ValueError(
                "The parameter value is unreasonable. The total number should be 10"
            )
        if len(self.players) < 11:
            raise AttributeError("The current number of players is less than 11")
        return self._get_starting_lineup(guard, midfield, forward)

    def get_players_by_location(self, location: list, quantity=1):
        """根据location中的球员位置返回指定数量的球员
        如果筛选出的球员不够指定数量时会抛出AttributeError

        Used:
            location = Club().locations['前锋']
            Club().get_players_by_location(location, quantity=2)

        :param location: 球员位置
        :param quantity: 球员数量
        :return: list
        """
        select = self._get_location_players(location, quantity)
        if len(select) < quantity:
            raise AttributeError(f"currently club less than {quantity} players")
        return select

    def _get_location_players(self, location: list, quantity: int):
        total_players = self.players
        if not total_players:
            return list()
        random.shuffle(total_players)
        filter_ = list()
        for players in total_players:
            if len(filter_) >= quantity:
                break
            if players.location in location:
                filter_.append(copy(players))
        return filter_

    def _get_starting_lineup(self, guard: int, midfield: int, forward: int):
        filter_, lack = list(), 0
        for locations, quantity in zip(self.locations.values(), [guard, midfield, forward, 1]):
            select = self._get_location_players(locations, quantity)
            if len(select) < quantity:
                lack += (quantity - len(select))
            filter_.extend(select)
        if lack == 0:
            return filter_
        for p in self.players:
            if lack == 0:
                break
            if p not in filter_:
                filter_.append(p)
                lack -= 1
        return filter_

    def get_random_lineup(self):
        """返回11位任意位置的球员"""
        if not self.players:
            return None
        random.shuffle(self.players)
        players_list = list()
        for players in self.players:
            if len(players_list) >= 11:
                break
            if players not in players_list:
                players_list.append(copy(players))
        return players_list


if __name__ == '__main__':
    from basedata import PLAYERS_DATABASE, COACH_DATABASE
    import pprint

    manchester_united = [
        '万·比萨卡', '克里斯蒂亚诺·罗纳尔多', '博格巴', '卡瓦尼', '卢克·肖', '布鲁诺·费尔南德斯', '弗雷德', '拉什福德', '拜利', '杰登·桑乔',
        '林德洛夫', '格林伍德', '特莱斯', '瓦拉内', '范德贝克', '达洛特', '马夏尔', '马奎尔', '马蒂奇', '麦克托米奈', '林加德', '德赫亚']

    description = {
        "city": "曼彻斯特",
        "coach": character.Coach("朗尼克", **COACH_DATABASE.get("朗尼克")),
        "honour": {"英超冠军杯": "5"},
        "players": [character.Players(players, **PLAYERS_DATABASE.get(players)) for players in manchester_united],
        "birthday": "1895",
        "football_court": "老特拉福德球场",
        "league_matches": "英超",
    }
    club = Club("曼彻斯特联", **description)
    pprint.pprint(club.starting_lineup())


