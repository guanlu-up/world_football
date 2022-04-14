from copy import copy
import base_class


class PlayersAttr(object):
    """球员类型所具有的属性;
    用于修改球员类型实例的属性时引用"""
    CH_NAME = "ch_name"
    EN_NAME = "en_name"
    HONOUR = "honour"
    ABILITY = "ability"
    LOCATION = "location"
    NUMBER = "number"
    AGE = "age"
    TEAM = "team"
    WORTH = "worth"
    PREFERRED_FOOT = "preferred_foot"
    NATIONALITY = "nationality"
    HEIGHT = "height"
    BIRTHDAY = "birthday"


class CoachAttr(object):
    """教练类型所具有的属性;
    用于修改教练类型实例的属性时引用"""
    CH_NAME = "ch_name"
    EN_NAME = "en_name"
    HONOUR = "honour"
    LOCATION = "location"
    AGE = "age"
    TEAM = "team"
    NATIONALITY = "nationality"
    HEIGHT = "height"
    BIRTHDAY = "birthday"


class Players(base_class.BasePlayer):
    """ 球员类

    Used:
        description = {
                    "ability": {"优势": "远射/最后一击/争高空球/护球/持球能力/传球/关键传球/头球/带球",
                                "弱点": "防守贡献/规避越位",
                                "风格": "喜欢内切/喜欢射门前调整/间接任意球威胁/反击威胁点/喜欢短传/不喜欢倒地飞铲"},
                    "age": 37,
                    "birthday": "1985-02-05",
                    "en_name": "Cristiano Ronaldo dos Santos Aveiro",
                    "height": "187 cm",
                    "honour": {"欧洲杯冠军": "1次",
                               "欧洲联赛冠军杯赛冠军": "4次",
                               "欧洲超级杯冠军": "3次",
                               ...},
                    "location": "中锋",
                    "nationality": "葡萄牙",
                    "number": "7  ",
                    "preferred_foot": "右脚",
                    "team": "曼彻斯特联",
                    "worth": "3150万英镑"}
        # 创建对象
        p = Players('克里斯蒂亚诺·罗纳尔多', 'Cristiano Ronaldo', **description)
        # 输出球员中文名称
        p.ch_name
        # 修改球员年龄
        p.modify(by=PlayersAttr.AGE, value="37")
        # 与另一个球员对象比较是否一致
        p == Players('ch_name', 'en_name', **kwargs)
    """

    def __init__(self, ch_name: str, en_name='', **kwargs):
        """
        :param ch_name: 球员中文名称
        :param en_name: 球员英文名称
        :param kwargs: 球员所具属性集合
        """
        self.__ch_name = ch_name
        self.__en_name = en_name
        self.__descript = kwargs.copy()

    def __str__(self):
        return (f"{self.__class__.__name__}({self.__ch_name},"
                f"{self.__descript.get(PlayersAttr.LOCATION)})")

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.__ch_name},"
                f"{self.__descript.get(PlayersAttr.LOCATION)})")

    def __iter__(self):
        return ((k, v) for k, v in self.description().items())

    def __len__(self):
        return len(self.__ch_name)

    def __bool__(self):
        return bool(self.__ch_name)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.__descript != other.__descript:
            return False
        return self.__ch_name == other.__ch_name and self.__en_name == other.__en_name

    @property
    def honour(self) -> dict:
        """返回球员个人荣誉"""
        return self.__descript.get(PlayersAttr.HONOUR, dict())

    @property
    def ability(self) -> dict:
        """返回球员能力分布"""
        return self.__descript.get(PlayersAttr.ABILITY, dict())

    @property
    def location(self) -> str:
        """返回球员所在球场位置; [门将, 后卫, 中场, 前锋]"""
        return self.__descript.get(PlayersAttr.LOCATION, str())

    @property
    def number(self) -> str:
        """返回球员球衣所属号码"""
        return self.__descript.get(PlayersAttr.NUMBER, str())

    @property
    def team(self) -> str:
        """返回球员所在球队"""
        return self.__descript.get(PlayersAttr.TEAM, str())

    @property
    def worth(self) -> str:
        """返回球员身价; 万欧"""
        return self.__descript.get(PlayersAttr.WORTH, str())

    @property
    def preferred_foot(self) -> str:
        """返回球员惯用脚; [左脚, 右脚, 左右脚]"""
        return self.__descript.get(PlayersAttr.PREFERRED_FOOT, str())

    @property
    def nationality(self) -> str:
        """返回球员国籍"""
        return self.__descript.get(PlayersAttr.NATIONALITY, str())

    @property
    def height(self) -> str:
        """返回球员身高"""
        return self.__descript.get(PlayersAttr.HEIGHT, str())

    @property
    def birthday(self) -> str:
        """返回球员出生日期"""
        return self.__descript.get(PlayersAttr.BIRTHDAY, str())

    @property
    def en_name(self) -> str:
        """返回球员英文名字"""
        return self.__en_name

    @property
    def ch_name(self) -> str:
        """返回球员中文名字"""
        return self.__ch_name

    @property
    def age(self) -> int:
        """返回球员年龄"""
        return self.__descript.get(PlayersAttr.AGE, int())

    def modify(self, by=PlayersAttr.CH_NAME, value=None):
        """根据传入的属性名称来修改对应的属性值"""
        if by not in PlayersAttr.__dict__.values():
            raise ValueError(
                f"{self.__class__.__name__} object not attribute: '{by}'"
            )
        self.__descript[by] = value

    def description(self) -> dict:
        """返回球员的所有属性信息"""
        desc = dict()
        attributes = [value for key, value in PlayersAttr.__dict__.items()
                      if isinstance(key, str) and key.isupper()]
        for name in attributes:
            desc[name] = copy(self.__descript.get(name))
        desc["ch_name"] = self.__ch_name
        desc["en_name"] = self.__en_name
        return desc


class Coach(base_class.BaseCoach):
    """ 教练类

    Used:
        coach_desc = {
            "honour": {"德国甲级联赛冠军": "1"},
            "location": "主教练",
            "age": "64",
            "team": "曼彻斯特联",
            "nationality": "德国",
            "height": "177",
            "birthday": "1958-06-29",
        }
        # 创建对象
        nick = Coach("朗尼克", "Ralf Rang nick", **coach_desc)
    """

    def __init__(self, ch_name: str, en_name='', **kwargs):
        """
        :param ch_name: 教练中文名称
        :param en_name: 教练英文名称
        :param kwargs: 教练所具属性集合
        """
        self.__ch_name = ch_name
        self.__en_name = en_name
        self.__descript = kwargs.copy()

    def __str__(self):
        return (f"{self.__class__.__name__}({self.__ch_name},"
                f"{self.__descript.get(CoachAttr.LOCATION)})")

    def __repr__(self):
        return (f"{self.__class__.__name__}({self.__ch_name},"
                f"{self.__descript.get(CoachAttr.LOCATION)})")

    def __iter__(self):
        return ((k, v) for k, v in self.description().items())

    def __len__(self):
        return len(self.__ch_name)

    def __bool__(self):
        return bool(self.__ch_name)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.__descript != other.__descript:
            return False
        return self.__ch_name == other.__ch_name and self.__en_name == other.__en_name

    @property
    def ch_name(self) -> str:
        """返回教练中文名字"""
        return self.__ch_name

    @property
    def en_name(self) -> str:
        """返回教练英文名字"""
        return self.__en_name

    @property
    def age(self) -> str:
        """返回教练年龄"""
        return self.__descript.get(CoachAttr.AGE, str())

    @property
    def birthday(self) -> str:
        """返回教练出生日期"""
        return self.__descript.get(CoachAttr.BIRTHDAY, str())

    @property
    def height(self) -> str:
        """返回教练身高"""
        return self.__descript.get(CoachAttr.HEIGHT, str())

    @property
    def nationality(self) -> str:
        """返回教练国籍"""
        return self.__descript.get(CoachAttr.NATIONALITY, str())

    @property
    def team(self) -> str:
        """返回教练所在球队名称"""
        return self.__descript.get(CoachAttr.TEAM, str())

    @property
    def location(self) -> str:
        """返回教练所在球场位置; [主教练, 助理教练]"""
        return self.__descript.get(CoachAttr.LOCATION, str())

    @property
    def honour(self) -> dict:
        """返回教练个人荣誉"""
        return self.__descript.get(CoachAttr.HONOUR, dict())

    def modify(self, by=CoachAttr.CH_NAME, value=None):
        """根据传入的属性名称来修改对应的属性值"""
        if by not in CoachAttr.__dict__.values():
            raise ValueError(
                f"{self.__class__.__name__} object not attribute: '{by}'"
            )
        self.__descript[by] = value

    def description(self) -> dict:
        """返回教练的所有属性信息"""
        desc = dict()
        attributes = [value for key, value in CoachAttr.__dict__.items()
                      if isinstance(key, str) and key.isupper()]
        for name in attributes:
            desc[name] = copy(self.__descript.get(name))
        desc["ch_name"] = self.__ch_name
        desc["en_name"] = self.__en_name
        return desc
