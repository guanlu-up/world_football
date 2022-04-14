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
        return f"{self.__class__.__name__}({self.__name})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name})"

    def __iter__(self):
        return ((k, v) for k, v in self.description().items())

    def __len__(self):
        return len(self.__name)

    def __bool__(self):
        return bool(self.__name)

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


if __name__ == '__main__':
    from basedata import PLAYERS_DATABASE, COACH_DATABASE
    import pprint
    manchester_united = [
        '万·比萨卡', '克里斯蒂亚诺·罗纳尔多', '博格巴', '卡瓦尼', '卢克·肖', '布鲁诺·费尔南德斯', '弗雷德', '拉什福德', '拜利', '杰登·桑乔',
        '林德洛夫', '格林伍德', '特莱斯', '瓦拉内', '范德贝克', '达洛特', '马夏尔', '马奎尔', '马蒂奇', '麦克托米奈', '林加德']

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
    pprint.pprint(club.description())
