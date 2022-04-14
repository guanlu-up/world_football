import abc


class BaseClub(abc.ABC):
    """抽象基类; 用于定义俱乐部类型"""

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """返回俱乐部名称"""

    @property
    @abc.abstractmethod
    def city(self) -> str:
        """返回俱乐部所在城市"""

    @property
    @abc.abstractmethod
    def birthday(self) -> str:
        """返回俱乐部成立日期"""

    @property
    @abc.abstractmethod
    def football_court(self) -> str:
        """返回俱乐部所属球场"""

    @property
    @abc.abstractmethod
    def league_matches(self) -> str:
        """返回俱乐部所在联赛"""

    @property
    @abc.abstractmethod
    def honour(self) -> dict:
        """返回俱乐部取得的所有荣誉"""

    @property
    @abc.abstractmethod
    def coach(self):
        """返回俱乐部现任主教练; 教练必须为...类型"""

    @property
    @abc.abstractmethod
    def players(self) -> list:
        """返回俱乐部目前有所的球员; 球员必须为...类型"""


class BasePlayer(abc.ABC):
    """抽象基类; 用于定义球员类型"""

    @property
    @abc.abstractmethod
    def ch_name(self) -> str:
        """返回球员中文名字"""

    @property
    @abc.abstractmethod
    def en_name(self) -> str:
        """返回球员英文名字"""

    @property
    @abc.abstractmethod
    def age(self) -> str:
        """返回球员年龄"""

    @property
    @abc.abstractmethod
    def birthday(self) -> str:
        """返回球员出生日期"""

    @property
    @abc.abstractmethod
    def height(self) -> str:
        """返回球员身高"""

    @property
    @abc.abstractmethod
    def nationality(self) -> str:
        """返回球员国籍"""

    @property
    @abc.abstractmethod
    def preferred_foot(self) -> int:
        """返回球员惯用脚; [左脚, 右脚, 左右脚]"""

    @property
    @abc.abstractmethod
    def worth(self) -> float:
        """返回球员身价; 万欧"""

    @property
    @abc.abstractmethod
    def team(self) -> str:
        """返回球员所在球队名称"""

    @property
    @abc.abstractmethod
    def number(self) -> str:
        """返回球员球衣所属号码"""

    @property
    @abc.abstractmethod
    def location(self) -> str:
        """返回球员所在球场位置; [守门员, 后卫, 中场, 前锋]"""

    @property
    @abc.abstractmethod
    def ability(self) -> dict:
        """返回球员能力分布"""

    @property
    @abc.abstractmethod
    def honour(self) -> dict:
        """返回球员个人荣誉"""


class BaseCoach(abc.ABC):
    """抽象基类; 用于定义教练类型"""

    @property
    @abc.abstractmethod
    def ch_name(self) -> str:
        """返回教练中文名字"""

    @property
    @abc.abstractmethod
    def en_name(self) -> str:
        """返回教练英文名字"""

    @property
    @abc.abstractmethod
    def age(self) -> str:
        """返回教练年龄"""

    @property
    @abc.abstractmethod
    def birthday(self) -> str:
        """返回教练出生日期"""

    @property
    @abc.abstractmethod
    def height(self) -> str:
        """返回教练身高"""

    @property
    @abc.abstractmethod
    def nationality(self) -> str:
        """返回教练国籍"""

    @property
    @abc.abstractmethod
    def team(self) -> str:
        """返回教练所在球队名称"""

    @property
    @abc.abstractmethod
    def location(self) -> str:
        """返回教练所在球场位置; [主教练, 助理教练]"""

    @property
    @abc.abstractmethod
    def honour(self) -> dict:
        """返回教练个人荣誉"""
