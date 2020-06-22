"""
    天龙八部技能系统
"""


class SkillDeployer:
    """
        技能释放器
    """

    def __init__(self, name):
        self.name = name
        self.__list_impact = self.__config_deployer()

    def __config_deployer(self):
        """
            配置释放器
        @return:
        """
        dict_skill_config = {
            "wtz": ["LowerDefense(100, 0.5)", "Damage(10)"],
            "xlsbz": ["LowerSpeed(3, 5)", "Damage(80)"],
        }
        list_impact_name = dict_skill_config[self.name]
        return [eval(item) for item in list_impact_name]

    def generate_skill(self):
        for item in self.__list_impact:
            item.impact()


class ImpactEffect:
    """
        影响效果
        隔离技能释放器 与 具体的影响效果
    """

    def impact(self):
        raise NotImplementedError()


class LowerDefense(ImpactEffect):
    """
        降低防御力
    """

    def __init__(self, distance, ratio):
        self.distance = distance
        self.ratio = ratio

    def impact(self):
        print("distance is %d, ratio is %.2f , LowerDefense" % (self.distance, self.ratio))


class LowerSpeed(ImpactEffect):
    """
        降低速度
    """

    def __init__(self, time, ratio):
        self.time = time
        self.ratio = ratio

    def impact(self):
        print("time is %d, ratio is %.2f , LowerSpeed" % (self.time, self.ratio))


class Damage(ImpactEffect):
    """
        伤害生命
    """

    def __init__(self, value):
        self.value = value

    def impact(self):
        print("value is %s, Damaged" % self.value)


s01 = SkillDeployer("wtz")
s01.generate_skill()
